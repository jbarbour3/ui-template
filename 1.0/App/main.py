

import sys
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class Main():

    def __init__(self):
        # ---GUI VARIABLES------------------------------------------------------------------------------------------###
        self.win = Tk()
        gui = self.win
        gui.current_tab = None
        gui.PAGE = {}



        # ----------------------------------------------------------------------------------------------------------###

        # ---gui formatting-----------------------------------------------------------------------------------------###


        self.application_data_file = "background_files/application_data.csv"
        self.app_settings = {}

        # Create the main root window, instantiate the object, and run the main loop!



        with open(self.application_data_file) as f:
            for row in f:
                row = row.strip('\n')
                key, values = row.split('=')
                values = values.split(',')
                self.app_settings[key] = values

        gui.colors = {"company": self.app_settings['color_company'][0],
                      "active": self.app_settings['color_active'][0],
                      "inactive": self.app_settings['color_inactive'][0]}
        gui.pages = self.app_settings['page_names']

        gui.config(bg=gui.colors["company"], padx=5, pady=5)
        gui.geometry(self.app_settings['gui_geometry'][0])
        gui.resizable(width=True, height=True)

        if get_platform() == 'Windows':
            gui.icon = PhotoImage('photo', file=self.app_settings['icon_file'][0])  # puts the icon we use for the window in memory
            gui.tk.call('wm', 'iconphoto', gui._w, gui.icon)
            gui.title(self.app_settings['title'][0])

        gui.head = Frame(gui, bg=gui.colors["company"])
        gui.head.pack(fill=X)
        gui.body = Frame(gui, padx=5, pady=5, bg=gui.colors["active"])
        gui.body.pack(fill=BOTH, expand=True)

        gui.footer = Frame(gui.body, bg=gui.colors["active"])
        gui.footer.pack(fill=X, side=BOTTOM)

        Button(gui.footer, text="Next", command=lambda var=gui.current_tab: next_page(var)).pack(side=RIGHT)
        Frame(gui.footer, width=5, bg=gui.colors["active"]).pack(side=RIGHT)

        Button(gui.footer, text="Previous", command=lambda var=gui.current_tab: back_page(var)).pack(side=RIGHT)
        gui.spacer = Frame(gui.body, height=5, bg=gui.colors["active"])
        gui.spacer.pack(fill=X, side=BOTTOM)

        # ---- build each page in the gui
        for page in gui.pages:
            gui.PAGE[page] = {}  # create a dict to store the page widgets
            f = gui.PAGE[page]  # the current page in memory
            f["data"] = {}  # create a dictionary to hold the data for each page

            # create the page header button
            f["label"] = Button(gui.head, bd=0, bg=gui.colors["inactive"], text=page,
                                command=lambda var=page: set_current_tab(var))
            f["label"].pack(side=LEFT)
            Frame(gui.head, bg=gui.colors["company"], width=5).pack(side=LEFT)  # just a spacer for looks

            # create the frame to pack widgets into
            f["frame"] = Frame(gui.body, bg="white")
            f["frame"].pack(expand=True, fill=BOTH)
            f["frame"].pack_forget()

        gui.current_tab = self.app_settings['starting_page'][0]  # set the variable to the starting page so it shows by default
        gui.PAGE[gui.current_tab]["label"].config(bg=gui.colors["active"])
        gui.PAGE[gui.current_tab]["frame"].pack(expand=True, fill=BOTH)

        # ---------------gui functions--------------------###
        def set_current_tab(aPageName):
            """sets the current page to a new page"""
            gui.PAGE[gui.current_tab]["label"].config(bg=gui.colors["inactive"])  # shade the page button
            gui.PAGE[gui.current_tab]["frame"].pack_forget()  #

            gui.current_tab = aPageName
            gui.PAGE[gui.current_tab]["frame"].pack(expand=True, fill=BOTH)
            gui.PAGE[gui.current_tab]["label"].config(bg=gui.colors["active"])
            return None

        def next_page(current_page):
            """locks the current page, checks the variables, executes the next step, proceeds to the next page"""
            current_page = gui.current_tab
            if current_page == gui.pages[-1]:
                messagebox.showerror("Error",
                                     "Can't procceed, no other pages remaining. "
                                     "Did you mean to click the 'Back' button?")
            else:
                set_current_tab(gui.pages[gui.pages.index(current_page) + 1])

            return None

        def back_page(current_page):
            """locks the current page, checks the variables, executes the next step, proceeds to the next page"""
            current_page = gui.current_tab
            print_dict(gui.PAGE[current_page]["data"])
            if current_page == gui.pages[0]:
                messagebox.showerror("Error",
                                     "Can't procceed, no other pages remaining. "
                                     "Did you mean to click the 'Next' button?")
            else:
                set_current_tab(gui.pages[gui.pages.index(current_page) - 1])  # once the variables are checked and analysis is done, show the next page

        def print_dict(dictionary, ident='', braces=1):
            """ Recursively prints nested dictionaries."""

            for (key, value) in dictionary.items():
                if isinstance(value, dict):
                    print('%s%s%s%s' % (ident, braces * '[', key, braces * ']'))
                    print_dict(value, ident + '  ', braces + 1)
                else:
                    try:
                        print(ident + '%s = %s' % (key, value.get()))
                    except:
                        pass





def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]

App = Main()

App.win.mainloop()
