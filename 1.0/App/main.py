#
#

import os

loc = os.getcwd()
print(loc)

files = loc + "/background_files"
data = files + "/data.csv"

with open(data) as f:
    for line in f:
        row = line.split(',')
        for i in row:
            print(i)
# from tkinter import *
# from tkinter import filedialog
# from tkinter import messagebox
#
# class UI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Trade Hub")
#         self.header = ("Verdana", 8)
#         self.header2 = ("Verdana", 5)
#         self.bg1="PaleGreen1"
#         self.bg2="lightgrey"
#         self.bg3="grey"
#         self.bg4="#00FF00" # bright green
#         self.gdax_connection = None
#
#         self.root.config(bg=self.bg2)
#
#
#         # the code bloc below uses the technique found here -->\
#         #  https://mail.python.org/pipermail/tkinter-discuss/2005-August/000489.html
#         # to create a background in the application homepage
#
#         # self.root.background = Image('photo', file="backgroundfiles\Circuitsmall.png")  # images must be saved or they will be collected as garbage!
#         # self.root.canvas = Label(self.root, image=self.root.background)   # uses label object as a frame with image backgroundr
#         # self.root.canvas.pack_propagate(0)
#         # self.root.canvas.pack()
#
#
#         self.root.withdraw()
#         self.root.deiconify()
#         self.build_input_frame()
#         self.build_stream_log_frame()
#
#
#     def build_input_frame(self):
#
#         # -- gui variables -- #
#         gui = self.root
#         gui.step1data = None
#         gui.step1filename = StringVar()
#
#
#         # -- gui functions -- #
#
#         # step 1
#         def showinstructions():
#             self.root.withdraw()  # hide the main window
#             popup = Toplevel()  # bring up the help popup
#             popup.picture = Image('photo', file="backgroundfiles\mcbzhelp.png")  # the image showing how to run the tool
#             popup.pictureframe = Label(popup, image=popup.picture)
#             popup.pictureframe.pack_propagate(0)
#             popup.pictureframe.pack()
#             Button(popup.pictureframe, text="CLOSE HELP WINDOW", command=popup.destroy).pack(pady=6)
#             self.root.deiconify()
#
#         def previewdata(a2dlist, view='numerical'):
#
#             data = a2dlist
#
#             # destroy all the children of gui.dataview.canvas
#             for child in gui.dataview.canvas.winfo_children():
#                 child.destroy()
#
#             #  set up a frame to center and pack the analysis into
#             gui.dataview.canvas.framecontainer = Frame(gui.dataview.canvas)
#             f = gui.dataview.canvas.framecontainer
#             f.pack(anchor=CENTER, expand=True)
#
#             if view=='numerical':  # show the data preview in tabular form
#                 columns = len(data[0])
#                 rows = len(data)
#                 if columns > 20:
#                     columns = 20
#                 if rows > 40:
#                     rows = 40
#                 columnwidths = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#                 columnwidths = columnwidths[0:columns]
#                 for row in data[0:rows]:
#                     columnpos=0
#                     for column in row[0:columns]:
#                         if len(str(column))>columnwidths[columnpos]:
#                             columnwidths[columnpos] = len(str(column))
#                         columnpos+=1
#                 frame=Frame(f,padx=15,pady=5)
#                 frame.pack(expand=True)
#
#                 for row in data[0:rows]:
#                     frame = Frame(f)
#                     frame.pack(expand=True)
#                     columnpos=0
#                     for column in row[0:columns]:
#                         Label(frame,text = str(column), width=columnwidths[columnpos],relief=SUNKEN,bg="silver").pack(side=LEFT)
#                         columnpos+=1
#
#             elif view =='graphical':
#                 pass # show the data preview in a linechart
#
#             self.root.withdraw()
#             self.root.deiconify()
#
#             return None
#
#         def clearstep1():
#             #clears all forecast data and resets pane
#             gui.step1filename.set("")
#             gui.step1data = None
#             gui.step1browse.config(state=ACTIVE)
#             gui.step1preview.config(state=DISABLED)#Lock the preview button
#             gui.step1cleardata.config(state=DISABLED)#Lock the clear data button
#             gui.step1lockanalysis.config(state=DISABLED)#Lock the lock button
#             gui.step1indicator.config(bg="red")#set indicatior to red
#             gui.step2indicator.config(bg="red")
#             gui.step2convertbutton.config(state=DISABLED)
#             gui.step3indicator.config(bg='red')
#             gui.exportstep2databutton.config(state=DISABLED)
#             gui.step3previewbutton.config(state=DISABLED)
#
#         def browsestep1():
#             clearstep1()
#             fname = filedialog.askopenfilename(title="Select Report") #get the MCBZ file
#
#             if fname.lower()[-4:] == ".csv": #checks filename variable to make sure it's ok for
#                 gui.step1data = self.convertcsvtoList(fname) #loads the raw data to a 2dlist
#                 validreport = True  # set up a variable indicating whether the forecast is valid
#
#                 # make sure the list is a rectangle
#                 for row in gui.step1data:
#                     if len(row)!= len(gui.step1data[0]):
#                         validreport = False
#                         messagebox.showerror("Bad Input", "The data is not rectangular")
#                     for data in row[1:]:
#                         if "." in data:
#                             validreport = False
#                             messagebox.showerror("Bad Input", "The material {0} cannot contain decimal values".format(row[0]))
#                 if validreport:
#                     gui.step1filename.set(fname)
#                     gui.step1browse.config(state=DISABLED)
#                     gui.step1preview.config(state=ACTIVE)
#                     gui.step1cleardata.config(state=ACTIVE)
#                     gui.step1lockanalysis.config(state=ACTIVE)
#                 else:
#                     clearstep1()
#             else:
#                 messagebox.showerror("Bad File", "Report must be a valid .csv file.")
#                 clearstep1()
#
#         def previewstep1():
#             previewdata(gui.step1data, view='numerical')
#
#         def lockstep1():
#             gui.step1browse.config(state=DISABLED)
#             gui.step1preview.config(state=DISABLED)
#             gui.step1cleardata.config(state=ACTIVE)
#             gui.step1lockanalysis.config(state=DISABLED)
#             gui.step1indicator.config(bg="green")
#             gui.step2convertbutton.config(state=ACTIVE)
#             # print(gui.step1indicator.cget("bg")) #.cget("key") must be used to get the properties of tkinter objects
#
#             # step 1 Load .CSV  Sub-Pane
#             gui.inputframe1 = Frame(gui.inputframe, bg=self.bg2, padx=5, pady=5)
#             gui.inputframe1.pack(expand=True, fill=BOTH)
#             gui.inputframe1.header = Frame(gui.inputframe1, padx=2, pady=2, bg=self.bg1)
#             gui.inputframe1.header.pack(expand=True, fill=X)
#             Label(gui.inputframe1.header, text="Load .CSV File", font=self.header, bg=self.bg1).pack(side=LEFT)
#             gui.step1indicator = Label(gui.inputframe1.header, text="   ", font=self.header2, bg="red")
#             gui.step1indicator.pack(padx=2, side=RIGHT, anchor=CENTER)
#             gui.inputframe1.body = Frame(gui.inputframe1, padx=4, pady=4, bg=self.bg3)
#             gui.inputframe1.body.pack(expand=True, fill=X)
#
#             gui.inputframe1.bodytop = Frame(gui.inputframe1.body, padx=2, pady=2)
#             gui.inputframe1.bodytop.pack(expand=True, fill=X)
#
#             gui.step1entry = Entry(gui.inputframe1.bodytop, width=20, textvariable=gui.step1filename, state=DISABLED)
#             gui.step1entry.pack(side=LEFT, expand=True, fill=X, padx=2)
#             gui.step1browse = Button(gui.inputframe1.bodytop, text=" ? ", command=showinstructions)
#             gui.step1browse.pack(side=RIGHT, padx=2)
#             gui.step1preview = Button(gui.inputframe1.bodytop, text="Preview", command=previewstep1, state=DISABLED)
#             gui.step1preview.pack(side=RIGHT)
#             gui.step1browse = Button(gui.inputframe1.bodytop, text="Browse", command=browsestep1)
#             gui.step1browse.pack(side=RIGHT, padx=2)
#
#             gui.inputframe1.bodybottom = Frame(gui.inputframe1.body, padx=2, pady=2)
#             gui.inputframe1.bodybottom.pack(expand=True, fill=X)
#             gui.step1cleardata = Button(gui.inputframe1.bodybottom, text="Clear All Data", command=clearstep1,
#                                         state=DISABLED)
#             gui.step1cleardata.pack(side=LEFT, expand=True, fill=X)
#             gui.step1lockanalysis = Button(gui.inputframe1.bodybottom, text="Lock for Conversion", state=DISABLED,
#                                            command=lockstep1)
#             gui.step1lockanalysis.pack(side=LEFT, expand=True, fill=X)
#
#             return None
#
#         # -- model inputs pane -- #
#         gui.inputframe = Frame(gui)
#         gui.inputframe.pack(side=LEFT, anchor=N, padx=15, pady=15)
#         Label(gui.inputframe, text="Time Series Conversion Steps", font=self.header, bg="#00FF00").pack(expand=True,
#                                                                                                         fill=X)
#
#         # step 1 Load .CSV  Sub-Pane
#         gui.inputframe1 = Frame(gui.inputframe, bg=self.bg3, padx=5, pady=5)
#         gui.inputframe1.pack(expand=True, fill=BOTH)
#         gui.inputframe1.header = Frame(gui.inputframe1, padx=2, pady=2, bg=self.bg1)
#         gui.inputframe1.header.pack(expand=True, fill=X)
#         Label(gui.inputframe1.header, text="Load .CSV File", font=self.header, bg=self.bg1).pack(side=LEFT)
#         gui.step1indicator = Label(gui.inputframe1.header, text="   ", font=self.header2, bg="red")
#         gui.step1indicator.pack(padx=2, side=RIGHT, anchor=CENTER)
#         gui.inputframe1.body = Frame(gui.inputframe1, padx=4, pady=4, bg=self.bg3)
#         gui.inputframe1.body.pack(expand=True, fill=X)
#
#         gui.inputframe1.bodytop = Frame(gui.inputframe1.body, padx=2, pady=2)
#         gui.inputframe1.bodytop.pack(expand=True, fill=X)
#
#         gui.step1entry = Entry(gui.inputframe1.bodytop, width=20, textvariable=gui.step1filename, state=DISABLED)
#         gui.step1entry.pack(side=LEFT, expand=True, fill=X, padx=2)
#         gui.step1browse = Button(gui.inputframe1.bodytop, text=" ? ", command=showinstructions)
#         gui.step1browse.pack(side=RIGHT, padx=2)
#         gui.step1preview = Button(gui.inputframe1.bodytop, text="Preview", command=previewstep1, state=DISABLED)
#         gui.step1preview.pack(side=RIGHT)
#         gui.step1browse = Button(gui.inputframe1.bodytop, text="Browse", command=browsestep1)
#         gui.step1browse.pack(side=RIGHT, padx=2)
#
#         gui.inputframe1.bodybottom = Frame(gui.inputframe1.body, padx=2, pady=2)
#         gui.inputframe1.bodybottom.pack(expand=True, fill=X)
#         gui.step1cleardata = Button(gui.inputframe1.bodybottom, text="Clear All Data", command=clearstep1,
#                                     state=DISABLED)
#         gui.step1cleardata.pack(side=LEFT, expand=True, fill=X)
#         gui.step1lockanalysis = Button(gui.inputframe1.bodybottom, text="Lock for Conversion", state=DISABLED,
#                                        command=lockstep1)
#         gui.step1lockanalysis.pack(side=LEFT, expand=True, fill=X)
#
#     def build_stream_log_frame(self):
#         gui = self.root
#         gui.outputframe = Frame(gui, bg="pink")
#         gui.outputframe.pack(side=LEFT, anchor=N, padx=15, pady=15, fill=BOTH, expand=True)
#
#         Label(gui.outputframe, text="Output", font=self.header, bg=self.bg4).pack(fill=X)
#
#         gui.outputtextframe = Text(gui.outputframe)
#         gui.outputtextframe.pack(expand=True, fill=BOTH)
#
#         return None
#
#     def write(self, string):
#         self.root.outputtextframe.config(state=NORMAL)
#         self.root.outputtextframe.insert("end", string)
#         self.root.outputtextframe.see("end")
#         self.root.outputtextframe.config(state=DISABLED)
#         return None
#
#
#
#
#
#
#
#
# if __name__ == "__main__":          #this runs the app when we run the .py file from command line
#
#     root = Tk()
#     root.geometry('+10+10')#set's the window so it opens left 5 and down 5
#     root.geometry('1440x900')#Create the main root window, instantiate the object, and run the main loop!
#
#     # root.icon = Image('photo', file='backgroundfiles\icon2.gif')  #puts the icon we use for the window in memory
#     # root.tk.call('wm', 'iconphoto', root._w, root.icon)
#     # root.resizable(width=False, height=False)
#     app = UI(root)
#     root.mainloop()
#     root.destroy()