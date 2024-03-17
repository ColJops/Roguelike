from random import randint
from config import *
import pygame

class Enemy:

    def __init__(self):
        self.x_cord = randint(X_LOW, X_MAX)
        self.y_cord = randint(Y_LOW, Y_MAX)
        self.image = pygame.image.load("graphics/wolf.png")
        self.widht = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 3
        self.start = 0
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)
        self.package = {"lives": 0, "ammunition": 0, "sheeps": 0}

    def move(self):
        """ create enemy random move"""
        
        if self.start == 0:
            self.x_cord += self.speed
            self.y_cord += self.speed
            if self.x_cord <= X_LOW:
                self.x_cord = X_LOW-self.widht
                self.x_cord += self.speed
                if self.x_cord >= X_MAX-self.widht:
                    self.x_cord -= self.speed
                if self.y_cord <= Y_LOW + self.height:
                    self.y_cord += self.speed
                if self.y_cord >= Y_MAX-self.height:
                    self.y_cord -= self.speed   
            if self.x_cord >= X_MAX-self.widht:
                self.x_cord = X_MAX
                self.x_cord -= self.speed
                if self.x_cord <= X_LOW:
                    self.x_cord += self.speed
                if self.y_cord <= X_LOW + self.height:
                    self.y_cord += self.speed
                if self.y_cord >= X_MAX-self.height:
                    self.y_cord -= self.speed   
            if self.y_cord <= Y_LOW + self.height:
                self.x_cord = Y_LOW
                self.y_cord += self.speed
                if self.y_cord >= Y_MAX-self.height:
                    self.y_cord -= self.speed
                if self.x_cord <= X_LOW + self.height:
                    self.x_cord += self.speed
                if self.x_cord >= X_MAX-self.widht:
                    self.x_cord -= self.speed
            if self.y_cord >= Y_MAX-self.height:
                self.y_cord = Y_MAX
                self.y_cord -= self.speed
                if self.y_cord <= Y_LOW + self.height:
                    self.y_cord += self.speed
                if self.x_cord <= X_LOW:
                    self.x_cord += self.speed
                if self.x_cord >= X_MAX-self.widht:
                    self.x_cord -= self.speed
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))