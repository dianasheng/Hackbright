from Tkinter import *
from ttk import *
import movie_info_manager

root_widget = Tk()                          # creates a widget window which will hold all other widgets.
cmb_box_years = Combobox()
lst_box_results = Listbox(width=30)


def cmb_box_select(event):
    selected_year = cmb_box_years.get()     # returns the text that is selected in the combobox
    movie_info_list = movie_info_manager.get_movie_info_by_year(selected_year)
    movie_names = []
    global lst_box_results

    lst_box_results.delete(0, END)          # clears the combobox each time

    for movie_info in movie_info_list:
        if not movie_names:
            movie_names.append(movie_info.title)
            lst_box_results.insert(END, movie_info.title)   # fills in the combobox entries with data

        else:
            if movie_info.title not in movie_names:
                movie_names.append(movie_info.title)
                lst_box_results.insert(END, movie_info.title)


def main():
    root_widget.geometry("300x300")                 # sets the size of the window
    root_widget.title("Search SF Movies by Year")   # sets the title of the window
    root_widget.configure(background = "dark grey")

    lbl_hello = Label(root_widget, text="Choose a year.")
    lbl_hello.pack()                                # shows the label

    movie_info_manager.load_movie_data()            # get data from movie_info_manager

    global cmb_box_years
    cmb_box_years = Combobox(values=movie_info_manager.get_release_year_list())
    cmb_box_years.bind("<<ComboboxSelected>>", cmb_box_select)  # event that calls cmb_box_select when triggered
    cmb_box_years.current(0)
    cmb_box_years.pack()                            # shows the combobox

    lst_box_results.configure(background = "light grey")
    lst_box_results.pack()                          # shows the listbox

    root_widget.mainloop()                          # runs the widget window


if __name__ == '__main__':
    main()
