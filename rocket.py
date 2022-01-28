import sys

import pygame


class Rocket():
    
    def __init__(self, screen):
        """ Инициализирует и задает его начальную позицию."""
        self.screen = screen
        
        # Загрузка изображения и получения прямоугольника.
        self.image = pygame.image.load('images/rocket-2442125_640.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Изображение в центре.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        
    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 5
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 5
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 5
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 5
            
    def blitme(self):
        """ Рисует в текущей позиции."""
        self.screen.blit(self.image, self.rect)
        

def check_events(rocket):
    """ Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)
        
        
def check_keydown_events(event, rocket):
    """ Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
        
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
        
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
                
def check_keyup_events(event, rocket):
    """ Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def rocket_lanch():
    # Главная функция
    pygame.init()
    screen = pygame.display.set_mode((1820, 980 ))
    pygame.display.set_caption("Rocket lanch")
    bg_color = (137, 207, 240)
    
    rocket = Rocket(screen)
    
    while True:
        check_events(rocket)
        screen.fill(bg_color)
        rocket.blitme()
        rocket.update()
        # Отображение экрана
        pygame.display.flip()
        
        
rocket_lanch()
