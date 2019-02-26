from tkinter import *
from tkinter import messagebox as mb
import math


def find_base_cir(points):
    first_vec_len = math.sqrt((points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2)
    seconds_vec_len = math.sqrt((points[1][0]-points[2][0])**2 + (points[1][1]-points[2][1])**2)
    third_vec_len = math.sqrt((points[2][0]-points[0][0])**2 + (points[2][1]-points[0][1])**2)

    half_per = (first_vec_len + seconds_vec_len + third_vec_len) / 2

    triagle_sq = math.sqrt(half_per *
                           round((half_per - first_vec_len), 3) *
                           round((half_per - seconds_vec_len), 3) *
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

    triagle_sq = math.sqrt(half_per *
                           round((half_per - first_vec_len), 3) *
                           round((half_per - seconds_vec_len), 3) *
                           round((half_per - third_vec_len), 3))

    incircle_sq = (triagle_sq / half_per)**2 * math.pi

    return abs(triagle_sq - incircle_sq)


def find_triangle(points):
    result = ()
    min_sq_diff = 0
    amount_of_point = len(points)

    # возможно тут ошибка в переборе треугольников

    for i in range(amount_of_point - 2):
        for j in range(i + 1, amount_of_point - 1):
            for k in range(j + 1, amount_of_point):
                curr_sq_diff = calcucalte_sq_diff([points[i], points[j], points[k]])
                # print(curr_sq_diff)
                if curr_sq_diff == 0:
                    continue
                if min_sq_diff == 0:
                    min_sq_diff = curr_sq_diff
                    result = [points[i], points[j], points[k]]
                elif curr_sq_diff < min_sq_diff:
                    min_sq_diff = curr_sq_diff
                    result = [points[i], points[j], points[k]]

    if min_sq_diff == 0:
        result = ()

    return result


def coordinates_validation(x, y):
    try:
        float(x)
        float(y)
    except ValueError:
        return 0

    return 1


def find_triangle_sq(points):
    first_vec_len = math.sqrt((points[0][0]-points[1][0])**2 + (points[0][1]-points[1][1])**2)
    seconds_vec_len = math.sqrt((points[1][0]-points[2][0])**2 + (points[1][1]-points[2][1])**2)
    third_vec_len = math.sqrt((points[2][0]-points[0][0])**2 + (points[2][1]-points[0][1])**2)

    half_per = (first_vec_len + seconds_vec_len + third_vec_len) / 2

    triagle_sq = math.sqrt(half_per *
                           round((half_per - first_vec_len), 3) *
                           round((half_per - seconds_vec_len), 3) *
                           round((half_per - third_vec_len), 3))
    return triagle_sq


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.border = 27

        self.geometry("780x710")
        self.resizable(False, False)

        self.coordinates_frame = None
        self.x_entry = None
        self.y_entry = None

        self.x_edited = None
        self.y_edited = None

        self.figure = None
        self.tkcanvas = None
        self.tkcanvas_wh = 500

        self.coordinates_listbox = None

        self.infolabel = None

        self.__create_coordinates_entry()
        self.__create_listbox()
        self.__create_listbox_editor()
        self.__create_canvas_window()
        self.__create_calculation_button()
        self.__create_infolabel()

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

        clear_button = Button(editor_frame, text="Очистить", command=self.__clear)

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
        calc_button.grid(row=3, column=0, pady=15)

        calc_button = Button(calc_button, text="Вычислить",
                             command=self.__calculate)
        calc_button.pack()

    def __clear(self):
        self.coordinates_listbox.delete(0, END)

    def __calculate(self):
        points = self.coordinates_listbox.get(0, END)

        if len(points) < 3:
            mb.showerror("Ошибка", "Необходимо минимум 3 точки")
        else:
            result = find_triangle(points)
            # print(result)
            if len(result) == 0:
                mb.showerror("Ошибка", "Не существует ни одного невырожденного треугольника")
            else:
                cir_rad, cir_center = find_base_cir(result)
                sq_triangle = find_triangle_sq(result)
                sq_cir = cir_rad**2 * math.pi
                self.infolabel.config(text="Точки, образующие треугольник: %s\n" % result +
                                      "Площадь треугольника: %.3f\n" % sq_triangle +
                                      "Площадь круга: %.3f\n" % sq_cir +
                                      "Разность: %.3f\n" % (sq_triangle-sq_cir))

                self.__draw_result(result, cir_center, cir_rad)

    def __draw_axes(self, shift_x=0, shift_y=0):
        # self.tkcanvas.create_line(self.border+shift_x, self.tkcanvas_wh+shift_y,
        #                           self.border+shift_x, self.border+shift_y, arrow=LAST)
        #
        # self.tkcanvas.create_line(self.border+shift_x, self.tkcanvas_wh+shift_y,
        #                           self.border+self.tkcanvas_wh+shift_x, self.tkcanvas_wh+shift_y, arrow=LAST)
        pass

    def __create_canvas_window(self):
        canvas_frame = Frame(self, bg='grey')

        self.tkcanvas = Canvas(canvas_frame,
                               width=self.tkcanvas_wh+4*self.border, height=self.tkcanvas_wh+4*self.border)

        canvas_frame.grid(row=0, column=1, rowspan=4)
        self.tkcanvas.grid(row=0, column=0, padx=10, pady=10)

        self.__draw_axes()

    def __get_scale(self, result):
        k = None

        min_x = min([result[i][0] for i in range(len(result))])
        max_x = max([result[i][0] for i in range(len(result))])
        min_y = min([result[i][1] for i in range(len(result))])
        max_y = max([result[i][1] for i in range(len(result))])

        k_x = self.tkcanvas_wh / (max_x - min_x)
        k_y = self.tkcanvas_wh / (max_y - min_y)

        if k_x >= 1 and k_y >= 1:
            k = min(k_x, k_y)
        elif k_x < 1 and k_y >= 1:
            k = k_x
        elif k_x >= 1 and k_y < 1:
            k = k_y
        elif k_x < 1 and k_y < 1:
            k = min(k_x, k_y)

        return k, min_x, min_y

    def __draw_result(self, result, cir_center, cir_rad):
        self.tkcanvas.delete("all")

        getsc = self.__get_scale(result)

        k = getsc[0]
        min_x, min_y = getsc[1], getsc[2]
        if min_x < 0:
            shift_x = abs(min_x)
        else:
            shift_x = -min_x
        if min_y < 0:
            shift_y = abs(min_y)
        else:
            shift_y = -min_y
        # print(shift_y, shift_x, k)

        self.__draw_axes(shift_x*k, shift_y*k)

        self.tkcanvas.create_line(self.border+(shift_x+result[0][0])*k,
                                  2*self.border+self.tkcanvas_wh-(result[0][1]+shift_y)*k,
                                  self.border+(shift_x+result[1][0])*k,
                                  2*self.border+self.tkcanvas_wh-(result[1][1]+shift_y)*k,
                                  fill='green')

        # print(self.border+(shift_x+result[0][0])*k,
        #                           2*self.border+self.tkcanvas_wh-(result[0][1]+shift_y)*k,
        #                           self.border+(shift_x+result[1][0])*k,
        #                           2*self.border+self.tkcanvas_wh-(result[1][1]+shift_y)*k)

        self.tkcanvas.create_line(self.border+(shift_x+result[1][0])*k,
                                  2*self.border+self.tkcanvas_wh-(result[1][1]+shift_y)*k,
                                  self.border+(shift_x+result[2][0])*k,
                                  2*self.border+self.tkcanvas_wh-(result[2][1]+shift_y)*k,
                                  fill='green')

        self.tkcanvas.create_line(self.border+(result[2][0]+shift_x)*k,
                                  2*self.border+self.tkcanvas_wh-(result[2][1]+shift_y)*k,
                                  self.border+(result[0][0]+shift_x)*k,
                                  2*self.border+self.tkcanvas_wh-(result[0][1]+shift_y)*k,
                                  fill='green')

        self.tkcanvas.create_oval(self.border+(cir_center[0]-cir_rad+shift_x)*k,
                                  2*self.border+self.tkcanvas_wh-(cir_center[1]+cir_rad+shift_y)*k,
                                  self.border+(cir_center[0]+cir_rad+shift_x)*k,
                                  2*self.border+self.tkcanvas_wh-(cir_center[1]-cir_rad+shift_y)*k)

        self.tkcanvas.create_text(self.border - 5 + (shift_x + result[0][0]) * k,
                                  2*self.border + self.tkcanvas_wh - (result[0][1] + shift_y) * k,
                                  text="({:.1f},{:.1f})".format(result[0][0], result[0][1]),
                                  fill='red')

        self.tkcanvas.create_text(self.border - 5 + (shift_x + result[1][0]) * k,
                                  2*self.border + self.tkcanvas_wh - (result[1][1] + shift_y) * k,
                                  text="({:.1f},{:.1f})".format(result[1][0], result[1][1]),
                                  fill='red')

        self.tkcanvas.create_text(self.border - 5 + (shift_x + result[2][0]) * k,
                                  2*self.border + self.tkcanvas_wh - (result[2][1] + shift_y) * k,
                                  text="({:.1f},{:.1f})".format(result[2][0], result[2][1]),
                                  fill='red')

    def __create_infolabel(self):
        label_frame = Frame(self)

        self.infolabel = Label(label_frame, text='')

        label_frame.grid(row=5, column=1)
        self.infolabel.pack()


def main():
    gui = GUI()
    gui.mainloop()


if __name__ == "__main__":
    main()
