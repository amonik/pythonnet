import tkinter


class MoonBank:
    def __init__(self):
        # Establish variables
        self.my_deposit = 0
        self.my_balance = 0
        self.my_withdrawal = 0
        self.my_total_deposits = []
        self.my_total_withdrawals = []
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Welcome to Moon Bank")
        self.main_window.geometry("350x350")
        self.button_frame = tkinter.Frame(self.main_window)
        self.deposit_frame = tkinter.Frame(self.main_window)
        self.withdraw_frame = tkinter.Frame(self.main_window)
        self.balance_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for Deposit.
        self.deposit_label = tkinter.Label(self.deposit_frame, text='Deposit Amount:    ')
        self.deposit_entry = tkinter.Entry(self.deposit_frame, width=10)
        self.deposit_label.pack(side='left')
        self.deposit_entry.pack(side='left')

        # Create and pack the widgets for Withdraw.
        self.withdraw_label = tkinter.Label(self.withdraw_frame, text='Withdrawal Amount:')
        self.withdraw_entry = tkinter.Entry(self.withdraw_frame, width=10)
        self.withdraw_label.pack(side='left')
        self.withdraw_entry.pack(side='left')

        # Create and pack the button widgets.
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.withdraw = tkinter.Button(self.button_frame, text='Withdraw', command=self.set_withdrawals)
        self.deposit = tkinter.Button(self.button_frame, text='Deposit', command=self.set_deposit)

        # Create and pack the widgets for the Balance.
        self.result_label = tkinter.Label(self.balance_frame,
                                          text='Balance:')
        self.check_balance_button = tkinter.Button(self.button_frame, text='Check Balance', command=self.get_balance)
        # Establish a string var to disable the balance.
        self.balance = tkinter.StringVar()
        self.balance_label = tkinter.Label(self.balance_frame, textvariable=self.balance)
        self.result_label.pack(side='left')
        self.balance_label.pack(side='left')

        # Textbox frames:
        self.deposit_frame.pack()
        self.withdraw_frame.pack()

        # Pack buttons
        self.check_balance_button.pack(side='left')
        self.deposit.pack(side='left')
        self.withdraw.pack(side='left')
        self.quit_button.pack(side='left')
        self.balance_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    def set_deposit(self):
        try:
            self.my_deposit = float(self.deposit_entry.get())
            self.my_total_deposits.append(self.my_deposit)
        except ValueError:
            print("Nothing entered or incorrect button pushed")
        print("Additions: {}".format(self.my_total_deposits))
        self.deposit_entry.delete(0, 'end')

    def set_withdrawals(self):
        try:
            self.my_withdrawal = float(self.withdraw_entry.get())
            self.my_total_withdrawals.append(self.my_withdrawal)
        except ValueError:
            print("Nothing entered or incorrect button pushed")
        print("Deductions: {}".format(self.my_total_withdrawals))
        self.withdraw_entry.delete(0, 'end')

    def get_balance(self):
        self.my_balance = sum(self.my_total_deposits) - sum(self.my_total_withdrawals)
        self.balance.set(round(self.my_balance, 2))


def main():
    MoonBank()


if __name__ == '__main__':
    main()
