from tkinter import Tk, Entry, Button, StringVar

class Calculator: 
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('360x400+0+0')
        master.config(bg='purple')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        
        self.entry = Entry(master, width=17, bg='#fff', font=('Arial Bold', 24), 
                          textvariable=self.equation, justify='right')
        self.entry.place(x=10, y=10, width=340, height=50)
        
        self.create_buttons(master)

    def create_buttons(self, master):
        buttons = [
            ('7', 10, 70), ('8', 95, 70), ('9', 180, 70), ('/', 265, 70),
            ('4', 10, 130), ('5', 95, 130), ('6', 180, 130), ('*', 265, 130),
            ('1', 10, 190), ('2', 95, 190), ('3', 180, 190), ('-', 265, 190),
            ('0', 10, 250), ('.', 95, 250), ('=', 180, 250), ('+', 265, 250),
            ('C', 10, 310)
        ]
        
        for (text, x, y) in buttons:
            if text == '=':
                Button(master, text=text, width=8, height=3, font=('Arial', 12),
                      command=self.solve, bg='orange').place(x=x, y=y)
            elif text == 'C':
                Button(master, text=text, width=8, height=3, font=('Arial', 12),
                      command=self.clear, bg='red', fg='white').place(x=x, y=y)
            else:
                Button(master, text=text, width=8, height=3, font=('Arial', 12),
                      command=lambda t=text: self.show(t), bg='lightgray').place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            expression = self.entry_value.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            self.equation.set(result)
            self.entry_value = str(result)
        except ZeroDivisionError:
            self.equation.set("Error: Division by zero")
            self.entry_value = ''
        except:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()