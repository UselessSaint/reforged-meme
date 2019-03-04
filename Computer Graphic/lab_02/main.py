from tkinter import *
from tkinter import messagebox as mb
import numpy as np
import math


def astroida_point(angle, radius):
    x = radius*math.cos(angle)**3
    y = radius*math.sin(angle)**3

    return [x, y]


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("760x600")
        self.resizable(False, False)

        self.sp_x_entry = None
        self.sp_y_entry = None
        self.t_x_entry = None
        self.t_y_entry = None
        self.sc_x_entry = None
        self.sc_y_entry = None
        self.angle_entry = None

        self.canvas = None
        self.canvas_size = 550
        self.border = 20

        self.astroida_points = None
        self.rect_points = None
        self.radius = 50
        self.rect_lesser_side = self.radius + 20

        self.in_circle_points = None
        self.in_circle_radius = self.radius/4
        self.in_circle_point = None

        self.__create_startpoint_menu()
        self.__create_canvas()
        self.__init_drawing_coordinated()
        self.__draw()
        self.__create_transfer_menu()
        self.__create_scaling_menu()
        self.__create_turn_menu()

    def __create_scaling_menu(self):
        scaling_frame = Frame(self)

        self.sc_x_entry = Entry(scaling_frame, width=5)
        self.sc_y_entry = Entry(scaling_frame, width=5)

        note_label = Label(scaling_frame, text="Масштабирование")
        x_label = Label(scaling_frame, text="kX:")
        y_label = Label(scaling_frame, text="kY:")

        scale_button = Button(scaling_frame, text="Масштабировать",
                              command=self.__scale)

        note_label.grid(row=0, column=0, columnspan=4)
        x_label.grid(row=1, column=0)
        self.sc_x_entry.grid(row=1, column=1)
        y_label.grid(row=1, column=2)
        self.sc_y_entry.grid(row=1, column=3)
        scale_button.grid(row=2, column=0, columnspan=4)
        scaling_frame.grid(row=2, column=0, padx=5, pady=5)

    def __scale(self):
        kx, ky = self.sc_x_entry.get(), self.sc_y_entry.get()
        sp_x, sp_y = self.sp_x_entry.get(), self.sp_y_entry.get()

        try:
            sp_x = float(sp_x)
            sp_y = float(sp_y)
        except ValueError:
            mb.showerror("Ошибка", "Координаты центра масштабирования "
                                   "должны быть вещественными числами")
            return

        sp_x = -sp_x

        try:
            kx = float(kx)
            ky = float(ky)
        except ValueError:
            mb.showerror("Ошибка", "kX и kY должны быть вещественными числами")
            return

        # x1 = kx * x + (1 - kx) xm

        for i in range(len(self.astroida_points)):
            self.astroida_points[i][0] = self.astroida_points[i][0]*kx+(1-kx)*sp_x
            self.astroida_points[i][1] = self.astroida_points[i][1]*ky+(1-ky)*sp_y

        for i in range(len(self.rect_points)):
            self.rect_points[i][0] = self.rect_points[i][0]*kx+(1-kx)*sp_x
            self.rect_points[i][1] = self.rect_points[i][1]*ky+(1-ky)*sp_y

        for i in range(len(self.in_circle_points)):
            self.in_circle_points[i][0] = self.in_circle_points[i][0]*kx+(1-kx)*sp_x
            self.in_circle_points[i][1] = self.in_circle_points[i][1]*ky+(1-ky)*sp_y

        for i in range(len(self.in_circle_point)):
            self.in_circle_point[i][0] = self.in_circle_point[i][0]*kx+(1-kx)*sp_x
            self.in_circle_point[i][1] = self.in_circle_point[i][1]*ky+(1-ky)*sp_y

        self.__draw()

    def __create_transfer_menu(self):
        transfer_frame = Frame(self)

        self.t_x_entry = Entry(transfer_frame, width=5)
        self.t_y_entry = Entry(transfer_frame, width=5)

        note_label = Label(transfer_frame, text="Перенос")
        x_label = Label(transfer_frame, text="dX:")
        y_label = Label(transfer_frame, text="dY:")

        transfer_button = Button(transfer_frame, text="Выполнить перенос",
                                 command=self.__transfer)

        note_label.grid(row=0, column=0, columnspan=4)
        x_label.grid(row=1, column=0)
        self.t_x_entry.grid(row=1, column=1)
        y_label.grid(row=1, column=2)
        self.t_y_entry.grid(row=1, column=3)
        transfer_button.grid(row=2, column=0, columnspan=4)
        transfer_frame.grid(row=1, column=0, padx=5, pady=5)

    def __transfer(self):
        dx = self.t_x_entry.get()
        dy = self.t_y_entry.get()

        try:
            dx = float(dx)
            dy = float(dy)
        except ValueError:
            mb.showerror("Ошибка", "dX и dY должны быть вещественными числами")
            return

        for i in range(len(self.astroida_points)):
            self.astroida_points[i][0] -= dx
            self.astroida_points[i][1] += dy

        for i in range(len(self.rect_points)):
            self.rect_points[i][0] -= dx
            self.rect_points[i][1] += dy

        for i in range(len(self.in_circle_point)):
            self.in_circle_point[i][0] -= dx
            self.in_circle_point[i][1] += dy

        for i in range(len(self.in_circle_points)):
            self.in_circle_points[i][0] -= dx
            self.in_circle_points[i][1] += dy

        self.__draw()

    def __create_turn_menu(self):
        turn_frame = Frame(self)

        self.angle_entry = Entry(turn_frame, width=5)

        note_label = Label(turn_frame, text="Поворот")
        angle_label = Label(turn_frame, text="Угол:")

        turn_button = Button(turn_frame, text="Повернуть",
                             command=self.__turn)

        note_label.grid(row=0, column=0, columnspan=4)
        angle_label.grid(row=1, column=0)
        self.angle_entry.grid(row=1, column=1)
        turn_button.grid(row=2, column=0, columnspan=4)
        turn_frame.grid(row=3, column=0, padx=5, pady=5)

    def __turn(self):
        angle = self.angle_entry.get()
        sp_x, sp_y = self.sp_x_entry.get(), self.sp_y_entry.get()

        try:
            sp_x = float(sp_x)
            sp_y = float(sp_y)
        except ValueError:
            mb.showerror("Ошибка", "Координаты центра масштабирования "
                                   "должны быть вещественными числами")
            return

        sp_x = -sp_x

        try:
            angle = float(angle)
        except ValueError:
            mb.showerror("Ошибка", "Угол должен быть вещественным числом")
            return

        angle = angle * math.pi / 180

        for i in range(len(self.astroida_points)):
            self.astroida_points[i][0], self.astroida_points[i][1] =\
                sp_x+(self.astroida_points[i][0]-sp_x)*math.cos(angle) + \
                (self.astroida_points[i][1]-sp_y)*math.sin(angle),\
                sp_y-(self.astroida_points[i][0]-sp_x)*math.sin(angle) + \
                (self.astroida_points[i][1]-sp_y)*math.cos(angle)

        for i in range(len(self.rect_points)):
            self.rect_points[i][0], self.rect_points[i][1] =\
                sp_x+(self.rect_points[i][0]-sp_x)*math.cos(angle) + \
                (self.rect_points[i][1]-sp_y)*math.sin(angle),\
                sp_y-(self.rect_points[i][0]-sp_x)*math.sin(angle) + \
                (self.rect_points[i][1]-sp_y)*math.cos(angle)

        for i in range(len(self.in_circle_points)):
            self.in_circle_points[i][0], self.in_circle_points[i][1] = \
                sp_x+(self.in_circle_points[i][0]-sp_x)*math.cos(angle) + \
                (self.in_circle_points[i][1]-sp_y)*math.sin(angle), \
                sp_y-(self.in_circle_points[i][0]-sp_x)*math.sin(angle) + \
                (self.in_circle_points[i][1]-sp_y)*math.cos(angle)

        for i in range(len(self.in_circle_point)):
            self.in_circle_point[i][0], self.in_circle_point[i][1] = \
                sp_x+(self.in_circle_point[i][0]-sp_x)*math.cos(angle) + \
                (self.in_circle_point[i][1]-sp_y)*math.sin(angle), \
                sp_y-(self.in_circle_point[i][0]-sp_x)*math.sin(angle) + \
                (self.in_circle_point[i][1]-sp_y)*math.cos(angle)


        self.in_circle_points[i][0] =

        self.__draw()

    def __create_startpoint_menu(self):
        startpoint_menu_frame = Frame(self)

        self.sp_x_entry = Entry(startpoint_menu_frame, width=5)
        self.sp_y_entry = Entry(startpoint_menu_frame, width=5)

        sp_show_button = Button(startpoint_menu_frame, text="Показать точку машт./пов.",
                                command=self.__show_sp)
        sp_show_button.grid(row=3, column=0, columnspan=4)

        note_label = Label(startpoint_menu_frame, text="т. Масштаба/Поворота")
        x_label = Label(startpoint_menu_frame, text="X:")
        y_label = Label(startpoint_menu_frame, text="Y:")

        note_label.grid(row=0, column=0, columnspan=4)
        x_label.grid(row=1, column=0)
        self.sp_x_entry.grid(row=1, column=1)
        y_label.grid(row=1, column=2)
        self.sp_y_entry.grid(row=1, column=3)
        startpoint_menu_frame.grid(row=0, column=0, padx=5, pady=5)

    def __show_sp(self):
        sp_x, sp_y = self.sp_x_entry.get(), self.sp_y_entry.get()

        try:
            sp_x = float(sp_x)
            sp_y = float(sp_y)
        except ValueError:
            mb.showerror("Ошибка", "Координаты центра масштабирования/поворота "
                                   "должны быть вещественными числами")

        self.__draw()
        self.canvas.create_oval(self.canvas_size/2+sp_x-2,
                                self.canvas_size/2-sp_y+2,
                                self.canvas_size/2+sp_x+2,
                                self.canvas_size/2-sp_y-2,
                                fill='red')

    def __create_canvas(self):
        canvas_frame = Frame(self, bg='grey')

        self.canvas = Canvas(canvas_frame,
                             width=self.canvas_size+self.border,
                             height=self.canvas_size+self.border)

        canvas_frame.grid(row=0, column=1, rowspan=4)
        self.canvas.grid(row=0, column=0, padx=5, pady=5)

    def __init_drawing_coordinated(self):
        pi_array = np.arange(0, 2*math.pi, 0.01)
        self.astroida_points = []
        self.in_circle_points = []
        self.rect_points = []

        for i in range(len(pi_array)):
            self.astroida_points.append(astroida_point(pi_array[i], self.radius))

        self.rect_points = [astroida_point(0, self.radius),
                            astroida_point(math.pi, self.radius),
                            astroida_point(math.pi, self.radius),
                            astroida_point(0, self.radius)]

        self.rect_points[2][1] -= self.rect_lesser_side
        self.rect_points[3][1] -= self.rect_lesser_side

        self.in_circle_points = [astroida_point(math.pi/2, self.radius),
                                 astroida_point(math.pi/2, self.radius)]

        self.in_circle_points[0][0] -= self.in_circle_radius
        self.in_circle_points[0][1] = self.in_circle_radius
        self.in_circle_points[1][0] += self.in_circle_radius
        self.in_circle_points[1][1] = -self.in_circle_radius

        self.in_circle_point = [astroida_point(math.pi/2, self.radius),
                                astroida_point(math.pi/2, self.radius)]

        self.in_circle_point[0][1] = 0
        self.in_circle_point[1][1] = 0

    def __draw(self):
        self.canvas.delete("all")
        print(self.in_circle_points)
        for i in range(len(self.astroida_points)-1):
            self.canvas.create_line(self.canvas_size/2-self.astroida_points[i][0],
                                    self.canvas_size/2-self.astroida_points[i][1],
                                    self.canvas_size/2-self.astroida_points[i+1][0],
                                    self.canvas_size/2-self.astroida_points[i+1][1])

        self.canvas.create_line(self.canvas_size/2-self.rect_points[1][0],
                                self.canvas_size/2-self.rect_points[1][1],
                                self.canvas_size/2-self.rect_points[2][0],
                                self.canvas_size/2-self.rect_points[2][1])

        self.canvas.create_line(self.canvas_size/2-self.rect_points[2][0],
                                self.canvas_size/2-self.rect_points[2][1],
                                self.canvas_size/2-self.rect_points[3][0],
                                self.canvas_size/2-self.rect_points[3][1])

        self.canvas.create_line(self.canvas_size/2-self.rect_points[3][0],
                                self.canvas_size/2-self.rect_points[3][1],
                                self.canvas_size/2-self.rect_points[0][0],
                                self.canvas_size/2-self.rect_points[0][1])

        self.canvas.create_oval(self.canvas_size/2-self.in_circle_points[0][0],
                                self.canvas_size/2-self.in_circle_points[0][1],
                                self.canvas_size/2-self.in_circle_points[1][0],
                                self.canvas_size/2-self.in_circle_points[1][1])

        self.canvas.create_oval(self.canvas_size/2-self.in_circle_point[0][0],
                                self.canvas_size/2-self.in_circle_point[0][1],
                                self.canvas_size/2-self.in_circle_point[1][0],
                                self.canvas_size/2-self.in_circle_point[1][1])


def main():
    gui = GUI()
    gui.mainloop()


if __name__ == '__main__':
    main()
