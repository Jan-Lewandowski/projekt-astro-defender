import pygame
import time
import os
import random
pygame.font.init()                                                          # Inicjalizacja czcionek
pygame.mixer.init()                                                         # Inicjalizacja systemu dźwiękowego

FONT_main = pygame.font.Font("FONTS/PixelsplitterBold-ErDW.ttf", 100)
FONT_level_ingame = pygame.font.Font("FONTS/PixelsplitterBold-ErDW.ttf", 150)
FONT_secondary = pygame.font.Font("FONTS/terminal-grotesque.ttf", 50)
FONT_scoreboard = pygame.font.Font("FONTS/terminal-grotesque.ttf", 40)

# Ustawienia okna gry
pygame.display.set_caption("AstroDefender")                                 # Tytuł okna
win_icon = pygame.image.load(os.path.join("IMAGES/alien_icon.png"))         # Ikona okna
pygame.display.set_icon(win_icon)                                           # Ustawienie ikony
WIDTH, HEIGHT = 768,768                                                     # Rozmiar okna
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))                           # Utworzenie okna gry

# Słownik dźwięków
sounds = {
    "effects": {
        "bonus": pygame.mixer.Sound("SOUND_EFFECTS/Bonus.wav"),
        "enemy_dies": pygame.mixer.Sound("SOUND_EFFECTS/Enemy_hit.ogg"),
        "player_dies": pygame.mixer.Sound("SOUND_EFFECTS/Player_dies.wav"),
        "laser": pygame.mixer.Sound("SOUND_EFFECTS/Player_laser.ogg"),
        "level_up" : pygame.mixer.Sound("SOUND_EFFECTS/Next_level.ogg"),
        "player_hit" : pygame.mixer.Sound("SOUND_EFFECTS/Player_hit.flac"),
    },
    "music": {
        "background1": pygame.mixer.Sound("MUSIC/background_music1.ogg"),
        "background2": pygame.mixer.Sound("MUSIC/background_music2.ogg"),
        "pause": pygame.mixer.Sound("MUSIC/pause_music.ogg"),
    },
    "interactive":{
        "button_click": pygame.mixer.Sound("SOUND_EFFECTS/Button_click.mp3"),
    }
}

# Ustawienie głośności dźwięków
effects_volume = 0.05
music_volume = 0.03
interactive_volume = 0.03
for effect in sounds["effects"].values():
    effect.set_volume(effects_volume)
for music in sounds["music"].values():
    music.set_volume(music_volume)
for sound in sounds["interactive"].values():
    sound.set_volume(interactive_volume)

# Właściwości obrazów
BUTTON_WIDTH = 236
BUTTON_HEIGHT = 92

METEO_VEL = 4
METEO_WIDTH = 45
METEO_HEIGHT = 142

PLAYER_VEL = 10
PLAYER_WIDTH = 81
PLAYER_HEIGHT = 100

ENEMY_VEL = 1
ENEMY_WIDTH = 45
ENEMY_HEIGHT = 68

PLAYER_LASER_VEL = 5
ENEMY_LASER_VEL = 2
LASER_WIDTH = 20
LASER_HEIGHT = 40

BOMB_VEL = 4
BOMB_WIDTH = 40
BOMG_HEIGHT = 40

BONUS_VEL = 10
BONUS_WIDTH = 70
BONUS_HEIGHT = 85

ADD_HEALTH_VEL = 8
ADD_HEALTH_WIDTH = 30
ADD_HEALTH_HEIGHT = 30

# Zmienne obrazów
background = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/menu_background.png")), (WIDTH, HEIGHT))
game_banner = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/GAME_banner1.png")), (600, 300))
start_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/START!_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
start_img_hover = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/START!_button_hover.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
options_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/OPTIONS_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
options_img_hover = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/OPTIONS_button_hover.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
quit_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/QUIT_button.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
quit_img_hover = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/QUIT_button_hover.png")), (BUTTON_WIDTH, BUTTON_HEIGHT))
scoreboard_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/SCOREBOARD_button.png")), (75, 75))
scoreboard_img_hover =pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/SCOREBOARD_button_hover.png")), (75, 75))
ingame_backtomenu_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/BACKTOMENU_button.png")), (300, 300))
ingame_backtomenu_img_hover = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/BACKTOMENU_button_hover.png")), (300, 300))
ingame_pause_button = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/PLAY_PAUSE.png")), (103, 121))
ingame_pause_button_hover = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/PLAY_PAUSE_hover.png")), (103, 121))
hearts_1 = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/1HEARTS.png")), (60, 300))
hearts_2 = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/2HEARTS.png")), (60, 300))
hearts_3 = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/3HEARTS.png")), (60, 300))
hearts_4 = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/4HEARTS.png")), (60, 300))
hearts_5 = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/5HEARTS.png")), (60, 300))
hearts_0 = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/0HEARTS.png")), (60, 300))
ingameover_menu_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/MENU_button.png")), (175, 75))
ingameover_menu_img_hover = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/MENU_button_hover.png")), (175, 75))
ingameover_reset_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/RESET_button.png")), (175, 75))
ingameover_reset_img_hover = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/RESET_button_hover.png")), (175, 75))
inoptions_back_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/BACK_button.png")), (100, 100))
inoptions_back_img_hover = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/BACK_button_hover.png")), (100, 100))
inoptions_MUSIC_label_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/MUSIC_label.png")), (350, 90))
inoptions_SOUNDEFFECTS_label_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/SOUNDEFFECTS_label.png")), (650, 90))
toggle_on_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/TOGGLE_on.png")), (100, 60))
toggle_on_img_hover = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/TOGGLE_on_hover.png")), (100, 60))
toggle_off_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/TOGGLE_off.png")), (100, 60))
toggle_off_img_hover = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/TOGGLE_off_hover.png")), (100, 60))
scoreboard_background = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/SCOREBOARD_BACKGROUND.png")), (507, 598))
meteo_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/METEORITE.png")), (METEO_WIDTH, METEO_HEIGHT))
player_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/PLAYER.png")), (PLAYER_WIDTH, PLAYER_HEIGHT))
enemy_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/ENEMY.png")), (ENEMY_WIDTH, ENEMY_HEIGHT))
player_laser_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/PLAYER_LASER.png")), (LASER_WIDTH, LASER_HEIGHT))
enemy_laser_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/ENEMY_LASER.png")), (LASER_WIDTH, LASER_HEIGHT))
bomb_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/BOMB.png")),(BOMB_WIDTH, BOMG_HEIGHT))
bonus_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/BONUS.png")), (BONUS_WIDTH, BONUS_HEIGHT))
add_health_img = pygame.transform.scale(pygame.image.load(os.path.join("IMAGES/ADD_HEALTH.png")), (ADD_HEALTH_WIDTH, ADD_HEALTH_HEIGHT))

