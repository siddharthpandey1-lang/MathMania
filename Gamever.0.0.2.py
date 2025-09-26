import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Math Quiz")

# Set up fonts
font_small = pygame.font.SysFont("comicsansms", 28)
font_medium = pygame.font.SysFont("arial", 36)
font_large = pygame.font.SysFont("timesnewroman", 48)

# Colors
GREEN=200, 255, 200
BG_COLORS = [GREEN]

# Questions list (mixed operations)
questions = [
    ("What is 9 × 4?", 36),
    ("What is 8 + 6?", 14),
    ("What is 7 - 3?", 4),
    ("What is 20 ÷ 5?", 4),
    ("What is 6 × 8?", 48),
    ("What is 15 - 7?", 8),
    ("What is 3 × 9?", 27),
    ("What is 2 + 6?", 8),
    ("What is 5 × 4?", 20),
    ("What is 7 + 8?", 15),
    ("What is 6 × 6?", 36),
    ("What is 9 ÷ 3?", 3),
    ("What is 12 + 15?", 27),
    ("What is 18 ÷ 6?", 3),
    ("What is 14 - 9?", 5),
]

def draw_text(text, x, y, font, color=(0, 0, 0)):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def show_message_screen():
    screen.fill(RED(BG_COLORS))
    draw_text("🎉 Welcome to the Colorful Math Quiz! 🎉", 50, 50, font_medium)
    draw_text("You'll get 10 questions: addition, subtraction,", 50, 100, font_small)
    draw_text("multiplication, and division.", 50, 140, font_small)
    draw_text("✅ +1 for correct, ❌ -1 for wrong, ⏭ 0 for skipped.", 50, 180, font_small)
    draw_text("Press any key to begin!", 50, 240, font_medium)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def show_questions():
    score = 0
    selected_questions = random.sample(questions, 10)
    for i, (question, answer) in enumerate(selected_questions):
        screen.fill(random.choice(BG_COLORS))
        draw_text(f"Question {i + 1}", 50, 50, font_large)
        draw_text(question, 50, 120, font_medium)
        draw_text("Type your answer and press Enter:", 50, 180, font_small)
        pygame.display.flip()

        user_input = ""
        input_active = True
        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if user_input.strip() == "":
                            score += 0
                        elif user_input.isdigit() and int(user_input) == answer:
                            score += 1
                        else:
                            score -= 1
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

            screen.fill(Green)(BG_COLORS)
            draw_text(f"Question {i + 1}", 50, 50, font_large)
            draw_text(question, 50, 120, font_medium)
            draw_text("Type your answer and press Enter:", 50, 180, font_small)
            draw_text(user_input, 50, 230, font_medium)
            pygame.display.flip()

    return score

def show_result(score):
    screen.fill(green(BG_COLORS))
    draw_text(f"🎯 Your final score is: {score}", 50, 100, font_large)
    draw_text("Want to play again? (Y/N)", 50, 160, font_medium)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False

def main():
    while True:
        show_message_screen()
        score = show_questions()
        if not show_result(score):
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()