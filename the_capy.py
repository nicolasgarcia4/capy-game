import pygame
import random
from pygame.locals import *


height = 1920
width = 1080
squere_height, squere_width = 60, 60
pygame.display.set_caption("Entre Ouros e cafezes")
tela = pygame.display.set_mode((height, width), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()

key = pygame.key.get_pressed()
exec_game = True
exec_intro = True
exec_main = True
exec_game_over = True
exec_finish_01 = True

def running_game():
    global exec_game
    global exec_main
    global exec_game_over
    global exec_finish_01

    exec_game_over = True

    lives = 3
    caps = 0


    cap_img = [pygame.transform.scale(pygame.image.load('sprites/cap2.png'), (squere_height, squere_width)),
        pygame.transform.scale(pygame.image.load('sprites/cap3.png'), (squere_height, squere_width)),]

    capybaras = [
    {'coluna': random.randint(1920, 3460), 'linha': random.randint(840, 1000), 'ativa': True, 'imagens': cap_img, 'velocidade': random.randint(2, 4)},
    {'coluna': random.randint(1920, 3460), 'linha': random.randint(840, 1000), 'ativa': True, 'imagens': cap_img, 'velocidade': random.randint(2, 4)},
    {'coluna': random.randint(1920, 3460), 'linha': random.randint(840, 1000), 'ativa': True, 'imagens': cap_img, 'velocidade': random.randint(2, 4)},
    {'coluna': random.randint(1920, 3460), 'linha': random.randint(840, 1000), 'ativa': True, 'imagens': cap_img, 'velocidade': random.randint(2, 4)},
    {'coluna': random.randint(1920, 3460), 'linha': random.randint(840, 1000), 'ativa': True, 'imagens': cap_img, 'velocidade': random.randint(2, 4)},
    {'coluna': random.randint(1920, 3460), 'linha': random.randint(840, 1000), 'ativa': True, 'imagens': cap_img, 'velocidade': random.randint(2, 4)},
    {'coluna': random.randint(1920, 3460), 'linha': random.randint(840, 1000), 'ativa': True, 'imagens': cap_img, 'velocidade': random.randint(2, 4)},
    {'coluna': random.randint(1920, 3460), 'linha': random.randint(840, 1000), 'ativa': True, 'imagens': cap_img, 'velocidade': random.randint(2, 4)}]

    #ground_images
    img1 = pygame.image.load('images/stoneground.png')
    img2 = pygame.image.load('images/brickground.png')
    img3 = pygame.image.load('images/dirtground.png')
    #redimensioning
    img1 = pygame.transform.scale(img1, (squere_height, squere_width))
    img2 = pygame.transform.scale(img2, (squere_height, squere_width))
    img3 = pygame.transform.scale(img3, (squere_height, squere_width))

    #sky_images
    sky01 = pygame.transform.scale(pygame.image.load('images/sky01.png'), (squere_height, squere_width))
    sky02 = pygame.transform.scale(pygame.image.load('images/sky02.png'), (squere_height, squere_width))
    sky03 = pygame.transform.scale(pygame.image.load('images/sky03.png'), (squere_height, squere_width))

    #buildings
    building1 = pygame.image.load('images/building1.png')
    building2 = pygame.image.load('images/building2.png')
    building3 = pygame.image.load('images/building3.png')

    #moon
    moon = pygame.image.load('images/moon.png')

    #pao_de_queio
    pao = pygame.transform.scale(pygame.image.load('images/paoqueijo.png'), (squere_height/1.5, squere_width/1.5))
    col_pao = random.randint(0, 1890)
    line_pao = random.randint(900, 1000)

    #cage
    cage = pygame.transform.scale(pygame.image.load('images/cage.png'), (squere_height/1.5, squere_width/1.5))
    col_cage = -60
    line_cage = -60

    #character
    character = pygame.transform.scale(pygame.image.load('sprites/p1.png'), (squere_height, squere_width))

    character_down = [
            pygame.transform.scale(pygame.image.load('sprites/p1.png'), (squere_height, squere_width)),
            pygame.transform.scale(pygame.image.load('sprites/p2.png'), (squere_height, squere_width)),
            pygame.transform.scale(pygame.image.load('sprites/p3.png'), (squere_height, squere_width))
        ]
    character_up = [
            pygame.transform.scale(pygame.image.load('sprites/p4.png'), (squere_height, squere_width)),
            pygame.transform.scale(pygame.image.load('sprites/p5.png'), (squere_height, squere_width)),
            pygame.transform.scale(pygame.image.load('sprites/p6.png'), (squere_height, squere_width))
        ]
    character_right = [
            pygame.transform.scale(pygame.image.load('sprites/p7.png'), (squere_height, squere_width)),
            pygame.transform.scale(pygame.image.load('sprites/p8.png'), (squere_height, squere_width)),
            pygame.transform.scale(pygame.image.load('sprites/p9.png'), (squere_height, squere_width))
        ]
    character_left = [
            pygame.transform.scale(pygame.image.load('sprites/p10.png'), (squere_height, squere_width)),
            pygame.transform.scale(pygame.image.load('sprites/p11.png'), (squere_height, squere_width)),
            pygame.transform.scale(pygame.image.load('sprites/p12.png'), (squere_height, squere_width))
        ]

    col_character = 50
    line_character = 950

    character_up_index = 0
    character_up_time = 0
    character_up_interval = 100

    character_down_index = 0
    character_down_time = 0
    character_down_interval = 100

    character_right_index = 0
    character_right_time = 0
    character_right_interval = 100

    character_left_index = 0
    character_left_time = 0
    character_left_interval = 100

    #matriz
    matriz = [
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6],
        [6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6],
        [6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6],
        [5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5],
        [5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5],
        [5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    while exec_game == True:
        clock.tick(60)
        pygame.display.update()
        tela.fill((0, 0, 0))
        font = pygame.font.Font(None, 100)

        #map
        for line in range(len(matriz)):
            for col in range(len(matriz[line])):
                x = col * squere_height
                y = line * squere_width
                valor = matriz[line][col]

                # Escolher qual imagem carregar de acordo com o valor na matriz
                if valor == 1:
                    tela.blit(img1, (x, y))  # Caminho
                elif valor == 2:
                    tela.blit(img2, (x, y))  # Parede
                elif valor == 3:
                    tela.blit(img3, (x, y))  # Parede2
                elif valor == 4:
                    tela.blit(sky01, (x, y))  # Parede2
                elif valor == 5:
                    tela.blit(sky02, (x, y))  # Parede2
                elif valor == 6:
                    tela.blit(sky03, (x, y))  # Parede2

        # moon_blit
        tela.blit(moon, (25, 20))

        # buildings
        tela.blit(building1, (-50, 600))
        tela.blit(building2, (60, 600))
        tela.blit(building3, (270, 600))
        tela.blit(building1, (160, 600))
        tela.blit(building2, (370, 600))
        tela.blit(building3, (470, 600))
        tela.blit(building1, (670, 600))
        tela.blit(building2, (570, 600))
        tela.blit(building3, (770, 600))
        tela.blit(building1, (-50, 600))
        tela.blit(building2, (60, 600))
        tela.blit(building3, (270, 600))
        tela.blit(building1, (160, 600))
        tela.blit(building2, (370, 600))
        tela.blit(building3, (470, 600))
        tela.blit(building1, (670, 600))
        tela.blit(building2, (570, 600))
        tela.blit(building3, (770, 600))
        tela.blit(building1, (870, 600))
        tela.blit(building2, (970, 600))
        tela.blit(building3, (1070, 600))
        tela.blit(building1, (1270, 600))
        tela.blit(building2, (1170, 600))
        tela.blit(building3, (1370, 600))
        tela.blit(building1, (1570, 600))
        tela.blit(building2, (1670, 600))
        tela.blit(building3, (1470, 600))
        tela.blit(building1, (1870, 600))
        tela.blit(building3, (1770, 600))

        # stars
        pygame.draw.rect(tela, (250, 250, 250), (230, 200, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (232, 198, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (300, 400, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (302, 398, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (400, 300, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (402, 298, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (500, 100, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (502, 98, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (600, 150, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (602, 148, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (540, 320, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (542, 318, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (700, 250, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (702, 248, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (800, 180, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (802, 178, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (860, 300, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (862, 298, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1000, 110, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1002, 108, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1090, 300, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1092, 298, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1190, 80, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1192, 78, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1260, 240, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1262, 238, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1390, 200, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1392, 198, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1460, 140, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1462, 138, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1600, 300, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1602, 298, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1700, 60, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1702, 58, 2, 6), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1800, 200, 6, 2), 0, 2)
        pygame.draw.rect(tela, (250, 250, 250), (1802, 198, 2, 6), 0, 2)


        tela.blit(font.render(f"Vidas: {lives}", True, (225, 225, 225)), (1600, 160))
        tela.blit(font.render(f"Capivaras capturadas: {caps} 'Meta 08'", True, (225, 225, 225)), (750, 80))

        # character_movement
        actual_time = pygame.time.get_ticks()
        key = pygame.key.get_pressed()

        if not key[pygame.K_RIGHT]:
            if not key[pygame.K_LEFT]:
                if not key[pygame.K_DOWN]:
                    if not key[pygame.K_UP]:
                        tela.blit(character, (col_character, line_character))

        if key[pygame.K_RIGHT]:
            col_character += squere_height / 4
            tela.blit(character_right[character_right_index], (col_character, line_character))
            if actual_time - character_right_time > character_right_interval:
                character_right_index = (character_right_index + 1) % len(character_right)
                character_right_time = actual_time

        if key[pygame.K_LEFT]:
            col_character -= squere_height / 4
            tela.blit(character_left[character_left_index], (col_character, line_character))
            if actual_time - character_left_time > character_left_interval:
                character_left_index = (character_left_index + 1) % len(character_left)
                character_left_time = actual_time

        if key[pygame.K_UP]:
            line_character -= squere_width / 4
            tela.blit(character_up[character_up_index], (col_character, line_character))
            if actual_time - character_up_time > character_up_interval:
                character_up_index = (character_up_index + 1) % len(character_up)
                character_up_time = actual_time

        if key[pygame.K_DOWN]:
            line_character += squere_width / 4
            tela.blit(character_down[character_down_index], (col_character, line_character))
            if actual_time - character_down_time > character_down_interval:
                character_down_index = (character_down_index + 1) % len(character_down)
                character_down_time = actual_time

        if line_character <= 850:
            line_character += squere_width / 4
        elif line_character >= 1020:
            line_character -= squere_width / 4
        if col_character <= 0:
            col_character += squere_height / 4
        elif col_character >= 1860:
            col_character -= squere_height / 4


        #pao_de_queijo
        tela.blit(pao, (col_pao, line_pao))
        pao_rect = pygame.Rect(col_pao, line_pao, 50, 50)
        #pao_colisions
        character_rect = pygame.Rect(col_character, line_character, 50, 50)
        if (character_rect.colliderect(pao_rect)):
            lives += 1
            col_pao = random.randint(0, 1890)
            line_pao = random.randint(900, 1000)

        #cage_drop_sound
        cage_drop_sound = pygame.mixer.Sound("audios/cage_drop.wav")

        #cage
        tela.blit(cage, (col_cage, line_cage))
        if key[pygame.K_SPACE]:
            col_cage = col_character
            line_cage = line_character
            cage_drop_sound.play()

        #capybara_blits&colisions 
        for capivara in capybaras:
            if capivara['ativa']:
                pos_x = capivara['coluna']
                pos_y = capivara['linha']
                
                imagem_capivara = random.choice(capivara['imagens'])
                
                tela.blit(imagem_capivara, (pos_x, pos_y))
                
                capivara_rect = pygame.Rect(capivara['coluna'], capivara['linha'], 60, 60 )
                personagem_rect = pygame.Rect(col_character, line_character, 60, 60)
                cage_rect = pygame.Rect(col_cage, line_cage, 50, 50)
                
                #capy&character_colisions
                if capivara_rect.colliderect(personagem_rect):
                    capivara['coluna'] = 1920
                    lives -= 1

                #cage&character_colisions
                if capivara_rect.colliderect(cage_rect):
                    capivara['ativa'] = False
                    col_cage = -600
                    caps += 1

        #capy_movementation
        for capivara in capybaras:
            if capivara['ativa']:
                if capivara['coluna'] > -60:
                    capivara['coluna'] -= squere_height / capivara['velocidade']
                else:
                    capivara['coluna'] = random.randint(1920, 3460)


        #ending_game_conditions
        if lives <= 0:
            game_over()

        if caps >= 8:
            finish_01()
            exec_finish_01 = True

        for evento in pygame.event.get():
            if evento.type == QUIT:
                exec_game = False
            if key[pygame.K_ESCAPE]:
                exec_game = False
                exec_main = False

def intro():
    global exec_intro

    backgrd = pygame.image.load('images/intro.png')

    while exec_intro == True:
        clock.tick(60)
        pygame.display.update()
        tela.fill((0, 0, 0))
        key = pygame.key.get_pressed()

        tela.blit(backgrd, (0, 0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                exec_intro = False
            if key[pygame.K_SPACE] or key[pygame.K_ESCAPE]:
                exec_intro = False

def finish_01():    
    global exec_finish_01
    global exec_game

    exec_game = False

    finish_01 = pygame.image.load('images/finish_01.png')

    while exec_finish_01 == True:
        clock.tick(60)
        pygame.display.update()
        tela.fill((0, 0, 0))
        key = pygame.key.get_pressed()

        tela.blit(finish_01, (0, 0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                exec_finish_01 = False
            if key[pygame.K_e]:
                exec_finish_01 = False
                exec_game = True
                running_game()

def game_over():
    global exec_game_over
    global exec_game

    exec_game = False

    game_over = pygame.image.load('images/game_over.png')

    while exec_game_over == True:
        clock.tick(60)
        pygame.display.update()
        tela.fill((0, 0, 0))
        key = pygame.key.get_pressed()

        tela.blit(game_over, (0, 0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                exec_game_over = False
            if key[pygame.K_SPACE]:
                exec_game_over = False
                exec_game = True
                running_game()


#game
while exec_main == True:
    clock.tick(60)
    pygame.display.update()
    tela.fill((0, 0, 0))
    key = pygame.key.get_pressed()

    intro()
    running_game()

    for evento in pygame.event.get():
        if evento.type == QUIT:
            exec_main = False


pygame.quit()