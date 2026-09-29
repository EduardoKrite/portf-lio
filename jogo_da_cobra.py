import pygame
import sys
import random
import os

#Nome do arquivo onde o maior recorde será armazenado
aquivo_recorde = "recorde.txt"

# Função responsável por ler o recorde salvo no arquivo
def ler_arquivo():
    # Verifica se o arquivo ainda não existe
    if not os.path.exists(aquivo_recorde):
        return 0

    with open(aquivo_recorde, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

        if not conteudo:
            return 0

        numero = int(conteudo)
    return numero


# INICIALIZAÇÃO DO PYGAME
pygame.init()

# Função responsável por salvar o novo recorde
def salva_recorde(recorde):
    with open(aquivo_recorde, 'w') as arquivo:
        arquivo.write(f"{recorde}\n")


salva_recorde(5)
recorde = ler_arquivo()
print(recorde)


#criar uma janela;
altura= 800
largura=  900
bloco = 50

tela = pygame.display.set_mode((largura,altura))
relogio=pygame.time.Clock()

# CORES E FONTE
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
fonte = pygame.font.SysFont(None, 60)

VELOCIDADE_COBRA = 50

# FUNÇÃO PARA GERAR UMA NOVA COMIDA
def gera_comida_nova(corpo):

    while True:
        x = random.randint(0, largura// bloco -1) * bloco
        y = random.randint(0, altura// bloco -1) * bloco
        if[x,y] not in corpo:
            return x,y

# FUNÇÃO PARA INICIAR/REINICIAR O JOGO


def novo_jogo():
    corpo = [[400, 300], [350, 300], [300, 300], [250, 300], [200, 300], [150, 300]]
    comida_x, comida_y = gera_comida_nova(corpo)
    return corpo, bloco, 0, comida_x, comida_y

corpo, dx, dy, comida_x, comida_y = novo_jogo()
game_over = False
rodando = True
pontuacao = 0
recorde = ler_arquivo()

# LOOP PRINCIPAL DO JOGO
while rodando:

    # EVENTOS DO TECLADO E DA JANELAtg
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if game_over:

                if evento.key == pygame.K_SPACE:
                    corpo, dx, dy, comida_x, comida_y = novo_jogo()
                    pontuacao = 0
                    game_over = False

            else:

                if evento.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -bloco, 0

                if evento.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = bloco, 0

                if evento.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -bloco

                if evento.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, bloco



#MOVIMENTAÇÃO DA COBRA

    if not game_over:

        nova_cabeca = [
            corpo[0][0] + dx,
            corpo[0][1] + dy
        ]

       # VERIFICAÇÃO DE COLISÃO

        if (
            nova_cabeca[0] < 0
            or nova_cabeca[0] >= largura
            or nova_cabeca[1] < 0
            or nova_cabeca[1] >= altura
            or nova_cabeca in corpo
        ):
            game_over = True

        else:
            corpo.insert(0, nova_cabeca)

            # VERIFICAÇÃO DA COMIDA

            if nova_cabeca == [comida_x, comida_y]:
                pontuacao +=1

                if pontuacao > recorde:
                    recorde = pontuacao

                comida_x, comida_y = gera_comida_nova(corpo)
            else:
                corpo.pop()


    # DESENHO DO JOGO
    tela.fill((50, 100, 50))
    pygame.draw.rect(tela, VERMELHO, (comida_x, comida_y, bloco, bloco))
    for x, y in corpo:
        pygame.draw.rect(tela, (0, 200, 0), (x, y, bloco, bloco))

        txt_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
        tela.blit(txt_pontuacao, (20, 20))

        txt_recorde = fonte.render(f"Recorde: {recorde}", True, BRANCO)
        tela.blit(txt_recorde, (20, 70))

    if game_over:
        txt_game_over = fonte.render("GAME OVER", True, VERMELHO)
        txt_restart = fonte.render("Pressione ESPACO para reiniciar", True, BRANCO)
        tela.blit(txt_game_over, txt_game_over.get_rect(center=(largura // 2, altura // 2 - 30)))
        tela.blit(txt_restart, txt_restart.get_rect(center=(largura // 2, altura // 2 + 30)))
        
    pygame.display.update()
    relogio.tick(8)

pygame.quit()
sys.exit()


