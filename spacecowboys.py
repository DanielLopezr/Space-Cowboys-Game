import pygame
import random
import warnings
import string
warnings.filterwarnings("ignore")

# Define los colores que usará el juego
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define las dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Inicializa Pygame
pygame.init()

# Crea la ventana del juego
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Cowboys")

# Define las fuentes que usará el juego
font = pygame.font.SysFont(None, 48)
big_font = pygame.font.SysFont(None, 72)

# Carga los sonidos que usará el juego
gunshot_sound = pygame.mixer.Sound("gunshot.wav")
gunshot_sound.set_volume(0.3)
win_sound = pygame.mixer.Sound("win.wav")
lose_sound = pygame.mixer.Sound("lose.wav")

# Carga los fondos del juego
img_start_menu = pygame.transform.scale(pygame.image.load('background_start_game.png'), (800, 600))
img_arena =  pygame.transform.scale(pygame.image.load('background_arena.png'), (800, 600))
img_arena2 = pygame.transform.scale(pygame.image.load('background_arena_2.png'), (800, 600))
img_arena3 = pygame.transform.scale(pygame.image.load('background_arena_3.png'), (800, 600))

#Carga los personajes del juego
cowboy = pygame.image.load('cowboy.png')
enemy1 = pygame.image.load('enemy1.png')

img_cowboy = pygame.transform.scale(pygame.image.load('cowboy.png'), (185, 275))
img_enemy1 = pygame.transform.scale(pygame.image.load('enemy1.png'), (185, 275))
img_enemy2 = pygame.transform.scale(pygame.image.load('enemy2.png'), (185, 275))
img_enemy3 = pygame.transform.scale(pygame.image.load('enemy32.png'), (185, 275))
img_bullet = pygame.transform.scale(pygame.image.load('bullet.png'), (161, 180))

def cowboy(x,y):
    screen.blit(img_cowboy, (x,y))

def enemy(ex, ey, lvl):
    if lvl == 1:
        screen.blit(img_enemy1, (ex, ey))
    elif lvl == 2:
        screen.blit(img_enemy2, (ex, ey))
    elif lvl == 3:
        screen.blit(img_enemy3, (ex, ey))

def bkgnd(lvl):
    if lvl == 1:
        screen.blit(img_arena,(0,0))
    if lvl == 2:
        screen.blit(img_arena2,(0,0))
    if lvl == 3:
        screen.blit(img_arena3,(0,0))

#Una función para disparar una bala, el usuario puede disparar varia balas, entonces hay que guardarlas.
def shoot(bullet_list,bx,by,rl):
    gunshot_sound.play()
    bullet_list.append(Bullet(bx, by,rl))

#Clase de bala para guardar las propiedades de la bala
class Bullet:
    def __init__(self, x, y,rl):
        # Initializing variables for the bullet
        self.x = x
        self.y = y
        self.rl = rl
        if self.rl == 'r':
            self.image = pygame.transform.scale(pygame.image.load('bullet.png'), (200, 220))
        elif self.rl == 'l':
            self.image = pygame.transform.scale(pygame.image.load('bullet_left.png'), (200, 200))
        self.bullet_speed = 75

    # Moves the bullet accross the screen by updating the x variable after each draw()
    def _move_bullet(self):
        if self.rl == 'r':
            self.x += self.bullet_speed
        elif self.rl == 'l':
            self.x -= self.bullet_speed

    def draw(self):
        # Get the surface (window)
        surface = pygame.display.get_surface()
        # Blit the bullet to the screen
        surface.blit(self.image, (self.x, self.y))
        # Update its position with the function above
        self._move_bullet()

# Define la función que muestra el mensaje de victoria
def show_win_message():
    win_text = big_font.render("YOU WIN!", True, GREEN)
    screen.blit(win_text, (SCREEN_WIDTH/2 - win_text.get_width()/2, SCREEN_HEIGHT/2 - win_text.get_height()/2))
    pygame.display.update()
    win_sound.play()

