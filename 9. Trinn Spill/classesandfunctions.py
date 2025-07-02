
from typing import Any
import pygame, math,random

# De første linjene av koden er for å sette opp grunnleggende variabler.

tile_list = []
screen = pygame.display.set_mode((1200,775))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

normtile = []
pygame.font.init()
killed = 0
text_font = pygame.font.Font("font/pxt.ttf",100)
text_font2 = pygame.font.Font("font/pxt.ttf",70)
"""Koden under lagde jeg som en sjapp måte å lage ulike maps til spillet.
   
   
   Bare for å vise hvordan of hvorfor koden fungerer, er det slik en liste med maps ser ut, tatt ifra den andre koden, main.py"""
"""[2, 1, 1, 1, 1, 1, 1, 6, 5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[2, 1, 1, 1, 1, 1, 1, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], """
"""Her representerer, 1 2  5 6 og 7 ulike typer blokker. Selv om jeg vet at denne er slow på større maps, 
   og bruker mye minne siden den må itterate over hver eneste brikke og lagre den,
   var den fungerende for det jeg trengte. """
   
class tille(pygame.sprite.Sprite):
    def __init__(self,x,y,atr):
        super().__init__()
        self.atr = atr
        if self.atr == "walkable":
            self.image = pygame.image.load("9. Trinn Spill/Data/floortile.png").convert_alpha()
        elif self.atr == "":
            self.image=pygame.image.load("9. Trinn Spill/Data/DungeonWall.png").convert_alpha()
        elif self.atr == "torch":
            self.image = pygame.image.load("9. Trinn Spill/Data/DungeonWall with Tortch.png").convert_alpha()
        self.rect = self.image.get_rect(center= (x,y))
    def checkatribs(self):
        return self.atr
pygame.init()
walllist = pygame.sprite.Group()
def world(data):
    global walllist,dor,normtile,nndor
    wall= pygame.image.load("9. Trinn Spill/Data/DungeonWall.png").convert_alpha()
    floor =pygame.image.load("9. Trinn Spill/Data/floortile.png").convert_alpha()
    walltorch= pygame.image.load("9. Trinn Spill/Data/DungeonWall with Tortch.png").convert_alpha()
    #wall = pygame.image.load("walltile.png").convert_alpha()
    rowcount = 0
    tile_size = 50
    for row in data:
        colcount = 0
        for tile in row:
            if tile == 1:
                img = pygame.transform.scale(wall,(tile_size,tile_size))
                img_rect = img.get_rect()
                img_rect.x = colcount*tile_size
                img_rect.y = rowcount * tile_size
                
                walllist.add(tille(colcount*tile_size,rowcount * tile_size,""))
            if tile == 0:
                img = pygame.transform.scale(floor,(tile_size,tile_size))
                img_rect = img.get_rect()
                img_rect.x = colcount*tile_size
                img_rect.y = rowcount * tile_size
                
                walllist.add(tille(colcount*tile_size,rowcount * tile_size,"walkable"))
            if tile == 2:
                img = pygame.transform.scale(walltorch,(tile_size,tile_size))
                img_rect = img.get_rect()
                img_rect.x = colcount*tile_size
                img_rect.y = rowcount * tile_size
                tile = (img, img_rect)
                walllist.add(tille(colcount*tile_size,rowcount * tile_size,"torch"))
            if tile == 3:
                img = pygame.transform.scale(floor,(tile_size,tile_size))
                img_rect = img.get_rect()
                img_rect.x = colcount*tile_size
                img_rect.y = rowcount * tile_size
                tile = (img, img_rect)
                walllist.add(tille(colcount*tile_size,rowcount * tile_size,"walkable"))
                enemy(colcount*tile_size,rowcount * tile_size)
            if tile == 4:
                img = pygame.transform.scale(floor,(tile_size,tile_size))
                img_rect = img.get_rect()
                img_rect.x = colcount*tile_size
                img_rect.y = rowcount * tile_size
                tile = (img, img_rect)
                walllist.add(tille(colcount*tile_size,rowcount * tile_size,"walkable"))
                shootingenemy((colcount*tile_size,rowcount * tile_size))
            if tile == 5:
                
                img = pygame.transform.scale(floor,(tile_size,tile_size))
                img_rect = img.get_rect()
                img_rect.x = colcount*tile_size
                img_rect.y = rowcount * tile_size
                tile = (img, img_rect)
                dor = door((colcount*tile_size-tile_size,rowcount * tile_size -tile_size),tile)
                
            if tile == 7:
                img = pygame.transform.scale(floor,(tile_size,tile_size))
                img_rect = img.get_rect()
                img_rect.x = colcount*tile_size
                img_rect.y = rowcount * tile_size
                tile = (img, img_rect)
                nndor =door((colcount*tile_size-tile_size,rowcount * tile_size-tile_size),tile)
                
            if tile == 8:
                img = pygame.transform.scale(floor,(tile_size,tile_size))
                img_rect = img.get_rect()
                img_rect.x = colcount*tile_size
                img_rect.y = rowcount * tile_size
                tile = (img, img_rect)
                mage((colcount*tile_size,rowcount * tile_size))
                walllist.add(tille(colcount*tile_size,rowcount * tile_size,"walkable"))

            colcount+=1
        rowcount+=1

offset = pygame.math.Vector2()
def resetw():
    walllist.empty()
