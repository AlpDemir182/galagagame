import pygame
import pgzrun

WIDTH = 600
HEIGHT = 800

game = True
galaga = Actor("galaga.png")

galaga.x = 300
galaga.y = 750

bullets = []
bugs = []
score = 0

for x in range(5):
    for y in range(5):
        bug2 = Actor("bug.png")
        bug2.x = 100+x*100
        bug2.y = 100+y*100
        bugs.append(bug2)

def draw():
    global game
    screen.fill("black")
    if game:
        galaga.draw()
        for i in bullets:
            i.draw()
        for j in bugs:
            j.draw()

        if len(bugs) == 0:
            game = False
            screen.draw.text("Game Over, You Win!", (100, 300), fontsize = 50)
            screen.draw.text("Press R to replay", (300,300), fontsize = 50)

        if game == "lost":
            screen.fill("black")
            screen.draw.text("Game Over, You Lost!", (100, 300), fontsize = 50)
            screen.draw.text("Press R to replay", (300,500), fontsize = 50)

    screen.draw.text("Score = " +str(score), (100, 600), fontsize = 25)


def update():
    global game, score
    if keyboard.left:
        galaga.x = galaga.x - 10
    if keyboard.right: 
        galaga.x = galaga.x + 10

    for i in bullets:
        i.y = i.y-10

    for j in bugs:
        j.y = j.y + 1
        for i in bullets:
            if i.colliderect(j):
                bullets.remove(i)
                bugs.remove(j)
                score += 1

        if j.colliderect(galaga):
            game = "lost"



def on_key_down(key):
    global game, bullets, bugs
    if key == keys.SPACE:
        bullet = Actor("bullet.png")
        bullet.x = galaga.x
        bullet.y = galaga.y
        bullets.append(bullet)

    if (game == False) or (game == "lost"):
        if key == keys.R:
            
            game = True
            bugs = []
            bullets = []
            for x in range(5):
                for y in range(5):
                    bug2 = Actor("bug.png")
                    bug2.x = 100+x*100
                    bug2.y = 100+y*100
                    bugs.append(bug2)


pgzrun.go()

        

        

