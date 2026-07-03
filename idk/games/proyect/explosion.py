import pygame
from config import *

class Explosion(object):
    def init(self,pos, blast_radius = 50, points_multiplier = 0, blast_color = NUKE_EXPLOSION, expand_rate = 0, dwell_time = 0):
        self.pos = pos
        self.blast_radius = blast_radius
        self.points_multiplayer = points_multiplier
        self.blast_color = blast_color
        self.expand_rate = expand_rate
        self.radius = 0
        self.complete = False

    def draw(self, screen):
        return pygame.draw.circle(screen, self.blast_color, self.pos, self.radius)

    #mepicaelpeneayudanojodamalditahijueputasealoddkdjdk

    def update(self):
        if not self.complete:
            self.radius += self.expand_rate
        if self.radius > self.blast_radius:
            self.complete = True

    def get_center(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def get_points_multiplier(self):
        return self.points_multiplier
    