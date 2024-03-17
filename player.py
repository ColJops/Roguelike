from config import *
import sys
import pygame

class Player:
    """ Define a player class"""

    def __init__(self):
        """ start funcion"""
        self.x_cord = X_LOW  # player's starting coordinates
        self.y_cord = Y_LOW
        self.image = pygame.image.load("graphics/sheepherd.png")  # load player's image
        self.rect = self.image.get_rect()
        self.widht = self.image.get_width()  # player's image widht
        self.height = self.image.get_height()  # player's image height
        self.speed = 4  # player's speed
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)  # create hitbox for player
        self.package = {"lives": 0, "ammunition": 0, "sheeps": 0}

    def move(self, keys):
        """ define player's move"""
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y_cord -= self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x_cord -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y_cord += self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x_cord += self.speed

        if keys[pygame.K_q]:  # wyjście z gry klawiszem q
            sys.exit()
        if keys[pygame.K_m]:  # zatrzymanie muzyki klawiszem M
            pygame.mixer.music.stop()
        if keys[pygame.K_p]:  # wznowienie muzyki klawiszem p
            musik.start()

        if self.x_cord < X_LOW:
            self.x_cord = X_LOW + self.widht
        if self.x_cord > X_MAX - self.widht:
            self.x_cord = X_MAX - self.widht
        if self.y_cord < Y_LOW:
            self.y_cord = Y_LOW + self.height
        if self.y_cord > Y_MAX -self.height:
            self.y_cord = Y_MAX-self.height

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)  # refresh Hitbox


    def draw(self):
        """ showing player on screen"""
        self.hitbox = (self.x_cord, self.y_cord, self.widht, self.height)
        pygame.draw.rect(window, (0,0,0), self.hitbox, 1)
        window.blit(self.image, (self.x_cord, self.y_cord))