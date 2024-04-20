import pygame
from time import sleep
from random import randint





pygame.init()

back = (100, 240, 100)
mw = pygame.display.set_mode((1500, 700))
mw.fill(back)
clock = pygame.time.Clock()
dx = 3
dy = 3




move_right = False
move_left = False
game_over = False


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

gen1c = (145, 145, 145)
gencent1c = (160, 160, 160)
gen2c = (214,148,0)
gencent2c = (239, 165, 0)

upgbuttc = (69, 229, 59)
upgtextc = (30, 150, 20)
upgtext2c = (64, 44, 0)

incc = (44, 44, 45)
inc2c = (174,120,0)

textc = (0,0,0)

Ach = (48,48,48)
Achcent = (110,110,110)

#Валюта
value=1

#Заработок
inc1 = 1
inc2 = 0
inc3 = 0


#Стоимость
upgcost11 = 5
upgcost12 = 15
upgcost13 = 30
gen2cost = 300

upgcost21 = 15
upgcost22 = 30
upgcost23 = 100

upg11plus = 1


# Интерфейс
gen1 = Area(100, 100, 500, 275, gen1c)
gen1.fill()
gencent1 = Area(125, 125, 450, 225, gencent1c)
gencent1.fill()

upgbutt1 = Label(425, 130, 125, 45, upgbuttc)
upgbutt1.set_text("buy $" + str(upgcost11), 27, upgtextc)
upgbutt1.draw()
upgbutt2 = Label(425, 215, 125, 45, upgbuttc)
upgbutt2.set_text("buy $" + str(upgcost12), 27, upgtextc)
upgbutt2.draw()
upgbutt3 = Label(425, 300, 125, 45, upgbuttc)
upgbutt3.set_text("buy $" + str(upgcost13), 27, upgtextc)
upgbutt3.draw()
incstr1 = str(inc1)
incg1 = Label(140, 135, 250, 75, incc)
incg1.set_text("+" + incstr1 + "/sec", 50, upgtextc)
incg1.draw()

# Интерфейс 2
gen2 = Area(800, 100, 500, 275, textc)
gen2.fill()
buy2butt = Label(810, 110, 280, 65, upgbuttc)
buy2butt.set_text("buy gen $" + str(gen2cost), 40, upgtextc)
buy2butt.draw()

clickbutt = Label(1185, 135, 80, 75, gen2c)
upgbutt21 = Label(840, 250, 125, 45, upgbuttc)
upgbutt22 = Label(975, 250, 125, 45, upgbuttc)
upgbutt23 = Label(1110, 250, 125, 45, upgbuttc)

buttons = [upgbutt1, upgbutt2, upgbutt3, buy2butt, clickbutt, upgbutt21, upgbutt22, upgbutt23]

valuetext = Label(30, 600, 800, 100, back)
valuetext.set_text("Money:" + str(value), 35, incc)
valuetext.draw()

