import tkinter as tk
from random import shuffle

colors = {
    0: 'black',
    1: '#14FA3E',
    2: '#3268FB',
    3: '#EEFF00',
    4: '#E866FF',
    5: '#BBFF0F',
    6: '#E70FFF',
    7: '#FF0F7B',
    8: '#FF0F0F',
}
class MyButton(tk.Button):
    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, bg='black', font='Calibri 15 bold', fg='#fff', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0

    def __repr__(self):
        return f'MyButton {self.x} {self.y} {self.number} {self.is_mine}'

class MineSweeper:
    window = tk.Tk()
    ROW = 10
    COLUMN =7
    MINES = 12

    def __init__(self):
        self.buttons = []
        for i in range(MineSweeper.ROW + 2):
            temp = []
            for j in range(MineSweeper.COLUMN + 2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)

    def click(self, clicked_button: MyButton):
        print(clicked_button)
        color = colours.get(clicked_button.count_bomb, "#fff")
        if clicked_button.is_mine:
            clicked_button.config(text="*", bg='red') #fg-disa
            clicked_button.is_open = True
            return
        elif clicked_button.count_bomb:
            clicked_button.config(text=clicked_button.count_bomb,disabledforeground=color, bg = "#8A8484")
            clicked_button.is_open = True
        else:
            clicked_button.config(text='',bg="#8A8484")
            clicked_button.is_open = True
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    btn = self.buttons[clicked_button.x+i][clicked_button.y+j]
                    if not btn.is_open and btn.number != 0:
                        self.click(btn)
        clicked_button.config(state='disabled')

        # if clicked_button.is_mine:
        #     clicked_button.config(text='*', bg='red')
        # else:
        #     color = colors.get(clicked_button.count_bomb, '#fff')
        #     clicked_button.config(text= clicked_button.count_bomb, disabledforeground=color)
        # clicked_button.config(state='disabled')
        # clicked_button.config(relief=tk.SUNKEN)

    def create_widgets(self):
        for i in range(1, MineSweeper.ROW +1):
            for j in range(1, MineSweeper.COLUMN +1):
                btn = self.buttons[i][j]
                btn.grid(row=i, column=j)

    def open_all_buttons(self):
        for i in range(MineSweeper.ROW + 2):
            for j in range(MineSweeper.COLUMN + 2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text='*', bg='red')
                # elif btn.count_bomb == 1:
                #     btn.config(text=btn.count_bomb, fg='#14FA3E')
                # elif btn.count_bomb == 2:
                #     btn.config(text=btn.count_bomb, fg='#3268FB')
                # elif btn.count_bomb == 3:
                #     btn.config(text=btn.count_bomb, fg='#EEFF00')
                # elif btn.count_bomb == 4:
                #     btn.config(text=btn.count_bomb, fg='#E866FF')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, '#fff')
                    btn.config(text=btn.count_bomb, fg=color)

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.count_mines_in_buttons()
        self.print_buttons()
        #self.open_all_buttons()
        MineSweeper.window.mainloop()

    def print_buttons(self):
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMN + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end=' ')
                else:
                    print(btn.count_bomb, end=' ')
            print()

    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        count = 1
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMN + 1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1

    def count_mines_in_buttons(self):
        for i in range(1, MineSweeper.ROW + 1):
            for j in range(1, MineSweeper.COLUMN + 1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i+row_dx][j+col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.ROW * MineSweeper.COLUMN + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]


game = MineSweeper()
game.start()

# photo = tk.PhotoImage(file='mask.png')
# win.iconphoto(False, photo)
# win.config(bg='#18084A')
# win.title('Калькулятор')
# win.geometry(f'240x280+100+200')
# win.resizable(False, False)

# def click(self,c_b:MyButton):
#         print(c_b)
#         color = colours.get(c_b.count_bomb, "black")
#         if c_b.is_mine:
#             c_b.config(text="*",background='red',disabledforeground='black')
#             c_b.is_open = True
#             return
#         elif c_b.count_bomb:
#             c_b.config(text=c_b.count_bomb,disabledforeground=color, bg = "#8A8484")
#             c_b.is_open = True
#         else:
#             c_b.config(text='',bg="#8A8484")
#             c_b.is_open = True
#             for i in [-1,0,1]:
#                 for j in [-1,0,1]:
#                     btn = self.buttons[c_b.x+i][c_b.y+j]
#                     if not btn.is_open and btn.number != 0:
#                         self.click(btn)
#         c_b.config(state='disabled')
