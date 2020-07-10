import tkinter as tk


class Calculator:
    def __init__(self):
        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("Calculator")
        self.main_window.geometry("500x500")
        # Make frames
        self.first_number_frame = tk.Frame(self.main_window)
        self.second_number_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)
        self.total_frame = tk.Frame(self.main_window)
        self.equal_to_frame = tk.Frame(self.main_window)

        self.first_number = 0
        self.second_number = 0
        self.total = 0

        self.first_number_label = tk.Label(self.first_number_frame, text='First Number: ')
        self.first_number_entry = tk.Entry(self.first_number_frame, width=10)
        self.first_number_label.pack(side='left')
        self.first_number_entry.pack(side='left')

        self.second_number_label = tk.Label(self.second_number_frame, text='Second Number: ')
        self.second_number_entry = tk.Entry(self.second_number_frame, width=10)
        self.second_number_label.pack(side='left')
        self.second_number_entry.pack(side='left')

        # Create and pack the widgets for the Balance.
        self.result_label = tk.Label(self.total_frame, text='Equals: ')
        self.equal_to = tk.StringVar()
        self.equal_to_label = tk.Label(self.equal_to_frame,
                                       textvariable=self.equal_to)
        self.result_label.pack(side='left')
        self.equal_to_label.pack(side='left')

        # Create button widgets and pass function to it.
        # The numbers allow for conditional statement to know which button is pushed.
        self.multiply_button = tk.Button(self.button_frame, text='*', command=lambda: self.get_total(1))
        self.divide_button = tk.Button(self.button_frame, text='/', command=lambda: self.get_total(2))
        self.add_button = tk.Button(self.button_frame, text='+', command=lambda: self.get_total(3))
        self.subtract_button = tk.Button(self.button_frame, text='-', command=lambda: self.get_total(4))

        self.first_number_frame.pack()
        self.second_number_frame.pack()
        self.button_frame.pack()
        self.total_frame.pack()
        self.equal_to_frame.pack()

        # Pack Buttons
        self.multiply_button.pack(side='left')
        self.multiply_button.config(height=5, width=5)
        self.divide_button.pack(side='left')
        self.divide_button.config(height=5, width=5)
        self.add_button.pack(side='left')
        self.add_button.config(height=5, width=5)
        self.subtract_button.pack(side='left')
        self.subtract_button.config(height=5, width=5)

        tk.mainloop()

    def get_total(self, the_id):
        self.first_number = float(self.first_number_entry.get())
        self.second_number = float(self.second_number_entry.get())

        if the_id == 1:
            self.total = self.first_number * self.second_number
        elif the_id == 2:
            self.total = self.first_number / self.second_number
        elif the_id == 3:
            self.total = self.first_number + self.second_number
        elif the_id == 4:
            self.total = self.first_number - self.second_number
        self.equal_to.set(self.total)
        print(self.total)
        self.first_number_entry.delete(0, 'end')
        self.second_number_entry.delete(0, 'end')


def main():
    Calculator()


if __name__ == '__main__':
    main()

