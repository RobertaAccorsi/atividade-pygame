import pygame
import random

pygame.init()

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Colisão de textos")

PRETO = (0, 0, 0)
clock = pygame.time.Clock()

fonte = pygame.font.SysFont(None, 60)


def tratar_colisao_borda(rect, largura, altura):
    mudou = False
    vx, vy = 0, 0

    if rect.right >= largura:
        vx = random.randint(-2, -1)
        vy = random.randint(-2, 2)
        mudou = True

    elif rect.left <= 0:
        vx = random.randint(1, 2)
        vy = random.randint(-2, 2)
        mudou = True

    elif rect.bottom >= altura:
        vx = random.randint(-2, 2)
        vy = random.randint(-2, -1)
        mudou = True

    elif rect.top <= 0:
        vx = random.randint(-2, 2)
        vy = random.randint(1, 2)
        mudou = True

    return mudou, vx, vy


def cor_aleatoria():
    return (
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255)
    )


texto1 = fonte.render("Roberta", True, cor_aleatoria())
texto2 = fonte.render("Accorsi", True, cor_aleatoria())

rect1 = texto1.get_rect(topleft=(100, 100))
rect2 = texto2.get_rect(topleft=(400, 250))

vel1_x, vel1_y = 2, 2
vel2_x, vel2_y = -2, 2


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


    rect1.x += vel1_x
    rect1.y += vel1_y

    rect2.x += vel2_x
    rect2.y += vel2_y

 
    mudou, vx, vy = tratar_colisao_borda(rect1, largura, altura)
    if mudou:
        vel1_x, vel1_y = vx, vy
        texto1 = fonte.render("Roberta", True, cor_aleatoria())


    mudou, vx, vy = tratar_colisao_borda(rect2, largura, altura)
    if mudou:
        vel2_x, vel2_y = vx, vy
        texto2 = fonte.render("Accorsi", True, cor_aleatoria())

    if rect1.colliderect(rect2):
        vel1_x *= -1
        vel1_y *= -1
        vel2_x *= -1
        vel2_y *= -1

        texto1 = fonte.render("Roberta", True, cor_aleatoria())
        texto2 = fonte.render("Accorsi", True, cor_aleatoria())

    tela.fill(PRETO)
    tela.blit(texto1, rect1)
    tela.blit(texto2, rect2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()