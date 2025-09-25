import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplication Quiz")

# Set up fonts and colors
font_large = pygame.font.SysFont("comicsansms", 48)
font_medium = pygame.font.SysFont("comicsansms", 36)
font_small = pygame.font.SysFont("comicsansms", 28)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
GREEN = (34, 177, 76)
RED = (200, 0, 0)

# Questions
questions = [
    ("What is 9 × 4?", 36),
    ("What is 8 × 6?", 48),
    ("What is 7 × 3?", 21),
    ("What is 5 × 5?", 25),
    ("What is 6 × 8?", 48),
    ("What is 4 × 7?", 28),
]

# Button class
class Button:
    def __init__(self, text, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        txt = font_small.render(self.text, True, WHITE)
        screen.blit(txt, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Game loop
def game_loop():
    score = 0
    question_index = 0
    running = True
    clock = pygame.time.Clock()

    # Prepare first question
    question, answer = questions[question_index]
    options = [answer, answer + 2, answer - 3, answer + 5]
    random.shuffle(options)
    buttons = [Button(str(opt), 100, 200 + i * 70, 200, 50, GREEN) for i, opt in enumerate(options)]
    time_limit = 10
    start_ticks = pygame.time.get_ticks()

    while running:
        screen.fill(BLUE)
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000

        if question_index < len(questions):
            question_text = font_medium.render(f"Q{question_index + 1}: {questions[question_index][0]}", True, WHITE)
            screen.blit(question_text, (100, 100))

            timer_text = font_small.render(f"Time left: {max(0, time_limit - seconds)}s", True, RED)
            screen.blit(timer_text, (600, 50))

            for btn in buttons:
                btn.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_sound.play()
                    for btn in buttons:
                        if btn.is_clicked(event.pos):
                            selected = int(btn.text)
                            if selected == questions[question_index][1]:
                                score += 1
                                correct_sound.play()
                            else:
                                score -= 1
                                wrong_sound.play()
                            question_index += 1
                            if question_index < len(questions):
                                question, answer = questions[question_index]
                                options = [answer, answer + 2, answer - 3, answer + 5]
                                random.shuffle(options)
                                buttons = [Button(str(opt), 100, 200 + i * 70, 200, 50, GREEN) for i, opt in enumerate(options)]
                                start_ticks = pygame.time.get_ticks()
                            break

            if seconds >= time_limit:
                question_index += 1
                if question_index < len(questions):
                    question, answer = questions[question_index]
                    options = [answer, answer + 2, answer - 3, answer + 5]
                    random.shuffle(options)
                    buttons = [Button(str(opt), 100, 200 + i * 70, 200, 50, GREEN) for i, opt in enumerate(options)]
                    start_ticks = pygame.time.get_ticks()

        else:
            result_text = font_large.render(f"Your Score: {score}", True, WHITE)
            screen.blit(result_text, (250, 200))
            play_again_btn = Button("Play Again", 300, 300, 200, 60, RED)
            play_again_btn.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_sound.play()
                    if play_again_btn.is_clicked(event.pos):
                        game_loop()

        pygame.display.flip()
        clock.tick(60)

# Welcome screen
def welcome_screen():
    clock = pygame.time.Clock()
    while True:
        screen.fill(BLACK)
        title = font_large.render("Welcome to the Maths Quiz!", True, WHITE)
        instructions = font_small.render("Answer 10 questions. +1 for correct, -1 for wrong, 0 for skip.", True, WHITE)
        start_btn = Button("Start Game", 300, 400, 200, 60, GREEN)

        screen.blit(title, (100, 150))
        screen.blit(instructions, (100, 220))
        start_btn.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.is_clicked(event.pos):
                    game_loop()

        pygame.display.flip()
        clock.tick(60)

# Run the game 
# welcome_screen()