""" Under er en funksjon for hvordan dørene skulle åpne seg. Ideen var at dørene (de som representeres av 6 5 og 7 i listen over)
    skulle åpne når alle fiendene i rommet var drept. Dette ble da sjekket, og etter det ville dørene åpne seg. Da jeg lagde koden,
    Hadde jeg mer fokus på Backenden, og mindre fokus på utseende, som jeg hadde tenkt å jobbe på videre på et tidspunkt. 
    Jeg rakk det ikke før innleveringsfristen på skolen, og endte opp med å sende den som den var. """
##############################################################################
class door(pygame.sprite.Sprite):
    def __init__(self,pos,tile) -> None:
        super().__init__(allspritegroups)
        self.image = pygame.image.load("9. Trinn Spill/Data/DungeonDoor_Closed.png").convert_alpha()
        self.pos = tile
        self.rect = self.image.get_rect(center=(pos[0]+25,pos[1]+50))
        self.changed = False
    def change(self):
        
        self.changed = True
        self.image = pygame.image.load("9. Trinn Spill/Data/DungeonDoor_Open.png.png").convert_alpha()
    def checkcol(self):
        if player.rect.colliderect(self.rect):
            self.kill()
            
            return True
        return False
###############################################################################
""" Her lagde jeg en klasse for levelene, som da lagde en ulik mengde med sprites og ulike typer fiender. 
    Classen justerte også på dørene, og samtidig også resetta alle de viktige variablene.
    Igjen, jeg viste ikke at denne koden ville bli brukt til noe, og variablene er ikke så godt navngitt som de burde vært."""
class level:
    def __init__(self,data,types):
        self.world = data
        self.types = types
        self.enemiesspawned = len(enemies.sprites()) + len(shootingenemys.sprites()) + len(mages.sprites())
        self.changed = []
        self.lenx = len(data[0])-2
        self.leny =len(data)-2
    def reset(self):
        if self.enemiesspawned == 0 and killed >0:
            dor.change()
            if dor.checkcol():
                return True

        return False
    def createenem(self,enems,world_data):
        worlds = world_data
        e = enems
        while e != 0:
            typ = random.choice(self.types)
            leny = random.randint(2,self.leny)
            lenx = random.randint(2,self.lenx)
            if worlds[leny][lenx]== 0:
                if typ == "bat":
                    worlds[leny][lenx] =3
                    self.changed.append([leny,lenx])
                    
                if typ == "shooting":
                    worlds[leny][lenx] =4
                    self.changed.append([leny,lenx])
                if typ == "mage":
                    worlds[leny][lenx] =8
                    self.changed.append([leny,lenx])
                e-=1

        world(worlds)
        worlds = world_data
        for place in self.changed:
            worlds[place[0]][place[1]] = 0
    def resets(self,worlds,enems,type1):
        global walllist,tile_list,killed,enemies,allspritegroups,shootingenemys,shootingenemysbullets,b,player,dor
        hs = 0
        abills = []
        for h in allspritegroups:
            try:
                if h.ha == 0:
                    hs +=1
                    print(hs)
                
            except:
                pass
            try:
                abills.append(h.type)
            except:
                pass
        dor.kill()
        enemies.empty()
        b.empty()
        g = player.gun
        plives = player.lives
        player.kill()
        
        allspritegroups.empty()
        shootingenemys.empty()
        shootingenemysbullets.empty()
        
        killed = 0
        walllist.empty()
        player = char(plives,g)
        self.types = type1
        allspritegroups.add(player)
        for i in range(hs):
            healthpack()
        self.createenem(enems,worlds)
################################################################################
"""Under har jeg da ulike classes til ulike objekter inkludert pistoler, fiender, main character, bullets, og andre ting. 
   Jeg skal prøve å holde meg på det viktigste. 
   Da jeg startet på denne koden, hadde jeg ikke så mye kunnskap om hvordan ulike deler av spill fungerte, som for eksempel: 
   Pathfinding
   Skudd, og hvordan vinkelen deres kalkuleres
   Jeg møtte også på mange andre problemer mens jeg lagde koden, og måtte lære meg mye nytt.
   Med skudd, lærte jeg meg hvordan sinus og cosinus fungerte, ( Jeg gikk i 9ende da jeg lagde denne koden)"""
################################################################################
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,angle,damage,image):
        super().__init__(allspritegroups,b)
        self.image = image 
        self.image = pygame.transform.rotozoom(self.image,0,1)
        self.damage = damage
        self.angle = math.radians(angle)
        self.image =pygame.transform.rotate(pygame.transform.rotate(self.image,angle),180)
        self.rect = self.image.get_rect(center = (x,y))
        self.et = False
        self.time = 0
        self.speed =25
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)
    def move(self):
        self.rect.x+= self.dx
        self.rect.y+= self.dy
        
    def destroy(self):
        for tillle in  walllist:
            if tillle.rect.colliderect(self.rect) and tillle.checkatribs() == "" or tillle.rect.colliderect(self.rect) and tillle.checkatribs() == "torch":
                self.image = pygame.image.load("9. Trinn Spill/Data/LaserbulletCrash.png").convert_alpha()
                self.image = pygame.transform.rotozoom(self.image,0,0.5)
                self.et = True
        
        for enemy in shootingenemys:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                if player.gun.hasabil and player.gun.hasabil[0] == "Seeping" and self.et == False:
                    player.lives +=0.5 if player.lives +0.5<=player.healthbar.maxhp else 0
                    player.healthbar.change_hps(player.lives)
                self.et = True
                
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                if player.gun.hasabil and player.gun.hasabil[0] == "Seeping" and self.et == False:
                    player.lives +=0.5 if player.lives +0.5<=player.healthbar.maxhp else 0
                    player.healthbar.change_hps(player.lives)
                self.et = True
                
        for enemy in mages:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                if player.gun.hasabil and player.gun.hasabil[0] == "Seeping" and self.et == False:
                    player.lives +=0.5 if player.lives +0.5 <=player.healthbar.maxhp else 0
                    player.healthbar.change_hps(player.lives)
                self.et = True
                
    def update(self):
        self.destroy()
        if self.et == False:
            self.move()
        if self.et  == True:
            self.damage = 0
            self.time += 1
        if self.time == 20:
            self.kill() 
        self.mask = pygame.mask.from_surface(self.image)
