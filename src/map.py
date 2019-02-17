import pygame

class Map:
    def display_map(self):
        #Variables
        is_running = True
        color_black = (0 , 0 , 0)
        color_white = (255 , 255 , 255)

        #Pygame Initialization
        pygame.init()

        #Display Setup
        game_Display = pygame.display.set_mode((800 , 600))
        pygame.display.set_caption("TEXT ADVENTURE")

        #Main Game Loop
        while is_running:
            #Event Handlers
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
        
            game_Display.fill(color_black)

            pygame.draw.rect(game_Display , color_white , [0 , 0 , 800 , 30])
            pygame.draw.rect(game_Display , color_white , [0 , 0 , 30 , 570])
            pygame.draw.rect(game_Display , color_white , [770 , 0 , 30 , 570])
            pygame.draw.rect(game_Display , color_white , [0 , 570 , 800 , 30])

            #Display Update
            pygame.display.update()

        #Quiting Functions
        pygame.quit()
        quit()