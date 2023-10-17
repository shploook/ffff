from pygame import *
from random import randint
from time import time as timer
#создай окно игры
window = display.set_mode((800,800))
display.set_caption("пальба")
background = transform.scale(image.load("fon.jpg"), (800,800))
font.init()
font = font.Font(None,70)

class Gamer(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Player(Gamer):
    def Control(self):
        control = key.get_pressed()
        
            
        if control[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if control[K_s] and self.rect.y < 700:
            self.rect.y += self.speed
    def fire(self):
        bullets = Bullets('bullet.png',self.rect.x,self.rect.y,5)
        bullet.add(bullets)
            
    def Control1(self):
        control = key.get_pressed()
        if control[K_o] and self.rect.y > 0:
            self.rect.y -= self.speed
        if control[K_l] and self.rect.y < 700:
            self.rect.y += self.speed
    def fire1(self):
        bullets = Bullets1('bullet1.png',self.rect.x,self.rect.y,5)
        bullet1.add(bullets)
            
class Bullets(Gamer):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >800:
            self.kill()
class Bullets1(Gamer):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <0:
            self.kill()


tank1 = Player('tanklevo.png',25,400,5)
tank2= Player('tankpravo.png',700,400,5)
bullet= sprite.Group()
bullet1=sprite.Group()

#задай фон сцены
Finish=False
game = True
clock = time.Clock()
reload = False
num_bullet = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_e:
                if num_bullet <5 and reload == False:
                    num_bullet +=1
                    tank1.fire()
                    
                if num_bullet >=5 and reload == False:
                    reload = True
                    reload_time = timer()
                    
        if e.type == KEYDOWN:
            if e.key == K_p:
                if num_bullet <5 and reload == False:
                    num_bullet +=1
                    tank2.fire1()
                    
                if num_bullet >=5 and reload == False:
                    reload = True
                    reload_time = timer()
                    
                    
                    
    if Finish != True:
        window.blit(background,(0,0))
        
        tank1.reset()
        tank1.Control()
        tank2.reset()
        tank2.Control1()
        
        bullet.draw(window)
        bullet.update()
        
        bullet1.draw(window)
        bullet1.update()
        
        if reload == True:
            new_time = timer()
            if new_time-reload_time <0.5:
                reload_text = font.render('reload',True,(randint(1,255),randint(1,255),randint(1,255)))
                window.blit(reload_text,(500,500))
            else:
                num_bullet=0
                reload = False
    

    display.update()
    clock.tick(60)