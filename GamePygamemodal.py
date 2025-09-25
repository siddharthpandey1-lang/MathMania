import pygame
import sys

# Initialize Pygame
pygame.init()
def main():
    print("game started")
    print("hello kids this is a game of maths")
    print("you will be given 10 questions")
    print("you will get 1 point for every correct answer")
    print("you will get -1 point for every wrong answer")
    print("you will get 0 points for every question you skip")

if __name__ == "__main__":
    main()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplication Quiz")

# Set up fonts and colors
font = pygame.font.SysFont(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Questions list
print ("Question 1")
print ("what is 9X4")
print ("Question 2")
print ("what is 8X6")
print ("Question 3")
print ("what is 7X3") 
print ("Question 4")
print ("what is 5X5")
print ("Question 5")
print ("what is 6X8")
print ("Question 6")
print ("what is 4X7")
print ("Want to play again")