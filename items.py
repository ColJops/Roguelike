from config import *
from random import randint
import pygame

class Potion:
    """ Define class for life potion"""

    def __init__(self):
        """ init potion"""
        self.x_cord = randint(X_LOW, X_MAX)  # random coordinates for shownig potion
        self.y_cord = randint(Y_LOW, Y_MAX)
        self.image = pygame.image.load("graphics/potion.png")
        self.widht = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def show(self):
        """ refresh the potion """
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Heart:
    """ Define class for life potion"""

    def __init__(self):
        """ init potion"""
        pygame.sprite.Sprite.__init__(self)
        self.x_cord = randint(X_LOW, X_MAX)  # random coordinates for shownig potion
        self.y_cord = randint(Y_LOW, Y_MAX)
        self.image = pygame.image.load("graphics/heart.png")
        self.widht = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def show(self):
        """ refresh the potion """
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Sheeps:
    """ Define class for life potion"""

    def __init__(self):
        """ init potion"""
        self.x_cord = randint(X_LOW, X_MAX)  # random coordinates for showwing sheep
        self.y_cord = randint(Y_LOW, Y_MAX)
        self.image = pygame.image.load("graphics/owca stoi.png")
        self.widht = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def show(self):
        """ refresh the potion """
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Walls:
    """ losowe pojedyncze bloczki - trzeba pomyśleć jak robimy te ściany"""
    def __init__(self):
        """ init walls"""
        self.x_cord = randint(X_LOW, X_MAX)  # random coordinates for shownig walls
        self.y_cord = randint(Y_LOW, Y_MAX)
        self.image = pygame.image.load("graphics/fance.png")
        self.widht = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def show(self):
        """ refresh the walls """
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


class Hays:
    """ losowe pojedyncze bloczki - trzeba pomyśleć jak robimy te ściany"""
    def __init__(self):
        """ init walls"""
        self.x_cord = randint(X_LOW, X_MAX)  # random coordinates for shownig walls
        self.y_cord = randint(Y_LOW, Y_MAX)
        self.image = pygame.image.load("graphics/hay.png")
        self.widht = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def show(self):
        """ refresh the walls """
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))