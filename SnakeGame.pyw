import pygame as game
from pygame.font import SysFont
import random
import sys
import time

game.init()

#colours variables
red = ((255,0,0))
black = ((0,0,0))
white = ((255,255,255))
LightBlue = ((210,210,240))
LightGrey = ((230,230,220))
blue = ((0,0,230))
cyan=((30,230,230))

#Window Initialize
window=game.display.set_mode((600,450))
game.display.set_caption("2D Sanke")
game.display.update()
game.display.flip()

#font Initialize
game.font.init()
font1 = SysFont("Calibri", 30,True,False)

# Functions
def showScores(text,colour,scorePos_x,scorePos_y):
    global font1
    show=font1.render(text,True,colour)
    window.blit(show,[scorePos_x,scorePos_y])

def draw_snake(window,colour,snk_list,snakeSize_x,snakeSize_y):
        for x,y in snk_list:
            game.draw.rect(window,colour,([x,y,snakeSize_x,snakeSize_y]))
        
def RunGame():
    
    # Game Specific Variables
    Quit = False

    Game_Over=False

    clock = game.time.Clock()

    snakePos_x = 100
    snakePos_y = 150

    snakeSize_x = 15
    snakeSize_y = 15
    foodSize = 15

    frame_per_sec = 50

    velocity_x=0
    velocity_y=0
    velocity = 1

    food_x = random.randint(21,578)
    food_y = random.randint(43,426)

    score = 0

    snk_list = []
    snk_length = 1

    
    
    try:
        
        f = open("snk_hiscore.snk","r")
        check_Hiscore = f.read()
        f.close()
    except:
        f = open("snk_hiscore.snk","w+")
        f.write(str(0))
        check_Hiscore = str(0)
        show1=font1.render("Hi-Score : "+str(score)+".",True,red)
        window.blit(show1,[218,85])
        f.close()
    while not Quit:
        
        if Game_Over == True:
            window.fill(LightBlue)

            
            show1=font1.render("Your Score is "+str(score)+".",True,red)
            window.blit(show1,[205,170])
            show2=font1.render(" Game Over! Press Enter to Restart Game.",True,red)
            window.blit(show2,[50,210])



            
            if int(score)>int(check_Hiscore):                
                playMusic2=game.mixer.Sound(r"./sound/music.wav")
                playMusic2.play()
                playMusic2.stop()
                
                f = open("snk_hiscore.snk","w+")
                f.write(str(score))
                show1=font1.render("New Hi-Score : "+str(score)+".",True,red)
                window.blit(show1,[200,85])
                f.close()
                
            else:
                time.sleep(3)
                playMusic2=game.mixer.Sound(r"./sound/music.wav")
                playMusic2.play()
                playMusic2.stop()
                
                show1=font1.render("Hi-Score : "+str(check_Hiscore)+".",True,red)
                window.blit(show1,[218,85])
                f.close()


            for event in game.event.get():
                if event.type == game.QUIT:
                    Quit = True
                elif event.type == game.KEYDOWN:
                    if event.key == game.K_RETURN:
                        Game_Over = False
                        RunGame()
                    elif event.key == game.K_ESCAPE:
                        Quit = True

                    
        elif Game_Over == False:
            game.mixer.init()
            game.mixer.music.load(r"./sound/music.wav")
            game.mixer.music.play()
            for event in game.event.get():
                if event.type == game.QUIT:
                    Quit = True

                if event.type == game.KEYDOWN:
                    if event.key == game.K_RIGHT:
                        if velocity_x < 0:
                            pass
                        else:
                            velocity_x = velocity
                            velocity_y = 0
                        
                    elif event.key == game.K_LEFT:
                        if velocity_x > 0:
                            pass
                        else:
                            velocity_x= -velocity
                            velocity_y= 0
                        
                    elif event.key == game.K_UP:
                        if velocity_y > 0:
                            pass
                        else:
                            velocity_y = -velocity
                            velocity_x = 0
                        
                    elif event.key == game.K_DOWN:
                        if velocity_y < 0:
                            pass
                        else:
                            velocity_y = velocity
                            velocity_x = 0
                            
                    elif event.key == game.K_RETURN:
                        Game_Over = False
                        RunGame()
                    elif event.key == game.K_ESCAPE:
                        Quit = True
                        
            snakePos_x +=velocity_x
            snakePos_y +=velocity_y
            window.fill(LightBlue)
            game.draw.rect(window,cyan,([0,0,600,40]))
            game.draw.line(window,blue,(0,40),(600,40),5)
            game.draw.line(window,blue,(0,3),(600,3),5)
            game.draw.line(window,blue,(2,0),(2,450),5)
            game.draw.line(window,blue,(597,0),(597,450),5)
            game.draw.line(window,blue,(0,448),(600,448),5)
            showScores("Score: "+str(score),blue,30,6)
            showScores("Hi-Score: "+str(check_Hiscore),blue,405,6)
            game.draw.rect(window,black,([food_x,food_y,foodSize,foodSize]))
            
            if abs(snakePos_x-food_x)<11 and abs(snakePos_y-food_y)<11:
                food_x = random.randint(21,578)
                food_y = random.randint(43,426)
                snk_length+=4
                score+=10
                velocity+=0.2
            
            snk_head=[]
            snk_head.append(snakePos_x)
            snk_head.append(snakePos_y)
            snk_list.append(snk_head)
            draw_snake(window,red,snk_list,snakeSize_x,snakeSize_y)
            if len(snk_list)>snk_length:
                del snk_list[0]

            if snk_head in snk_list[:-1]:
                Game_Over = True
                game.mixer.init()
                playMusic=game.mixer.Sound(r"./sound/GameOver.wav")
                playMusic.play()
                time.sleep(1)
                playMusic.stop()
                
            if (snakePos_x<3 or snakePos_x>583 or snakePos_y<41 or snakePos_y>432):
                Game_Over = True
                game.mixer.init()
                playMusic=game.mixer.Sound(r"./sound/GameOver.wav")
                playMusic.play()
                time.sleep(1)
                playMusic.stop()
        
            
        clock.tick(frame_per_sec)
        game.display.update()
    
    game.quit()
    sys.exit()

