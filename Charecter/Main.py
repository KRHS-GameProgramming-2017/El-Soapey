import from player *
import from npc *
import from boss *
import from score *
import from health *
import from background *
pygame.init()

clock = pygame.time.Clock()

size = [width, height] = 800, 600
screen = pygame.display.set_mode(size)

bgColor = [r, g, b] = [138, 138, 138]


players = pygame.sprite.Group()
blocks = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Player.containers = (all, balls)
Block.containers = (all, blocks)

players = Player([random.randint(0,width/4), random.randint(0, height/5)])
