from tkinter import *
import math
from tkinter import messagebox as mb
import numpy


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("770x585")
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
                        ("Брезенхэма", None),
                        ("Средней точки", None),
                        ("Каноническое уравнение", None),
                        ("Параметричекое уравнение", None)]

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

        draw_circle.pack(pady=2)
        cmp_button_c.pack(pady=2)
        draw_ellipse.pack(pady=2)
        cmp_button_e.pack(pady=2)
        clear_button.pack(pady=2)

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
        self.__clear()

        color = self.colors[self.color_rb.get()][1]
        method = self.methods[self.method_rb.get()][1]
        radius = 10

        xc, yc = self.canvas_size/2, self.canvas_size/2

        for i in range(17):
            method(radius, xc, yc, color)
            radius += 20
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
        self.__clear()

        color = self.colors[self.color_rb.get()][1]
        method = self.methods[self.method_rb.get()][2]
        ox, oy = 10, 30

        xc, yc = self.canvas_size/2, self.canvas_size/2

        for i in range(10):
            method(ox, oy, xc, yc, color)
            ox += 20
            oy += 20
# ------------------------------------

    def __clear(self):
        self.canvas.delete("all")


def main():
    gui = GUI()
    gui.mainloop()


if __name__ == '__main__':
    main()