def WelcomeGame():
    QuitGame=False
    global Quit
    Quit=None
    game.mixer.init()
    playMusic1=game.mixer.Sound(r"./sound/music.wav")
    playMusic1.play()

    clock = game.time.Clock()
    window.fill(cyan)
    output_img=random.randint(1,8)
    
    bgimg3 = game.image.load(r"./img/3.jpg")
    bgimg1 = game.image.load(r"./img/1.jpg")
    bgimg2 = game.image.load(r"./img/2.png")
    bgimg4 = game.image.load(r"./img/4.jpg")
    bgimg5 = game.image.load(r"./img/5.jpg")
    
    if output_img==3:
        bgimg3= game.transform.scale(bgimg3,(600,450)).convert_alpha()
        window.blit(bgimg3,(0,0))
        
    elif output_img == 1:
        bgimg1= game.transform.scale(bgimg1,(600,450)).convert_alpha()
        window.blit(bgimg1,(0,0))
        
    elif output_img == 2 or 8:
        bgimg2= game.transform.scale(bgimg2,(600,400)).convert_alpha()
        window.blit(bgimg2,(0,13))
        
    elif output_img==4 or 7 or 6:
        bgimg4= game.transform.scale(bgimg4,(600,450)).convert_alpha()
        window.blit(bgimg4,(0,0))
        
    elif output_img == 5:
        bgimg5 = game.transform.scale(bgimg5,(600,450)).convert_alpha()
        window.blit(bgimg5,(0,0))
        
    while not QuitGame:
        game.font.init()
        font2 = SysFont("Calibri", 30,True,False)
        wlcm = font2.render("Welcome to the 2D Snake Game",True,blue,True)
        window.blit(wlcm,[100,6])
        Start = font2.render("Press Enter to Start the Game.",True,blue,True)
        window.blit(Start,[115,400])
        game.display.update()
        for event in game.event.get():
            if event.type == game.QUIT:
                QuitGame = True
            if event.type == game.KEYDOWN:
                if event.key == game.K_RETURN:
                    playMusic1.stop()
                    RunGame()
                elif event.key == game.K_ESCAPE:
                    QuitGame = True
                else:
                    pass
                
    clock.tick(50)
    game.display.update()
    game.quit()
    sys.exit()

if __name__ == "__main__":
    WelcomeGame()
        

    

