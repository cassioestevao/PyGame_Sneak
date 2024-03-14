# configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Python | Cássio Estevão")
largura, altura = 800, 640
monitor = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

box = 20
taxa_atualizacao = 3

def frut_game():
    comida_x = round(random.randrange(0, largura - box) / float(box)) * float(box)
    comida_y = round(random.randrange(0, altura - box) / float(box)) * float(box)
    return comida_x, comida_y

def desing_frut(tamanho, comida_x, comida_y):
    pygame.draw.rect(monitor, verde, [comida_x, comida_y, tamanho, tamanho])

def desing_sneak(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(monitor, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desing_record(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render("Pontos: {}".format(pontuacao), True, vermelha)
    monitor.blit(texto, [1, 1])

def frame_fps(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = box
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -box
    elif tecla == pygame.K_RIGHT:
        velocidade_x = box
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -box
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    end_game = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = frut_game()

    while not end_game:
        monitor.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = frame_fps(evento.key)

        # desing_frut
        desing_frut(box, comida_x, comida_y)

        # atualizar a posicao da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            end_game = True

        x += velocidade_x
        y += velocidade_y

        # desing_sneak
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # se a cobrinha bateu no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True

        desing_sneak(box, pixels)

        # desenhar_pontos
        desing_record(tamanho_cobra - 1)

        # atualizacao da monitor
        pygame.display.update()

        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = frut_game()

        relogio.tick(taxa_atualizacao)

rodar_jogo()