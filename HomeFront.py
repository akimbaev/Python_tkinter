
import tkinter as tk
from tkinter import *
from LibraryBackend import  Database
import tkinter.ttk as ttk
import matplotlib
matplotlib.use("TkAgg")

# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

try:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
except ImportError:
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
except:
    raise



style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

import sqlite3
database = Database("books.db")
with sqlite3.connect('books.db') as conn:
    cur = conn.cursor()
LARGEFONT=("Verdana", 20)
class tkinterApp(tk.Tk): 
      
    # __init__ function for class tkinterApp  
    def __init__(self, *args, **kwargs):  
          
        # __init__ function for class Tk 
        tk.Tk.__init__(self, *args, **kwargs) 
      #  tk.Tk.iconbitmap(self, default="library2.bmp")
        tk.Tk.wm_title(self, "Library")  
        # creating a container 
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
        # initializing frames to an empty array 
        self.frames = {}   
   
        # iterating through a tuple consisting 
        # of the different page layouts 
        for F in (StartPage, GraphPage): 
   
            frame = F(container, self) 
   
            # initializing frame of that object from 
            # startpage, page1, page2 respectively with  
            # for loop 
            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(StartPage) 
   
    # to display the current frame passed as 
    # parameter 
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 


class StartPage(tk.Frame):
    def To_library(self):
        # # self.master=master
        
        
        # from LibraryFront import Window
        # window = Tk()
        # Window(window)
        import subprocess
        subprocess.call(" python LibraryFront.py 1", shell=True)
 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="StartPage", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
   
        # button to show frame 2 with text 
        # layout2 
        button1 = ttk.Button(self, text ="to_GraphPage", 
                            command = lambda : controller.show_frame(GraphPage)) 
      
        # putting the button in its place  
        # by using grid 

        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
        # from LibraryFront import Window

        button2 = ttk.Button(self, text ="to Library",
                            command =self.To_library) 
      
        # # putting the button in its place  
        # # by using grid 
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
        closeButton = Button(self, text="  Exit  ",command=quit,width=10)
        closeButton.grid(row = 3, column = 1, padx=10,pady=160)







class GraphPage(tk.Frame):
        
    def __init__(self, parent, controller):
        

        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="GraphPage", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
   
        # button to show frame 2 with text 
        # layout2 
        button1 = ttk.Button(self, text ="to_StartPage", 
                            command = lambda : controller.show_frame(StartPage)) 
      
        # putting the button in its place  
        # by using grid 
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
        closeButton = Button(self, text="  Exit  ",command=quit,width=10)
        closeButton.grid(row = 2, column = 1, padx=10,pady=200)


app = tkinterApp() 
app.geometry("450x350")
app.resizable(False, False)
app.mainloop() 

