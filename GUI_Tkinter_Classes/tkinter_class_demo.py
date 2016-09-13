from Tkinter import *
'''
This is an example of using a class that contains widgets and their behaviors.
    - Using a class makes this UI reusable.
    - There is a label, text entry box, and button.
    - When the button is clicked, a function is executed.
    - This file has a main() that creates and instance of AppMain().
    - This file can also be imported and used about another file.
'''


class AppMain(object):
    # master is passed in because if multiple instances are created, it needs to know
    # which root widget instance to put the widgets onto.
    def __init__(self, master):

        # creates a label
        var_lbl_message = StringVar(master) # Special Tkinter Variable for label text
        var_lbl_message.set("Display your text here.")
        lbl_message = Label(master, textvariable=var_lbl_message)
        lbl_message.pack()

        # creates a text entry box
        entry_message = Entry(master)
        entry_message.insert(0, "Type a message here.")
        entry_message.pack()

        # creates a button
        # command= sets the function to be called when the button is clicked.
        btn_ok = Button(master, text='Ok',command=lambda: var_lbl_message.set(entry_message.get()))
        btn_ok.pack()


# main function where 2 instances of the GUI are created
def main():

    root_widget = Tk()                    # creates a widget window which will hold all other widgets.
    root_widget.geometry("300x100")       # sets the size of the window
    root_widget.title("Demo Input Text")  # set the title of the window
    app = AppMain(root_widget)            # creates an instance of AppMain which has all the other widgets.
                                          # root_widget is the master

    root_widget2 = Tk()                   # creates another widget window
    root_widget2.geometry("400x200")
    root_widget2.title("Second Demo Input Text")
    app2 = AppMain(root_widget2)          # creates an instance of AppMain which has all the other widgets.

    root_widget.mainloop()                # make the widget window run continuously. only called once.


# if running file directly
# allow option to import file and call main() from another file
if __name__ == '__main__':
    main()


