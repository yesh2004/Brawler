import pygame
from fighter import Fighter

pygame.init()

SCREEN_WIDTH=1000
SCREEN_HEIGHT=600
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

bg_image=pygame.image.load("D:/personal/Programing/Python/StreetFighter/assets\images/background/background.jpg").convert_alpha()
warroir_sheet=pygame.image.load("D:/personal/Programing/Python/StreetFighter/assets\images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet=pygame.image.load("D:/personal/Programing/Python/StreetFighter/assets\images/wizard/Sprites/wizard.png").convert_alpha()
victory_img = pygame.image.load("D:/personal/Programing/Python/StreetFighter/assets/images/icons/victory.png").convert_alpha()

count_font = pygame.font.Font("D:/personal/Programing/Python/StreetFighter/assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("D:/personal/Programing/Python/StreetFighter/assets/fonts/turok.ttf", 30)
clock=pygame.time.Clock()
FPS=60

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

WORRIOR_SIZE=162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WORRIOR_DATA=[WORRIOR_SIZE,WARRIOR_SCALE,WARRIOR_OFFSET]
WIZARD_SIZE=250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA=[WIZARD_SIZE,WIZARD_SCALE,WIZARD_OFFSET]
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def draw_bg():
    scaled_bg=pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg,(0,0))

def draw_health_bar(health,x,y):
    ratio=health/100
    pygame.draw.rect(screen,RED,(x,y,400,30))
    pygame.draw.rect(screen,YELLOW,(x,y,400*ratio,30))

fighter_1=Fighter(1,200,310,False,WORRIOR_DATA,warroir_sheet,WARRIOR_ANIMATION_STEPS)
fighter_2=Fighter(2,700,310,True,WIZARD_DATA,wizard_sheet,WIZARD_ANIMATION_STEPS)

run=True
while run:

    clock.tick(FPS)

    draw_bg()
    fighter_1.update()
    fighter_2.update()

    fighter_1.draw(screen)
    fighter_2.draw(screen)
    draw_health_bar(fighter_1.health,20,20)
    draw_health_bar(fighter_2.health,580,20)
    draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
    draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)
    if intro_count <=0:
        fighter_1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_2)
        fighter_2.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter_1)
    else:
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        if(pygame.time.get_ticks()-last_count_update)>=1000:
            intro_count-=1
            last_count_update=pygame.time.get_ticks()
            

    
    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        #display victory image
        screen.blit(victory_img, (360, 150))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            fighter_1 = Fighter(1, 200, 310, False, WORRIOR_DATA, warroir_sheet, WARRIOR_ANIMATION_STEPS)
            fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()