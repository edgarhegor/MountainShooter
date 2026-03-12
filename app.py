import pygame
print("Setup Start")
pygame.init()

#define o tamanho da janela
window = pygame.display.set_mode(size=(720,340))
#apenas para manter o loop 
running = True

while running:


    #for checka por todos os eventos
    # pygame.QUIT é um evento que o usuário clica no x e fecha a janela
    # Se o evento tipo de evento for QUI então o running que controla o loop
    # vira falso e a janela fecha. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()# close the window
            quit()#end pygame 
            #running = False
print("Setup ends")



