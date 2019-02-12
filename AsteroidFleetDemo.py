import pygame, sys, math, random
from Ship import *
from PlayerShip import *
from Asteroid import *
from Missile import *
from PowerUps import *
from Screens import *
pygame.init()

size = width, height
go = True
missile = None

player1 = PlayerShip(1)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(True)


mode = "ready"
asteroids = []

while len(asteroids) < 4:
   # print len(asteroids)
    asteroids += [Asteroid(width)]
    for asteroid in asteroids:
        for otherAsteroid in asteroids:
            if asteroid.collideAsteroid(otherAsteroid):
                asteroids.remove(asteroid)



while go:
    startimage = pygame.transform.scale(pygame.image.load("Screen Display/StartScreen/images/startscreen.png"), [width,height])
   
   #STARTSCREEN
 
    while mode == "ready":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(1000)
                mode = "play"  
        screen.blit(startimage, (0,0))
        pygame.display.flip()
        clock.tick(60)
        
    
    while mode == "play":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                missile = Missile(player1.rect.center, event.pos)
            if event.type == pygame.MOUSEMOTION:
                if missile:
                    missile.headTo(event.pos)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    paused = True
                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT: sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_t:
                                    paused = False
                                
                if event.key == pygame.K_w:
                    player1.go("north")
                if event.key == pygame.K_a:
                    player1.go("west")
                if event.key == pygame.K_s:
                    player1.go("south")
                if event.key == pygame.K_d:
                    player1.go("east") 
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_q:
                    pygame.quit()    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1.go("northU")
                if event.key == pygame.K_a:
                    player1.go("westU")
                if event.key == pygame.K_s:
                    player1.go("southU")
                if event.key == pygame.K_d:
                    player1.go("eastU")
    
        if len(asteroids)<15:
            if random.randint(0,10) == 0:
                asteroids += [Asteroid(width)]
                for otherAsteroid in asteroids:
                    if asteroids[-1].collideAsteroid(otherAsteroid):
                        asteroids[-1].living = False
    
    
    
        player1.update(size)
        #HealthBar.update()
    
        
        for asteroid in asteroids:
            asteroid.update(size)
            if missile:
                missile.collide(asteroid)
            if not asteroid.living:
                asteroids.remove(asteroid)
  
        if missile:
            missile.update()
            if not missile.living:
                missile.remove(Missile)
          ############  if missile.collideAsteroid:
			#	missile.remove(Missile)
        
        for hitter in asteroids:
            for hittie in asteroids:
                hitter.collideAsteroid(hittie)
            hitter.collideShip(player1)
            player1.collide(hitter)

            
        
        
        bg = pygame.transform.scale(pygame.image.load("Screen Display/Background/images/space.png"), [width,height])
        screen.blit(bg, (0,0))
        if missile:
            screen.blit(missile.image, missile.rect)
        screen.blit(player1.image, player1.rect)
        for asteroid in asteroids:
            screen.blit(asteroid.image, asteroid.rect)
        screen.blit(health.image, health.rect)
        screen.blit(shield.image, shield.rect)
        screen.blit(repair.image, repair.rect)
        screen.blit(lightspeed.image, lightspeed.rect)
        screen.blit(complete.image, complete.rect)

        pygame.display.flip()
        clock.tick(60)
        # print clock.get_fps()
