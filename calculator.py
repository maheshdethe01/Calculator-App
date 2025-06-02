#importing necessary library

import tkinter as tk

#creating window 
window = tk.Tk()
window.title("Basic Calculator App")
window.geometry("600x250")

#adding label 
label = tk.Label(window, text= " Basic Arithmetic Operations ")
label.pack()

# creating buttons

buttons = [['7','8','9','/'],
           ['4','5','6','*'],
           ['1','2','3','-'],
           ['0','C','=','+']]

#Entry Display

entry = tk.Entry(window,font= 'Arial', bd = 5, justify= 'right')
entry.pack(fill='both', ipadx= 8, ipady= 15, padx= 10, pady= 10)


def click(event):
    current = str(entry.get()) #first entry ..eg = 1
    entry.delete(0,tk.END) #clearing the input field from start 0 to end
    entry.insert(0,current + event.widget["text"]) #appending the text of the button that was clicked

def clear():
    entry.delete(0,tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except Exception:
        entry.delete(0,tk.END)
        entry.insert(0,'Error')

for row in buttons:
    frame = tk.Frame(window)
    frame.pack(expand = True, fill= 'both',)
    for char in row:
        btn = tk.Button(frame, text = char, font= ("Arial",18), relief= 'ridge', border= 2)
        btn.pack(fill= 'both',side = 'left',expand = True, padx= 2, pady=2)
        if char == '=':
            btn.config(command= calculate)
        elif char == 'C':
            btn.config(command=clear)
        else:
            btn.bind('<Button-1>',click)



# Run the App
window.mainloop()