
from tkinter.messagebox import showinfo,showerror

from tkinter import *
from tkinter import messagebox as ms
from PIL import ImageTk, Image
import sqlite3
from frontend import Window
# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
db.commit()
db.close()
class main:
    def __init__(self,master):
        self.n_username = StringVar()
        self.n_password = StringVar()
        # Window
        self.master = master
        # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        #Create Widgets
        self.widgets()
    def login(self):
        #Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            self.head['text'] = self.username.get() + '\n Loged In'
            self.head['pady'] = 150
            showinfo(title = "success", message = "Username and password correct")
    		# self.destroy()
    	    # window = Tk()
    		# Window(window)
        else:
            ms.showerror('Oops!','Username Not Found.')
            # showerror(title = "warning", message = "incorrect username or password")
    	# Connect to database


    def registration(self):
        #Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user,[(self.n_username.get())])
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()
    def widgets(self):


        self.head = Label(self.master,text = 'Start page',font = ('',35),pady = 10)

        self.head.pack()
        # self.head1 = Frame(self.master,padx=0,pady=0)
        # self.head1.pack()


        self.logf = Frame(self.master,padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 3,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 3,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 ,borderwidth=3,width = 15,padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Sign Up ',bd = 3 ,borderwidth=3,width = 15,padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        # tkinter.Button(self, text="SignUp",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 15, command = register).grid(row = 10,column=1,  padx=(50, 0), pady=(20, 10))

        self.logf.pack()

        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.crf,text = 'Create Account',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.registration).grid()
        Button(self.crf,text = 'Go to Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=2,column=1)

    	# bg_color = "white"
    	# fg_color = "#383a39"
    	# # -------username
        #
    	# # ----password
    	# tkinter.Label(self,  text="Password:", fg=fg_color, bg=bg_color, font=("Helvetica", 15)).grid(row=9, padx=(50, 0), pady=(20, 10))
    	# --------button
    	# tkinter.Button(self, text="Login",borderwidth=3, relief='ridge', fg=fg_color, bg=bg_color, width = 15, command = login).grid(row = 10,  padx=(50, 0), pady=(20, 10))

if __name__ == "__main__":
    # root =tkinter.Tk()
    # app = Main(root)
    # app.pack()

    #Create Object
	#and setup window
    root = Tk()
    # root.title('Login Form')

    root.title("Hof Library")
    root.geometry("450x350")
    img = ImageTk.PhotoImage(Image.open("library4.png"))
    panel = Label(root, image = img)
    panel.pack(side = "top")

    #root.geometry('400x350+300+300')
    main(root)
    root.mainloop()

    # root.geometry("450x350")
    # root.resizable(False, False)

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