# Define la función que muestra el mensaje de derrota
def show_lose_message():
    lose_text = big_font.render("YOU LOSE!", True, RED)
    screen.blit(lose_text, (SCREEN_WIDTH/2 - lose_text.get_width()/2, SCREEN_HEIGHT/2 - lose_text.get_height()/2))
    pygame.display.update()
    lose_sound.play()

# Define la función que muestra la pantalla de inicio
def show_title_screen():
    title_text = big_font.render("Space Cowboy Duels!", True, BLACK)
    start_text = font.render("Press SPACE to start", True, BLACK)
    screen.blit(img_start_menu,(0,0))
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_text.get_width()/2, SCREEN_HEIGHT/2 - title_text.get_height()))
    screen.blit(start_text, (SCREEN_WIDTH/2 - start_text.get_width()/2, SCREEN_HEIGHT/2 + start_text.get_height()))
    pygame.display.update()


# Define la función que muestra la pantalla de juego
def show_game_screen(x,y,ex,ey, lvl, rand=None):
    bkgnd(lvl)
    player_text = font.render("Player", True, WHITE)
    enemy_text = font.render("Enemy "+str(lvl), True, WHITE)
    screen.blit(player_text, (SCREEN_WIDTH/2 - player_text.get_width() - 50, 50))
    screen.blit(enemy_text, (SCREEN_WIDTH/2 + 50, 50))
    cowboy(x,y)
    enemy(ex, ey,lvl)
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT), 5)

    if rand is not None:
        fontt = pygame.font.Font(None, 60)
        text = fontt.render('SHOOT KEY: '+rand, True, BLACK)
        text_surface = pygame.Surface((text.get_width() + 20, text.get_height() + 20))
        text_surface.fill(WHITE)
        text_surface.blit(text,(10,10)) 
        screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT/2 - text_surface.get_height()/2))

    pygame.display.update()
    

