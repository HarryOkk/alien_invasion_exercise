import pygame


class Ship:

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.settings = ai_game.settings#让ship类能够访问游戏对象的设置值

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()#rect来存储飞船的外接矩形

        #for the new ship, put it in the central
        self.rect.midbottom = self.screen_rect.midbottom#飞船外接矩形和屏幕外接矩形的中点对齐

        self.x = float(self.rect.x)#用新对象存储张昭矩形的浮点型X坐标，先确定X的坐标再进行幅值

        self.moving_right = False#这是一个标志，用于判断状态以进行下一步操作
        self.moving_left = False#这是一个标志，用于判断当前张昭是否向左移动


    def blitme(self):
        """picture the ship in somewhere"""
        self.screen.blit(self.image, self.rect)#在屏幕上显示飞船（前面已经设置好飞船的位置，这边直接显示就行7）

    def update(self):#更新飞船矩形块位置的方法
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x#重新更新张昭surface的矩形对象坐标

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)