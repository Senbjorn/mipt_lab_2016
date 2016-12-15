from random import randrange as rnd, choice
from tkinter import *
import math
 
#print (dir(math))
 
import time
root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH,expand=1)


class ball():
    """ Класс ball описывает мяч. """
    global balls
    def __init__(self,x=40,y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.avx = 100
        self.avy = 100
        self.time = 0
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue','green','red','brown', 'black'])
        self.id = canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color)
        self.live = 30

    def set_coords(self):
        canv.coords(self.id, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)

    def move(self, z, k):
        """ Метод move описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения 
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
            и стен по краям окна (размер окна 800х600).
        """
        #FIXME
        if self.vy <= 597:
            self.vy += z
        self.time += 1
        self.avy = (self.avy * (self.time - 1) + abs(self.vy)) / self.time if self.time != 1 else abs(self.vy)
        self.avx = (self.avx * (self.time - 1) + abs(self.vx)) / self.time if self.time != 1 else abs(self.vx)
        if (self.x > 800 and self.vx > 0) or (self.x < 0 and self.vx < 0):
            self.vx = -self.vx
        if self.y < 0 and self.vy > 0:
            self.vy = -self.vy
        if  self.y > 600 and self.vy < 0:
            self.vy = -self.vy
        if self.y > 597:
            self.vy -= self.vy * k
            self.vx -= self.vx * k
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()

    def remballs(self):
        if self.avy <= 0.01 and self.avx <= 0.01:
            balls.remove(self)
            canv.delete(self.id)

    def hittest(self,ob):
        if (self.x - ob.x) ** 2 + (self.y - ob.y) ** 2 < (self.r + ob.r) ** 2:
            return True
        return False


class gun():
    """ Класс gun описывает пушку. """
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7) # FIXME: don't know how to set it...
         
    def fire2_start(self,event):
        self.f2_on = 1
 
    def fire2_end(self,event):
        """ Выстрел мячом происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y)/(event.x-new_ball.x))
        new_ball.vx = self.f2_power*math.cos(self.an)
        print(new_ball.vx)#asdasdasdasdasdddddddddddddddddddddddddd
        new_ball.vy = -self.f2_power*math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
 
 
    def targetting (self,event=0):
        """ Прицеливание. Зависит от положения мыши.
        """
        if event:
            self.an = math.atan((event.y-450)/(event.x-20))    
        if self.f2_on:
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an), 450 + max(self.f2_power, 20) * math.sin(self.an))
         

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id,fill = 'orange')
        else:
            canv.itemconfig(self.id,fill = 'black')
        
class target():
    """ Класс target описывает цель. """
    global points
    def __init__(self):
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
         
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600,780)
        y = self.y = rnd(300,550)
        r = self.r = rnd(2,50)
        color = self.color = 'green'
        canv.coords(self.id, x-r,y-r,x+r,y+r)
        canv.itemconfig(self.id, fill = color)
         
    def hit(self,points = 1):
        """ Попадание шарика в цель. """
        canv.coords(self.id,-10,-10,-10,-10)
        points += points

points = 0
id_points = canv.create_text(30, 30, text = str(points), font = '28')
t1 = target()
t2 = target()
screen1 = canv.create_text(400,300, text = '',font = '28')
g1 = gun()
bullet = 0
balls = []



def new_game(event=''):
    global gun, t1, t2, screen1, balls, bullet, points, id_points
    t1.new_target()
    t2.new_target()
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    z = -1.13
    k = 0.50
    t1.live = 1
    t2.live = 1
    while t1.live or balls or t2.live:
        for b in balls:
            b.move(z, k)
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
            if b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            if not t2.live and not t1.live:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text = 'Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
            b.remballs()
        n = 0
        while n < len(balls):
            
            n += 1
        canv.itemconfig(id_points, text = str(points))
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text = '')
    canv.delete(gun)
    root.after(750,new_game)

new_game()   
 
mainloop()

