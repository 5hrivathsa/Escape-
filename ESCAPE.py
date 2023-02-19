#------------------------------------------------------------------------------------------------
#                                 Importing modules
#------------------------------------------------------------------------------------------------

import pygame
import time
import random
import turtle

from PIL import ImageTk 
from tkinter import *
from turtle import *

# Definitions

L_1 = 100
B_1 = 2
r_1=255

L_2 = 2
B_2 = 180
r_2=255

bg_1 = True
camera_1 = True
camera_2 = False
CamTime = True
laser_play = True

name = ''
number =  ''
sum=''
operator = ''
secret_num = 0
jump_height = 0.2

window = Tk()
window.title("Escape")
window.geometry("1280x720")
window.resizable(False,False)

bg = ImageTk.PhotoImage(file = 'bg.png')
bg_image = Label(window,image = bg).place(x=0,y=0,relwidth=1,relheight=1)

label = Label(window,text = 'ESCAPE!',bg = 'black',fg = 'pink',font = ('ariel',25,'bold')).pack()

def play():

    window.destroy()
    
    #SCREEN
    screenwidth = 720
    screenlength = 1280

    #Creating a pygame page
    pygame.init()
    root = pygame.display.set_mode((screenlength,screenwidth))
    pygame.display.set_caption("ESCAPE")

    #BG IMAGES AND SPRITES
    walkright = [pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png"),pygame.image.load("R4.png"),pygame.image.load("R5.png"),pygame.image.load("R6.png"),pygame.image.load("R7.png"),pygame.image.load("R8.png"),pygame.image.load("R9.png")]
    walkleft = [pygame.image.load("L1.png"),pygame.image.load("L2.png"),pygame.image.load("L3.png"),pygame.image.load("L4.png"),pygame.image.load("L5.png"),pygame.image.load("L6.png"),pygame.image.load("L7.png"),pygame.image.load("L8.png"),pygame.image.load("L9.png")]
    bg = pygame.image.load("-GREY BG-.jpg")
    stand = pygame.image.load("standing.png")
    grey_piece = pygame.image.load('grey_piece.png')

    nail_1 = nail_2 = nail_3 = nail_4 = nail_5 = pygame.image.load('nail.png')

    scanner = pygame.image.load('scanner.png')
    alarm = pygame.image.load('alarm.png')
    comp = pygame.image.load('computer.jpg')
    cam_1 = pygame.image.load('cam_1.png')
    cam_2 = pygame.image.load('cam_2.png')

    #ADDING SOUND EFFECTS AND BGM

    lose_bgm = pygame.mixer.Sound("-LOSE-.wav")
    win_bgm = pygame.mixer.Sound("-WIN-.wav")
    laser = pygame.mixer.Sound("-LASER-.wav")
    shouting = pygame.mixer.Sound("Shouting.wav")
    music = pygame.mixer.music.load("-BGM-.mp3")
    pygame.mixer.music.play(-1)

    #Declaring the necessary variable
    
        #TIME
    
    clock = pygame.time.Clock()
    Time = 0
    b=time.time()

        #HEALTH
    Health = 10
    
        #SECRET_NUM
    value = random.randint(0,10000)

    #Defining some functions

    def game_over():
        game_over = font_2.render('GAME OVER' , 1 , (255 , 0 , 0))
        root.blit(game_over,(255,255))
        pygame.display.update()
        lose_bgm.play()
        
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i+=1
        pygame.quit()

    def finishing():
        global name
        
        finishing = font_2.render('YOU WON!' , 1 , (0 , 255 ,0))
        root.blit(finishing , (255,255))
        pygame.display.update()
        win_bgm.play()

        file = open('Game.txt','a+')
        file.write(' {} '.format(name) + str(Time))
        file.seek(0)
        file.close()

        i = 0
        while i < 300:
            pygame.time.delay(10)
            i+=1

        pygame.quit()
        
    def create():
        window = Tk()
        window.title("Main page")
        window.geometry("600x600")
        window.configure(bg = "skyblue")
        window.resizable(False,False)
        help_button = Button(window , text = "HELP" ,bg = "green" , fg = "yellow" ,font = "Bold  20", command = help).place(relx=0.4,rely=0.3,relheight=0.1,relwidth=0.2)
        window.mainloop()

        #MEASUREMENTS

    class player(object):
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.v = 10 #(velocity)

            #Jump
            self.jump = False
            self.jumpcount = 10

            #Walk
            self.left = False
            self.right = False
            self.walkcount = 0
            
        def draw(self,root):

            root.blit(scanner,(900,300))
            root.blit(alarm , (250,300))
            root.blit(comp , (800,642))

            root.blit(nail_1 , (100,645))
            root.blit(nail_2 , (100,114))
            root.blit(nail_3 , (800,116))
            root.blit(nail_4 , (650,300))
            root.blit(nail_5 , (900,480))

            if camera_1 == True:
                root.blit(cam_1 , (500,-5))
            else:
                root.blit(cam_2 , (535,-5))

            if self.walkcount + 1 >= 27:
                self.walkcount = 0

            if self.left:
                root.blit(walkleft[self.walkcount//3], (self.x,self.y))
                self.walkcount += 1

            elif self.right:
                root.blit(walkright[self.walkcount//3], (self.x,self.y))
                self.walkcount +=1

            else:
                root.blit(stand,(self.x,self.y))
                
            pygame.draw.rect(root , (255,0,0) , (1000 , 100 , 100 ,20))
            pygame.draw.rect(root , (0,255,0) , (1000 , 100 , 100 - (5 * (10 - Health)) ,20))

    #Creating platforms
    def platforms():
        platform_1 = pygame.draw.rect(root,(0,0,0),(0 , 720 , screenlength , 20))
        platform_2 = pygame.draw.rect(root,(0,0,0),(0 , 540 , 1050 , 10))
        platform_3 = pygame.draw.rect(root,(0,0,0),(1150 , 542 , 180 , 10))
        platform_4 = pygame.draw.rect(root,(0,0,0),(0 , 358 , 105 , 10))
        platform_5 = pygame.draw.rect(root,(0,0,0),(200 , 358 , 1116 , 10))
        platform_6 = pygame.draw.rect(root,(0,0,0),(0 , 169 , 1192 , 10))

        global L_1 , B_1 , L_2 , B_2 , r_1 , r_2
        
        pygame.draw.rect(root, (128,128,128) , (350,540,125,10))
        pygame.draw.rect(root, (r_1,0,0) , (1050,540,L_1,B_1))
        pygame.draw.rect(root, (r_1,0,0) , (1050,550,L_1,B_1))
        pygame.draw.rect(root, (r_2,0,0) , (1000,180,L_2,B_2))
        pygame.draw.rect(root, (r_2,0,0) , (1010,180,L_2,B_2))
        pygame.draw.rect(root, (0,0,0) , (700,540,10,170))

    #Defining the coordinates of the platforms
    platform_1_cor = (0 , 700)
    platform_2_cor = (0 , 540)
    platform_3_cor = (1150 , 542)
    platform_4_cor = (0 , 358)
    platform_5_cor = (180 , 358)
    platform_6_cor = (0 , 169)

    text_ =  '''THE PASSWORD TO
    THE DOOR IS :




            
    ''' , value 


    text_1 = '''just like one you passed,
    there are other thorns here as well
    and if you step on them, you are
    sure to lose health Remember ....
    Time is ticking... you need to
    make out before it is 3 minutes....

    So be careful and watch your
    steps!!
            - TOM '''

    text_2 = '''Now look into this PC
    and search for the password  and
    be sure to note it down somewhere
    and don't waste time searching
    something else...you have got a
    long way to go...so better hurry up
    '''
    
    text_3 = '''HI bob... How are you
    doing ??? I hope that you are fine.
    See those prisoners , they are put
    in jail cauz they tried to escape
    and got caught so better be careful
    .....and that laser... be sure you
    dont't step on that without
    disarming it "
    
            - TOM '''
              
    text_4 = ''' To disarm the lasser,
    you need to go to an alarm box
    and press "V" be sure not to step
    away form the box untill you hear
    a laser sound cauz sometimes there
    might be a malfunctioning which
    might end up in you getting caught...

                  - TOM ''' 

    text_5 = '''See that scanning
    machine? yes, that one....i hope
    you remember the password. Now
    type the password in the machine
    and to get the machine working ,
    go near it and press "V" and
    just like before, don't leave
    untill you hear a lazer sound .
    ...just to be safe....

                  - TOM '''

    text_6 = '''I am glad you came
    this far !!! ... i am glad you
    came this far....now for the
    toughest part, you will face
    a CCTV camera in the top floor
    first, observe how it works
    and then plan on how to move
    and for this, i can't guide
    you, you need to use your
    brain!!...
    See you soon!
                  - TOM'''

    def message_1():
        win_1 = Tk()
        win_1.title("MESSAGE")
        win_1.geometry("650x650")
        win_1.configure(bg = "skyblue")
        win_1.resizable(False,False)
        message = Label(win_1 , text = text_1, bg = "skyblue" , font = "bold 30").pack()
        win_1.mainloop()

    def message_2():
        win_2 = Tk()
        win_2.title("MESSAGE")
        win_2.geometry("650x650")
        win_2.configure(bg = "skyblue")
        win_2.resizable(False,False)
        message = Label(win_2 , text = text_2 , bg = "skyblue" , font = "bold 30").pack()
        win_2.mainloop()

    def message_3():
        win_3 = Tk()
        win_3.title("MESSAGE")
        win_3.geometry("650x650")
        win_3.configure(bg = "skyblue")
        win_3.resizable(False,False)
        message = Label(win_3 , text = text_3 , bg = "skyblue" , font = "bold 30").pack()
        win_3.mainloop()

    def message_4():
        win_4 = Tk()
        win_4.title("MESSAGE")
        win_4.geometry("650x650")
        win_4.configure(bg = "skyblue")
        win_4.resizable(False,False)
        message = Label(win_4 , text = text_4 , bg = "skyblue" , font = "bold 30").pack()
        win_4.mainloop()

    def message_5():
        win_5 = Tk()
        win_5.title("MESSAGE")
        win_5.geometry("650x650")
        win_5.configure(bg = "skyblue")
        win_5.resizable(False,False)
        message = Label(win_5 , text = text_5 , bg = "skyblue" , font = "bold 30").pack()
        win_5.mainloop()
        
    def message_6():
        win_6 = Tk()
        win_6.title("MESSAGE")
        win_6.geometry("650x650")
        win_6.configure(bg = "skyblue")
        win_6.resizable(False,False)
        message = Label(win_6 , text = text_6 , bg = "skyblue" , font = "bold 30").pack()
        win_6.mainloop()

    def game_loop():
        root.blit(bg, (0,0))
        HEALTH = font_1.render('HEALTH : ' , 1 , (0,0,0))
        root.blit(HEALTH , (880 ,100))
        TIME = font_1.render('TIME : ' + str(Time) + "  Seconds" , 1 , (0,0,0))
        Version = font_3.render('version: 2.0.7.13 ', 1 , (0,0,0))
        root.blit(TIME , (600,100))
        root.blit(Version , (1120,50))
        platforms()
        man.draw(root)
        pygame.display.update()

    def TIME_loop():
        TIME = font_1.render('TIME : ' + str(Time) + "  Seconds" , 1 , (0,0,0))
        root.blit(TIME , (600,100))
        pygame.display.update()

    def keypad():
        pad=Tk()
        pad.title("SCANNER")
        pad.configure(bg="skyblue")
        pad.geometry("375x450")

        #FUNCTIONS

        def click(no):
            global number
            number += str(no)
            entry_value.set(number)

        def AC():
            global number
            number = ''
            entry_value.set(number)

        def Clear():
            global number
            number = str(int(number) // 10)
            entry_value.set(number)
            
        def enter_():
            global number , sum ,operator , secret_num
            secret_num = int(number)
            if number == '':
                number = '0'
            pad.destroy()
            
        entry_value=IntVar()
        entry_value.set(" ")
        entry=Entry(pad,textvar=entry_value,bg="lightblue",font=("arial",40 , 'bold'))
        entry.grid(row=0,column=0,columnspan=500)

        #LAYOUT

        button_ac=Button(pad,text=" AC ",bg="skyblue",fg="white",font="bold 25",command = AC)
        button_ac.grid(row=1,column=0)
        button_clear=Button(pad,text="Clear",bg="skyblue",fg="white",font="bold 25",command = Clear)
        button_clear.grid(row=1,column=1)

        button_enter = Button(pad,text = 'E\nn\nt\ne\nr\n',bg='skyblue',fg = 'white',font='bold 40',command = enter_)
        button_enter.grid(row=1,column=4,rowspan = 100,)


        button_7=Button(pad,text=" 7",bg="skyblue",fg="white",font="bold 40",command = lambda:click(7))
        button_7.grid(row=2,column=0)
        button_8=Button(pad,text=" 8 ",bg="skyblue",fg="white",font="bold 40",command = lambda:click(8))
        button_8.grid(row=2,column=1)
        button_9=Button(pad,text=" 9",bg="skyblue",fg="white",font="bold 40",command = lambda:click(9))
        button_9.grid(row=2,column=2)
        button_4=Button(pad,text=" 4",bg="skyblue",fg="white",font="bold 40",command = lambda:click(4))
        button_4.grid(row=3,column=0)
        button_5=Button(pad,text=" 5 ",bg="skyblue",fg="white",font="bold 40",command = lambda:click(5))
        button_5.grid(row=3,column=1)
        button_6=Button(pad,text=" 6",bg="skyblue",fg="white",font="bold 40",command = lambda:click(6))
        button_6.grid(row=3,column=2)
        button_1=Button(pad,text=" 1",bg="skyblue",fg="white",font="bold 40",command = lambda:click(1))
        button_1.grid(row=4,column=0)
        button_2=Button(pad,text=" 2 ",bg="skyblue",fg="white",font="bold 40",command = lambda:click(2))
        button_2.grid(row=4,column=1)
        button_3=Button(pad,text=" 3",bg="skyblue",fg="white",font="bold 40",command = lambda:click(3))
        button_3.grid(row=4,column=2)
        button_0=Button(pad,text="Zero",bg="skyblue",fg="white",font="bold 25",command = lambda:click(0))
        button_0.grid(row=1,column=2)

        pad.mainloop()

    def comp_page():
        Web = Tk()
        Web.title("WEB PAGE")
        Web.geometry("1280x720")
        Web.configure(bg = "skyblue")

        def quit():
            quit = Web.destroy()

        def password():
            page = Tk()
            page.title("PASSWORD")
            page.geometry("600x600")
            page.configure(bg = "White")
            text = Label(page , text = text_, bg = "white" , font = "Bold 20").pack()

        def shapes():
            a=turtle.Turtle()
            turtle.bgcolor("green")
            a.color("yellow","orange")
            a.begin_fill()
            i=0
            a.left(85)
            a.speed(2)
            while i<5:
                a.forward(100)
                a.right(144)
                i+=1
            a.end_fill()

        def paint():
            paint=turtle.Screen()
            paint.bgcolor("Black")
            pen=Turtle("turtle")
            pen.speed(0)
            pen.pensize(2)
            pen.color("White")

            def dragging(x,y):
                pen.ondrag(None)
                pen.setheading(pen.towards(x,y))
                pen.goto(x,y)
                pen.ondrag(dragging)

            def clickright(x,y):
                pen.clear()

            def main():
                turtle.listen()
                pen.ondrag(dragging)
                turtle.onscreenclick(clickright,3)
                paint.mainloop()
            main()


        def game():
            root_2 = turtle.Screen()
            root_2.setup(width=1000,height=650)
            root_2.bgcolor("black")
            root_2.title("Game")

            player = turtle.Turtle()
            player.color("Blue")
            player.shape("circle")
            player.speed(0)
            player.shapesize(1)
            player.penup()
            playerspeed = 10

            #Defining some functions to make the turtle move

            def move_left():
                x = player.xcor()
                x -= playerspeed
                player.setx(x)
                if x <= -435:
                    x =-435
                    player.setx(x)
                    
            def move_right():
                x = player.xcor()
                x += playerspeed
                player.setx(x)
                if x >= 435:
                    x = 435
                    player.setx(x)
                
            def move_up():
                y = player.ycor()
                y += playerspeed
                player.sety(y)
                if y >= 250:
                    y = 250
                    player.sety(y)

            def move_down():
                y = player.ycor()
                y -= playerspeed
                player.sety(y)
                if y <= -250:
                    y =- 250
                    player.sety(y)
                
            #Binding these functions with the keyboard

            turtle.listen()
            turtle.onkeypress(move_left,"Left")
            turtle.onkeypress(move_right,"Right")
            turtle.onkeypress(move_up,"Up")
            turtle.onkeypress(move_down,"Down")
            
        game_button = Button(Web , text = " GAMES " ,bg = "darkblue" , fg = "white" ,font = "Bold  15", command = game).place(relx=0.1,rely=0.1,relheight=0.1,relwidth=0.1)
        paint_button = Button(Web , text = " PAINT " ,bg = "darkblue" , fg = "white" ,font = "Bold  15", command = paint).place(relx=0.1,rely=0.2,relheight=0.1,relwidth=0.1)    
        shape_button = Button(Web , text = " SHAPES " , bg = "darkblue" , fg = "white" ,font = "Bold  15", command = shapes).place(relx=0.1,rely=0.3,relheight=0.1,relwidth=0.1)
        password_button = Button(Web , text = " PASSWORD " ,bg = "darkblue" , fg = "white" ,font = "Bold  15", command = password).place(relx=0.1,rely=0.4,relheight=0.1,relwidth=0.1)
        quit_button = Button(Web , text = " SHUT DOWN " ,bg = "darkblue" , fg = "white" ,font = "Bold  15", command = quit).place(relx=0.1,rely=0.5,relheight=0.1,relwidth=0.1)

        icon_1 = Button(Web , text = "  START  ", bg = "darkblue" ,fg="white", font = "bold 15").place(relx = 0.0 , rely = 0.95)                                                
        icon_2 = Button(Web , text = " LIBRARY ", bg = "darkblue" ,fg="white", font = "bold 15").place(relx = 0.1 , rely = 0.95)
        icon_3 = Button(Web , text = "EXPLORER ", bg = "darkblue" ,fg="white", font = "bold 15").place(relx = 0.2 , rely = 0.95)
        icon_4 = Button(Web , text = " CHROME  ", bg = "darkblue" ,fg="white", font = "bold 15").place(relx = 0.3 , rely = 0.95)
        icon_5 = Button(Web , text = "U-TORRENT", bg = "darkblue" ,fg="white", font = "bold 15").place(relx = 0.4 , rely = 0.95)
        icon_6 = Button(Web , text = " PYTHON  ", bg = "darkblue" ,fg="white", font = "bold 15").place(relx = 0.5 , rely = 0.95)

        Web.mainloop()
            
    #MAINLOOP

    font_1 = pygame.font.SysFont("conicsans" , 30 , True , True)
    font_2 = pygame.font.SysFont("conicsans" , 75 , True , True)
    font_3 = pygame.font.SysFont('conicsans' , 20 , True , True)
    

    #Creating and moving an object
        
    man=player(25,638,64,64)

    Gravity_1 = True
    Gravity_2 = True
    Gravity_3 = True
    Gravity_4 = True

    val = True
    while val:

        if man.y < 640 and man.y >= 638:
            Gravity_1 = False

        if man.y < 550 and man.y >= 540:
            if man.x >= 1050 and man.x <= 1150:
                Gravity_2 = False
            if man.x >= 350 and man.x <= 475:
                Gravity_2 = False
            
        if man.y < 370 and man.y >= 350 and man.x >= 95 and man.x <= 165:
            Gravity_3 = False

        if man.y < 190 and man.y >= 150 and man.x >= 1195 and man.x <= 1275:
            Gravity_4 = False
            
        #Animations
        clock.tick(27)
        global camera_1,camera_2,CamTime

        a = time.time()
        Time = ((a-b)//1)

        if Time >= 181:
            game_over()
            pygame.quit()

        if Time % 4 == 0:
            if CamTime == True:
                camera_1,camera_2 = camera_2,camera_1
                CamTime = False

        if (Time-1) % 4 == 0:
            CamTime = True

        if camera_2 == True:
            if man.x >= 550 and man.x <=1400 and man.y > 0 and man.y <= 115:
                if (Time) % 4 == 0:
                    root.blit(grey_piece,(500,-5))
                    root.blit(cam_2,(535,-5))
                game_over()

        if camera_2 == False:
            if man.x <= 470 and man.x >= 0 and man.y >= 0 and man.y <= 115:
                if (Time) % 4 == 0:
                    root.blit(grey_piece,(535,-5))
                    root.blit(cam_1,(505,-5))
                game_over()

        
        #Quiting the pygame page
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                val=False

        global L_1 , B_1 ,r_1 , L_2 , B_2 , r_2 , laser_play 

        if man.y >= 480 and man.y <= 500 and man.x >= 1010 and man.x <= 1110:
            if L_1 == 100 and B_1 == 2:
                game_over()
            else:
                pass

        if man.y >= 205 and man.y <= 305 and man.x >= 950 and man.x <= 1100:
            if L_2 == 2 and B_2 == 180:
                game_over()
            else:
                pass

        #Binding keys with object

        keys = pygame.key.get_pressed()

        if man.y >= -100 and man.y < 115 and man.x >= 25 and man.x <= 45:
            if bg_1 == True:
                if keys[pygame.K_LEFT] and man.x > man.v:
                    man.x -= 0
                    man.right=False
                    man.left=True
                    
                elif keys[pygame.K_RIGHT] and man.x < screenlength - man.width - man.v :
                    man.x += man.v
                    man.right=True
                    man.left=False

                else:
                    man.left=False
                    man.right=False
                    man.walkcount=0
            else:
                if keys[pygame.K_LEFT] and man.x > man.v:
                    man.x -= man.v
                    man.right=False
                    man.left=True
                    
                elif keys[pygame.K_RIGHT] and man.x < screenlength - man.width - man.v :
                    man.x += man.v
                    man.right=True
                    man.left=False

                else:
                    man.left=False
                    man.right=False
                    man.walkcount=0

        elif man.y >= 500 and man.y < 640 and man.x >= 700 and man.x <= 705:
            if bg_1 == True:
                if keys[pygame.K_LEFT] and man.x > man.v:
                    man.x -= 0
                    man.right=False
                    man.left=True
                    
                elif keys[pygame.K_RIGHT] and man.x < screenlength - man.width - man.v :
                    man.x += man.v
                    man.right=True
                    man.left=False

                else:
                    man.left=False
                    man.right=False
                    man.walkcount=0
            else:
                if keys[pygame.K_LEFT] and man.x > man.v:
                    man.x -= man.v
                    man.right=False
                    man.left=True
                    
                elif keys[pygame.K_RIGHT] and man.x < screenlength - man.width - man.v :
                    man.x += man.v
                    man.right=True
                    man.left=False

                else:
                    man.left=False
                    man.right=False
                    man.walkcount=0

        elif man.y >= 500 and man.y < 640 and man.x >= 640 and man.x < 660:
            if bg_1 == True:
                if keys[pygame.K_LEFT] and man.x > man.v:
                    man.x -= man.v
                    man.right=False
                    man.left=True
                    
                elif keys[pygame.K_RIGHT] and man.x < screenlength - man.width - man.v :
                    man.x += 0
                    man.right=True
                    man.left=False

                else:
                    man.left=False
                    man.right=False
                    man.walkcount=0
            else:
                if keys[pygame.K_LEFT] and man.x > man.v:
                    man.x -= man.v
                    man.right=False
                    man.left=True
                    
                elif keys[pygame.K_RIGHT] and man.x < screenlength - man.width - man.v :
                    man.x += man.v
                    man.right=True
                    man.left=False

                else:
                    man.left=False
                    man.right=False
                    man.walkcount=0
            
        
        else:
            if keys[pygame.K_LEFT] and man.x > man.v:
                man.x -= man.v
                man.right=False
                man.left=True
                
            elif keys[pygame.K_RIGHT] and man.x < screenlength - man.width - man.v :
                man.x += man.v
                man.right=True
                man.left=False

            else:
                man.left=False
                man.right=False
                man.walkcount=0

        if keys[pygame.K_p]:
            create()

        if man.x >= 245 and man.x <255 and man.y >= 295 and man.y <= 305:
            if keys[pygame.K_v]:
                L_1 = 0
                B_1 = 0
                r_1 = 0
                laser.play()

        if man.x >= 770 and man.x <= 840 and man.y >= 638 and man.y <= 641:
            if keys[pygame.K_v]:
                comp_page()

        if man.x >= 875 and man.x <= 920 and man.y >= 295 and man.y <= 305:
            if keys[pygame.K_v]:
                keypad()

        if laser_play == True:
            if int(secret_num) == int(value):
                L_2 = 0
                B_2 = 0
                r_2 = 0
                laser.play()
                laser_play = False
                pygame.display.update()

        if keys[pygame.K_v]:
            
            if man.x >= 600 and man.x <= 630 and man.y >= 638 and man.y < 640 :
                message_1()
            if man.x >= 705 and man.x <= 745 and man.y >= 638 and man.y < 640 :
                message_2()
            if man.x >= 525 and man.x <= 565 and man.y >= 475 and man.y < 485 :
                message_3()
            if man.x >= 40 and man.x <= 100 and man.y >= 295 and man.y < 305 :
                message_4()
            if man.x >= 530 and man.x <= 570 and man.y >= 295 and man.y < 305 :
                message_5()
            if man.x >= 1100 and man.x <= 1140 and man.y >= 295 and man.y < 305 :
                message_6()

        #what if a thorn pricks him??

        if man.x >= 85 and man.x <= 200 and man.y >= 638 and man.y < 640:
            if Health > -10:
                Health -=1
                shouting.play()
            else:
                game_over()

        if man.x >= 95 and man.x <= 200 and man.y >= 108 and man.y < 112:
            if Health > -10:
                Health -=1
                shouting.play()
            else:
                game_over()

        if man.x >= 795 and man.x <= 900 and man.y >= 108 and man.y < 112:
            if Health > -10:
                Health -=1
                shouting.play()
            else:
                game_over()

        if man.x >= 625 and man.x <= 745 and man.y >= 299 and man.y < 301:
            if Health > -10:
                Health -=1
                shouting.play()
            else:
                game_over()

        if man.x >= 880 and man.x <= 1005 and man.y >= 478 and man.y <= 482:
            if Health > -10:
                Health -=1
                shouting.play()
            else:
                game_over()

        if man.y <= 115 and man.y >= 105 and man.x <= 50 :
            finishing()
            
        #My first jump!

        global jump_height
        if man.y >= 638 and man.y <= 640 and man.x >= 1035 and man.x <= 1135:
            jump_height = 0.5

        if man.y >= 475 and man.y <= 485 and man.x >= 85 and man.x <= 165:
            jump_height = 0.5

        if man.y >= 638 and man.y <= 640 and man.x >= 350 and man.x <= 450:
            jump_height = 0.5

        if man.y >= 295 and man.y <= 305 and man.x >= 1175 and man.x <= 1275:
            jump_height = 0.5

        if not(man.jump):    
            if keys[pygame.K_UP]:
                man.jump = True
                man.right=False
                man.left=False
                man.walkcount=0
        else:
            if man.jumpcount >= -10:
                sign = 1
                if man.jumpcount < 0:
                    sign = -1
                man.y -= (man.jumpcount **2) * jump_height * sign
                man.jumpcount -= 1
                
            else:
                man.jump=False
                man.jumpcount=10

        i = 0
        gravity = 0.01
        while i <1000 and man.jump == False :    

            if Gravity_1 == False:
                man.y = 638
            else:
                man.y += gravity

            if Gravity_2 == False:
                man.y = 480
            if man.x >= 1035 and man.x <= 1115:
                jmp_height = 0.5
                man.y += gravity
                
                if Gravity_1 == False:
                    man.y = 638
                    Gravity_2 = True

            elif man.x >= 325 and man.x <= 440:
                jump_height = 0.5
                man.y += gravity

                if Gravity_1 == False:
                    man.y = 638
                    Gravity_2 = True
            
            else:
                man.y += gravity
                jump_height = 0.2

            if Gravity_3 == False:
                man.y = 300
            if man.x >= 95 and man.x <= 165:
                jump_height = 0.5
                man.y += gravity

                if Gravity_2 == False:
                    man.y = 480
                    Gravity_3 = True
            else:
                man.y += gravity
                jump_height = 0.2

            if Gravity_4 == False:
                man.y = 110
                
            if man.x >= 1175 and man.x <= 1275:
                jump_height = 0.5
                man.y += gravity
                if Gravity_3 == False:
                    man.y = 300
                    Gravity_4 = True
            else:
                man.y += gravity
                jump_height = 0.2

            i += 1
        game_loop()
    pygame.quit()

def help():

    info_2 = '''Hey there!....
All you need to do is to stand
below those white messages(and
(click 'v' to view these messages)...
and it will guide your next moves

CONTROLS:

"LEFT"  - move left
"RIGHT" - move right
"UP"    - jump
"V"     - to view
"P"     - pause (for help only)'''

    help_screen_2 = Tk()
    help_screen_2.title("INSTRUCTIONS")
    help_screen_2.geometry("600x600")
    help_screen_2.configure(bg = "white")
    help_screen_2.resizable(False,False)
    message = Label(help_screen_2 , text = info_2, bg = "white" , font = "bold 20").pack()
    help_screen_2.mainloop()

def high_score():
    f = open('Game.txt','r')
    g = f.readlines()
    for i in g:
        h = i.split()

    length = len(h)
    min_time = 181
    min_name = ''
    for i in range(1,length+1,2):
        y = int(float((h[i])))
        if y <= min_time:
            min_time = int(float((h[i])))
            min_name = h[i-1]

    highscore = Tk()
    highscore.title('HIGHSCORE')
    highscore.geometry("600x600")
    highscore.resizable(False,False)
    highscore.configure(bg = 'Skyblue')
    text_1 = 'The highscorer is {} \n The time taken is {} seconds'.format(min_name.upper(),min_time) 
    message = Label(highscore , text = text_1, bg = "skyblue", font = "bold 20").pack()
    highscore.mainloop()

def quit_():
    window.destroy()

def _login_():

    login = Tk()
    login.title('GAME')
    login.geometry("600x300")
    login.configure(bg = 'Grey')
    login.resizable(False,False)
    
    username = Label(login,text = "NAME : " ,bg = 'Grey',font = ("arial ", 30 ,"bold")).place(x = 10,y=10)

    entry_value = StringVar()
    entry_value.set("")
    entry = Entry(login,textvariable=entry_value,bg="lightblue",font=("arial",30,'bold'))
    entry.place(relx=0.3,rely=0.06,relheight=0.12,relwidth=0.6)

    def enter():
        global name
        name = entry.get()
        entry_value.set("")
        login.destroy()
        play()

    button = Button(login,text = "SUBMIT" , bg = "skyblue" ,font = ("arial",20,'bold'),command = enter).place(x=270,y=125)

    login.mainloop()
    
#BUTTONS

quit_button = Button(window , text = "QUIT" ,bg = "purple" , fg = "pink" ,font = "Bold  20", command = quit_).place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.15)
play_button = Button(window , text = "PLAY" ,bg = "purple" , fg = "pink" ,font = "Bold  20", command = _login_).place(relx=0.1,rely=0.1,relheight=0.1,relwidth=0.3)
help_button = Button(window , text = "HELP" ,bg = "purple" , fg = "pink" ,font = "Bold  20", command = help).place(relx=0.1,rely=0.3,relheight=0.1,relwidth=0.25)
highscore_button = Button(window , text = "HIGHSCORE" ,bg = "purple" , fg = "pink" ,font = "Bold  20", command = high_score).place(relx=0.1,rely=0.5,relheight=0.1,relwidth=0.2)
window.mainloop()
