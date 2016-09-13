from Tkinter import *
'''
This is a simple GUI example.
There is a label, text entry box, and button.
When the button is clicked, a function is executed.
Limitations - If I wanted to create many instances of this GUI,
I would have to duplicate this code over and over.
'''

root_widget = Tk()                          # creates a widget window which will hold all other widgets.
root_widget.geometry("300x100")             # sets the size of the window
root_widget.title("Simple GUI Demo")        # set the title of the window

var_label_text = StringVar()                # Special Tkinter Variable for label text
var_label_text.set("This is a simple GUI.")
lbl_hello = Label(root_widget, textvariable=var_label_text)
lbl_hello.pack()                            # show the label

entry_text = Entry()                        # creates a text entry box
entry_text.insert(0, "Type here please.")   # text to display on start up
entry_text.pack()                           # show the entry box


def set_text():
    var_label_text.set(entry_text.get())
# create a button
# command sets a function to run when the button is CLICKED. AKA as an event and callback
# command expects the NAME of the function not to call it.
#btn_ok = Button(text='Ok', command=lambda: var_label_text.set(entry_text.get()))
btn_ok = Button(text='Ok', command=set_text)
btn_ok.pack()




# runs the window in a loop so it continuously detects the button click event
root_widget.mainloop()

