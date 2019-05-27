from tkinter import *
from math import cos, sin, pi, sqrt
from tkinter import messagebox as mb
import numpy


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("770x610")
        self.resizable(False, False)

        self.radius_entry = None
        self.ellipse_x_entry = None
        self.ellipse_y_entry = None

        self.color_rb = None
        self.colors = None

        self.canvas = None
        self.canvas_size = 550

        self.param_frame = Frame(self, bd=2, relief="groove")
        self.param_frame.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.cir_step_entry = None
        self.el_step_entry = None

        self.__create_params_entry()
        self.__create_color_rb()
        self.__create_method_rb()
        self.__create_canvas()
        self.__create_draw_n_cmp_n_clear_buttons()
# ------------------------------------

    def __create_params_entry(self):
        entry_frame = Frame(self.param_frame)
        entry_frame.grid(row=0, column=0, sticky=W+E)

        self.radius_entry = Entry(entry_frame, width=10)
        self.ellipse_x_entry = Entry(entry_frame, width=5)
        self.ellipse_y_entry = Entry(entry_frame, width=5)

        label = Label(entry_frame, text="Введите радиус:")
        label.grid(row=0, column=0, columnspan=4)
        label = Label(entry_frame, text="R:")
        label.grid(row=1, column=0)
        self.radius_entry.grid(row=1, column=1, columnspan=3)

        label = Label(entry_frame, text="Введите полуоси: ")
        label.grid(row=2, column=0, columnspan=4)
        label = Label(entry_frame, text="По Х:")
        label.grid(row=3, column=0)
        self.ellipse_x_entry.grid(row=3, column=1)
        label = Label(entry_frame, text="По Y:")
        label.grid(row=3, column=2)
        self.ellipse_y_entry.grid(row=3, column=4)

    def __create_color_rb(self):
        color_rb_frame = Frame(self.param_frame)
        color_rb_frame.grid(row=1, column=0, sticky=W+E)
        self.color_rb = IntVar()

        color_label = Label(color_rb_frame, text="\nВыберите цвет:")
        color_label.pack()

        self.colors = [("Белый", "#FFFFFF"),
                       ("Красный", "#FF0000"),
                       ("Зеленый", "#00FF00"),
                       ("Синий", "#3375dd"),
                       ("Черный", "#151515")]

        for i in range(len(self.colors)):
            rb = Radiobutton(color_rb_frame, text=self.colors[i][0], value=i, variable=self.color_rb)
            rb.pack(anchor=W, padx=5)

    def __create_method_rb(self):
        method_rb_frame = Frame(self.param_frame)
        method_rb_frame.grid(row=2, column=0, sticky=W+E)
        self.method_rb = IntVar()

        method_label = Label(method_rb_frame, text="\nВыберите алгоритм:")
        method_label.pack()

        self.methods = [("Библиотечный", self.__bib_method_crs, self.__bib_method_ell),
                        ("Брезенхэма", self.__brez_c, self.__brez_e),
                        ("Средней точки", self.__mid_p_c, self.__mid_p_e),
                        ("Каноническое уравнение", self.__canon_c, self.__canon_e),
                        ("Параметричекое уравнение", self.__param_c, self.__param_e)]

        for i in range(len(self.methods)):
            rb = Radiobutton(method_rb_frame, text=self.methods[i][0], value=i, variable=self.method_rb)
            rb.pack(anchor=W, padx=5)

    def __create_draw_n_cmp_n_clear_buttons(self):
        draw_n_cmp_frame = Frame(self.param_frame)
        draw_n_cmp_frame.grid(row=3, column=0, sticky=W+E, pady=5)

        draw_ellipse = Button(draw_n_cmp_frame, text="Нарисовать эллипс", command=self.__draw_ell)
        draw_circle = Button(draw_n_cmp_frame, text="Нарисовать окружность", command=self.__draw_crs)
        cmp_button_c = Button(draw_n_cmp_frame, text="Сравнить окружности", command=self.__compare_c)
        cmp_button_e = Button(draw_n_cmp_frame, text="Сравнить эллписы", command=self.__compare_e)
        clear_button = Button(draw_n_cmp_frame, text="Очистить", command=self.__clear)

        self.cir_step_entry = Entry(draw_n_cmp_frame, width=5)
        self.el_step_entry = Entry(draw_n_cmp_frame, width=5)

        draw_circle.grid(row=0, column=0, columnspan=2, padx=10)
        Label(draw_n_cmp_frame, text="Шаг: ").grid(row=1, column=0, padx=10)
        self.cir_step_entry.grid(row=1, column=1, padx=10)
        cmp_button_c.grid(row=2, column=0, columnspan=2, padx=10)
        draw_ellipse.grid(row=3, column=0, columnspan=2, padx=10)
        Label(draw_n_cmp_frame, text="Шаг: ").grid(row=4, column=0, padx=10)
        self.el_step_entry.grid(row=4, column=1, padx=10)
        cmp_button_e.grid(row=5, column=0, columnspan=2, padx=10)
        clear_button.grid(row=6, column=0, columnspan=2, padx=10)

    def __create_canvas(self):
        canvas_frame = Frame(self)
        canvas_frame.grid(row=0, column=1, rowspan=4)

        self.canvas = Canvas(canvas_frame,
                             width=self.canvas_size,
                             height=self.canvas_size,
                             bg="#151515")

        self.canvas.pack()
