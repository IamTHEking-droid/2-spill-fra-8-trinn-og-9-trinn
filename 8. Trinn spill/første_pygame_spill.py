import pygame, time
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player = pygame.image.load("Graphics/player_walk_1.png").convert_alpha()
        player = pygame.transform.rotozoom(player,0,1.2)
        player_surf2 = pygame.image.load("Graphics/player_walk_2.png").convert_alpha()
        player_surf2 = pygame.transform.rotozoom(player_surf2,0,1.2)
        self.player_jump = pygame.image.load("Graphics/jump.png").convert_alpha()
        self.player_jump = self.player_jump = pygame.transform.rotozoom(self.player_jump,0,1.2)
        self.crouch = pygame.image.load("Graphics/slide3.png")
        self.y = 1
        self.crouch = pygame.transform.rotozoom(self.crouch,0,1)
        self.player_walk =[player,player_surf2]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (200,710))
        self.gravity = 0
        self.crouching = False
        self.jump_sound = pygame.mixer.Sound("Audio/jump.mp3")
        self.jump_sound.set_volume(0.5)
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 710 and  self.crouching ==False or keys[pygame.K_UP] and self.rect.bottom >= 710 and self.crouching ==False:
            self.jump_sound.play()
            self.gravity = x
        if keys[pygame.K_DOWN] and self.rect.bottom >= 710:
            self.image = self.crouch
            
            self.crouching = True
            self.rect = self.image.get_rect(midbottom = (200,710))
       
        
        if keys[pygame.K_DOWN] and self.rect.bottom >= 710:
            self.image = self.crouch
            
            self.crouching = True
            self.rect = self.image.get_rect(midbottom = (200,710))
        else:
            self.crouching = False
            
    def apply_gravity(self):
        self.gravity += self.y
        self.rect.y += self.gravity
        if self.rect.bottom >= 710:
            self.rect.bottom = 710
    def movement(self):
        if self.rect.bottom < 710:
            self.image = self.player_jump
        elif self.crouching == False:
            self.player_index += 0.1
            self.rect = self.image.get_rect(midbottom = (200,710))
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]    
        
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.movement()
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == "fly":
            fly1 = pygame.image.load("Graphics/Fly1.png").convert_alpha()
            fly1 = pygame.transform.rotozoom(fly1,0,1.1)
            fly2 = pygame.image.load("Graphics/Fly2.png").convert_alpha()
            fly2 = pygame.transform.rotozoom(fly2,0,1.1)
            self.frames = [fly1, fly2]
            y_pos =550
            
            self.l = 6
            self.y = True 
        if type == "snail":
            snail1 = pygame.image.load("Graphics/snail1.png").convert_alpha()
            snail1 = pygame.transform.rotozoom(snail1,0,1.1)
            snail2 = pygame.image.load("Graphics/snail2.png").convert_alpha()
            snail2 = pygame.transform.rotozoom(snail2,0,1.1)
            self.frames =[snail1, snail2]
            self.l = 6
            self.y = True 
            y_pos = 710
        if type == "bullet":
            self.bullet = pygame.mixer.Sound("Audio/pew.mp3")
            self.bullet.set_volume(2)
            self.bullet.play()
            bullet = pygame.image.load("Graphics/bullet(2).png")
            bullet2 =pygame.image.load("Graphics/bullet(3).png")
            self.frames = [bullet,bullet2]
            self.l = 15
            y_pos = 630
            self.y = False 
        self.movement_index =0
        self.image = self.frames[self.movement_index]
        self.rect = self.image.get_rect(midbottom = (randint(1450,1550),y_pos))
    def movement(self):
        self.movement_index +=0.1
        if self.movement_index>= len(self.frames):
            self.movement_index = 0
        self.image= self.frames[int(self.movement_index)]
    def update(self):
        self.movement()
        self.rect.x -= self.l
        self.destroy()
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
        if self.rect.x <= -2 and phase6 or self.rect.x <= -2 and phase5 or self.rect.x <= -2 and phase7 or self.rect.x <= -2 and phase8: 
            self.rect.x=1250