# Zmienne globalne
level = 0
score = 0
lives = 5

# Zmienne globalne dla muzyki i efektów dźwiękowych
music_on = True
effects_on = True

# Klasa przycisku
class Button:
    def __init__(self, x, y, img, sound = None, hover=None):
        self.image = img
        self.hover = hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.sound = sound
    # Funkcja sprawdzająca, czy przycisk został kliknięty
    def update(self):
        action = False
        m_position = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(m_position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.sound.play()
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
    # Funkcja wyświetlająca przycisk
    def draw(self, window):
        m_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(m_position) and self.hover:
            window.blit(self.hover, (self.rect.x, self.rect.y))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))

# Klasa Lasera (obiekt, który może poruszać się w grze)
class Laser():
    def __init__(self, x, y, laser_image):
        self.x = x
        self.y = y
        self.image = laser_image
        self.mask = pygame.mask.from_surface(self.image) # Tworzenie maski do detekcji kolizji
    
    # Funkcja rysująca laser
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
    
    # Funkcja przesuwająca laser
    def move(self, vel):
        self.y += vel
    
    # Funkcja sprawdzająca, czy laser wyszedł poza ekran
    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)
    
    # Funkcja sprawdzająca kolizję z innym obiektem
    def collision(self, image):
        return collide(image, self)

# Funkcja do sprawdzania kolizji
def collide(img1, img2):
    distance_x = img2.x - img1.x
    distance_y = img2.y - img1.y
    return img1.mask.overlap(img2.mask, (distance_x, distance_y)) is not None

