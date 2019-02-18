import pygame

class Game:
    #Variables
    __is_running = True
    __color_black = (0 , 0 , 0)
    __color_white = (255 , 255 , 255)
    __color_red = (255 , 0 , 0)
    __player_x = 45
    __player_y = 45

    #Pygame Initialization
    pygame.init()

    #Display Setup
    __game_display = pygame.display.set_mode((810 , 600))
    pygame.display.set_caption("Text Adventure")
    
    #Create Map
    def __display_map(self):
        pygame.draw.rect(self.__game_display , self.__color_white , [0 , 0 , 810 , 30]) #Top Border
        pygame.draw.rect(self.__game_display , self.__color_white , [0 , 0 , 30 , 570]) #Left Border
        pygame.draw.rect(self.__game_display , self.__color_white , [780 , 0 , 30 , 570]) #Right Border
        pygame.draw.rect(self.__game_display , self.__color_white , [0 , 570 , 810 , 30]) #Bottom Border
    
    #Create Player
    def __display_player(self):
        pygame.draw.circle(self.__game_display , self.__color_red , (self.__player_x , self.__player_y) , 15)

    #Border Function
    def __border(self):
        if self.__player_x > 780:
            self.__player_x -= 30
        if self.__player_x < 30:
            self.__player_x += 30
        if self.__player_y > 570:
            self.__player_y -= 30
        if self.__player_y < 30:
            self.__player_y += 30

    #Main Game Function
    def game(self):
        #Main Game Loop
        while self.__is_running:
            #Event Handlers
            for event in pygame.event.get():
                #Quit Event
                if event.type == pygame.QUIT:
                    self.__is_running = False

            key_state = pygame.key.get_pressed()
            if key_state[pygame.K_UP] or key_state[pygame.K_w]:
                self.__player_y -= 2
            if key_state[pygame.K_DOWN] or key_state[pygame.K_s]:
                self.__player_y += 2
            if key_state[pygame.K_RIGHT] or key_state[pygame.K_d]:
                self.__player_x += 2
            if key_state[pygame.K_LEFT] or key_state[pygame.K_a]:
                self.__player_x -= 2
            
            #Background Color
            self.__game_display.fill(self.__color_black)

            #Display Map
            self.__display_map()

            #Display Player
            self.__display_player()

            #Logical Functions
            self.__border()

            #Display Update
            pygame.display.update()

        #Quiting Functions
        pygame.quit()
        quit()