################################################################################

################################################################################
class char(pygame.sprite.Sprite):
    def __init__(self,lives,gun):
        super().__init__()
        player = pygame.image.load("9. Trinn Spill/Data/player_front.png").convert_alpha()
        self.image = pygame.transform.rotozoom(player,0,3)
        self.move = None
        """ list will be sorted with players images of : up, down, left, right"""
        self.images = [pygame.transform.rotozoom(pygame.image.load("9. Trinn Spill/Data/player_back.png").convert_alpha(),0,3),pygame.transform.rotozoom(pygame.image.load("9. Trinn Spill/Data/player_front.png").convert_alpha(),0,3),pygame.transform.rotozoom(pygame.image.load("9. Trinn Spill/Data/player_left.png").convert_alpha(),0,3),pygame.transform.rotozoom(pygame.image.load("9. Trinn Spill/Data/player_right.png").convert_alpha(),0,3)]
        self.rect = self.image.get_rect(center =(400,800))
        self.v = False
        self.posshoot = False
        self.lives = 100
        self.healthbar = healthbar(self.lives,lives)
        self.lives = lives
        self.barpos = 360
        self.barposx = 250
        self.barsize = [600,40]
        self.gun = gun
        self.name = gunname[guns.index(self.gun)]
        self.bulimage = gunimage[guns.index(self.gun)]
    def checkmovepossible(self,dir):
        crect = self.rect.copy()
        crect.x += dir[0]
        crect.y += dir[1]
        for tile in walllist:
            if crect.colliderect(tile.rect) and tile.checkatribs() == "" or crect.colliderect(tile.rect) and tile.checkatribs() == "torch":
                return False
        try:
            if crect.colliderect(dor.rect) and dor.changed == False:
                return False
        except:
            pass
        try:
            if crect.colliderect(nndor.rect) and nndor.changed == False:
                return False
        except: 
            pass
        return True
    def inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.checkmovepossible([0,-5]) or keys[pygame.K_w] and self.checkmovepossible([0,-5]):
            self.move = "U"
            self.rect.y-=5
            self.image = self.images[0]  
        if keys[pygame.K_DOWN] and self.checkmovepossible([0,5]) or keys[pygame.K_s] and self.checkmovepossible([0,5]):
            self.move = "D"
            self.rect.y+=5
            self.image = self.images[1]
        if keys[pygame.K_LEFT] and self.checkmovepossible([-5,0]) or keys[pygame.K_a] and self.checkmovepossible([-5,0]):
            self.move = "L"
            self.rect.x-=5
            self.image = self.images[2]
        if keys[pygame.K_RIGHT] and self.checkmovepossible([5,0]) or keys[pygame.K_d] and self.checkmovepossible([5,0]):
            self.move = "R"
            self.rect.x+=5
            self.image = self.images[3]
            
    def checkcol(self):
       
        for enm in enemies:
            if self.rect.colliderect(enm.rect):
                self.lives -=enm.damage
                self.healthbar.change_hps(self.lives)
        for bul in shootingenemysbullets:
            if self.rect.colliderect(bul.rect):
                self.lives -=bul.damage
                self.healthbar.change_hps(self.lives)
                bul.et = True
        for bil in mageshots:
            if self.rect.colliderect(bil.rect):
                self.lives -=bil.damage
                bil.kill()
                self.healthbar.change_hps(self.lives)            
    def shoot(self):
        pos = pygame.mouse.get_pos() + offset
        x_dist = pos[0]-self.rect.center[0]
        y_dist = -(pos[1]-self.rect.center[1])
        self.angle = math.degrees(math.atan2(y_dist,x_dist))
        if pygame.mouse.get_pressed()[0]:
            if self.gun.checkshootable():
                if self.gun.hasabil and self.gun.hasabil[0] == "throwable":
                    throwable(self.rect.center[0],self.rect.center[1],self.angle,self.gun.damage,self.bulimage,pygame.transform.rotozoom(pygame.image.load("9. Trinn Spill/Data/LaserbulletCrash.png"),0,0.3),"mage",25)
                elif self.gun.hasabil and self.gun.hasabil[0] == "throwable1":
                    throwable(self.rect.center[0],self.rect.center[1],self.angle,self.gun.damage,self.bulimage,pygame.transform.rotozoom(pygame.image.load("9. Trinn Spill/Data/LaserbulletCrash.png"),0,0.3),"spawnshot",1)
                elif self.gun.hasabil and self.gun.hasabil[0] == "throwable2":
                    throwable(self.rect.center[0],self.rect.center[1],self.angle,self.gun.damage,self.bulimage,pygame.transform.rotozoom(pygame.image.load("9. Trinn Spill/Data/Mine.png"),0,0.3),"miner",15)
                elif self.gun.hasabil and self.gun.hasabil[0] == "tel":
                    tpbullet(self.rect.center[0],self.rect.center[1],self.angle,self.gun.damage,self.bulimage,"miner",20)

                else: 
                    Bullet(self.rect.center[0],self.rect.center[1],self.angle,self.gun.damage,self.bulimage)
                
        if pygame.mouse.get_pressed()[2]:
            if self.gun.checkshootable():
                if self.gun.hasabil and self.gun.hasabil[0] == "throwable2":
                    throwable(self.rect.center[0],self.rect.center[1],self.angle,self.gun.damage,self.bulimage,pygame.transform.rotozoom(pygame.image.load("9. Trinn Spill/Data/Mine.png"),0,0.3),"miner",1)
    def update(self):
        self.shoot()
        self.inputs()
        self.checkcol()
        self.name = gunname[guns.index(self.gun)]
        self.bulimage = gunimage[guns.index(self.gun)]
        