# Define la función principal del juego
def main():
    #Diferentes posiciones de la bala
    bx2 = 330
    bx3 = 440
    bx4 = 550
    #Posicion inicial de la bala
    bxr = 220
    by = 220
    bxl = 370
    #Velocidad de la bala 
    bspeed = 165
    x =  50
    ex = 550
    ey = 200
    y = 200

    #Actualizar la posicion de los bichos
    x_change = 0
    speed = 0
    lvl = 1

    clock = pygame.time.Clock()
    dead = False
    # Muestra la pantalla de inicio
    show_title_screen()

    if lvl ==1:
        # Espera a que el jugador presione la tecla SPACE para empezar
        game_started = False
        while not game_started:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_started = True

        # Ejecuta el duelo
        player_wins = False
        enemy_wins = False

        # Muestra la pantalla de juego
        show_game_screen(x,y,ex,ey,lvl)

        # Obtiene el tiempo actual
        font = pygame.font.Font(None, 60)
        start_time = pygame.time.get_ticks()
        text = font.render(str(4), True, BLACK)
        text_surface = pygame.Surface((text.get_width() + 20, text.get_height() + 20))
        text_surface.fill(WHITE)
        screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT/2 - text_surface.get_height()/2))
        pygame.time.delay(1000)
        pygame.display.update()

        # Muestra el texto emergente
        for i in range(3):
            j = 3- i
            text = font.render(str(j), True, BLACK)
            show_game_screen(x,y,ex,ey,lvl)

            # Actualiza la superficie de texto para que desaparezca gradualmente
            text_surface.fill(WHITE)
            text_surface.blit(text,(10,10)) 
            screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT/2 - text_surface.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1000)

        rand = random.choice(string.ascii_lowercase) 
        letters = dict(zip(list(string.ascii_letters), ['K_'+i for i in list(string.ascii_lowercase)]))
        randkey = letters[rand] 
        pygkeyboard = [getattr(pygame,j) for j in ['K_'+i for i in list(string.ascii_lowercase)]]
        pygkeyboard.remove(getattr(pygame, randkey))
        show_game_screen(x,y,ex,ey,lvl,rand)    
        bullet_list = [] # Since the user can have multiple bullets firing, we need to keep track of them
        start_time = pygame.time.get_ticks()
        while not dead:
            show_game_screen(x,y,ex,ey,lvl,rand)#Move this to the top so you're filling the screen before drawing anything
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        dead = True
                elif player_wins == False and enemy_wins==False:  
                    if event.type == pygame.KEYDOWN:
                        print(event.key)
                        if event.key == getattr(pygame, randkey): # Moved this up here
                            shoot(bullet_list,bxr,by,'r') # Spawn the bullet
                            player_wins = True
                            rand = None
                        elif event.key in pygkeyboard:
                            shoot(bullet_list,bxl,by,'l') # Spawn the bullet
                            enemy_wins = True
                            rand = None

            if pygame.time.get_ticks() -start_time > 2000:
                shoot(bullet_list,bxl,by,'l') # Spawn the bullet
                enemy_wins = True      
                rand = None
            # Draw each bullet onto the screen by iterating over the list
            for bullet in bullet_list:
                # If the bullet has exited the screen we remove it from the list so they are not kept in memory
                if bullet.x > SCREEN_WIDTH or bullet.x < 0:
                    bullet_list.remove(bullet)
                    dead = True
                # Draw the bullet (called from the Class)
                bullet.draw()

            pygame.display.update()

        if player_wins:
                show_win_message()
                pygame.time.delay(3000)
                lvl = 2
        if enemy_wins:
                show_lose_message()
                pygame.time.delay(3000)
                show_title_screen()
            
    if lvl == 2:
        # Ejecuta el duelo
        player_wins = False
        enemy_wins = False
        dead = False

        # Muestra la pantalla de juego
        show_game_screen(x,y,ex,ey,lvl)

        # Obtiene el tiempo actual
        font = pygame.font.Font(None, 60)
        start_time = pygame.time.get_ticks()
        text = font.render(str(4), True, BLACK)
        text_surface = pygame.Surface((text.get_width() + 20, text.get_height() + 20))
        text_surface.fill(WHITE)
        screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT/2 - text_surface.get_height()/2))
        pygame.time.delay(1000)
        pygame.display.update()

        # Muestra el texto emergente
        for i in range(3):
            j = 3- i
            text = font.render(str(j), True, BLACK)
            show_game_screen(x,y,ex,ey,lvl)

            # Actualiza la superficie de texto para que desaparezca gradualmente
            text_surface.fill(WHITE)
            text_surface.blit(text,(10,10)) 
            screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT/2 - text_surface.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1000)

        rand = random.choice(string.ascii_lowercase) 
        letters = dict(zip(list(string.ascii_letters), ['K_'+i for i in list(string.ascii_lowercase)]))
        randkey = letters[rand] 
        pygkeyboard = [getattr(pygame,j) for j in ['K_'+i for i in list(string.ascii_lowercase)]]
        pygkeyboard.remove(getattr(pygame, randkey))
        show_game_screen(x,y,ex,ey,lvl,rand)    
        bullet_list = [] # Since the user can have multiple bullets firing, we need to keep track of them
        start_time = pygame.time.get_ticks()
        while not dead:
            show_game_screen(x,y,ex,ey,lvl,rand)#Move this to the top so you're filling the screen before drawing anything
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        dead = True
                elif player_wins == False and enemy_wins==False:  
                    if event.type == pygame.KEYDOWN:
                        print(event.key)
                        if event.key == getattr(pygame, randkey): # Moved this up here
                            shoot(bullet_list,bxr,by,'r') # Spawn the bullet
                            player_wins = True
                            rand = None
                        elif event.key in pygkeyboard:
                            shoot(bullet_list,bxl,by,'l') # Spawn the bullet
                            enemy_wins = True
                            rand = None

            if pygame.time.get_ticks() -start_time > 1500:
                shoot(bullet_list,bxl,by,'l') # Spawn the bullet
                enemy_wins = True      
                rand = None
            # Draw each bullet onto the screen by iterating over the list
            for bullet in bullet_list:
                # If the bullet has exited the screen we remove it from the list so they are not kept in memory
                if bullet.x > SCREEN_WIDTH or bullet.x < 0:
                    bullet_list.remove(bullet)
                    dead = True
                # Draw the bullet (called from the Class)
                bullet.draw()

            pygame.display.update()

        if player_wins:
                show_win_message()
                pygame.time.delay(3000)
                lvl = 3
        if enemy_wins:
                show_lose_message()
                pygame.time.delay(3000)
                show_title_screen()
    if lvl == 3:
        # Ejecuta el duelo
        player_wins = False
        enemy_wins = False
        dead = False

        # Muestra la pantalla de juego
        show_game_screen(x,y,ex,ey,lvl)

        # Obtiene el tiempo actual
        font = pygame.font.Font(None, 60)
        start_time = pygame.time.get_ticks()
        text = font.render(str(4), True, BLACK)
        text_surface = pygame.Surface((text.get_width() + 20, text.get_height() + 20))
        text_surface.fill(WHITE)
        screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT/2 - text_surface.get_height()/2))
        pygame.time.delay(1000)
        pygame.display.update()

        # Muestra el texto emergente
        for i in range(3):
            j = 3- i
            text = font.render(str(j), True, BLACK)
            show_game_screen(x,y,ex,ey,lvl)

            # Actualiza la superficie de texto para que desaparezca gradualmente
            text_surface.fill(WHITE)
            text_surface.blit(text,(10,10)) 
            screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT/2 - text_surface.get_height()/2))
            pygame.display.update()
            pygame.time.delay(1000)

        rand = random.choice(string.ascii_lowercase) 
        letters = dict(zip(list(string.ascii_letters), ['K_'+i for i in list(string.ascii_lowercase)]))
        randkey = letters[rand] 
        pygkeyboard = [getattr(pygame,j) for j in ['K_'+i for i in list(string.ascii_lowercase)]]
        pygkeyboard.remove(getattr(pygame, randkey))
        show_game_screen(x,y,ex,ey,lvl,rand)    
        bullet_list = [] # Since the user can have multiple bullets firing, we need to keep track of them
        start_time = pygame.time.get_ticks()
        while not dead:
            show_game_screen(x,y,ex,ey,lvl,rand)#Move this to the top so you're filling the screen before drawing anything
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        dead = True
                elif player_wins == False and enemy_wins==False:  
                    if event.type == pygame.KEYDOWN:
                        print(event.key)
                        if event.key == getattr(pygame, randkey): # Moved this up here
                            shoot(bullet_list,bxr,by,'r') # Spawn the bullet
                            player_wins = True
                            rand = None
                        elif event.key in pygkeyboard:
                            shoot(bullet_list,bxl,by,'l') # Spawn the bullet
                            enemy_wins = True
                            rand = None

            if pygame.time.get_ticks() -start_time > 500:
                shoot(bullet_list,bxl,by,'l') # Spawn the bullet
                enemy_wins = True      
                rand = None
            # Draw each bullet onto the screen by iterating over the list
            for bullet in bullet_list:
                # If the bullet has exited the screen we remove it from the list so they are not kept in memory
                if bullet.x > SCREEN_WIDTH or bullet.x < 0:
                    bullet_list.remove(bullet)
                    dead = True
                # Draw the bullet (called from the Class)
                bullet.draw()

            pygame.display.update()

        if player_wins:
                show_title_screen()
                show_win_message()
                pygame.time.delay(3000)
        if enemy_wins:
                show_lose_message()
                pygame.time.delay(3000)
                show_title_screen()
    clock.tick(60)
    # Sale del juego
    pygame.quit()

# Ejecuta el juego
if __name__ == "__main__":
    main()