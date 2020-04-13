import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载图像并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人的横纵坐标，左上角为（0,0）
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 准确位置
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外星人撞到屏幕，则返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """具体位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
