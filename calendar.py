from tkinter import *
import calendar
from tkinter import messagebox

def Calendar_see():
    try:
        year_value = int(year_entry.get())
        if year_value < 1 or year_value > 9999:
            messagebox.showerror("Error", "Please enter a valid year (1-9999)")
            return
            
        # create new windows for this calendar
        window = Toplevel(root)
        window.config(background="white")
        window.title(f"Calendar for {year_value}")
        window.geometry("700x600")
        
        # create calendar content
        cal_content = calendar.calendar(year_value)
        
        # create frame for better organization of this calendar
        frame = Frame(window, bg="white")
        frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        
        # create text widget for better formatting
        cal_text = Text(frame, font=("Courier", 10), wrap=WORD, bg="white", relief=FLAT)
        cal_text.insert(END, cal_content)
        cal_text.config(state=DISABLED)  # make this read-only
        
        # for adding a scrollbar
        scrollbar = Scrollbar(frame, orient=VERTICAL, command=cal_text.yview)
        cal_text.configure(yscrollcommand=scrollbar.set)
        
        # layout
        cal_text.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid year number")

if __name__ == '__main__':
    root = Tk()
    root.config(background="skyblue")
    root.title("Calendar by Aronno")
    root.geometry("400x300")
    
    # main title
    name = Label(root, text="Aronno's Calendar", bg="skyblue", 
                 font=("Arial", 20, "bold"), fg="navy")
    name.pack(pady=20)
    
    # instructions
    instruction = Label(root, text="Enter a year to view its calendar", 
                       bg="skyblue", font=("Arial", 12))
    instruction.pack(pady=5)
    
    # year input frame
    input_frame = Frame(root, bg="skyblue")
    input_frame.pack(pady=15)
    
    year_label = Label(input_frame, text="Year:", bg="skyblue", 
                      font=("Arial", 12))
    year_label.pack(side=LEFT, padx=5)
    
    year_entry = Entry(input_frame, font=("Arial", 12), width=10, 
                      justify=CENTER)
    year_entry.pack(side=LEFT, padx=5)
    year_entry.insert(0, "")
    
    # show button
    show_button = Button(root, text="Show Calendar", fg="white", bg="green3", 
                        font=("Arial", 12, "bold"), command=Calendar_see)
    show_button.pack(pady=15)
    
    # footer
    footer = Label(root, text=("Made with Python & Tkinter", "Aronno Saha"), bg="skyblue", 
                  font=("Arial", 9), fg="gray50")
    footer.pack(side=BOTTOM, pady=10)
    
    root.mainloop()