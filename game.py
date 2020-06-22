
import tkinter
import time

sleep_time = 0.02
root = tkinter.Tk()
root.title("game")
canvas = tkinter.Canvas(root, bg='white', height=400, width=600)
canvas.pack()


class Player:
    def __init__(self, _canvas, _barrier):
        self.canvas = _canvas
        self.barrier = _barrier
        self.pos_y = 300
        self.img = self.canvas.create_rectangle(80, 30, 100, 10, fill='black')
        self.canvas.bind_all('<Button-1>', self.jump)
        self.status = 0
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        print(self.width, self.height)

    def get_pos(self):
        if self.status == 0:
            pass
        elif self.status == 1:
            self.pos_y -= 5
            if self.pos_y == 200:
                self.status = 2
        elif self.status == 2:
            self.pos_y += 5
            if self.pos_y == 300:
                self.status = 0

    def draw(self):
        self.get_pos()
        self.img = self.canvas.create_rectangle(80, 30 + self.pos_y,
                                                100, 10 + self.pos_y, fill='black')

    def jump(self, event):
        if self.status == 0:
            self.status = 1
        else:
            pass
        print("get click", self.pos_y)

    def is_end(self):
        if 10 + self.barrier.pos_x <= 100 and \
                self.pos_y + 10 > 300 and \
                1 + self.barrier.pos_x >= 70:
            return True
        else:
            return False


class Cloud:
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos_x = 30
        self.pos_y = 20
        self.img = self.canvas.create_oval(10, 10, 25, 25, fill='red')

    def get_pos(self):
        self.pos_x -= 3
        if self.pos_x <= 0:
            self.pos_x = 600

    def draw(self):
        self.get_pos()
        self.img = self.canvas.create_oval(10 + self.pos_x, 30, 40 + self.pos_x, 55, fill='red')


class Barrier:
    def __init__(self, canvas):
        self.canvas = canvas
        self.pos_x = 600
        self.pos_y = 20
        self.img = self.canvas.create_oval(10, 10, 25, 25)

    def get_pos(self):
        self.pos_x -= 5
        if self.pos_x <= 0:
            self.pos_x = 600

    def draw(self):
        self.get_pos()
        self.img = self.canvas.create_rectangle(10 + self.pos_x, 300, 40 + self.pos_x, 330)


cloud = Cloud(canvas)
barrier = Barrier(canvas)
player = Player(canvas, barrier)

on_stage = []
on_stage.append(player)
on_stage.append(cloud)
on_stage.append(barrier)

while 1:
    for i in on_stage:
        i.draw()

    if player.is_end():
        break

    root.update_idletasks()
    root.update()
    time.sleep(sleep_time)
    canvas.delete('all')

print("game over")
