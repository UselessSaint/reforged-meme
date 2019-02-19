from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")

        self.coordinates_frame = None
        self.x_entry = None
        self.y_entry = None

        self.coordinates_listbox = None

        self.create_coordinates_entry()
        self.create_listbox()

    def create_coordinates_entry(self):
        coordinates_frame = Frame(self)

        self.x_entry = Entry(coordinates_frame, width = 5)
        self.y_entry = Entry(coordinates_frame, width = 5)

        x_lable = Label(coordinates_frame, text = "X = ")
        y_lable = Label(coordinates_frame, text = "Y = ")

        coordinates_frame.grid(row = 0, column = 0, padx = 5, pady = 5)
        x_lable.grid(row = 0, column = 0)
        self.x_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
        y_lable.grid(row = 0, column = 2)
        self.y_entry.grid(row = 0, column = 3, padx = 5, pady = 5)

        adding_coordinates_buttor = Button(coordinates_frame, text = "Добавить точку",
                                           command = self.__add_coordinate_to_listbox)
        adding_coordinates_buttor.grid(row = 1, column = 0, columnspan = 4)

    def create_listbox(self):
        coordinates_listbox_frame = Frame(self)

        self.coordinates_listbox = Listbox(coordinates_listbox_frame, height = 20)

        coordinates_listbox_frame.grid(row = 1, column = 0)
        self.coordinates_listbox.grid(row = 0, column = 0)

    def __add_coordinate_to_listbox(self):
        current_x = self.x_entry.get()
        current_y = self.y_entry.get()

        self.coordinates_listbox.insert(0, "(%s, %s)" % (current_x, current_y))

def main():
    gui = GUI()
    gui.mainloop()

if __name__ == "__main__":
    main()