class chest(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__(allspritegroups)
        self.image = pygame.image.load("9. Trinn Spill/Data/DungeonChest.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        
        self.what = random.choice(["h","g"])
        self.changed = False
        i =random.choice(guns) 
        self.holdsgun = i if i!= player.gun else guns[2]
        self.other = 0
        
    def changegun(self):
        keys = pygame.key.get_pressed()
        self.other = player.gun
        
        if self.rect.colliderect(player.rect) and keys[pygame.K_e]:
            if self.what == "g":
                if self.changed == False:
                    player.gun = self.holdsgun
                    self.holdsgun = self.other
                    self.changed = True
            elif self.what == "h":
                healthpack()
                self.kill()
        else:
            self.changed = False
    def update(self):
        self.changegun()
        for h in allspritegroups:
            try:
                if h.ha == 0:
                    self.ishealthpack = True
            except:
                pass
        try:
            if self.ishealthpack:
                self.what = random.choice("g")
        except:
            pass
class tutchest(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__(allspritegroups)
        self.image = pygame.image.load("9. Trinn Spill/Data/DungeonChest.png").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        
        self.what = random.choice(["h","g"])
        self.changed = False
        i =random.choice(guns) 
        self.holdsgun = i if i!= player.gun else guns[2]
        self.other = 0
        
    def changegun(self):
        keys = pygame.key.get_pressed()
        self.other = player.gun
        
        if self.rect.colliderect(player.rect) and keys[pygame.K_e]:
            healthpack()
            return True
        return False
class healthpack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(allspritegroups)
        self.image = pygame.image.load("9. Trinn Spill/Data/healthpack.png")
        self.rect = self.image.get_rect(center =(player.rect.center[0]-300,player.rect.center[1]+300))
        self.ha = 0
    def heal(self):
        i =player.healthbar.maxhp -player.healthbar.hp
        self.healing = i if i != 0 else 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            player.healthbar.change_hps(player.healthbar.hp+self.healing)
            player.lives += self.healing
            self.kill()
    def update(self):
        self.heal()
        self.rect.center = (player.rect.center[0]-350,player.rect.center[1]+350)
################################################################################
"""Et problem jeg hadde med fienden som kunne skyte var hvordan å vite når den skulle skyte, og noen ting rundt det. 
   Jeg valgte å bruke en lett Line Of Sight system, som ville sjekke om fienden så spilleren, og om den gjorde det, 
   ville motstanderen skyte"""
"""Enemies som flytter seg er lagd ved å lage 2 vektorer, direction og hvor den skal. Jeg finner hva forskjellen på vektoren til 
     og jeg enemyen og playeren er nærme nok vil jeg skyte, hvis ikke vil jeg flytte enemyen nærmere, med den nye verdien av enemyen.
     Dette skjer bare hvis det er ingen vegger i veien til playeren, som jeg sjekker med clipline funksjonen. Hvis dette ikke går, bruker jeg alle
     Tilllene til å sjekke det samme. Hvis de kan se playeren, vil enemyen gå dit slik at den kan bruke den andre algoritmen. """
class shootingenemy(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__(allspritegroups,shootingenemys)
        self.lives = 120
        self.healthbar = healthbar(self.lives,self.lives)
        self.image = pygame.image.load("9. Trinn Spill/Data/Axethrower.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,0,2)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.shoot_delay = 3000
        self.last_shot_time = pygame.time.get_ticks()
        self.speed = 3
        self.dir = pygame.math.Vector2()
        self.vel = pygame.math.Vector2()
        self.position = pygame.math.Vector2()
        self.position = self.rect.center
        self.range = 400
        self.barpos = 150
        self.barposx = 20
        self.los = False
        self.coldir = None
    def changelos(self):
        self.checkpath(self.rect.center,player.rect.center)
        if self.los == False:
            self.coldir = "M"
        if self.los:
            self.checkpath(self.rect.topright,player.rect.topright)
        if self.los == False:
            self.coldir = "TR"
        if self.los:
            self.checkpath(self.rect.topleft,player.rect.topleft)
        if self.los == False:
            self.coldir = "TL"
        if self.los:
            self.checkpath(self.rect.bottomright,player.rect.bottomright)
        if self.los == False:
            self.coldir = "BR"
        if self.los:
            self.checkpath(self.rect.bottomleft,player.rect.bottomleft)
        if self.los == False:
            self.coldir = "BL"
        else:
            self.coldir = None
    def move(self):
        
        
        player_vec = pygame.math.Vector2(player.rect.center)
        enemvec =pygame.math.Vector2(self.rect.center)
        distance = self.calculate_dist(player_vec,enemvec)
        if distance > self.range:
            self.direction = (player_vec - enemvec).normalize()
            
        else:
            self.direction = pygame.math.Vector2()
            
            self.throw()
        self.vel = self.direction *self.speed
        
        self.position += self.vel
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y
    def findpath(self):
        self.changelos()
        if self.los:
            self.move()
    def checkpath(self,cur,goal):
        
        
        for tile in walllist:
            if tile.rect.clipline((cur[0],cur[1]),(goal[0], goal[1])) and tile.checkatribs() == "" or tile.rect.clipline((cur[0],cur[1]),(goal[0], goal[1])) and tile.checkatribs() == "torch":
                self.los = False
                pygame.draw.line(screen,"red",(cur[0],cur[1])-offset,(goal[0], goal[1])-offset)
                return
        pygame.draw.line(screen,"green",(cur[0],cur[1])-offset,(goal[0], goal[1])-offset)
        self.los = True
        return  
    def throw(self):
        currtime = pygame.time.get_ticks()
        if currtime-self.last_shot_time>self.shoot_delay:
            pos =  player.rect.center
            x_dist = pos[0]-self.rect.center[0]
            y_dist = -(pos[1]-self.rect.center[1])
            self.angle = math.degrees(math.atan2(y_dist,x_dist))
            enembull(self.rect.center[0],self.rect.center[1], self.angle)
            self.last_shot_time = currtime
    def checkcol(self):
        if self.lives <=0:
            global killed
            self.kill()
            killed += 1
    def calculate_dist(self,vec1,vec2):
        return(vec1-vec2).magnitude()

    def update(self):
        self.findpath()
        self.checkcol()
################################################################################
class enembull(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        super().__init__(allspritegroups,shootingenemysbullets)
        self.image = pygame.image.load("9. Trinn Spill/Data/Axe.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,220,1)
        self.damage = 15
        self.angle = math.radians(angle)
        self.image = pygame.transform.rotozoom(self.image,0,2)
        self.image =pygame.transform.rotate(self.image,angle)
        self.rect = self.image.get_rect(center = (x,y))
        self.et = False
        self.time = 0
        self.speed =4
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)
    def move(self):
        self.rect.x+= self.dx
        self.rect.y+= self.dy
    def destroy(self):
        for tile in  walllist:
            if tile.rect.colliderect(self.rect) and tile.checkatribs() == "" or tile.rect.colliderect(self.rect) and tile.checkatribs() == "torch":
                self.et = True
    def changemode(self):
        if self.et == False:
            self.move()
        if self.et  == True:
            self.damage = 0
            self.time += 1
        if self.time == 20:
            self.kill()
    def update(self):
        self.destroy()
        self.changemode()
################################################################################
class tpbullet(pygame.sprite.Sprite):
    def __init__(self,x,y,angle,damage,image,t,rangse):
        super().__init__(allspritegroups,b)
        self.image= image 
        self.rect = self.image.get_rect(center = (x,y))
        self.speed =20
        self.disttraveled = 0
        self.angle = math.radians(angle) 
        self.damage = damage
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)
        self.t = t
        self.max = rangse
        self.wtime =0
        self.stt = False
    def move(self):
        self.rect.x+= self.dx
        self.rect.y+= self.dy
        self.disttraveled +=1
    def killself(self):
        
        for tile in  walllist:
            if tile.rect.colliderect(self.rect) and tile.checkatribs() == "" or tile.rect.colliderect(self.rect) and tile.checkatribs() == "torch":
                self.kill()
        for enemy in shootingenemys:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.kill()
                
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                
                self.kill()
                
        for enemy in mages:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.kill()
        if self.disttraveled == self.max:
            self.stt = True
        if self.stt:
            self.wtime +=1
        if self.wtime >20:
            player.rect.center = self.rect.center
            self.kill()
    def update(self):
        if self.stt== False:
            self.move()
        self.killself()


################################################################################
class throwable(pygame.sprite.Sprite):
    def __init__(self,x,y,angle,damage,image,splashimage,t,rangse):
        super().__init__(allspritegroups,b)
        self.image= image 
        self.splashimage = splashimage
        self.rect = self.image.get_rect(center = (x,y))
        self.speed =20
        self.disttraveled = 0
        self.angle = math.radians(angle) 
        self.damage = damage
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)
        self.t = t
        self.max = rangse
    def move(self):
        self.rect.x+= self.dx
        self.rect.y+= self.dy
        self.disttraveled +=1
    def killself(self):
        if self.disttraveled == self.max:
            self.shootbullets()
            self.kill()
        for tile in  walllist:
            if tile.rect.colliderect(self.rect) and tile.checkatribs() == "" or tile.rect.colliderect(self.rect) and tile.checkatribs() == "torch":
                self.kill()
        for enemy in shootingenemys:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.shootbullets()
                self.kill()
                
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.shootbullets()
                self.kill()
                
        for enemy in mages:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.shootbullets()
                self.kill()
    def shootbullets(self):
        if self.t == "mage":
            angle = 0
            for i in range(10):
                throwshots2((self.rect.center[0],self.rect.center[1]),angle,self.splashimage,self.damage )
                angle +=36
        if self.t == "spawnshot":
            angle = math.degrees(self.angle)-40
            for i in range(5):
                throwshots2((self.rect.center[0],self.rect.center[1]),angle,self.splashimage,self.damage)
                angle+=20
        if self.t == "miner":
            throwshots3((self.rect.center[0],self.rect.center[1]),pygame.image.load("9. Trinn Spill/Data/Mine_Hidden.png").convert_alpha(),self.damage,pygame.image.load("9. Trinn Spill/Data/Mine_Explotion.png").convert_alpha()) 
    def update(self):
        self.move()
        self.killself()


################################################################################      
"""Det største problemet jeg hadde med fiendene, var pathfinding. På starten hadde jeg en lett  kode som gjorde at fiendene 
   Bare  følgte etter spilleren, og ikke hadde noen hindringer. Men, Jeg prøvde meg å lære ulike andre metoder. 
   Jeg kunne for eksempel prøvd å mappe ut en grid, og bruke a* eller andre algoritmer, men dette ville ta lang tid, 
   både for meg å lage, og for spillet å kjøre."""
"""Jeg endte derfor opp med å heller prøve å bruke Line Of Sight. 
   Basicaly, bakken var nå en del av fienden. Hvis en såkalt"Floortile" som var i området til fienden så spilleren, 
    Ville han gå til den floortilen, og deretter se spilleren, slik at den andre koden kunne kjøre på.    """
class enemy(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        super().__init__(allspritegroups,enemies)
        self.isanim = False
        self.image = pygame.image.load("9. Trinn Spill/Data/DungeonBat1.png").convert_alpha()
        self.sprites = [self.image,pygame.image.load("9. Trinn Spill/Data/DungeonBat2.png").convert_alpha()]
        self.image = pygame.transform.rotozoom(self.image,0,1.5)
        self.currsprite = 0
        self.rect = self.image.get_rect(center =(posx,posy))
        self.damage = 0
        self.lives = 5
        self.dir = pygame.math.Vector2()
        self.vel = pygame.math.Vector2()
        self.position = pygame.math.Vector2()
        self.position+=self.rect.center
        self.speed = 3
        self.cooldown = 500
        self.timer = pygame.time.get_ticks()
        self.healthbar = healthbar(self.lives,self.lives)
        self.barpos = 60
        self.barposx = 25
        self.coldir = False
        self.animtimer = pygame.time.get_ticks()
        self.los = False
    def animate(self):
        currtime = pygame.time.get_ticks()
        if currtime-self.animtimer>100:
            if self.currsprite >= len(self.sprites):
                self.currsprite = 0
            
            self.animtimer = currtime
            self.image = self.sprites[self.currsprite]
            self.currsprite +=1
    def changelos(self):
        self.checkpath(self.rect.center,player.rect.center)
        if self.los == False:
            self.coldir = "M"
        if self.los:
            self.checkpath(self.rect.topright,player.rect.topright)
        if self.los == False:
            self.coldir = "TR"
        if self.los:
            self.checkpath(self.rect.topleft,player.rect.topleft)
        if self.los == False:
            self.coldir = "TL"
        if self.los:
            self.checkpath(self.rect.bottomright,player.rect.bottomright)
        if self.los == False:
            self.coldir = "BR"
        if self.los:
            self.checkpath(self.rect.bottomleft,player.rect.bottomleft)
        if self.los == False:
            self.coldir = "BL"
        else:
            self.coldir = None
    def hunt_player(self,place):
        
        player_vec = pygame.math.Vector2(place)
        enemvec =pygame.math.Vector2(self.rect.center)
        distance = self.calculate_dist(player_vec,enemvec)
        if distance > 0:
            self.direction = (player_vec - enemvec).normalize()
            self.vel = self.direction *self.speed
        else:
            self.direction = pygame.math.Vector2()
            self.vel = self.direction *self.speed
        
        self.position += self.vel
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y 
    def findpath(self):
        self.changelos()
        if self.los:
            self.hunt_player(player.rect.center)
        else:
            tr = pygame.Rect(self.rect.topleft[0]-100,self.rect.topleft[1]-100,300,300)
            trs = tr.copy()
            trs.center -=offset
            pygame.draw.rect(screen,(255,255,255),trs,1)
            
            for f in walllist:
                if tr.colliderect(f) and f.checkatribs() == "walkable":
                    if self.othercheckpath(f.rect.center,player.rect.center) and self.othercheckpath(f.rect.topright,player.rect.center) and self.othercheckpath(f.rect.bottomleft,player.rect.center) and self.othercheckpath(f.rect.bottomright,player.rect.center) :
                        self.hunt_player(f.rect.center)
                        return
            pass
    def damagechange(self):
        currtime = pygame.time.get_ticks()
        if currtime-self.timer>self.cooldown:
            self.damage = 5
            self.timer = currtime
        else:
            self.damage = 0
    def checkpath(self,cur,goal):
        for tile in walllist:
            if tile.rect.clipline((cur[0],cur[1]),(goal[0], goal[1])) and tile.checkatribs() == "" or  tile.rect.clipline((cur[0],cur[1]),(goal[0], goal[1])) and tile.checkatribs() == "torch":
                
                self.los = False
                
                return
            
        self.los = True
        
        return  
    def othercheckpath(self,cur,goal):
        
        for tile in walllist:
            if tile.rect.clipline((cur[0],cur[1]),(goal[0], goal[1])) and tile.checkatribs() == "" or  tile.rect.clipline((cur[0],cur[1]),(goal[0], goal[1])) and tile.checkatribs() == "torch":
                return False        
        return  True
    def calculate_dist(self,vec1,vec2):
        return(vec1-vec2).magnitude()
    def coll(self):
        if self.lives <=0:
            global killed
            killed+=1
            self.kill()
                
                
    def update(self):
        self.animate()
        self.findpath()
        self.coll()
        self.damagechange()
################################################################################
class healthbar():
    def __init__(self,maxhp,hp):
        self.hp = hp
        self.maxhp = maxhp
    def change_hps(self,hp):
        self.hp = hp
################################################################################      
""" Jeg lærte mye fra dette prosjektet, og så på mange tutorials, for å inkorporere alt inn i en kode. 
    Da lærte jeg også dette med kameraet. Måten dette fungerte, var at hver gang spilleren flyttet seg, 
    Flyttet alt annet istedet. Spilleren ville altid være på midten av skjærmen på denne måten. """
class camera(pygame.sprite.Group):
    def __init__(self) :
        super().__init__()
        self.offset  = pygame.math.Vector2()
    def custom_draw(self):
        global offset
        self.offset.x = player.rect.centerx - 600
        self.offset.y = player.rect.centery - 375
        offset = self.offset
        
        for tile in walllist:
            offset_pos = tile.rect.topleft -self.offset
            screen.blit(tile.image,offset_pos)
        """ r = tile[1].copy()
            r.center -= offset
            pygame.draw.rect(screen,(255,255,255),r,1)"""
        for sprite in allspritegroups:
            offset_pos = sprite.rect.topleft - self.offset
            r = sprite.rect.copy()
            r.center -= offset
            screen.blit(sprite.image,offset_pos)
            
            try:
                ratio = sprite.healthbar.hp/sprite.healthbar.maxhp
                if sprite != player:
                    if sprite.healthbar.hp != sprite.healthbar.maxhp:
                        pygame.draw.rect(screen,"red", (offset_pos.x-sprite.barposx,offset_pos.y+sprite.barpos,100,20))
                        
                        pygame.draw.rect(screen,"green", (offset_pos.x-sprite.barposx,offset_pos.y+sprite.barpos,100 * ratio,20))
                        pygame.draw.rect(screen,"black", (offset_pos.x-sprite.barposx,offset_pos.y+sprite.barpos,100,20),1)
                else:
                    pygame.draw.rect(screen,"red", (offset_pos.x-sprite.barposx,offset_pos.y+sprite.barpos,600,40))
                        
                    pygame.draw.rect(screen,"green", (offset_pos.x-sprite.barposx,offset_pos.y+sprite.barpos,600 * ratio,40))
                    pygame.draw.rect(screen,"black", (offset_pos.x-sprite.barposx,offset_pos.y+sprite.barpos,600,40),1)
                    guninfo = sprite.name
                    guninfo = pygame.transform.rotozoom(guninfo,0,3)
                    currhp = text_font2.render(str(sprite.healthbar.hp),0,"Blue")
                    currhprect =currhp.get_rect(center =(offset_pos.x-sprite.barposx+300,offset_pos.y+sprite.barpos+25))
                    gunplace = guninfo.get_rect(center = (offset_pos.x + 450,offset_pos.y+370))
                    bullets =str(sprite.gun.needtoreload-sprite.gun.amountshot)
                    bulletstxt = text_font.render(bullets,0,"white")
                    bullets_rect = bulletstxt.get_rect(center = (offset_pos.x + 550,offset_pos.y+370))
                    screen.blit(guninfo,gunplace)
                    screen.blit(bulletstxt,bullets_rect)
                    screen.blit(currhp,currhprect)
            except:
                pass
################################################################################

class mage(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__(mages,  allspritegroups)
        self.image = pygame.image.load("9. Trinn Spill/Data/DungeonMage.png").convert_alpha()
        self.image = pygame.transform.rotozoom(self.image,0,2)
        self.rect = self.image.get_rect(center = pos) 
        self.prevshot = pygame.time.get_ticks()
        self.delay = 3000
        self.lives = 150
        self.healthbar = healthbar(self.lives,self.lives)
        self.barpos = 100
        self.barposx = 20
    def shootit(self):
        self.currbull = pygame.time.get_ticks()
        angle = 0
        if  self.currbull - self.prevshot >self.delay:
            for i in range(17):
                mageshoots((self.rect.center[0],self.rect.center[1]),angle)
                angle +=20
            self.prevshot = self.currbull
    def hit(self):
        global killed
       
        if self.lives <=0:
            killed +=1
            self.kill()
    def update(self):
        self.shootit()
        self.hit()
################################################################################
class mageshoots(pygame.sprite.Sprite):
    def __init__(self,pos,angle) -> None:
        super().__init__(allspritegroups,mageshots)
        self.image = pygame.image.load("9. Trinn Spill/Data/MagePowerball.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.damage = 5
        self.angle = math.radians(angle)
        self.speed =3
        self.time = 0
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)
        self.et = False
    def move(self):
        self.rect.x+= self.dx
        self.rect.y+= self.dy
    def destroy(self):
        for tile in  walllist:
            if tile.rect.colliderect(self.rect) and tile.checkatribs() == "" or tile.rect.colliderect(self.rect) and tile.checkatribs() == "torch":
                self.kill()
    def update(self):
        self.move()
        self.destroy()
class throwshots2(pygame.sprite.Sprite):
    def __init__(self,pos,angle,image,damage) -> None:
        super().__init__(allspritegroups,b)
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.damage = damage
        self.angle = math.radians(angle)
        self.speed =4
        self.time = 0
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)
        self.et = False
    def move(self):
        self.rect.x+= self.dx
        self.rect.y+= self.dy
    def destroy(self):
        for tile in  walllist:
            if tile.rect.colliderect(self.rect) and tile.checkatribs() == "" or tile.rect.colliderect(self.rect) and tile.checkatribs() == "torch":
                self.kill()
        for enemy in shootingenemys:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.kill()       
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.kill()
                
        for enemy in mages:
            if self.rect.colliderect(enemy.rect):
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.kill()
    def update(self):
        self.move()
        self.destroy()
################################################################################
class gun:
    def __init__(self,delay,needtoreload,needtoreloadtime,damage,*ab):
        self.delay = delay
        self.ordinary = delay
        self.needtoreload = needtoreload
        self.needtoreloadtime = needtoreloadtime
        self.amountshot = 0
        self.curr = False
        self.prevbull = pygame.time.get_ticks()
        self.damage = damage
        self.hasabil = ab
    def checkshootable(self):
        if self.amountshot >= self.needtoreload:
            self.delay = self.needtoreloadtime
            self.curr = True 
        currbull = pygame.time.get_ticks()
        if currbull - self.prevbull > self.delay:
            self.prevbull = currbull
            if self.curr == True:
                self.amountshot = 0
                self.curr = False
            self.amountshot += 1
            
            self.delay= self.ordinary
            return True
        return False
    def resets(self):
        if self.amountshot >= self.needtoreload:
            self.delay = self.needtoreloadtime
            
            self.curr = True
        currbull = pygame.time.get_ticks()
        if currbull - self.prevbull > self.delay:
            self.prevbull = currbull
            if self.curr == True:
                self.amountshot = 0
                self.curr = False
            self.delay= self.ordinary
            return True
        return False
################################################################################
class throwshots3(pygame.sprite.Sprite):
    def __init__(self,pos,image,damage, blast) -> None:
        super().__init__(allspritegroups,b)
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        self.damage = damage
        self.blast = blast
        self.et = False
        self.frames = 0
        self.colld = []
    def move(self):
        for enemy in shootingenemys:
            if self.rect.colliderect(enemy.rect) and enemy not in self.colld:
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.colld.append(enemy)
                self.image = self.blast
                self.et = True      
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect) and enemy not in self.colld:
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.colld.append(enemy)
                self.image = self.blast
                self.et = True     

        for enemy in mages:
            if self.rect.colliderect(enemy.rect) and enemy not in self.colld:
                enemy.lives -= self.damage
                enemy.healthbar.change_hps(enemy.lives)
                self.colld.append(enemy)
                self.image = self.blast
                self.et = True     
    def change(self):
        if self.et == True:
            self.frames +=1
        
            if self.frames == 20:
                self.kill()
        
    def update(self):
        self.change()
        self.move()
################################################################################
def shops():
    pygame.draw.rect(screen,(179,105,68),pygame.Rect(100,50,1000,600))
    gunsu = [pygame.image.load("9. Trinn Spill/Data/Dungeon_Pistol.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Minigun.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Rappidfire.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Hardhitter.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_AR.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Minigun_Seeping.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Blastgun.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Sniper.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Sniper_Seeping.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Shotgun.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Minelanucher.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Teleportgun.png").convert_alpha()]
    col = 200
    c = 0
    row = 60
    rects = []
    for g in gunsu:
        g = pygame.transform.rotozoom(g,0,3)
        gr =g.get_rect(center = (col,row))
        rects.append(gr)
        screen.blit(g,(col,row))
        col += 200
        c += 1
        if c == 4:
            c = 0
            col = 200 
            row += 100
""" Dette var en utvikling jeg ville lage, som jeg ikke rakk å lage. Jeg ville lage en butikk til spillet. 
    Jeg prøvde også ut mange ulike andre ting med randomized dungeons, men det var selvfølgelig vannskeligere
    og de jeg endte opp med var ikke så veldig gode."""


################################################################################
def updateit():
    allspritegroups.update()
################################################################################
gunname =[pygame.image.load("9. Trinn Spill/Data/Dungeon_Pistol.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Minigun.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Rappidfire.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Hardhitter.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_AR.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Minigun_Seeping.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Blastgun.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Sniper.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Sniper_Seeping.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Shotgun.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Minelanucher.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Teleportgun.png").convert_alpha()]

guns = [gun(500,12,1000,15,),gun(100,30,1500,3.5),gun(5,40,1000,1),gun(2000,100,0,100),gun(300,30,1000,30),gun(100,30,1500,2,"Seeping"),gun(1000,30,1200,10,"throwable"), gun(3000,1,3000,250),gun(3000,1,3000,250,"Seeping"),gun(2000,3,3000,30,"throwable1"),gun(500,12,1000,15,"throwable2"),gun(500,30,1000,30,"tel")]
gunimage = [pygame.image.load("9. Trinn Spill/Data/bullet.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/bullet.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/bullet.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/HB1.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/bullet.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Bullet_Seeping.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/bullet.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/bullet.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Bullet_Seeping.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/bullet.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Mine.png").convert_alpha(),pygame.image.load("9. Trinn Spill/Data/Dungeon_Teleportgun_Shot.png").convert_alpha()] #images for bullets
enemies =pygame.sprite.Group()
b = pygame.sprite.Group()
player = char(100,guns[0])
def dam():
    player.lives -=50
    player.healthbar.change_hps(player.lives)
allspritegroups =pygame.sprite.Group() 
allspritegroups.add(player)
shootingenemys = pygame.sprite.Group()
shootingenemysbullets =pygame.sprite.Group()
mages = pygame.sprite.Group()
mageshots = pygame.sprite.Group()
def checkend():
    if player.lives <=0:
        return True
    else:
        return False
