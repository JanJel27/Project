import pygame,Tests
from pygame.locals import * 
pygame.init()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.music.load('music/main_theme.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

font = pygame.font.Font("River Adventurer.ttf",40)
text = "Welcome to my game \n\nIn a distant and mystical land, nestled between towering and lush forests, lived a young and adventurous explorer named Marshal. He was known throughout his village for his insatiable curiosity and his love for uncovering hidden mysteries. However, what intrigued his the most were the ancient stories of the Enchanted Treasures a set of magical artifacts said to possess unimaginable power."
text1 = font.render("Press any key to continue ....", True, 'black') 
textRect = text1.get_rect()
textRect.center = ((screen.get_width() // 4)*3, (screen.get_height() // 10)*9)
blue=(0,100,128)
def display_text(surface, text, pos, font, color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= 1350:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height


def run():
    Tests.login()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
        if events.type==pygame.KEYDOWN:
            run()
    screen.fill(blue)
    display_text(screen, text, (200,100), font, 'grey')
    screen.blit(text1,textRect)
    pygame.display.update()