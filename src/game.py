# src/game.py

import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, IMAGE_DIR, LOGIC_WIDTH, LOGIC_HEIGHT
from shop import Shop
import os

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("植物大战僵尸")
        self.canvas = pygame.Surface((LOGIC_WIDTH, LOGIC_HEIGHT))

        self.clock = pygame.time.Clock()
        self.running = True

        self.bg = pygame.image.load(os.path.join(IMAGE_DIR, "Background.jpg")).convert()
        self.shop = Shop()

        # 缩放比例
        self.scale_x = SCREEN_WIDTH / LOGIC_WIDTH
        self.scale_y = SCREEN_HEIGHT / LOGIC_HEIGHT

    def run(self):
        while self.running:
            self.handle_events()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 缩放坐标映射
                logic_pos = (
                    event.pos[0] / self.scale_x,
                    event.pos[1] / self.scale_y
                )
                self.shop.handle_click(logic_pos)

    def render(self):
        self.canvas.blit(self.bg, (0, 0))
        self.shop.render(self.canvas)

        # 拉伸画布到屏幕大小
        scaled_surface = pygame.transform.scale(self.canvas, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()
