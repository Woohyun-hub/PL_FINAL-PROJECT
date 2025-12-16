import pygame
from .settings import *
from .player import Player
from .obstacle import Obstacle
from .score import load_highscore, save_highscore

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Neon Dodge")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 32)
    big_font = pygame.font.SysFont(None, 64)

    highscore = load_highscore()

    while True:
        player = Player()
        obstacles = []
        score = 0
        lives = INITIAL_LIVES
        frame = 0
        running = True

        while running:
            clock.tick(FPS)
            frame += 1
            score += 1

            difficulty = min(score // 500, 6)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()
            player.move(keys)

            if frame % max(15, SPAWN_DELAY - difficulty * 4) == 0:
                obstacles.append(Obstacle(difficulty))

            for obs in obstacles[:]:
                obs.update()
                if obs.rect.colliderect(player.rect):
                    obstacles.remove(obs)
                    lives -= 1
                    if lives <= 0:
                        running = False

            obstacles = [o for o in obstacles if o.rect.top < SCREEN_HEIGHT]

            screen.fill(BLACK)
            player.draw(screen)

            for obs in obstacles:
                obs.draw(screen)

            screen.blit(font.render(f"Score: {score}", True, WHITE), (20, 20))
            screen.blit(font.render(f"High: {highscore}", True, WHITE), (20, 50))
            screen.blit(font.render(f"Lives: {lives}", True, WHITE), (20, 80))

            pygame.display.flip()

        # GAME OVER
        if score > highscore:
            highscore = score
            save_highscore(highscore)

        screen.fill(BLACK)

        game_over_text = big_font.render("GAME OVER", True, NEON_PINK)
        score_text = font.render(f"Score: {score}", True, WHITE)
        high_text = font.render(f"High Score: {highscore}", True, WHITE)
        info_text = font.render("Press R to Restart or Q to Quit", True, WHITE)

        screen.blit(game_over_text,
                    (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 260))
        screen.blit(score_text,
                    (SCREEN_WIDTH//2 - score_text.get_width()//2, 340))
        screen.blit(high_text,
                    (SCREEN_WIDTH//2 - high_text.get_width()//2, 380))
        screen.blit(info_text,
                    (SCREEN_WIDTH//2 - info_text.get_width()//2, 440))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        return
