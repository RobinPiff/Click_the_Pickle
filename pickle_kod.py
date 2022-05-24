import pgzrun
import time
import random


WIDTH = 900
HEIGHT = 900

skin = "deafult"

if skin == "deafult":
    pickle = Actor("pickle", (WIDTH/2, HEIGHT/2))
elif skin == "rickle":
    pickle = Actor("rickle", (WIDTH/2, HEIGHT/2))




pickle_mini = Actor("pickle_mini", (45, 100))


highscore_file = open("highscore.txt","r")
highscore = int(highscore_file.read())
highscore_file.close()


points = highscore


def draw():
    global points
    screen.fill((255,123,46))
    if skin == "deafult":
        pickle.draw()
    elif skin == "rickle":
        pickle.draw()
    screen.draw.text("= " + str(points), midleft=(75, 95), color = "black", fontsize=50)
    pickle_mini.draw()

def update():
    global pickle
    pickle.y
    pickle.x




def on_mouse_down(pos):
    global points
    if pickle.collidepoint(pos):
        if skin == "deafult" or skin == "rickle":
            points += 1
            pickle.y = random.randint(60,840)
            pickle.x = random.randint(60,840)
            sounds.splash.play()
            highscore_file = open("highscore.txt", "w")
            highscore_file.write(str(points))
            highscore_file.close()



pgzrun.go()