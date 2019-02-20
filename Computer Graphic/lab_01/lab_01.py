from tkinter import *
from tkinter import messagebox as mb
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, \
    NavigationToolbar2Tk
from matplotlib.figure import Figure

def coordinates_validation(x, y):
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return 0

    return 1


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")

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
            self.coordinates_listbox.insert(0, "(%.3f, %.3f)" % (current_x, current_y))
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
                self.coordinates_listbox.insert(selected, "(%.3f, %.3f)" % (current_x, current_y))
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

    def __create_matplot_window(self):
        # self.figure = Figure()
        # a = self.figure.add_subplot(111)
        # a.plot([1,2])
        #
        # canvas = FigureCanvasTkAgg(self.figure, self)
        # canvas.draw()
        # canvas.get_tk_widget().grid(row = 0, column = 1, rowspan = 3)
        pass

def main():
    gui = GUI()
    gui.mainloop()


if __name__ == "__main__":
    main()