# ------------------------------------

    def __draw_crs(self):
        color = self.colors[self.color_rb.get()][1]
        method = self.methods[self.method_rb.get()][1]
        radius = self.radius_entry.get()

        xc, yc = self.canvas_size/2, self.canvas_size/2

        method(radius, xc, yc, color)

    def __bib_method_crs(self, radius, xc, yc, color):
        try:
            xc = float(xc)
            yc = float(yc)
            radius = float(radius)
        except ValueError:
            mb.showerror("Ошибка", "Радиус должен быть вещественным числом.")
            return

        self.canvas.create_oval(xc-radius, yc-radius, xc+radius, yc+radius, outline=color)

    def __compare_c(self):
        color = self.colors[self.color_rb.get()][1]
        method = self.methods[self.method_rb.get()][1]
        try:
            radius = int(self.radius_entry.get())

            xc, yc = self.canvas_size/2, self.canvas_size/2

            while radius < self.canvas_size/2:
                method(radius, xc, yc, color)
                radius += int(self.cir_step_entry.get())

        except ValueError:
            return

    def __param_c(self, r, xc, yc, color):
        try:
            r = int(r)
        except ValueError:
            return

        l = round(pi*r/2)

        for i in range(0, l+1, 1):
            fi = i/r
            x = round(r*cos(fi))
            y = round(r*sin(fi))

            self.canvas.create_oval(xc+x, yc+y, xc+x, yc+y, outline=color)
            self.canvas.create_oval(xc-x, yc+y, xc-x, yc+y, outline=color)
            self.canvas.create_oval(xc+x, yc-y, xc+x, yc-y, outline=color)
            self.canvas.create_oval(xc-x, yc-y, xc-x, yc-y, outline=color)

    def __canon_c(self, r, xc, yc, color):
        try:
            r = int(r)
        except ValueError:
            return

        for x in range(0, round(r/sqrt(2)), 1):
            y = sqrt(r*r - x*x)

            self.canvas.create_oval(xc+x, yc+y, xc+x, yc+y, outline=color)
            self.canvas.create_oval(xc-x, yc+y, xc-x, yc+y, outline=color)
            self.canvas.create_oval(xc+x, yc-y, xc+x, yc-y, outline=color)
            self.canvas.create_oval(xc-x, yc-y, xc-x, yc-y, outline=color)
            self.canvas.create_oval(xc+y, yc+x, xc+y, yc+x, outline=color)
            self.canvas.create_oval(xc-y, yc+x, xc-y, yc+x, outline=color)
            self.canvas.create_oval(xc+y, yc-x, xc+y, yc-x, outline=color)
            self.canvas.create_oval(xc-y, yc-x, xc-y, yc-x, outline=color)

    def __mid_p_c(self, r, xc, yc, color):
        try:
            r = int(r)
        except ValueError:
            return

        x, y = 0, r
        d = 5/4 - r

        while x <= y:
            self.canvas.create_oval(xc+x, yc+y, xc+x, yc+y, outline=color)
            self.canvas.create_oval(xc-x, yc+y, xc-x, yc+y, outline=color)
            self.canvas.create_oval(xc+x, yc-y, xc+x, yc-y, outline=color)
            self.canvas.create_oval(xc-x, yc-y, xc-x, yc-y, outline=color)
            self.canvas.create_oval(xc+y, yc+x, xc+y, yc+x, outline=color)
            self.canvas.create_oval(xc-y, yc+x, xc-y, yc+x, outline=color)
            self.canvas.create_oval(xc+y, yc-x, xc+y, yc-x, outline=color)
            self.canvas.create_oval(xc-y, yc-x, xc-y, yc-x, outline=color)

            x += 1

            if d < 0:
                d += 2*x + 1
            else:
                d += 2*x - 2*y + 5
                y -= 1

    def __brez_c(self, r, xc, yc, color):
        try:
            r = int(r)
        except ValueError:
            return

        x = 0
        y = r

        di = 2 - 2*r
        y_end = 0

        while y >= y_end:
            self.canvas.create_oval(xc+x, yc+y, xc+x, yc+y, outline=color)
            self.canvas.create_oval(xc-x, yc+y, xc-x, yc+y, outline=color)
            self.canvas.create_oval(xc+x, yc-y, xc+x, yc-y, outline=color)
            self.canvas.create_oval(xc-x, yc-y, xc-x, yc-y, outline=color)

            if di < 0:
                b = 2*di + 2*y -1
                x += 1

                if b < 0:
                    di += 2*x + 1
                else:
                    y -= 1
                    di += 2*x - 2*y + 2

            elif di > 0:
                b = 2*di - 2*x - 1
                y -= 1

                if b <= 0:
                    x += 1
                    di += 2*x - 2*y + 2
                else:
                    di = di - 2*y + 1
            else:
                x += 1
                y -= 1
                di += 2*x - 2*y + 2

