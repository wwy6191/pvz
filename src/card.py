# src/card.py

import pygame
import os
from config import IMAGE_DIR

class Card:
    def __init__(self, name, sun_cost, position):
        self.name = name
        self.sun_cost = sun_cost
        self.image = pygame.image.load(os.path.join(IMAGE_DIR, f"{name}.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 50))
        self.rect = pygame.Rect(position[0], position[1], 60, 80)

    def render(self, surface):
        # 画卡片边框（可以用Card.png）
        border = pygame.image.load(os.path.join(IMAGE_DIR, "Card.png")).convert_alpha()
        border = pygame.transform.scale(border, (60, 80))
        surface.blit(border, self.rect)

        # 植物图片居中显示在卡片上
        img_rect = self.image.get_rect(center=self.rect.center)
        surface.blit(self.image, img_rect)

        # TODO: 加阳光消耗的文字绘制


    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
