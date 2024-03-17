from random import randint
from config import *
from player import *
from enemy import *
from items import Potion, Heart, Sheeps
import pygame
from pygame.locals import *
import sys
from music import musik

pygame.init()

BG = pygame.image.load("graphics/stagesecond.png")

musik.start()
# generate a game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roguelike OOP version test mode")

class Hays:
    """ losowe pojedyncze bloczki - trzeba pomyśleć jak robimy te ściany"""

    def __init__(self):
        """ init walls"""
        self.x_cord = randint(X_LOW, X_MAX)  # random coordinates for shownig walls
        self.y_cord = randint(Y_LOW, Y_MAX)
        self.image = pygame.image.load("graphics/tree.png")
        self.widht = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def show(self):
        """ refresh the walls """
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Walls:
    """ losowe pojedyncze bloczki - trzeba pomyśleć jak robimy te ściany"""

    def __init__(self):
        """ init walls"""
        self.x_cord = randint(X_LOW, X_MAX)  # random coordinates for shownig walls
        self.y_cord = randint(Y_LOW, Y_MAX)
        self.image = pygame.image.load("graphics/las.png")
        self.widht = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def show(self):
        """ refresh the walls """
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.widht, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))




def main():
    player = Player()
    enemy = Enemy()
    sheep = Sheeps()
    heart = Heart()
    potion = Potion()
    wall = Walls()
    hay = Hays()
    walls = []
    hays = []
    potions = []
    hearts = []
    sheeps = []
    clock = 0
    life = 3
    enemy_life = 2

    for i in range(10):
        sheeps.append(Sheeps())

    for i in range(15):
        walls.append(Walls())

    for i in range(5):
        hays.append(Hays())

    while True:
        clock += pygame.time.Clock().tick(FPS) / 1000  # count in seconds
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        # sprawdzić, czty ta linijka jest potrzebna
        enemy.move()
        # generate potion
        if clock >= 4:  # generate new potion every 4 seconds
            clock = 0
            if len(potions) < 2:  # żeby nie było więcej soku i serc niż 2 na planszy
                potions.append(Potion())
            if len(hearts) < 2:
                hearts.append(Heart())
        player.move(keys)
        for potion in potions:
            potion.show()

        for potion in potions:
            if player.hitbox.colliderect(potion.hitbox):  # check, if player take a potion
                player.speed = 6
                potions.remove(potion)

            if enemy.hitbox.colliderect(potion.hitbox):  # check, if enemy take a potion
                potions.remove(potion)
                enemy_life += 1
        if player.hitbox.colliderect(enemy.hitbox):
            if life > enemy_life:
                life -= enemy_life
                del (enemy)

            if life < enemy_life:
                life = 0
                print("GAME OVER")
                # pygame.quit()
                # sys.exit()

        for sheep in sheeps:
            if player.hitbox.colliderect(sheep.hitbox):
                player.package["sheeps"] += 1
                sheeps.remove(sheep)
            if enemy.hitbox.colliderect(sheep.hitbox):
                enemy.package["sheeps"] += 1

        for heart in hearts:
            if player.hitbox.colliderect(heart.hitbox):
                player.package["lives"] += 1
                hearts.remove(heart)
            if enemy.hitbox.colliderect(heart.hitbox):
                enemy.package["lives"] += 1

        for wall in walls:
            if player.hitbox.colliderect(wall.hitbox):
                if player.x_cord + player.speed > wall.x_cord - wall.widht:
                    player.x_cord = wall.x_cord - wall.widht
                if player.x_cord + player.speed > wall.x_cord - wall.widht:
                    player.x_cord = wall.x_cord + wall.widht
                if player.y_cord + player.speed > wall.y_cord - wall.height:
                    player.y_cord = wall.y_cord - wall.height
                if player.y_cord + player.speed > wall.y_cord - wall.height:
                    player.y_cord = wall.y_cord + wall.height

            if enemy.hitbox.colliderect(wall.hitbox):
                if enemy.x_cord + enemy.speed > wall.x_cord - wall.widht:
                    enemy.x_cord = wall.x_cord - wall.widht
                if enemy.x_cord + enemy.speed > wall.x_cord - wall.widht:
                    enemy.x_cord = wall.x_cord + wall.widht
                if enemy.y_cord + enemy.speed > wall.y_cord - wall.height:
                    enemy.y_cord = wall.y_cord - wall.height
                if enemy.y_cord + enemy.speed > wall.y_cord - wall.height:
                    enemy.y_cord = wall.y_cord + wall.height

        for hay in hays:
            if player.hitbox.colliderect(hay.hitbox):
                if player.x_cord + player.speed > hay.x_cord - hay.widht:
                    player.x_cord = hay.x_cord - hay.widht
                if player.x_cord + player.speed > hay.x_cord - hay.widht:
                    player.x_cord = hay.x_cord + hay.widht
                if player.y_cord + player.speed > hay.y_cord - hay.height:
                    player.y_cord = hay.y_cord - hay.height
                if player.y_cord + player.speed > hay.y_cord - hay.height:
                    player.y_cord = hay.y_cord + hay.height

            if enemy.hitbox.colliderect(hay.hitbox):
                if enemy.x_cord + enemy.speed > hay.x_cord - hay.widht:
                    enemy.x_cord = hay.x_cord - hay.widht
                if enemy.x_cord + enemy.speed > hay.x_cord - hay.widht:
                    enemy.x_cord = hay.x_cord + hay.widht
                if enemy.y_cord + enemy.speed > hay.y_cord - hay.height:
                    enemy.y_cord = hay.y_cord - hay.height
                if enemy.y_cord + enemy.speed > hay.y_cord - hay.height:
                    enemy.y_cord = hay.y_cord + hay.height

        window.blit(BG, (0, 0))
        player.draw()
        enemy.draw()

        for sheep in sheeps:
            sheep.draw()

        for wall in walls:
            wall.draw()

        for heart in hearts:
            heart.draw()

        for potion in potions:
            potion.draw()

        for hay in hays:
            hay.draw()

        pygame.display.update()


if __name__ == "__main__":
    main()