# ------------------------------------

    def __draw_ell(self):
        color = self.colors[self.color_rb.get()][1]
        method = self.methods[self.method_rb.get()][2]
        ox, oy = self.ellipse_x_entry.get(), self.ellipse_y_entry.get()

        xc, yc = self.canvas_size/2, self.canvas_size/2

        method(ox, oy, xc, yc, color)

    def __bib_method_ell(self, ox, oy, xc, yc, color):
        try:
            xc = float(xc)
            yc = float(yc)
            ox = float(ox)
            oy = float(oy)
        except ValueError:
            mb.showerror("Ошибка", "Полуоси должены быть вещественными числами.")
            return

        self.canvas.create_oval(xc-ox, yc-oy, xc+ox, yc+oy, outline=color)

    def __compare_e(self):
        try:
            color = self.colors[self.color_rb.get()][1]
            method = self.methods[self.method_rb.get()][2]

            ox, oy = int(self.ellipse_x_entry.get()), int(self.ellipse_y_entry.get())

            xc, yc = self.canvas_size/2, self.canvas_size/2

            dx = 1.0
            dy = 1.0

            if ox > oy:
                dx = ox/oy
            else:
                dy = oy/ox

            while (ox < self.canvas_size/2) and (oy < self.canvas_size/2):
                method(ox, oy, xc, yc, color)
                ox += dx * int(self.el_step_entry.get())
                oy += dy * int(self.el_step_entry.get())
        except ValueError:
            return

    def __param_e(self, ox, oy, xc, yc, color):
        try:
            ox = int(ox)
            oy = int(oy)
        except ValueError:
            return

        m = max(ox, oy)
        l = round(pi/2*m)

        for i in range(0, l+1, 1):
            fi = i/m

            x = round(ox*cos(fi))
            y = round(oy*sin(fi))

            self.canvas.create_oval(xc+x, yc+y, xc+x, yc+y, outline=color)
            self.canvas.create_oval(xc-x, yc+y, xc-x, yc+y, outline=color)
            self.canvas.create_oval(xc+x, yc-y, xc+x, yc-y, outline=color)
            self.canvas.create_oval(xc-x, yc-y, xc-x, yc-y, outline=color)

    def __canon_e(self, ox, oy, xc, yc, color):
        try:
            ox = int(ox)
            oy = int(oy)
        except ValueError:
            return

        for x in range(0, ox + 1, 1):
            y = round(oy * sqrt(1.0 - x ** 2 / ox / ox))

            self.canvas.create_oval(xc+x, yc+y, xc+x, yc+y, outline=color)
            self.canvas.create_oval(xc-x, yc+y, xc-x, yc+y, outline=color)
            self.canvas.create_oval(xc+x, yc-y, xc+x, yc-y, outline=color)
            self.canvas.create_oval(xc-x, yc-y, xc-x, yc-y, outline=color)

        for y in range(0, oy + 1, 1):
            x = round(ox * sqrt(1.0 - y ** 2 / oy / oy))

            self.canvas.create_oval(xc+x, yc+y, xc+x, yc+y, outline=color)
            self.canvas.create_oval(xc-x, yc+y, xc-x, yc+y, outline=color)
            self.canvas.create_oval(xc+x, yc-y, xc+x, yc-y, outline=color)
            self.canvas.create_oval(xc-x, yc-y, xc-x, yc-y, outline=color)

    def __mid_p_e(self, ox, oy, xc, yc, color):
        try:
            ox = int(ox)
            oy = int(oy)
        except ValueError:
            return

        x = 0
        y = oy
        p = oy*oy - ox*ox*oy + 0.25*ox*ox
        while 2*(oy*oy)*x < 2*ox*ox*y:
            self.canvas.create_oval(xc+x, yc+y, xc+x, yc+y, outline=color)
            self.canvas.create_oval(xc-x, yc+y, xc-x, yc+y, outline=color)
            self.canvas.create_oval(xc+x, yc-y, xc+x, yc-y, outline=color)
            self.canvas.create_oval(xc-x, yc-y, xc-x, yc-y, outline=color)

            x += 1

            if p < 0:
                p += 2*oy*oy*x + oy*oy
            else:
                y -= 1
                p += 2*oy*oy*x - 2*ox*ox*y + oy*oy

        p = oy*oy*(x+0.5)*(x+0.5) + ox*ox*(y-1)*(y-1) - ox*ox*oy*oy

        while y >= 0:
            self.canvas.create_oval(xc+x, yc+y, xc+x, yc+y, outline=color)
            self.canvas.create_oval(xc-x, yc+y, xc-x, yc+y, outline=color)
            self.canvas.create_oval(xc+x, yc-y, xc+x, yc-y, outline=color)
            self.canvas.create_oval(xc-x, yc-y, xc-x, yc-y, outline=color)

            y -= 1

            if p > 0:
                p -= 2*ox*ox*y + ox*ox
            else:
                x += 1
                p += 2*oy*oy*x - 2*ox*ox*y + ox*ox

    def __brez_e(self, ox, oy, xc, yc, color):
        try:
            a = int(ox)*int(ox)
            b = int(oy)
        except ValueError:
            return

        x = 0
        y = b

        d = round(b * b / 2 - a * b * 2 + a / 2)
        b = b ** 2

        while y >= 0:

            self.canvas.create_oval(xc+x, yc+y, xc+x, yc+y, outline=color)
            self.canvas.create_oval(xc-x, yc+y, xc-x, yc+y, outline=color)
            self.canvas.create_oval(xc+x, yc-y, xc+x, yc-y, outline=color)
            self.canvas.create_oval(xc-x, yc-y, xc-x, yc-y, outline=color)

            if d < 0:
                buf = 2*d + 2*a*y - a
                x += 1
                if buf <= 0:
                    d = d + 2*b*x + b
                else:
                    y -= 1
                    d = d + 2*b*x - 2*a*y + a + b

            elif d > 0:
                buf = 2*d - 2*b*x - b
                y -= 1

                if buf > 0:
                    d = d - 2*y*a + a
                else:
                    x += 1
                    d = d + 2*x*b - 2*y*a + a + b

            else:
                x += 1
                y -= 1
                d = d + 2*x*b - 2*y*a + a + b
# ------------------------------------

    def __clear(self):
        self.canvas.delete("all")


def main():
    gui = GUI()
    gui.mainloop()


if __name__ == '__main__':
    main()
