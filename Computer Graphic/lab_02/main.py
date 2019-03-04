from tkinter import *
from tkinter import messagebox as mb
import math


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.resizable(False, False)

        self.sp_x_entry = None
        self.sp_y_entry = None

        self.canvas = None
        self.canvas_size = 400
        self.border = 20

        self.__create_startpoint_menu()
        self.__create_canvas()

    def __create_scaling_menu(self):
        pass

    def __create_transfer_menu(self):
        pass

    def __create_turn_menu(self):
        pass

    def __create_startpoint_menu(self):
        startpoint_menu_frame = Frame(self)

        self.sp_x_entry = Entry(startpoint_menu_frame, width=5)
        self.sp_y_entry = Entry(startpoint_menu_frame, width=5)

        note_label = Label(startpoint_menu_frame, text="т. Масштаба/Поворота")
        x_label = Label(startpoint_menu_frame, text="X:")
        y_label = Label(startpoint_menu_frame, text="Y:")

        note_label.grid(row=0, column=0, columnspan=4)
        x_label.grid(row=1, column=0)
        self.sp_x_entry.grid(row=1, column=1)
        y_label.grid(row=1, column=2)
        self.sp_y_entry.grid(row=1, column=3)
        startpoint_menu_frame.grid(row=0, column=0, padx=5, pady=5)

    def __create_canvas(self):
        canvas_frame = Frame(self, bg='grey')

        self.canvas = Canvas(canvas_frame,
                             width=self.canvas_size+self.border,
                             height=self.canvas_size+self.border)

        canvas_frame.grid(row=0, column=1, rowspan=4)
        self.canvas.grid(row=0, column=0, padx=5, pady=5)

def main():
    gui = GUI()
    gui.mainloop()


if __name__ == '__main__':
    main()
