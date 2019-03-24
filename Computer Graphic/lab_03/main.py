from tkinter import *
import math
from tkinter import messagebox as mb
import numpy
# import time


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("760x550")
        self.resizable(False, False)

        self.colors = None
        self.methods = None

        self.x_start = None
        self.y_start = None
        self.x_end = None
        self.y_end = None

        self.color_rb = None
        self.method_rb = None

        self.canvas = None
        self.canvas_size = 550

        self.param_frame = Frame(self, bd=2, relief="groove")
        self.param_frame.grid(row=0, column=0, sticky=W, pady=10)

        self.__create_points_entry()
        self.__create_color_rb()
        self.__create_method_rb()
        self.__create_draw_n_cmp_n_clear_buttons()
        self.__create_canvas()

    def __create_points_entry(self):
        entry_frame = Frame(self.param_frame, bd=2, relief="groove")
        entry_frame.grid(row=0, column=0, sticky=W+E)

        self.x_start = Entry(entry_frame, width=5)
        self.y_start = Entry(entry_frame, width=5)
        self.x_end = Entry(entry_frame, width=5)
        self.y_end = Entry(entry_frame, width=5)

        note_label = Label(entry_frame, text="Начальная точка:")
        x_label = Label(entry_frame, text="X:")
        y_label = Label(entry_frame, text="Y:")

        note_label.grid(row=0, column=0, columnspan=4)
        x_label.grid(row=1, column=0)
        self.x_start.grid(row=1, column=1)
        y_label.grid(row=1, column=2)
        self.y_start.grid(row=1, column=3)

        note_label = Label(entry_frame, text="Конечная точка:")
        x_label = Label(entry_frame, text="X:")
        y_label = Label(entry_frame, text="Y:")

        note_label.grid(row=2, column=0, columnspan=4)
        x_label.grid(row=3, column=0)
        self.x_end.grid(row=3, column=1)
        y_label.grid(row=3, column=2)
        self.y_end.grid(row=3, column=3)

    def __create_color_rb(self):
        color_rb_frame = Frame(self.param_frame, bd=2, relief="groove")
        color_rb_frame.grid(row=1, column=0, sticky=W+E)
        self.color_rb = IntVar()

        color_label = Label(color_rb_frame, text="\nВыберите цвет:")
        color_label.pack()

        self.colors = [("Белый", "#FFFFFF"),
                       ("Красный", "#FF0000"),
                       ("Зеленый", "#00FF00"),
                       ("Синий", "#3375dd"),
                       ("Фиолетовый", "#7020FF")]

        for i in range(len(self.colors)):
            rb = Radiobutton(color_rb_frame, text=self.colors[i][0], value=i, variable=self.color_rb)
            rb.pack(anchor=W, padx=5)

    def __create_method_rb(self):
        method_rb_frame = Frame(self.param_frame, bd=2, relief="groove")
        method_rb_frame.grid(row=2, column=0, sticky=W+E)
        self.method_rb = IntVar()

        method_label = Label(method_rb_frame, text="\nВыберите алгоритм:")
        method_label.pack()

        self.methods = [("Библиотечный", self.__bib_method),
                        ("Брезенхэма c целыми числами", self.__braz_int),
                        ("Брезенхэма с удалением ступ.", self.__braz_stepless),
                        ("Брезенхэма с дейтв. числами", self.__braz_float),
                        ("ЦДА", self.__cda)]

        for i in range(len(self.methods)):
            rb = Radiobutton(method_rb_frame, text=self.methods[i][0], value=i, variable=self.method_rb)
            rb.pack(anchor=W, padx=5)

    def __create_draw_n_cmp_n_clear_buttons(self):
        draw_n_cmp_frame = Frame(self.param_frame, bd=2, relief="groove")
        draw_n_cmp_frame.grid(row=3, column=0, sticky=W+E)

        draw_button = Button(draw_n_cmp_frame, text="Нарисовать отрезок", command=self.__draw)
        cmp_button = Button(draw_n_cmp_frame, text="Сравнить визуальные хар-ки", command=self.__compare)
        clear_button = Button(draw_n_cmp_frame, text="Очистить", command=self.__clear)

        draw_button.pack(pady=5)
        cmp_button.pack(pady=5)
        clear_button.pack(pady=5)

    def __create_canvas(self):
        canvas_frame = Frame(self)
        canvas_frame.grid(row=0, column=1, rowspan=4)

        self.canvas = Canvas(canvas_frame,
                             width=self.canvas_size,
                             height=self.canvas_size,
                             bg="#151515")

        self.canvas.pack()

    def __draw(self):
        color = self.colors[self.color_rb.get()][1]
        method = self.methods[self.method_rb.get()][1]

        xs, ys, xe, ye = self.x_start.get(), self.y_start.get(), self.x_end.get(), self.y_end.get()

        method(xs, ys, xe, ye, color)

    def __compare(self):
        self.__clear()

        color = self.colors[self.color_rb.get()][1]
        method = self.methods[self.method_rb.get()][1]

        xs, ys, xe, ye = self.canvas_size/2, self.canvas_size/2, self.canvas_size/2 + 200, self.canvas_size/2
        angles = numpy.arange(-math.pi, math.pi + math.pi/12, math.pi/6)

        for angle in angles:
            xt, yt = xs + (xe - xs)*math.cos(angle) + (ye - ys)*math.sin(angle),\
                     ye + (xe - xs)*math.sin(angle) + (ye - ys)*math.cos(angle)

            method(xs, ys, xt, yt, color)

    def __clear(self):
        self.canvas.delete("all")

    def __bib_method(self, xs, ys, xe, ye, color):
        try:
            xs = float(xs)
            ys = float(ys)
            xe = float(xe)
            ye = float(ye)
        except ValueError:
            mb.showerror("Ошибка", "Координаты должны быть вещественными числами.")
            return

        if (xs, ys) == (xe, ye):
            self.canvas.create_oval(xs, ys, xe, ye, fill=color)

        self.canvas.create_line(xs, ys, xe, ye, fill=color)

    def __sigh(self, coord):
        if coord > 0:
            return 1
        elif coord < 0:
            return -1
        else:
            return 0

    def __braz_int(self, xs, ys, xe, ye, color):
        try:
            xs = float(xs)
            ys = float(ys)
            xe = float(xe)
            ye = float(ye)
        except ValueError:
            mb.showerror("Ошибка", "Координаты должны быть вещественными числами.")
            return

        xs, ys, xe, ye = round(xs), round(ys), round(xe), round(ye)

        xchng = 0

        if (xs, ys) == (xe, ye):
            self.canvas.create_oval(xs, ys, xe, ye, outline=color)
            return

        x, y = xs, ys

        dx = xe - xs
        dy = ye - ys

        sx, sy = self.__sigh(dx), self.__sigh(dy)
        dx, dy = abs(dx), abs(dy)

        if dx <= dy:
            dx, dy = dy, dx
            xchng = 1

        e = 2*dy - dx

        for i in range(1, dx+1):
            self.canvas.create_oval(x, y, x, y, outline=color)

            if e >= 0:
                if not xchng:
                    y += sy
                else:
                    x += sx
                e -= 2*dx

            if not xchng:
                x += sx
            else:
                y += sy

            e += 2*dy

    def __braz_float(self, xs, ys, xe, ye, color):
        try:
            xs = float(xs)
            ys = float(ys)
            xe = float(xe)
            ye = float(ye)
        except ValueError:
            mb.showerror("Ошибка", "Координаты должны быть вещественными числами.")
            return

        xs, ys, xe, ye = round(xs), round(ys), round(xe), round(ye)

        xchng = 0

        if (xs, ys) == (xe, ye):
            self.canvas.create_oval(xs, ys, xe, ye, outline=color)
            return

        x, y = xs, ys

        dx = xe - xs
        dy = ye - ys

        sx, sy = self.__sigh(dx), self.__sigh(dy)
        dx, dy = abs(dx), abs(dy)

        if dx <= dy:
            dx, dy = dy, dx
            xchng = 1

        m = dy / dx
        e = m - 0.5

        for i in range(1, dx+1):
            self.canvas.create_oval(x, y, x, y, outline=color)

            if e >= 0:
                if not xchng:
                    y += sy
                else:
                    x += sx
                e -= 1.0

            if not xchng:
                x += sx
            else:
                y += sy
            e += m

    def __alpha_color(self, color, alpha):
        re_color = [int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)]

        re_color = [round(i * alpha) for i in re_color]
        re_color = "#%02x%02x%02x" % tuple(i for i in re_color)

        return re_color

    def __braz_stepless(self, xs, ys, xe, ye, color):
        try:
            xs = float(xs)
            ys = float(ys)
            xe = float(xe)
            ye = float(ye)
        except ValueError:
            mb.showerror("Ошибка", "Координаты должны быть вещественными числами.")
            return

        xs, ys, xe, ye = round(xs), round(ys), round(xe), round(ye)

        if (xs, ys) == (xe, ye):
            self.canvas.create_oval(xs, ys, xe, ye, outline=color)
            return

        xchng = 0
        x, y = xs, ys

        dx = xe - xs
        dy = ye - ys

        sx, sy = self.__sigh(dx), self.__sigh(dy)
        dx, dy = abs(dx), abs(dy)

        if dx <= dy:
            dx, dy = dy, dx
            xchng = 1

        m = dy / dx

        w = 1 - m
        e = 0.5

        for i in range(1, dx+1):
            t_color = self.__alpha_color(color, e)
            self.canvas.create_oval(x, y, x, y, outline=t_color)

            if e < w:
                if not xchng:
                    x += sx
                else:
                    y += sy
                e += m
            else:
                y += sy
                x += sx
                e -= w

            e = round(e, 2)

    def __cda(self, xs, ys, xe, ye, color):
        try:
            xs = float(xs)
            ys = float(ys)
            xe = float(xe)
            ye = float(ye)
        except ValueError:
            mb.showerror("Ошибка", "Координаты должны быть вещественными числами.")
            return

        xs, ys, xe, ye = round(xs), round(ys), round(xe), round(ye)

        if (xs, ys) == (xe, ye):
            self.canvas.create_oval(xs, ys, xe, ye, outline=color)
            return

        x, y = xs, ys

        dx = xe - xs
        dy = ye - ys

        l = max(abs(dx), abs(dy))

        dx = dx / l
        dy = dy / l

        for i in range(1, l+1):
            self.canvas.create_oval(x, y, x, y, outline=color)
            x += dx
            y += dy


def main():
    gui = GUI()
    gui.mainloop()


if __name__ == '__main__':
    main()
