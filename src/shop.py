# src/shop.py

import pygame
import os
from config import SCREEN_WIDTH, IMAGE_DIR, LOGIC_WIDTH, LOGIC_HEIGHT
from card import Card

class Shop:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(IMAGE_DIR, "Shop.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = LOGIC_WIDTH // 2
        self.rect.top = 0

        # 创建一些卡片作为示例
        self.cards = [
            Card("Peashooter", 50, (100, 10)),
            Card("SunFlower", 50, (200, 10)),
            Card("WallNut", 50, (300, 10)),
        ]
    
    def init_cards(self):
        card_spacing = 10
        start_x = self.x + 30
        card_y = self.y + 10
        plants = [
            ("Peashooter", "Peashooter.png", 100),
            ("SunFlower", "SunFlower.png", 50),
            ("CherryBomb", "CherryBomb.png", 150),
        ]
        for i, (name, img, cost) in enumerate(plants):
            position = (start_x + i * (50 + card_spacing), card_y)
            card = PlantCard(name, img, cost, position)
            self.cards.append(card)

    def render(self, surface):
        surface.blit(self.image, self.rect)
        for card in self.cards:
            card.render(surface)

    def handle_click(self, pos):
        for card in self.cards:
            if card.rect.collidepoint(pos):
                print(f"点击了 {card.name}")
