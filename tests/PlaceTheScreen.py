#!/usr/bin/env python3

import pygame
import os

def oldwindow():
    os.environ['SDL_VIDEO_CENTERED'] = '0'

    background_colour = (255,255,255)
    (width, height) = (300, 200)

    pygame.init()
    pygame_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tutorial 1')
    pygame_screen.fill(background_colour)

    button1 = Button_Pygame(100, 100, 50, 44, "Play")
    buttons = [button1]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            for button in buttons:
                button.handle_event(event, pygame_screen)

        for button in buttons:
            button.draw(pygame_screen)

        pygame.display.flip()

def newwindow():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)

    pygame.init()
    screen = pygame.display.set_mode((1000, 300))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

class Button_Pygame:
    def __init__(self ,x ,y, w, h, text):
        self.COLOR_INACTIVE_TEXT = [255, 255, 255]
        self.COLOR_ACTIVE_TEXT = [0, 0, 0]
        self.COLOR = [160, 160, 160]
        self.color_text = self.COLOR_INACTIVE_TEXT
        self.color = self.COLOR
        self.FONT = pygame.font.Font(None, 25)
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.active = False

    def handle_event(self, event, pygame_screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            #Toggle the color variable
            self.color_text = self.COLOR_ACTIVE_TEXT
            self.text_surface = self.FONT.render(self.text, True, self.color_text)
            #Blit the rectangle
            pygame.draw.rect(pygame_screen, self.color, self.rect)

        else:
            #Toggle the color variable
            self.color_text = self.COLOR_INACTIVE_TEXT
            self.text_surface = self.FONT.render(self.text, True, self.color_text)
            #Blit the rectangle
            pygame.draw.rect(pygame_screen, self.color, self.rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
                #Call the function
                newwindow()
            else:
                self.active = False

    def draw(self, pygame_screen):
        #Blit the rectangle
        pygame.draw.rect(pygame_screen, self.color, self.rect)
        #Blit the text
        pygame_screen.blit(self.text_surface, (self.rect.x+8, self.rect.y+15))

if __name__ == "__main__":
    oldwindow()
