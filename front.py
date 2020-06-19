
from tkinter.messagebox import showinfo,showerror
import sqlite3
from tkinter import *
import tkinter
from PIL import ImageTk, Image
from login1 import open_dialog

class Main(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
    	def login():
    		# Connect to database
    		db = sqlite3.connect('Form.db')
    		c = db.cursor()
    		username = lblusername.get()
    		password = lblpassword.get()
    		
    		c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    		
    		if c.fetchall():
    			showinfo(title = "success", message = "Username and password correct")
    		else:
    			showerror(title = "warning", message = "incorrect username or password")
    			
    		c.close()

    	bg_color = "white"
    	fg_color = "#383a39"
    	# -------username
    	tkinter.Label(self,  text="Username:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=8, padx=(50, 0), pady=(20, 10))
    	lblusername = tkinter.Entry(self)
    	lblusername.grid(row=8, column=1, padx=(10, 10), pady=(20, 10))

    	# ----password
    	tkinter.Label(self,  text="Password:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=9, padx=(50, 0), pady=(20, 10))
    	lblpassword = tkinter.Entry(self)
    	lblpassword.grid(row=9, column=1, padx=(10, 10),pady=(20, 10))

    	# --------button
    	tkinter.Button(self, text="Login",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 15, command = login).grid(row = 10,  padx=(50, 0), pady=(20, 10))

if __name__ == "__main__":
    root =tkinter.Tk()
    app = Main(root)
    app.pack()
    photo = ImageTk.PhotoImage(Image.open("library4.png"))
    tkinter.Label(app, image=photo).grid(rowspan = 3, columnspan = 5, row =0,column = 0)
    tkinter.Button(app, text="SignUp",borderwidth=3, relief='ridge', fg="#383a39", bg="white", width = 15, command = open_dialog).grid(row = 10, column=1, padx=(25, 0), pady=(20, 10))

    root.title("Hof Library")
    root.geometry("450x350")
    root.resizable(False, False)

    root.mainloop()
# from tkinter import *
# import random
# import time

# window=tkinter()
# window.geometry("1600x700+0+0")
# window.title("Library Hof")
# Tops = Frame(window,bg="white",width = 1600,height=50,relief=SUNKEN)
# Tops.pack(side=TOP)

# f1 = Frame(window,width = 900,height=700,relief=SUNKEN)
# f1.pack(side=LEFT)

# f2 = Frame(window ,width = 400,height=700,relief=SUNKEN)
# f2.pack(side=RIGHT)
# #------------------TIME--------------
# localtime=time.asctime(time.localtime(time.time()))
# #-----------------INFO TOP------------
# lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Library Hof",fg="black",bd=10,anchor='w')
# lblinfo.grid(row=0,column=0)
# lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="black",anchor=W)
# lblinfo.grid(row=1,column=0)

# label1=Label(f1,text="Name of book")
# label1.grid(row=0,column=0)

# label2=Label(f1,text="Author")
# label2.grid(row=1,column=0)

# label3=Label(f1,text="Library3")
# label3.grid(row=2,column=0)

# label4=Label(f1,text="Library4")
# label4.grid(row=3,column=0)

# label5=Label(f1,text="Library5")
# label5.grid(row=4,column=0)


# window.mainloop()
