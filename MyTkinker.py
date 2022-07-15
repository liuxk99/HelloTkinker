import tkinter


class Calculator:
    def __init__(self):
        self.frame = tkinter.Tk()

    def show(self):
        self.frame.mainloop()


if __name__ == "__main__":
    this_gui = Calculator()
    this_gui.show()
    # top = tkinter.Tk()
    # top.mainloop()
    pass