while not game_over:
    #Прокачка
    click = randint(1,3)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if upgbutt1.collidepoint(x, y):
                if value >= upgcost11:
                    value -= upgcost11
                    upgcost11 *= 2
                    inc1 += 1
                    incstr1 = str(inc1)
                    incg1.set_text("+" + incstr1 + "/sec", 50, upgtextc)
                    incg1.draw()
                    upgbutt1 = Label(425, 130, 125, 45, upgbuttc)
                    upgbutt1.set_text("buy $" + str(upgcost11), 27, upgtextc)
                    upgbutt1.draw()
            elif upgbutt2.collidepoint(x, y):
                if value >= upgcost12:
                    value -= upgcost12
                    upgcost12 *= 2
                    inc1 += upg11plus
                    upg11plus *= 2
                    incstr1 = str(inc1)
                    incg1.set_text("+" + incstr1 + "/sec", 50, upgtextc)
                    incg1.draw()
                    upgbutt2 = Label(425, 215, 125, 45, upgbuttc)
                    upgbutt2.set_text("buy $" + str(upgcost12), 27, upgtextc)
                    upgbutt2.draw()
            elif upgbutt3.collidepoint(x, y):
                if value >= upgcost13:
                    value -= upgcost13
                    upgcost13 *= 5
                    inc1 *= 3
                    incstr1 = str(inc1)
                    incg1.set_text("+" + incstr1 + "/sec", 50, upgtextc)
                    incg1.draw()
                    upgbutt3 = Label(425, 300, 125, 45, upgbuttc)
                    upgbutt3.set_text("buy $" + str(upgcost13), 27, upgtextc)
                    upgbutt3.draw()
            elif buy2butt.collidepoint(x, y):
                if value >= gen2cost:
                    value -= gen2cost
                    value = 0
                    upgcost11 = 5
                    upgcost12 = 15
                    upgcost13 = 30
                    inc1 = 1

                    incstr1 = str(inc1)
                    incg1.set_text("+" + incstr1 + "/sec", 50, upgtextc)
                    incg1.draw()
                    upgbutt1.set_text("buy $" + str(upgcost11), 27, upgtextc)
                    upgbutt1.draw()
                    upgbutt2.set_text("buy $" + str(upgcost12), 27, upgtextc)
                    upgbutt2.draw()
                    upgbutt3.set_text("buy $" + str(upgcost13), 27, upgtextc)
                    upgbutt3.draw()

                    inc2 = 1

                    gen2 = Area(800, 100, 500, 275, gen2c)
                    gen2.fill()
                    gencent2 = Area(825, 125, 450, 225, gencent2c)
                    gencent2.fill()

                    incg2 = Label(840, 135, 325, 75, inc2c)
                    incg2.set_text("1 click =" + str(inc2) + "$", 50, upgtext2c)
                    incg2.draw()
                    clickbutt.set_text("click", 30, upgtext2c)
                    clickbutt.draw()

                    upgbutt21.set_text("buy $" + str(upgcost21), 27, upgtextc)
                    upgbutt21.draw()
                    upgbutt22.set_text("buy $" + str(upgcost22), 27, upgtextc)
                    upgbutt22.draw()
                    upgbutt23.set_text("buy $" + str(upgcost23), 27, upgtextc)
                    upgbutt23.draw()
            elif clickbutt.collidepoint(x, y):
                value += inc2
            elif upgbutt21.collidepoint(x, y):
                if value >= upgcost21:
                    value -= upgcost21
                    upgcost21 *= 2
                    inc2 += 1
                    upgbutt21 = Label(840, 250, 125, 45, upgbuttc)
                    upgbutt21.set_text("buy $" + str(upgcost21), 27, upgtextc)
                    upgbutt21.draw()
                    incg2 = Label(840, 135, 300, 75, inc2c)
                    incg2.set_text("1 click =" + str(inc2) + "$", 50, upgtext2c)
                    incg2.draw()
            elif upgbutt22.collidepoint(x, y):
                if value >= upgcost22:
                    value -= upgcost22
                    upgcost22 *= 2
                    inc2 *= 2
                    upgbutt22 = Label(975, 250, 125, 45, upgbuttc)
                    upgbutt22.set_text("buy $" + str(upgcost22), 27, upgtextc)
                    upgbutt22.draw()
                    incg2 = Label(840, 135, 300, 75, inc2c)
                    incg2.set_text("1 click =" + str(inc2) + "$", 50, upgtext2c)
                    incg2.draw()
            elif upgbutt23.collidepoint(x, y):
                if value >= upgcost23:
                    value -= upgcost23
                    upgcost23 *= 5
                    inc1 *= 2
                    upgbutt23 = Label(1110, 250, 125, 45, upgbuttc)
                    upgbutt23.set_text("buy $" + str(upgcost23), 27, upgtextc)
                    upgbutt23.draw()
                    incg1 = Label(140, 135, 250, 75, incc)
                    incg1.set_text("+" + incstr1 + "/sec", 50, upgtextc)
                    incg1.draw()


    if value >= 10000:
        Achiviment = Area(1000, 500, 1500, 200, Ach)
        Achiviment.fill()
        achcent = Label(1025, 525, 1500, 150, Achcent)
        achcent.set_text("Secret Achievement!", 35, textc)
        achcent.draw()
        achcent2 = Label(1025, 625, 1500, 50, Achcent)
        achcent2.set_text("You got 10k$. Congrats!", 35, textc)
        achcent2.draw()




    value += inc1

    valuetext.set_text("Money:" + str(value), 35, incc)
    valuetext.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    pygame.display.update()
    clock.tick(1)