# Klasa bazowa dla obiektów poruszających się w grze
class Moving_Object():
    laser_cooldown = 30
    
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.lasers = []
        self.cool_down_counter = 0
    
    # Funkcja rysująca laser
    def draw(self, window):
        window.blit(self.object_image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
    
    # Funkcja obsługująca odnowienie lasera
    def cooldown(self):
        if self.cool_down_counter >= self.laser_cooldown:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    
    # Funkcja poruszająca laserem
    def move(self, vel):
        self.y += vel

# Klasa dla gracza
class Player(Moving_Object):
    def __init__(self, x, y):
        super().__init__(x, y,)
        self.object_image = player_img
        self.mask = pygame.mask.from_surface(self.object_image)
        self.laser_image = player_laser_img
    
    # Funkcja tworząca nowe lasery, gdy cooldown jest zakończony
    def create_lasers(self):
        action = False
        if self.cool_down_counter == 0:
            laser = Laser(self.x + self.object_image.get_width()//2 - LASER_WIDTH//2, self.y, self.laser_image)
            sounds["effects"]["laser"].play()
            self.lasers.append(laser)
            self.cool_down_counter = 1
            action = True

        return action
    
    # Funkcja poruszająca laserami gracza
    def move_lasers(self, vel, objects):
        global score
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for object in objects:
                    if laser.collision(object):
                        objects.remove(object)
                        if len(self.lasers) > 0:
                            self.lasers.remove(laser)
                            sounds["effects"]["enemy_dies"].play()
                        score += 1

# Klasa wroga
class Enemy(Moving_Object):
    def __init__(self, x, y):
        super().__init__(x, y,)
        self.object_image = enemy_img
        self.laser_image = enemy_laser_img
        self.mask = pygame.mask.from_surface(self.object_image)
    
    # Funkcja tworząca nowe lasery, gdy cooldown jest zakończony
    def create_lasers(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + self.object_image.get_width()//2 - LASER_WIDTH//2, self.y + self.object_image.get_height() - 10, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1   
    
    # Funkcja poruszająca laserami przeciwnika
    def move_lasers(self, vel, object):
         global lives
         self.cooldown()
         for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(object):
                self.lasers.remove(laser)
                sounds["effects"]["player_hit"].play()
                lives -= 1
    
     # Funkcja poruszająca przeciwnika
    def move(self, vel):
        self.y += vel
        
    
# Klasa meteorytu
class Meteo(Moving_Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.object_image = meteo_img
        self.mask = pygame.mask.from_surface(self.object_image)
    def move(self, vel):
        self.y += vel
        
# Klasa bonusu
class Bonus(Moving_Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.object_image = bonus_img
        self.mask = pygame.mask.from_surface(self.object_image)
    def move(self, vel):
        self.y += vel

# Klasa zdrowia
class HEART(Moving_Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.object_image = add_health_img
        self.mask = pygame.mask.from_surface(self.object_image)
    def move(self,vel):
        self.y += vel

# Klasa bomby
class BOMB(Moving_Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.object_image = bomb_img
        self.mask = pygame.mask.from_surface(self.object_image)
    def move(self,vel):
        self.y += vel

# Funkcja wyświetlająca listę wyników w formie tabeli
def scoreboard_list(file):
    WINDOW.blit(scoreboard_background,(127,120))
    
    # Odczytywanie wyników z pliku
    with open(file, "r") as scoreboard_file:
        lines = scoreboard_file.readlines()
    
    list_sorted = []
    for line in lines:
        list_sorted.append(int(line))
    # Sortowanie wyników malejąco (najwyższe na początku)
    for i in range(len(list_sorted)):
        for j in range(len(list_sorted) - 1 - i):
            if list_sorted[j] < list_sorted[j+1]:
                list_sorted[j], list_sorted[j+1] = list_sorted[j+1], list_sorted[j] 
    list_sorted_TOP10 = list_sorted[:10]

    # Wyświetlanie wyników TOP 10 na ekranie
    if len(list_sorted_TOP10) >= 1: 
        number_1 = list_sorted_TOP10[0]
        number_1_text = FONT_scoreboard.render(f"1:   {number_1}", 1, "red")
        WINDOW.blit(number_1_text, (200,200))
    if len(list_sorted_TOP10) >= 2: 
        number_2 = list_sorted_TOP10[1]
        number_2_text = FONT_scoreboard.render(f"2:  {number_2}", 1, "black")
        WINDOW.blit(number_2_text, (200,200 + 50))
    if len(list_sorted_TOP10) >= 3: 
        number_3 = list_sorted_TOP10[2]
        number_3_text = FONT_scoreboard.render(f"3:  {number_3}", 1, "black")
        WINDOW.blit(number_3_text, (200,200 + 100))
    if len(list_sorted_TOP10) >= 4: 
        number_4 = list_sorted_TOP10[3]
        number_4_text = FONT_scoreboard.render(f"4:  {number_4}", 1, "black")
        WINDOW.blit(number_4_text, (200,200 + 150))
    if len(list_sorted_TOP10) >= 5: 
        number_5 = list_sorted_TOP10[4]
        number_5_text = FONT_scoreboard.render(f"5:  {number_5}", 1, "black")
        WINDOW.blit(number_5_text, (200,200 + 200))
    if len(list_sorted_TOP10) >= 6: 
        number_6 = list_sorted_TOP10[5]
        number_6_text = FONT_scoreboard.render(f"6:  {number_6}", 1, "black")
        WINDOW.blit(number_6_text, (200,200 + 250))
    if len(list_sorted_TOP10) >= 7: 
        number_7 = list_sorted_TOP10[6]
        number_7_text = FONT_scoreboard.render(f"7:  {number_7}", 1, "black")
        WINDOW.blit(number_7_text, (200,200 + 300))
    if len(list_sorted_TOP10) >= 8: 
        number_8 = list_sorted_TOP10[7]
        number_8_text = FONT_scoreboard.render(f"8:  {number_8}", 1, "black")
        WINDOW.blit(number_8_text, (200,200 + 350))
    if len(list_sorted_TOP10) >= 9: 
        number_9 = list_sorted_TOP10[8]
        number_9_text = FONT_scoreboard.render(f"9:  {number_9}", 1, "black")
        WINDOW.blit(number_9_text, (200,200 + 400))
    if len(list_sorted_TOP10) >= 10:
        number_10 = list_sorted_TOP10[9]
        number_10_text = FONT_scoreboard.render(f"10: {number_10}", 1, "black")
        WINDOW.blit(number_10_text, (200,200 + 450))
    top_10_text = FONT_secondary.render(f"TOP 10", 1, "black")
    WINDOW.blit(top_10_text, (175, 150))
    
    list_score_LAST = []
    for line in lines:
        list_score_LAST.append(int(line))
    # Wyświetlanie wyników (10 ostatnich)
    if len(list_score_LAST) >= 1:
        number_1_last = list_score_LAST[-1]
        number_1_last_text = FONT_scoreboard.render(f"1:  {number_1_last}", 1, "red")
        WINDOW.blit(number_1_last_text, (460,200))
    if len(list_score_LAST) >= 2:
        number_2_last = list_score_LAST[-2]
        number_2_last_text = FONT_scoreboard.render(f"2:  {number_2_last}", 1, "black")
        WINDOW.blit(number_2_last_text, (450,200 + 50))
    if len(list_score_LAST) >= 3:
        number_3_last = list_score_LAST[-3]
        number_3_last_text = FONT_scoreboard.render(f"3:  {number_3_last}", 1, "black")
        WINDOW.blit(number_3_last_text, (450,200 + 100))
    if len(list_score_LAST) >= 4:
        number_4_last = list_score_LAST[-4]
        number_4_last_text = FONT_scoreboard.render(f"4:  {number_4_last}", 1, "black")
        WINDOW.blit(number_4_last_text, (450,200 + 150))
    if len(list_score_LAST) >= 5:
        number_5_last = list_score_LAST[-5]
        number_5_last_text = FONT_scoreboard.render(f"5:  {number_5_last}", 1, "black")
        WINDOW.blit(number_5_last_text, (450,200 + 200))
    if len(list_score_LAST) >= 6:
        number_6_last = list_score_LAST[-6]
        number_6_last_text = FONT_scoreboard.render(f"6:  {number_6_last}", 1, "black")
        WINDOW.blit(number_6_last_text, (450,200 + 250))
    if len(list_score_LAST) >= 7:
        number_7_last = list_score_LAST[-7]
        number_7_last_text = FONT_scoreboard.render(f"7:  {number_7_last}", 1, "black")
        WINDOW.blit(number_7_last_text, (450,200 + 300))
    if len(list_score_LAST) >= 8:
        number_8_last = list_score_LAST[-8]
        number_8_last_text = FONT_scoreboard.render(f"8:  {number_8_last}", 1, "black")
        WINDOW.blit(number_8_last_text, (450,200 + 350))
    if len(list_score_LAST) >= 9:
        number_9_last = list_score_LAST[-9]
        number_9_last_text = FONT_scoreboard.render(f"9:  {number_9_last}", 1, "black")
        WINDOW.blit(number_9_last_text, (450,200 + 400))
    if len(list_score_LAST) >= 10:
        number_10_last = list_score_LAST[-10]
        number_10_last_text = FONT_scoreboard.render(f"10: {number_10_last}", 1, "black")
        WINDOW.blit(number_10_last_text, (450,200 + 450))
    
    last_10_last_text = FONT_secondary.render(f"LAST 10", 1, "black")
    WINDOW.blit(last_10_last_text, (425, 150))

# Funkcja wyświetlająca i obsługująca ekran opcji w grze
def options():
    sounds["music"]["background2"].stop()
    sounds["music"]["pause"].play(-1)
    
    BACK_button = Button(20,20,inoptions_back_img,sounds["interactive"]["button_click"],inoptions_back_img_hover)  
    MUSIC_toggle_button_on = Button(440, 299,toggle_on_img, sounds["interactive"]["button_click"], toggle_on_img_hover)
    MUSIC_toggle_button_off = Button(440, 299,toggle_off_img, sounds["interactive"]["button_click"], toggle_off_img_hover)
    
    if music_on:
        MUSIC_toggle_button = MUSIC_toggle_button_on
    else:
        MUSIC_toggle_button = MUSIC_toggle_button_off
    
    EFFECTS_toggle_button_on = Button(600, 400,toggle_on_img, sounds["interactive"]["button_click"], toggle_on_img_hover)
    EFFECTS_toggle_button_off = Button(600, 400,toggle_off_img, sounds["interactive"]["button_click"], toggle_off_img_hover)
    
    if effects_on:
        EFFECTS_toggle_button = EFFECTS_toggle_button_on
    else:
        EFFECTS_toggle_button = EFFECTS_toggle_button_off
    
    # Funkcja wyświetlająca ekran opcji
    def redraw_options():
        WINDOW.blit(background, (0,0))
        WINDOW.blit(inoptions_MUSIC_label_img,(WIDTH/2 - inoptions_MUSIC_label_img.get_width()/2, HEIGHT/2 - 100))
        WINDOW.blit(inoptions_SOUNDEFFECTS_label_img,(WIDTH/2 - inoptions_SOUNDEFFECTS_label_img.get_width()/2, HEIGHT/2))
        BACK_button.draw(WINDOW)
        MUSIC_toggle_button.draw(WINDOW)
        EFFECTS_toggle_button.draw(WINDOW)
        pygame.display.update()
    
    # Funkcja do przełączania stanu muzyki
    def toggle_music():
        global music_on
        global music_volume
        music_on = not music_on
        
        if music_on:
            for music in sounds["music"].values():
                music.set_volume(music_volume)
            MUSIC_toggle_button.image = toggle_on_img
            MUSIC_toggle_button.hover = toggle_on_img_hover
        else:
            for music in sounds["music"].values():
                music.set_volume(0.0)
            MUSIC_toggle_button.image = toggle_off_img
            MUSIC_toggle_button.hover = toggle_off_img_hover
    
    # Funkcja do przełączania stanu efektów dźwiękowych    
    def toggle_effects():
        global effects_on
        global effects_volume
        effects_on = not effects_on

        if effects_on:
            for effect in sounds["effects"].values():
                effect.set_volume(effects_volume)
            EFFECTS_toggle_button.image = toggle_on_img
            EFFECTS_toggle_button.hover = toggle_on_img_hover
        else:
            for effect in sounds["effects"].values():
                effect.set_volume(0.0)
            EFFECTS_toggle_button.image = toggle_off_img
            EFFECTS_toggle_button.hover = toggle_off_img_hover
    
    clicked_music = False
    clicked_effects = False    
    
    # Pętla obsługująca zdarzenia w opcjach
    options_run = True
    while options_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and not clicked_music:
                if event.key == pygame.K_m:
                    toggle_music()
                    clicked_music = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_m:
                        clicked_music = False
            if event.type == pygame.KEYDOWN and not clicked_effects:
                if event.key == pygame.K_n:
                    toggle_effects()
                    clicked_effects = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_n:
                        clicked_effects = False
        
        if BACK_button.update():
            sounds["music"]["pause"].stop()
            menu()
        
        if MUSIC_toggle_button.update():
            toggle_music()
        if EFFECTS_toggle_button.update():
            toggle_effects()
        
        redraw_options()

# Funkcja wyświetlająca i obsługująca ekran statystyk w grze
def scoreboard():
    sounds["music"]["background2"].stop()
    BACK_button = Button(20,20,inoptions_back_img,sounds["interactive"]["button_click"],inoptions_back_img_hover)
    
    scoreboard_list("scoreboard.csv")
    
    # Funkcja do wyświetalnia ekranu scoreboard
    def redraw_scoreboard():
        WINDOW.blit(background, (0,0))
        BACK_button.draw(WINDOW)
        scoreboard_list("scoreboard.csv") 
        pygame.display.update()
    
    # Pętla gry, która kontroluje wyświetlanie i interakcje z ekranem scoreboard
    scoreboard_run = True
    while scoreboard_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if BACK_button.update() == True:
            scoreboard_run = False
            menu()

        redraw_scoreboard()
    
# Funkcja wyświetlająca i obsługująca ekran przegranej w grze        
def gameover():
        global score
        
        with open('scoreboard.csv', "a") as file:
            file.write(str(score) + "\n")
        
        ingameover_RESET_button = Button(WIDTH/2 - ingameover_reset_img.get_width()/2, HEIGHT/2 + 50, ingameover_reset_img, sounds["interactive"]["button_click"], ingameover_reset_img_hover)
        ingameover_MENU_button = Button(WIDTH/2 - ingameover_menu_img.get_width()/2, HEIGHT/2 - 50, ingameover_menu_img, sounds["interactive"]["button_click"], ingameover_menu_img_hover)
        
        # Funkcja do wyświetalnia ekranu
        def redraw_gameover():
            global score
            WINDOW.blit(background,(0,0))
            
            ingameover_RESET_button.draw(WINDOW)
            ingameover_MENU_button.draw(WINDOW)
            
            score_text = FONT_secondary.render(f"Your score: {score}", 1 ,"red")
            WINDOW.blit(score_text, (WIDTH/2 - score_text.get_width()/ 2, HEIGHT / 2 - 150))
            
            gameover_text = FONT_main.render("GAMEOVER", 1, "white")
            WINDOW.blit(gameover_text,(WIDTH/2 - gameover_text.get_width()/2,HEIGHT/2 - gameover_text.get_height()/2 - 200))
            
            pygame.display.update()
        
         # Pętla główna obsługująca zdarzenia
        gameover_run = True
        while gameover_run:
            redraw_gameover()
            
            sounds["music"]["pause"].play(-1)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover_run = False
                    quit()
                # Obsługa przycisku RESET (nowa gra)
                if ingameover_RESET_button.update():
                    sounds["music"]["pause"].stop()
                    sounds["music"]["background1"].play(-1)
                    game()
                # Obsługa przycisku MENU (powrót do menu)
                if ingameover_MENU_button.update() == True:
                    sounds["music"]["pause"].stop()
                    while pygame.mouse.get_pressed()[0] == 1:
                        pygame.event.pump()
                    menu()

# Funkcja wyświetlająca i obsługująca ekran pauzy w grze     
def pause():            
        global game_run
        global score
        global level
        
        play_pause_button_inpause = Button(15,10,ingame_pause_button_hover, sounds["interactive"]["button_click"], ingame_pause_button)
        ingame_backtomenu_button = Button(WIDTH/2 - ingame_backtomenu_img.get_width()/2, HEIGHT/2 - 100, ingame_backtomenu_img, sounds["interactive"]["button_click"], ingame_backtomenu_img_hover)
        play_pause_button = Button(15,10,ingame_pause_button, sounds["interactive"]["button_click"], ingame_pause_button_hover)
        
        # Funkcja do wyświetlania ekranu pauzy
        def redraw_pause():
                play_pause_button_inpause.draw(WINDOW)
                ingame_backtomenu_button.draw(WINDOW)
                
                paused_text = FONT_main.render("PAUZA", 1 ,"white")
                WINDOW.blit(paused_text, (WIDTH/2 - paused_text.get_width()/2, HEIGHT/2 - 250))
                
                pygame.display.update()
        
        # Pętla główna dla pauzy
        paused = True        
        while paused:
            active = True
            sounds["music"]["background1"].stop()
            sounds["music"]["pause"].play(-1)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused = False
                    quit()
                
                if play_pause_button.update() == True and paused == True :
                    paused = False
                    active = False
                    sounds["interactive"]["button_click"].play()
                    sounds["music"]["pause"].stop()
                    sounds["music"]["background1"].play(-1)
                # Obsługa wznowienia przez klawisz 'O'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o and paused == True:
                        paused = False
                        active = False
                        sounds["music"]["pause"].stop()
                        sounds["music"]["background1"].play(-1)
                # Obsługa przycisku powrotu do menu
                if ingame_backtomenu_button.update() == True:
                    sounds["music"]["pause"].stop()
                    game_run= False
                    paused = False
                
                # Zapisanie wyniku do pliku scoreboard.csv
                    with open('scoreboard.csv', "a") as file:
                        file.write(str(score) + "\n")
                
                    while pygame.mouse.get_pressed()[0] == 1:
                        pygame.event.pump()
                
                    menu()
                    
            redraw_pause()
        
        return active

def game():
    global score
    global lives
    global level
    score = 0
    lives = 5
    level = 0
    game_run = True
    FPS = 60
    clock = pygame.time.Clock()

    sounds["music"]["background1"].play(-1)

    level = 0
    
    lost = False
    lost_counter = 0
    
    # Inicjalizacja zmiennych związanych z falami przeciwników, meteorytów, bonusów, itd.
    wave_length_enemy = 0
    wave_length_meteo = 0
    wave_length_bonus = 0
    wave_length_add_health = 0
    wave_length_bomb = 0
    enemies = []
    meteos = []
    bonusy = []
    add_health = []
    bombs = []
    
    # Inicjalizacja gracza
    player = Player(WIDTH/2 - PLAYER_WIDTH/2, HEIGHT-105)
    
    play_pause_button = Button(15,10,ingame_pause_button, sounds["interactive"]["button_click"], ingame_pause_button_hover)
    
    # Funkcja wyświetlająca ekran gry
    def redraw_game():
        WINDOW.blit(background, (0,0))
        
        # Rysowanie poziomu
        level_text = FONT_level_ingame.render(f"{level}", 1, "white")
        level_text.set_alpha(150)
        WINDOW.blit(level_text, (WIDTH/2 - level_text.get_width()/2, HEIGHT/2 - 200))
        
        # Rysowanie wyniku
        score_text = FONT_secondary.render(f"Score: {score}", 1, "white")
        WINDOW.blit(score_text, (WIDTH/2 - score_text.get_width()/2, 20))
        
        # Rysowanie żyć gracza
        if lives == 5:
            WINDOW.blit(hearts_5, (WIDTH - 90, 30))
        elif lives == 4:
            WINDOW.blit(hearts_4, (WIDTH - 90, 30))    
        elif lives == 3:
            WINDOW.blit(hearts_3, (WIDTH - 90, 30))    
        elif lives == 2:
            WINDOW.blit(hearts_2, (WIDTH - 90, 30))    
        elif lives == 1:
            WINDOW.blit(hearts_1, (WIDTH - 90, 30))    
        elif lives == 0:
            WINDOW.blit(hearts_0, (WIDTH - 90, 30))    
    
        # Rysowanie przycisku pauzy
        play_pause_button.draw(WINDOW)        
        
        # Rysowanie wszystkich obiektów w grze
        for enemy in enemies:
            enemy.draw(WINDOW)
        for meteo in meteos:
            meteo.draw(WINDOW)
        for bonus in bonusy:
            bonus.draw(WINDOW)
        for hearth in add_health:
            hearth.draw(WINDOW)
        for bomb in bombs:
            bomb.draw(WINDOW)
        
        # Rysowanie gracza
        player.draw(WINDOW)        

        pygame.display.update()

    # Funkcja do przełączania muzyki
    def toggle_music():
        global music_on
        global music_volume
        music_on = not music_on
        
        # Ustawianie głośności w zależności od stanu
        if music_on:
            for music in sounds["music"].values():
                music.set_volume(music_volume)
        else:
            for music in sounds["music"].values():
                music.set_volume(0.0)

    def toggle_effects():
        global effects_on
        global effects_volume
        effects_on = not effects_on
        
        # Ustawianie głośności efektów dźwiękowych w zależności od stanu
        if effects_on:
            for effect in sounds["effects"].values():
                effect.set_volume(effects_volume)
        else:
            for effect in sounds["effects"].values():
                effect.set_volume(0.0)
    
    # Główna pętla gry
    while game_run:
        clock.tick(FPS)     # Kontrolowanie liczby klatek na sekundę
        redraw_game()
        
        if lives <= 0:
            lost = True
            lost_counter += 1
            
        if lost == True:
            if lost_counter == 1:
                sounds["effects"]["player_dies"].play()
                sounds["music"]["background1"].stop()
                gameover()
            else:
                continue
        
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
                quit()
            
            if event.type == pygame.KEYDOWN and not clicked:
                if event.key == pygame.K_m:
                    toggle_music()
                    clicked = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    clicked = False
                    
            if event.type == pygame.KEYDOWN and not clicked:
                if event.key == pygame.K_n:
                    toggle_effects()
                    clicked = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    clicked = False
        
        if play_pause_button.update() == True:
            pause()
        
        keys = pygame.key.get_pressed()
        
        # Jeśli naciśnięto P, pauzujemy grę
        if keys[pygame.K_p]:
            pause()
        
        # Ruch gracza
        if keys[pygame.K_a] and player.x >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_s] and player.y + PLAYER_HEIGHT < HEIGHT:
            player.y += PLAYER_VEL - 2
        if keys[pygame.K_w] and player.y > 0 and player.y > HEIGHT/2:
            player.y -= PLAYER_VEL - 2
        
        # Jeśli naciśnięto spację, gracz strzela
        if keys[pygame.K_SPACE]:
            player.create_lasers()   
        
        # Sprawdzanie, czy należy przejść do kolejnego poziomu
        if len(enemies) == 0:
            level += 1
            sounds["effects"]["level_up"].play()
            wave_length_enemy += 5
            if level <= 3:
                for x in range(round(wave_length_enemy/2), wave_length_enemy):
                    enemy = Enemy(random.randrange(50,WIDTH-50),random.randrange(-200, -100))
                    enemies.append(enemy)
            if level > 3 and level <= 6:
                for x in range(round(wave_length_enemy/2), wave_length_enemy):
                    enemy = Enemy(random.randrange(50,WIDTH-50),random.randrange(-700, -150))
                    enemies.append(enemy)
            if level > 6 and level <= 9:
                for x in range(round(wave_length_enemy/2), wave_length_enemy):
                    enemy = Enemy(random.randrange(50,WIDTH-50),random.randrange(-1200, -200))
                    enemies.append(enemy)
            if level > 9 and level <= 12:
                for x in range(round(wave_length_enemy/2), wave_length_enemy):
                    enemy = Enemy(random.randrange(50,WIDTH-50),random.randrange(-2000, -300))
                    enemies.append(enemy)
            if level > 12 and level <= 15:
                for x in range(round(wave_length_enemy/2), wave_length_enemy):
                    enemy = Enemy(random.randrange(50,WIDTH-50),random.randrange(-2600, -350))
                    enemies.append(enemy)
            if level > 15:
                for x in range(round(wave_length_enemy/2), wave_length_enemy):
                    enemy = Enemy(random.randrange(50,WIDTH-50),random.randrange(-4000, -500))
                    enemies.append(enemy)        
        # Ruch przeciwników
        for enemy in enemies[:]:
            enemy.move(ENEMY_VEL)
            # Ruch laserów przeciwnika
            enemy.move_lasers(ENEMY_LASER_VEL, player)
            if enemy.y > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
            if player.mask.overlap(enemy.mask, (enemy.x - player.x, enemy.y - player.y)):
                sounds["effects"]["enemy_dies"].play()
                lives -= 1
                enemies.remove(enemy)
            
            if random.randrange(0, 4*60) == 1:
                enemy.create_lasers()
        
        # Ruch laserów gracza       
        player.move_lasers(-PLAYER_LASER_VEL, enemies)
           
        # Spawnowanie meteorytów, bonusów i innych obiektów w zależności od poziomu
        if len(meteos) == 0 and len(enemies) == 0:
            wave_length_meteo += 2
            for x in range(round(wave_length_meteo/2), wave_length_meteo):
                meteo = Meteo(random.randrange(50,WIDTH-50),random.randrange(-3000, -100))
                meteos.append(meteo)
        for meteo in meteos[:]:
            meteo.move(METEO_VEL)
            if meteo.y > HEIGHT:
                meteos.remove(meteo)
            elif player.mask.overlap(meteo.mask, (meteo.x - player.x, meteo.y - player.y)):
                lives -= 3
                meteos.remove(meteo)
    
        if len(bonusy) == 0 and len(enemies) == 0:
                if level >= 3:
                    wave_length_bonus += 1
                if level > 3 and level <= 6:
                    for x in range(round(wave_length_bonus/2), wave_length_bonus):
                        bonus = Bonus(random.randrange(50,WIDTH-50),random.randrange(-2000, -500))
                        bonusy.append(bonus)
                if level > 6 and level <= 9:
                    for x in range(round(wave_length_bonus/2), wave_length_bonus):
                        bonus = Bonus(random.randrange(50,WIDTH-50),random.randrange(-4000, -1000))
                        bonusy.append(bonus)
                if level > 9 and level <= 12:
                    for x in range(round(wave_length_bonus/2), wave_length_bonus):
                        bonus = Bonus(random.randrange(50,WIDTH-50),random.randrange(-6000, -1500))
                        bonusy.append(bonus)
                if level > 12 and level <= 15:
                    for x in range(round(wave_length_bonus/2), wave_length_bonus):
                        bonus = Bonus(random.randrange(50,WIDTH-50),random.randrange(-8000, -2000))
                        bonusy.append(bonus)
                if level > 12 and level <= 15:
                    for x in range(round(wave_length_bonus/2), wave_length_bonus):
                        bonus = Bonus(random.randrange(50,WIDTH-50),random.randrange(-10000, -2500))
                        bonusy.append(bonus)
                if level > 15:
                    for x in range(round(wave_length_bonus/2), wave_length_bonus):
                        bonus = Bonus(random.randrange(50,WIDTH-50),random.randrange(-12000, -3000))
                        bonusy.append(bonus)
        for bonus in bonusy[:]:
            bonus.move(BONUS_VEL)
            if bonus.y > HEIGHT:
                bonusy.remove(bonus)
            elif player.mask.overlap(bonus.mask, (bonus.x - player.x, bonus.y - player.y)):
                sounds["effects"]["bonus"].play()
                bonusy.remove(bonus)
                score += 3
        
        if len(add_health) == 0 and len(enemies) == 0:
            if level >= 5:
                wave_length_add_health += 2
            if level >= 5 and level <= 6:   
                for x in range(round(wave_length_add_health/2), wave_length_add_health):
                    add_health_var = HEART(random.randrange(50,WIDTH-50),random.randrange(-4000, -500))
                    add_health.append(add_health_var)
            if level > 6 and level <= 9:   
                for x in range(round(wave_length_add_health/2), wave_length_add_health):
                    add_health_var = HEART(random.randrange(50,WIDTH-50),random.randrange(-5000, -700))
                    add_health.append(add_health_var)
            if level > 9 and level <= 12:   
                for x in range(round(wave_length_add_health/2), wave_length_add_health):
                    add_health_var = HEART(random.randrange(50,WIDTH-50),random.randrange(-6000, -900))
                    add_health.append(add_health_var)
            if level > 12 and level <= 15:   
                for x in range(round(wave_length_add_health/2), wave_length_add_health):
                    add_health_var = HEART(random.randrange(50,WIDTH-50),random.randrange(-7000, -1100))
                    add_health.append(add_health_var)
            if level > 15:   
                for x in range(round(wave_length_add_health/2), wave_length_add_health):
                    add_health_var = HEART(random.randrange(50,WIDTH-50),random.randrange(-8000, -1500))
                    add_health.append(add_health_var)
        for add_health_var in add_health[:]:
            add_health_var.move(ADD_HEALTH_VEL)
            if add_health_var.y > HEIGHT:
                add_health.remove(add_health_var)
            elif player.mask.overlap(add_health_var.mask, (add_health_var.x - player.x, add_health_var.y - player.y)):
                add_health.remove(add_health_var)
                if lives < 5 and lives > 0:
                    lives += 1
        
        if len(bombs) == 0 and len(enemies) == 0:
            if level >= 5:
                wave_length_bomb += 1
            if level >= 5 and level <= 6:    
                for x in range(round(wave_length_bomb/2), wave_length_bomb):
                    bomb = BOMB(random.randrange(50,WIDTH-50),random.randrange(-4000, -500))
                    bombs.append(bomb)
            if level >= 6 and level <= 9:    
                for x in range(round(wave_length_bomb/2), wave_length_bomb):
                    bomb = BOMB(random.randrange(50,WIDTH-50),random.randrange(-5000, -700))
                    bombs.append(bomb)
            if level >= 9 and level <= 12:    
                for x in range(round(wave_length_bomb/2), wave_length_bomb):
                    bomb = BOMB(random.randrange(50,WIDTH-50),random.randrange(-6000, -900))
                    bombs.append(bomb)
            if level >= 12 and level <= 15:    
                for x in range(round(wave_length_bomb/2), wave_length_bomb):
                    bomb = BOMB(random.randrange(50,WIDTH-50),random.randrange(-7000, -1100))
                    bombs.append(bomb)
            if level > 15:    
                for x in range(round(wave_length_bomb/2), wave_length_bomb):
                    bomb = BOMB(random.randrange(50,WIDTH-50),random.randrange(-8000, -1500))
                    bombs.append(bomb)
        for bomb in bombs[:]:
            bomb.move(BOMB_VEL)
            if bomb.y > HEIGHT:
                bombs.remove(bomb)
            elif player.mask.overlap(bomb.mask, (bomb.x - player.x, bomb.y - player.y)):
                bombs.remove(bomb)
                lives -= 5
            
def menu():
    FPS = 60
    clock = pygame.time.Clock()
    sounds["music"]["background2"].play(-1)
    
    # Tworzenie przycisków menu
    start_button = Button(WIDTH/2-BUTTON_WIDTH/2, HEIGHT/2-100, start_img, sounds["interactive"]["button_click"], start_img_hover)
    options_button = Button(WIDTH/2-BUTTON_WIDTH/2, HEIGHT/2, options_img, sounds["interactive"]["button_click"], options_img_hover)
    quit_button = Button(WIDTH/2-BUTTON_WIDTH/2, HEIGHT/2+100, quit_img, sounds["interactive"]["button_click"], quit_img_hover)
    scoreboard_button = Button(WIDTH/2-scoreboard_img.get_width()/2 - 175, HEIGHT/2-90, scoreboard_img, sounds["interactive"]["button_click"], scoreboard_img_hover)
    
    # Funkcja wyświetlająca ekran menu
    def redraw_menu():
        WINDOW.blit(background, (0,0))
        WINDOW.blit(game_banner,(WIDTH/2 - 300 ,10))
        start_button.draw(WINDOW)
        options_button.draw(WINDOW)
        quit_button.draw(WINDOW)
        scoreboard_button.draw(WINDOW)
        
        pygame.display.update()
    
    menu_run = True
    while menu_run:
        clock.tick(FPS)
        
        # Sprawdzanie, który przycisk został kliknięty
        if start_button.update() == True:
            sounds["music"]["background2"].stop()
            game()
        if options_button.update() == True:
            options()
        if quit_button.update() == True:
            menu_run = False
            quit()
        if scoreboard_button.update() == True:
            menu_run = False
            scoreboard()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_run = False
                quit()
        
        redraw_menu()

menu()