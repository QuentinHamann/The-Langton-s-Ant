from tkinter import *
from tkinter import ttk

class langton :
    def __init__(self, row, col):
        self.window = Tk()
        self.window.title("Game of Life")
        self.window.geometry("900x610")
        self._screen_size = 610
        self.board = [[0] * col for _ in range(0, row)]
        self.sizex =10
        self.sizey =10
        self.canvas = Canvas(self.window, width=self._screen_size, height=self._screen_size)
        self.canvas.pack(side=LEFT)

        self.frame = Frame(self.window)
        self.frame.pack()

        self.start = Checkbutton(self.frame, width = 15, text = "Add ant",)
        self.start .pack(padx = 5, pady = 5)

        self.start = Checkbutton(self.frame, width = 15, text = "Grid",)
        self.start .pack(padx = 5, pady = 5)

        self.scale = Scale(self.frame, from_=0, to=10, orient=HORIZONTAL)
        self.scale.pack(side=TOP)

        self.button1 = Button(self.frame, text = "Start")
        self.button1.pack(padx = 3, pady = 3)

        self.button2 = Button(self.frame, text = "Stop")
        self.button2.pack(padx = 4, pady = 4)

        self.button3 = Button(self.frame, text = "Next")
        self.button3.pack(padx = 5, pady = 5)

        self.button4 = Button(self.frame, text = "Clear")
        self.button4.pack(padx = 6, pady = 6)
        
        
        for y in range(0, row):
            for x in range(0, col):
                self.board[y][x] = self.canvas.create_rectangle(x * self.sizex,y *self.sizey,x * self.sizex + self.sizex, y * self.sizey + self.sizey, outline='black')
        self.canvas.itemconfig(self.board[30][30], fill="red")



    def draw(self, y, x, color):
        self.canvas.itemconfig(self.board[y][x], fill=color)
    
    
    def refresh(self):
        self.window.update()


obj = langton(60, 60)
obj.window.mainloop()