import tkinter


def get_deposit(my_deposit):
    return my_deposit


class SweetMoonBank:
    def __init__(self):
        # Establish variables
        self.my_deposit = 0
        self.my_balance = 0
        self.my_withdrawal = 0
        self.my_total_deposits = []
        self.my_total_withdrawals = []
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Welcome to Sweet Moon Bank")
        self.main_window.geometry("350x350")
        self.button_frame = tkinter.Frame(self.main_window)
        self.withdraw_frame = tkinter.Frame(self.main_window)
        self.deposit_frame = tkinter.Frame(self.main_window)
        self.balance_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for Withdraw.
        self.withdraw_label = tkinter.Label(self.withdraw_frame, text='Withdrawal Amount:')
        self.withdraw_entry = tkinter.Entry(self.withdraw_frame, textvariable=0, width=10)
        self.withdraw_label.pack(side='left')
        self.withdraw_entry.pack(side='left')

        # Create and pack the widgets for Deposit.
        self.deposit_label = tkinter.Label(self.deposit_frame, text='Deposit Amount:    ')
        self.deposit_entry = tkinter.Entry(self.deposit_frame, textvariable=0, width=10)
        self.deposit_label.pack(side='left')
        self.deposit_entry.pack(side='left')

        # Create and pack the button widgets.
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        # Pass the set_withdrawals method below to the withdraw button.
        self.withdraw = tkinter.Button(self.button_frame, text='Withdraw', command=self.set_withdrawals)
        # Pass the set_deposit function to the deposit button.
        self.deposit = tkinter.Button(self.button_frame, text='Deposit', command=self.set_deposit)

        # Create and pack the widgets for the Balance.
        self.result_label = tkinter.Label(self.balance_frame,
                                          text='Balance:')
        # Pass the method get_balance below to the button.
        self.check_balance_button = tkinter.Button(self.button_frame, text='Check Balance', command=self.get_balance)
        # Establish a string var to display the balance.
        self.balance = tkinter.StringVar()
        self.balance_label = tkinter.Label(self.balance_frame, textvariable=self.balance)
        self.result_label.pack(side='left')
        self.balance_label.pack(side='left')

        # Textbox frames:
        self.withdraw_frame.pack()
        self.deposit_frame.pack()

        # Pack buttons
        self.check_balance_button.pack(side='left')
        self.withdraw.pack(side='left')
        self.deposit.pack(side='left')
        self.quit_button.pack(side='left')
        self.balance_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    def set_deposit(self):
        # Gets the deposit from the user, calls entry from above.
        self.my_deposit = float(self.deposit_entry.get())
        # Creates list of deposits.
        self.my_total_deposits.append(self.my_deposit)
        # Added this to display deposit list as text.
        print("Additions: {}".format(self.my_total_deposits))
        # Each time pressing deposit button the entry clears.
        self.deposit_entry.delete(0, 'end')

    def set_withdrawals(self):
        # Calls the withdraw entry from above.
        self.my_withdrawal = float(self.withdraw_entry.get())
        self.my_total_withdrawals.append(self.my_withdrawal)
        # Added this to display the withdraw list as text.
        print("Deductions: {}".format(self.my_total_withdrawals))
        # Each time pressing deposit button the entry clears.
        self.withdraw_entry.delete(0, 'end')

    def get_balance(self):
        self.my_balance = sum(self.my_total_deposits) - sum(self.my_total_withdrawals)
        self.balance.set(round(self.my_balance, 2))


def main():
    SweetMoonBank()


if __name__ == '__main__':
    main()
