from tkinter import *
from tkinter import messagebox as mb
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math

def find_base_cir(points):
    first_vec_len = math.sqrt((points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2)
    seconds_vec_len = math.sqrt((points[1][0]-points[2][0])**2 + (points[1][1]-points[2][1])**2)
    third_vec_len = math.sqrt((points[2][0]-points[0][0])**2 + (points[2][1]-points[0][1])**2)

    half_per = (first_vec_len + seconds_vec_len + third_vec_len) / 2

    triagle_sq = math.sqrt(half_per*
                           round((half_per - first_vec_len), 3)*
                           round((half_per - seconds_vec_len), 3)*
                           round((half_per - third_vec_len), 3))
    cir_radius = triagle_sq / half_per

    cir_x = (seconds_vec_len * points[0][0] +
             third_vec_len * points[1][0] +
             first_vec_len * points[2][0])
    cir_x /= (first_vec_len + seconds_vec_len + third_vec_len)

    cir_y = (seconds_vec_len * points[0][1] +
             third_vec_len * points[1][1] +
             first_vec_len * points[2][1])
    cir_y /= (first_vec_len + seconds_vec_len + third_vec_len)

    cir_cen = (cir_x, cir_y)

    return cir_radius, cir_cen

def calcucalte_sq_diff(points):
    first_vec_len = math.sqrt((points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2)
    seconds_vec_len = math.sqrt((points[1][0]-points[2][0])**2 + (points[1][1]-points[2][1])**2)
    third_vec_len = math.sqrt((points[2][0]-points[0][0])**2 + (points[2][1]-points[0][1])**2)

    half_per = (first_vec_len + seconds_vec_len + third_vec_len) / 2

    triagle_sq = math.sqrt(half_per*
                           round((half_per - first_vec_len), 3)*
                           round((half_per - seconds_vec_len), 3)*
                           round((half_per - third_vec_len), 3))

    incircle_sq = (triagle_sq / half_per)**2 * math.pi

    return abs(triagle_sq - incircle_sq)

def find_triangle(points):
    min_sq_diff = calcucalte_sq_diff([points[i] for i in range(3)])
    result = [points[i] for i in range(3)]

    amount_of_point = len(points)

    # возможно тут ошибка в переборе треугольников

    for i in range(amount_of_point - 2):
        for j in range(i + 1, amount_of_point - 1):
            for k in range(j + 1, amount_of_point):
                curr_sq_diff = calcucalte_sq_diff([points[i], points[j], points[k]])
                if curr_sq_diff == 0:
                    continue
                # print(curr_sq_diff, min_sq_diff)
                if curr_sq_diff < min_sq_diff:
                    min_sq_diff = curr_sq_diff
                    result = [points[i], points[j], points[k]]

    if curr_sq_diff == 0:
        result = ()

    return result

def coordinates_validation(x, y):
    try:
        float(x)
        float(y)
    except ValueError:
        return 0

    return 1


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("660x600")

        self.coordinates_frame = None
        self.x_entry = None
        self.y_entry = None

        self.x_edited = None
        self.y_edited = None

        self.figure = None

        self.coordinates_listbox = None

        self.__create_coordinates_entry()
        self.__create_listbox()
        self.__create_listbox_editor()
        self.__create_matplot_window()
        self.__create_calculation_button()

    def __create_coordinates_entry(self):
        coordinates_frame = Frame(self)

        self.x_entry = Entry(coordinates_frame, width=5)
        self.y_entry = Entry(coordinates_frame, width=5)

        x_lable = Label(coordinates_frame, text="X = ")
        y_lable = Label(coordinates_frame, text="Y = ")

        coordinates_frame.grid(row=0, column=0, padx=5, pady=5)
        x_lable.grid(row=0, column=0)
        self.x_entry.grid(row=0, column=1, padx=5, pady=5)
        y_lable.grid(row=0, column=2)
        self.y_entry.grid(row=0, column=3, padx=5, pady=5)

        adding_coordinates_button = Button(coordinates_frame, text="Добавить точку",
                                           command=self.__add_coordinates_to_listbox)
        adding_coordinates_button.grid(row=1, column=0, columnspan=4)

    def __create_listbox(self):
        coordinates_listbox_frame = Frame(self)
        coordinates_listbox_frame.grid(row=1, column=0)

        scrollbar = Scrollbar(coordinates_listbox_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.coordinates_listbox = Listbox(coordinates_listbox_frame, height=20,
                                           yscrollcommand=scrollbar.set)
        self.coordinates_listbox.pack(side=LEFT)

        scrollbar.config(command=self.coordinates_listbox.yview)

    def __add_coordinates_to_listbox(self):
        current_x = self.x_entry.get()
        current_y = self.y_entry.get()

        if coordinates_validation(current_x, current_y):
            current_x = float(current_x)
            current_y = float(current_y)
            # self.coordinates_listbox.insert(0, "(%.3f, %.3f)" % (current_x, current_y))
            self.coordinates_listbox.insert(0, [round(current_x, 3), round(current_y, 3)])
        else:
            mb.showerror("Ошибка", "Координаты должны быть вещественными числами.")

        self.y_entry.delete(0, END)
        self.x_entry.delete(0, END)

    def __create_listbox_editor(self):
        editor_frame = Frame(self)
        editor_frame.grid(row=2, column=0, padx=5, pady=5)

        self.x_edited = Entry(editor_frame, width=5)
        self.y_edited = Entry(editor_frame, width=5)

        x_lable = Label(editor_frame, text="X = ")
        y_lable = Label(editor_frame, text="Y = ")

        x_lable.grid(row=0, column=0)
        self.x_edited.grid(row=0, column=1, padx=5, pady=5)
        y_lable.grid(row=0, column=2)
        self.y_edited.grid(row=0, column=3, padx=5, pady=5)

        edit_coordinates_button = Button(editor_frame, text="Изменить точку",
                                         command=self.__edit_coordinates)
        delete_coordinates_button = Button(editor_frame, text="Удалить точку",
                                           command=self.__delete_coordinates)

        clear_button = Button(editor_frame, text="Очистить",
                                command=self.__clear)

        clear_button.grid(row=3, column=0, columnspan=4)
        edit_coordinates_button.grid(row=1, column=0, columnspan=4)
        delete_coordinates_button.grid(row=2, column=0, columnspan=4)

    def __edit_coordinates(self):
        selected = self.coordinates_listbox.curselection()

        if len(selected) == 0:
            mb.showerror("Ошибка", "Необходимо выбрать точку")
        else:
            selected = selected[0]

            current_x = self.x_edited.get()
            current_y = self.y_edited.get()

            if coordinates_validation(current_x, current_y):
                current_x = float(current_x)
                current_y = float(current_y)

                self.coordinates_listbox.delete(selected)
                self.coordinates_listbox.insert(selected, [round(current_x, 3), round(current_y, 3)])
            else:
                mb.showerror("Ошибка", "Координаты должны быть вещественными числами.")

            self.y_edited.delete(0, END)
            self.x_edited.delete(0, END)

    def __delete_coordinates(self):
        selected = self.coordinates_listbox.curselection()

        if len(selected) == 0:
            mb.showerror("Ошибка", "Необходимо выбрать точку")
        else:
            selected = selected[0]
            self.coordinates_listbox.delete(selected)

    def __create_calculation_button(self):
        calc_button = Frame(self)
        calc_button.grid(row = 3, column = 0, pady=15)

        calc_button = Button(calc_button, text="Вычислить",
                             command=self.__calculate)
        calc_button.pack()

    def __clear(self):
        self.coordinates_listbox.delete(0, END)

    def __calculate(self):
        points = self.coordinates_listbox.get(0, END)

        if (len(points) < 3):
            mb.showerror("Ошибка", "Необходимо минимум 3 точки")
        else:
            result = find_triangle(points)
            print(result)
            if len(result) == 0:
                mb.showerror("Ошибка", "Не существует ни одного невырожденного треугольника")
            else:
                cir_rad, cir_center = find_base_cir(result)
                self.__draw_triange(result, cir_center, cir_rad)

    def __draw_triange(self, points, cir_center, cir_rad):
        self.to_draw.clear()

        self.to_draw.plot([points[0][0], points[1][0]],
                          [points[0][1], points[1][1]], color = "blue")
        self.to_draw.text(points[0][0], points[0][1], "(%.2f, %.2f)"%(points[0][0], points[0][1]), color = "red")

        self.to_draw.plot([points[1][0], points[2][0]],
                          [points[1][1], points[2][1]], color = "blue")
        self.to_draw.text(points[1][0], points[1][1], "(%.2f, %.2f)"%(points[1][0], points[1][1]), color = "red")

        self.to_draw.plot([points[2][0], points[0][0]],
                          [points[2][1], points[0][1]], color = "blue")
        self.to_draw.text(points[2][0], points[2][1], "(%.2f, %.2f)"%(points[2][0], points[2][1]), color = "red")

        circle = plt.Circle(cir_center, cir_rad, fill=False)

        self.to_draw.add_patch(circle)

        self.canvas.draw()

    def __create_matplot_window(self):
        self.figure = Figure(dpi=100, facecolor="grey", figsize=(5,5))

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row = 0, column = 1, rowspan = 3)

        self.to_draw = self.figure.add_subplot(1, 1, 1)

    # def __create_la

def main():
    gui = GUI()
    gui.mainloop()


if __name__ == "__main__":
    main()
