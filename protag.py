import pygame

#Define player class
class Player:
    def __init__(self):
        self.name = "Player"
        self.health = 100
        self.damage = 20
        self.abilities = ["Slash", "Heal"]
        self.items = ["Health Potion", "Mana Potion"]
        
    def draw(self, screen):
        #Draw player character using pixels
        pygame.draw.circle(screen, (255, 255, 255), (100, 100), 25)  # Head
        pygame.draw.rect(screen, (255, 255, 255), (80, 120, 40, 125))  # Torso
        pygame.draw.rect(screen, (255, 255, 255), (70, 140, 20, 200))  # Left leg
        pygame.draw.rect(screen, (255, 255, 255), (110, 140, 20, 200))  # Right leg
        pygame.draw.rect(screen, (255, 255, 255), (180, 120, 10, 150))  # Left arm
        pygame.draw.rect(screen, (255, 255, 255), (120, 120, 10, 150))  # Right arm
        
        #Draw player name
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(self.name, True, (255, 255, 255))
        screen.blit(text, (100, 100))
        
        #Draw player stats
        stats = f"HP: {self.health}  DMG: {self.damage}"
        text = font.render(stats, True, (255, 255, 255))
        screen.blit(text, (100, 120))

#Initialize Pygame and create game window
pygame.init()
screen = pygame.display.set_mode((800, 600))

#Create player character
player = Player()

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #Draw background
    screen.fill((0, 0, 0))
    
    #Draw player character
    player.draw(screen)
    
    #Update game screen, handle input
    pygame.display.update()
