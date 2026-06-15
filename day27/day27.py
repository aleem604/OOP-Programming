import tkinter
import turtle

window = tkinter.Tk()
window.title("Day 27 TKInter practice")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text='I am a Label', font=("Arial", 12, 'normal'))
my_label.pack(side='top')
my_label['text'] = 'New Text'
my_label.config(text="New After Text")

def button_clicked():
    if len(entry.get())  > 0:
        my_label['text'] = entry.get()
    else:
        my_label['text'] = 'button got clicked'

button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()

#Text
entry = tkinter.Entry(width=30)
entry.pack()
print(entry.get())

#Multiline Text
text = tkinter.Text(width=30, height=5)
text.focus()
text.insert(tkinter.END, "Example of multi-line text entry")
print(text.get('1.0', tkinter.END))
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()



#tim = turtle.Turtle()











window.mainloop()