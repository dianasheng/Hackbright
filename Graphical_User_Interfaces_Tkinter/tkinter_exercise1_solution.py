from Tkinter import *
'''
Tkinter GUI Exercise 1
'''

root_widget = Tk()                          # creates a widget window which will hold all other widgets.
root_widget.geometry("250x150")             # sets the size of the window
root_widget.title("Simple GUI Demo")        # set the title of the window

var_label_text = StringVar()                # Special Tkinter Variable for label text
var_label_text.set("Display your full name here.")
lbl_hello = Label(textvariable=var_label_text)
lbl_hello.grid(row=0, column=1)             # show the label using grid()


Label(text="First").grid(row=1, column=0)
Label(text="Last").grid(row=2, column=0)

entry_first = Entry()                      # creates a text entry box
entry_first.insert(0, "Type First Name")   # text to display on start up
entry_first.grid(row=1, column=1)

entry_last = Entry()                       # creates a text entry box
entry_last.insert(0, "Type Last Name")     # text to display on start up
entry_last.grid(row=2, column=1)

# create a button
# command sets a function to run when the button is clicked. AKA as an event and callback
btn_ok = Button(text='Ok',
                command=lambda: var_label_text.set("My name is " + entry_first.get() + " " + entry_last.get()))
btn_ok.grid(row=3, column=1)

# runs the window in a loop so it continuously detects the button click event
root_widget.mainloop()