class Chest(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image = pygame.image.load("Graphics/chest.png")
        self.image = pygame.transform.rotozoom(self.image,0,5)
        self.rect = self.image.get_rect(midbottom = (randint(1250,1400),710))
        chest1 =  pygame.image.load("Graphics/chest (1).png")
        chest1 =  pygame.transform.rotozoom(chest1,0,5)
    def update(self):
        self.rect.x -=6
        self.chestmash()
        self.destroy()
        self.chestmove()
        self.chestmove1()
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
    def chestmash(self):
        if pygame.sprite.spritecollide(player.sprite,chest_group,False): 
            self.rect.y -=1
            self.image = pygame.image.load("Graphics/chest (1).png")
            self.image =  pygame.transform.rotozoom(self.image,0,5)
    def chestmove(self):
        if self.rect.x < -2 and game_over:
            self.rect.x = randint(1250,1400)
    
    def chestmove1(self):
        if self.rect.x < -2:
            chestin = False
    
            
class ability(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        global phase5,phase6,phase7,phase,phase8,ti,phase9,tim91,tim9
        
        self.b = type 
        if self.b == "bird":
            self.bird1= pygame.image.load("Graphics/Bird1.png")
            self.bird2 = pygame.image.load("Graphics/Bird2.png")
            self.bird3 = pygame.image.load("Graphics/bird3.png")
            self.bird_index = [self.bird1,self.bird3,self.bird3,self.bird2,self.bird3,self.bird3]
            self.image = self.bird1
            self.rect = self.image.get_rect(center =(100,200))
            self.mi = 0
            self.t = False
            self.i = False
        if self.b == "bowling":
            self.b1=pygame.image.load("Graphics/Bowling_rolling_1.png")
            self.b2 =pygame.image.load("Graphics/Bowling_rolling_2.png")
            self.b3 = pygame.image.load("Graphics/Bowling_rolling_3.png")
            self.b4 =pygame.image.load("Graphics/Bowling_rolling_4.png")
            self.b_index = [self.b1,self.b3,self.b3,self.b2,self.b3,self.b3,self.b4,]
            self.image = self.b1
            self.rect = self.image.get_rect(center =(100,200))
            self.mi = 0
            self.t = False
            self.i = False
            self.num = 3
        if self.b== "bullet":
            self.b1=pygame.image.load("Graphics/bull1.png")
            self.b2 =pygame.image.load("Graphics/bull2.png")
            self.b_index= [self.b1,self.b2]
            self.mi = 0
            self.image = self.b1
            self.rect = self.image.get_rect(center =(100,200))
            self.t = False
            self.i = False
        if self.b == "sheild":
            self.image = pygame.image.load("Graphics/shield.png")
            self.rect = self.image.get_rect(center =(100,200))
            self.tall = 3
    def update(self):
        global phase5,phase6,phase7,phase8,phase,ti,phase9,tim91,tim9
        self.movement()
        self.destroy() 
        if self.b == "bird" and self.t:
            self.rect.x +=6 
            self.image = self.bird_index[int(self.mi)]
            self.mi +=0.2
            if self.mi > len(self.bird_index):
                self.mi = 0
        if self.b == "bowling" and self.t:
            self.rect.x +=6 
            self.image = self.b_index[int(self.mi)]
            self.mi +=0.2
            if self.mi > len(self.b_index):
                
                self.mi = 0
        if self.b == "bullet" and self.t:
            self.rect.x +=15
            self.image = self.b_index[int(self.mi)]
            self.mi +=0.2
            if self.mi > len(self.b_index):
                
                self.mi = 0
       
    def movement(self):
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            
            if self.b == "bird": 
                self.t =True
                if self.i == False:
                    self.rect.y += 350
                    self.i = True
            if self.b == "bowling": 
                self.t =True
                if self.i == False:
                    self.rect.y += 475
                    self.i = True
            if self.b == "bullet": 
                self.t =True
                if self.i == False:
                    self.rect.y += 405
                    self.i = True
            if self.b == "sheild":
                self.rect = self.image.get_rect(center =(300,650))
                self.i = True
    def destroy(self):
        global phase5,phase6,phase7,phase8,phase,ti,phase9,tim91,tim9
        xy = pygame.sprite.spritecollide(ability1.sprite,obstacle_group,True)
        if phase8 and xy:
            ability1.empty()
            obstacle_group.empty()
            tim91=300
            tim9 = True
            phase9 = True
            phase8= False
            
             
            
        if phase7 and xy:
            ability1.empty()
            obstacle_group.empty()  
            phase7= False
            phase8 = True
            
        if phase6 and xy:
            ability1.empty()
            obstacle_group.empty()  
            phase6= False
            phase7 = True
        if phase5 and xy:
            ability1.empty()
            obstacle_group.empty()  
            phase5= False
            phase6 = True
        
            
        
            
            
    
        if self.b == "bullet" and xy:
            self.kill()
        if self.rect.x >= 1450:
            self.kill()
        if self.b == "sheild" and xy:
            self.tall-=1
            
        if self.b == "sheild" and self.tall <=0:
            self.kill()
        if self.b == "sheild" and self.tall == 2:
            self.image = pygame.image.load("Graphics/shield1.png")
        if self.b == "sheild" and self.tall == 1:
            self.image = pygame.image.load("Graphics/shield2.png")
        if self.b == "bowling" and xy:
            self.num -=1
        if self.b == "bowling" and self.num <=0:
            self.kill()

def showscore():
    time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = text_font.render("Score:"+ str(time) ,False,"Red")
    score_rect = score_surf.get_rect(center = (600,200))
    screen.blit(score_surf,score_rect)
    return time


def collision_sprite():
    global death_count
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
        death.play()
        obstacle_group.empty()
        death_count+=1
             
        
        return False

    else:
        return True


            

pygame.init()


# Variabler for screen og lage en screen
screen = pygame.display.set_mode((1200,775))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
score=0
start_time=0
text_font = pygame.font.Font("font/pxt.ttf",100)
# Andre variabler
yuo = 60
hit = False          
x = -22    
chestin = False
times = 0
a = False
phase1 = False
l = 0
death_count= 0


lai = False
h=True
ful = 0
b_s = 0
c1 = False
c2 =False
c3 = False
c4 = False

#bilder
player_stand = pygame.image.load("Graphics/player_stand.png").convert_alpha()
player_stand2 = pygame.transform.scale(player_stand,(400,600))
player_rect2 = player_stand2.get_rect(center= (600,450))
test_surface  = pygame.image.load("Graphics/back.jpg").convert_alpha()
ground_surface = pygame.image.load("Graphics/ground.png").convert_alpha()
ground2= pygame.image.load("Graphics/ground.png").convert_alpha()
back1 = pygame.image.load("Graphics/back2.png").convert_alpha()
#tekster

start_game = text_font.render("CLICK ON THIS TO PLAY",False,"Blue")
startgame_rect = start_game.get_rect(center = (600,650))
how = text_font.render("How to play",False,"Blue")
how_rect = start_game.get_rect(center = (800,550))

start_text = text_font.render("PIXEL RUNNER",False,"Blue")
start_rect=start_text.get_rect(center = (600,100))

speed_up= text_font.render("You have died " +str(death_count) + " times",False,"red")
speed_rect =speed_up.get_rect(center= (600,550))
chose1= text_font.render("Easy",False,"Blue")
chose11=start_text.get_rect(center = (300,100))
chose2= text_font.render("Normal",False,"Blue")
chose22=start_text.get_rect(center = (550,100))
chose3= text_font.render("Hard",False,"Blue")
chose33=start_text.get_rect(center = (850,100))
chose4= text_font.render("Impossible",False,"Blue")
chose44=start_text.get_rect(center = (1050,100))
#game phases
game_start = True
game_over = False 
game = False
game_2 = False
tms = False 
once = False
print("if you get any errors like the tutorial stopping up, try running the code again and wait a bit before you use the items")


#Groups                          
player = pygame.sprite.GroupSingle()
player.add(Player())
ability1 = pygame.sprite.GroupSingle()

obstacle_group = pygame.sprite.Group()
#lyder

chest_group = pygame.sprite.Group()
chestsound = pygame.mixer.Sound("Audio/12_3.mp3")
death = pygame.mixer.Sound("Audio/death.mp3")
chestsound.set_volume(4)
bg_music = pygame.mixer.Sound("Audio/music.wav")
bg_music.set_volume(0.5)
bg_music.play(loops = -1)
#phases og variabler i tutorial
r = 1
ail = True 
score = 0
l2 = 1200
phase = False
phase1 = True
phase2 = False
phase3 = False
phase4 = False
phase5 = False
phase6 = False
phase7 =False
phase8 = False
phase9 = False 
tim2 =False
tim31=True 
tim = 300
tim21 = 0
tim3=0
tim32 = 0
tim4 = 0
tim5 = 0
tim51 = False
tim52 = False
tim53 = False
tim54 = False
tim61 = False
tim62 = False
tim63 = False
tim64 = False
tim71 = False
tim72 = False
tim73 = False
tim74 = False
tim81 = False
tim82 = False
tim83 = False
tim84 = False
tim9 = False
tim91 = 0
ti = 0

while True:        
    if game_start ==True:
        l = 0
        l2 = 1200
        chestin = False
        yuo = 60
        times = 0
        x = -22
        b = ""
        game_over = False
        player_gravity = 0
        screen.fill((94,129,162))
        ability1.empty()
        chest_group.empty()
        screen.blit(player_stand2,player_rect2)
        scoremessage = text_font.render("Your score was "+ str(score),False,"Blue")
        scorem=scoremessage.get_rect(center = (600,100))
        
        screen.blit(start_game,startgame_rect)
        keys = pygame.mouse.get_pressed()
       
        #if keys[pygame.K_b]:
            #phase1 =True 
            #game_start = False 
        if score ==0:
            screen.blit(start_text,start_rect)
            
            
        else:    
            
            screen.blit(scoremessage,scorem)
                
                
        
        if startgame_rect.collidepoint(pygame.mouse.get_pos()) and keys[0]:
            game_start = False                    
            game_2 = True
            
        
    if game_2 == True:
        screen.fill((94,129,162))
        screen.blit(player_stand2,player_rect2)
        screen.blit(chose1,chose11)
        screen.blit(chose2,chose22)
        screen.blit(chose3,chose33)
        screen.blit(chose4,chose44)
        l = 0
        l2 = 1200
        chestin = False
        yuo = 60
        times = 0
        x = -22
        b = ""
        game_over = False
        player_gravity = 0
        obstacle_group.empty()
        chest_group.empty()
        ability1.empty()
        if tms == False:
            screen.blit(how,how_rect)
        
        keys = pygame.mouse.get_pressed()
        if chose11.collidepoint(pygame.mouse.get_pos()) and keys[0]:
            obstacle_timer =pygame.USEREVENT + 1
            pygame.time.set_timer(obstacle_timer,3000)
            bullet_timer =pygame.USEREVENT + 2
            pygame.time.set_timer(bullet_timer,randint(3000,7000))
            game_start = False
            game_over = False 
            game = True
            game_2 = False
            start_time = int(pygame.time.get_ticks() / 1000)
            l = 0
            l2 = 1200
            c1 = True 
            c2 =False
            c3 = False
            c4 = False
        if chose22.collidepoint(pygame.mouse.get_pos()) and keys[0]:
            
            obstacle_timer =pygame.USEREVENT + 1
            pygame.time.set_timer(obstacle_timer,1250)
            bullet_timer =pygame.USEREVENT + 2
            pygame.time.set_timer(bullet_timer,randint(3000,7000))
            game_start = False
            game_over = False 
            game = True
            game_2= False
            l = 0
            l2 = 1200
            c1 = False
            c2 =True 
            c3 = False
            c4 = False
            start_time = int(pygame.time.get_ticks() / 1000)
        if chose33.collidepoint(pygame.mouse.get_pos()) and keys[0]:
            obstacle_timer =pygame.USEREVENT + 1
            pygame.time.set_timer(obstacle_timer,775)
            bullet_timer =pygame.USEREVENT + 2
            pygame.time.set_timer(bullet_timer,7000)
            game_start = False
            game_over = False 
            game = True
            game_2 = False
            l = 0
            l2 = 1200
            c1 = False
            c2 =False
            c3 = True 
            c4 = False
            start_time = int(pygame.time.get_ticks() / 1000)
        if chose44.collidepoint(pygame.mouse.get_pos()) and keys[0]:
            obstacle_timer =pygame.USEREVENT + 1
            pygame.time.set_timer(obstacle_timer,750)
            bullet_timer =pygame.USEREVENT + 2
            pygame.time.set_timer(bullet_timer,100)
            game_start = False
            game_over = False 
            game = True
            game_2 = False
            start_time = int(pygame.time.get_ticks() / 1000)
            l = 0
            l2 = 1200
            c1 = False
            c2 =False
            c3 = False
            c4 = True
        elif how_rect.collidepoint(pygame.mouse.get_pos()) and keys[0] :
            game_over = True
            game_2 = False
            l = 0
            l2 = 1200
            tms = True 
        
    if game == True:
        if pygame.sprite.spritecollide(player.sprite,chest_group,False):     
            a =choice(["b_s","TEST","TEST","bird","bowling","sheild","bullet"])
            
            if a =="bird" and ail:
                ability1.add(ability("bird"))
                chestsound.play()
                ail = False
                yuo = 60
            elif a =="bowling" and ail:
                ability1.add(ability("bowling"))
                chestsound.play()
                ail = False
                yuo = 60
            elif a == "TEST" and ail:
                times = randint(600,1200)
                yuo = 100
                ail = False
                
                
                chestsound.play()
                
            elif a == "bullet" and ail:
                ability1.add(ability("bullet"))
                chestsound.play()
                ail = False
                yuo = 60
            elif a == "sheild" and ail:
                ability1.add(ability("sheild"))
                chestsound.play()
                ail = False
                yuo = 60
            elif a == "b_s" and ail:
                b_s = 100
                pygame.time.set_timer(bullet_timer,450)
                chestsound.play()
                ail = False
                yuo = 60
                
        
        else:
            ail = True
        if times <0:
            yuo = 60
            r = 1
            
        else:
            r = 2
        if score<50:
            screen.blit(test_surface,(0,0))
        else:
            screen.blit(back1,(0,0))
        screen.blit(ground_surface,(l,0))
        screen.blit(ground2,(l2,0))
        
        
        score =showscore()
        times -=1
        if l2 == 0:
            l=1200
        if l ==0:
            l2 =1200
        l-=r
        l2-=r
        
        b_s-=1
        if b_s ==0:
            if c1:
                pygame.time.set_timer(bullet_timer,randint(3000,7000))
            if c2:
                pygame.time.set_timer(bullet_timer,randint(3000,7000))
            if c3:
                pygame.time.set_timer(bullet_timer,100000)
            if c4:
                pygame.time.set_timer(bullet_timer,1000)
            
        
            
        game = collision_sprite()
        
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        chest_group.draw(screen)
        chest_group.update()
        
        ability1.draw(screen)
        ability1.update()
    if game == False and game_over == False and game_2 == False:
        game_start = True
        
    if game_over == True:
        keys = pygame.key.get_pressed()
        screen.blit(test_surface,(0,0))
        how_text = text_font.render("Hello! My name is Raatiko.",False,"Black")
        how_text_rect = start_game.get_rect(center = (600,100))
        t2 = text_font.render("I will be guiding you today.",False,"Black")
        t23 = t2.get_rect(center = (600,150))
        t1 = text_font.render("Dodge the obstacles ",False,"Black")
        t11 = t1.get_rect(center = (600,250))
        
        
        back = text_font.render("Click space or up arrow to jump",False,"Black")
        back_rect = back.get_rect(center = (600,150))
        tutor = text_font.render("Now click down arrow to slide",False,"Black")
        
        tutor1 =tutor.get_rect(center = (600,250))
        t3 = text_font.render("Good Job",False,"Black")
        t33 = t3.get_rect(center= (600,150))
        t = text_font.render("Now know how to play the game",False,"Black")
        tt = t3.get_rect(center = (250,150))
        t4 = text_font.render("Chests can give you power ups",False,"Black")
        t5 = text_font.render("Click b to use the ability ",False,"Black")
        t55 = t5.get_rect(center = (600,250))
       
        l1 = t5.get_rect(center = (600,850))
        t44 = t4.get_rect(center= (600,150))
        t6 = text_font.render("Take the chest!",False,"Black")
        t66 = t5.get_rect(center = (600,150))
        t7 = text_font.render("Bowling balls will kill snails",False,"Black")
        t77 = t7.get_rect(center = (600,150))
        t8 = text_font.render("It has 3 durability. Use it!",False,"Black")
        t88 = t8.get_rect(center = (600,250))
        t9 = text_font.render("Bullets will kill bullets",False,"Black")
        t99 = t9.get_rect(center = (600,150))
        t10 = text_font.render("It has 1 durability. Use it!",False,"Black")
        t110 = t10.get_rect(center = (600,250))
        t1111 = text_font.render("It has infinite durability. Use it!",False,"Black")
        t111 = t1111.get_rect(center = (600,250))
        t12 = text_font.render("The bird kills flies",False,"Black")
        t112 = t12.get_rect(center = (600,150))
        t13 = text_font.render("The sheild stops everything",False,"Black")
        t113 = t13.get_rect(center = (600,150))
        t14 = text_font.render("it has 3 durability",False,"Black")
        t114 = t14.get_rect(center = (600,250))
        t15 = text_font.render("You can get Speedup or Bulletrush",False,"Black")
        t115 = t15.get_rect(center = (600,150))
        t16 = text_font.render("Speedup speeds up the game ",False,"Black")
        t116 = t16.get_rect(center = (600,250))
        t17 = text_font.render("Bulletrush fires three bullets at you ",False,"Black")
        t117= t17.get_rect(center = (600,350))
        t18 = text_font.render("it has 3 durability",False,"Black")
        t118 = t18.get_rect(center = (600,250))
       
        screen.blit(ground_surface,(l,0))
        screen.blit(ground2,(l2,0))
        
        if l2 == 0:
            l=1200
        if l ==0:
            l2 =1200
        l-=r
        l2-=r
        tim-=1
        tim21-=1
        tim3-=1
        tim32 -=1
        tim4-=1
        tim91-=1
        ti -= 1
        
        if phase1:
            if tim>0:
                screen.blit(how_text,how_text_rect)
                screen.blit(t2,t23)
            elif tim <0:
                phase2 = True
                phase1= False
                print("phase2")
             
        if phase2:
            if tim2==False:
                screen.blit(back,back_rect)
                if keys[pygame.K_SPACE]or keys[pygame.K_UP]:
                    tim21 = 100
                    tim2 = True
            if tim2 == True:
                screen.blit(tutor,tutor1)
                if keys[pygame.K_DOWN]:
                    tim21 = 100
                    phase3 = True
                    phase2 = False
                    print("phase3")
        if tim21 >0:
            screen.blit(t3,t33)
            
        if phase3:
            screen.blit(t1,t11)
            if tim31:
                obstacle_group.add(Obstacle("snail"))
                tim3 = 300
                tim31= False
            if tim3 == 0 and tim31 == False:
                obstacle_group.add(Obstacle("bullet"))
                tim32 =100
            if tim32==0:
                phase4 = True
                phase3 =False
                tim4 = 200
                
            if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
                phase3=False
                phase2 = True
                tim31 = True
                tim2 = False
                obstacle_group.empty()
        if phase4:
            screen.blit(t4,t44)
            screen.blit(t5,t55)
            if tim4 == 0:
                phase5 = True
                phase4 = False
                
                
        if phase5:
            if tim51 == False:
                chest_group.add(Chest())
                tim51 = True
                tim52 = True
            if tim52:
                screen.blit(t6,t66)
            if pygame.sprite.spritecollide(player.sprite,chest_group,False):
                tim52 = False
                ability1.add(ability("bowling"))
                chest_group.empty()
                tim54 = True
                tim53 = True
            if tim54:
                obstacle_group.add(Obstacle("snail"))
                tim54 = False
            if tim53:
                screen.blit(t7,t77)
                screen.blit(t8,t88)
            if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
                chest_group.empty()
                obstacle_group.empty()
                ability1.empty()
                tim51 = False
                tim52 = False
                tim53 = False
                tim54 = False
                ability1.empty()
        if phase6:
            if tim61 == False:
                chest_group.add(Chest())
                tim61 = True
                tim62 = True
            if tim62:
                screen.blit(t6,t66)
            if pygame.sprite.spritecollide(player.sprite,chest_group,False):
                tim62 = False
                ability1.add(ability("bullet"))
                chest_group.empty()
                tim64 = True
                tim63 = True
            if tim64:
                obstacle_group.add(Obstacle("bullet"))
                tim64 = False
            if tim63:
                screen.blit(t9,t99)
                screen.blit(t10,t110)
            if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
                chest_group.empty()
                obstacle_group.empty()
                tim61 = False
                tim62 = False
                tim63 = False
                tim64 = False
                ability1.empty()
            
            
        if phase7:
            if tim71 == False:
                chest_group.add(Chest())
                tim71 = True
                tim72 = True
            if tim72:
                screen.blit(t6,t66)
            if pygame.sprite.spritecollide(player.sprite,chest_group,False):
                tim72 = False
                ability1.add(ability("bird"))
                chest_group.empty()
                tim74 = True
                tim73 = True
            if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
                chest_group.empty()
                obstacle_group.empty()
                tim71 = False
                tim72 = False
                tim73 = False
                tim74 = False
                ability1.empty()
            if tim74:
                obstacle_group.add(Obstacle("fly"))
                tim74 = False
            if tim73:
                screen.blit(t1111,t111)
                screen.blit(t12,t112)
        if phase8:
            if tim81 == False:
                chest_group.add(Chest())
                tim81 = True
                tim82 = True
            if tim82:
                screen.blit(t6,t66)
            if pygame.sprite.spritecollide(player.sprite,chest_group,False):
                tim82 = False
                ability1.add(ability("sheild"))
                chest_group.empty()
                tim84 = True
                tim83 = True
            if tim84:
                obstacle_group.add(Obstacle("snail"))
                
                tim84 = False
            if tim83:
                screen.blit(t13,t113)
                screen.blit(t14,t114)
            if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
                chest_group.empty()
                obstacle_group.empty()
                tim81 = False
                tim82 = False
                tim83 = False
                tim84 = False
                ability1.empty()
        if phase9:
            screen.blit(t15,t115)
            screen.blit(t16,t116)
            screen.blit(t17,t117)
            
            if tim91 ==0:
                tim9 = False
                phase= True
                ti = 100
                phase9 = False
            
                
            
            
        if phase:
            
            screen.blit(t,tt)
            if ti == 0 :
                game_over = False
                game_start = True 
                
            
                    
            
                    
                
                
        
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        chest_group.draw(screen)
        chest_group.update()
        
        ability1.draw(screen)
        ability1.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #if event.type == pygame.KEYDOWN:
           # if event.key == pygame.K_SPACE
                
    
        
            
        try:
            if event.type == obstacle_timer and game ==True  :
                a = choice(["chest","chest","fly","fly","fly","fly","fly","fly","fly","fly","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","snail","chest"])
                
                
                
                if a == "fly":
                    obstacle_group.add(Obstacle("fly"))
                elif a == "snail":
                    obstacle_group.add(Obstacle("snail"))
                    
                elif a == "chest" and chestin== False :
                    chest_group.add(Chest())
                    chestin = True
                
        
            if event.type == bullet_timer and game ==True:            
                obstacle_group.add(Obstacle("bullet"))
                
        except:
            pass


    pygame.display.update()
    clock.tick(yuo)
    
         
