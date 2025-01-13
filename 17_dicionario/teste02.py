# # Dicionário de códigos de cores em RGB
# cores = {
#     "vermelho": (255, 0, 0),
#     "verde": (0, 255, 0),
#     "azul": (0, 0, 255),
#     "amarelo": (255, 255, 0),
#     "ciano": (0, 255, 255),
#     "magenta": (255, 0, 255),
#     "preto": (0, 0, 0),
#     "branco": (255, 255, 255),
#     "cinza": (128, 128, 128),
#     "laranja": (255, 165, 0),
#     "roxo": (128, 0, 128),
#     "rosa": (255, 192, 203),
#     "marrom": (165, 42, 42),
#     "azul claro": (173, 216, 230),
#     "verde escuro": (0, 100, 0)
# }

# # Exemplo de uso: imprimir os códigos de cores
# for nome, rgb in cores.items():
#     print(f"Cor: {nome} - RGB: {rgb}")

import pygame

# Inicializar o pygame
pygame.init()

# Configurações da tela
largura, altura = 400, 200
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Teste de Combinação de Cores")

# Dicionário de cores
cores = {
    "vermelho": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "amarelo": (255, 255, 0),
    "ciano": (0, 255, 255),
    "magenta": (255, 0, 255)
}

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(cores["amarelo"])  # Preencher a tela com a cor escolhida
    # Atualizar a tela
    pygame.display.flip()

# Encerrar o pygame
pygame.quit()
