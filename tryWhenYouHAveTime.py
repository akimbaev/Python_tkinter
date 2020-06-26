LARGEFONT=("Verdana", 12)



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
        for F in (StartPage, TestPage, GraphPage): 
   
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


        button2 = ttk.Button(self, text ="to_TestPage", 
                            command = lambda : controller.show_frame(TestPage)) 
      
        # # putting the button in its place  
        # # by using grid 
        button2.grid(row = 1, column = 1, padx = 10, pady = 10) 




class TestPage(tk.Frame):


    # def __init__(self,self):
    #     self.self = self
    #     self.self.wm_title("The Book Store")

    

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent) 

        # self = Tk()
        # self.window = window
        # self.window.wm_title("The Book Store")

        l1 = ttk.Label(self, text="TitleYYYYY")
        l1.grid(row=0, column=0)

        # l2 = Label(self, text="Author")
        # l2.grid(row=0, column=2)

        # l3 = Label(self, text="Year")
        # l3.grid(row=1, column=0)

        # l4 = Label(self, text="ISBN")
        # l4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.e1 = ttk.Entry(self, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        # self.author_text = StringVar()
        # self.e2 = Entry(self, textvariable=self.author_text)
        # self.e2.grid(row=0, column=3)

        # self.year_text = StringVar()
        # self.e3 = Entry(self, textvariable=self.year_text)
        # self.e3.grid(row=1, column=1)

        # self.ISBN_text = StringVar()
        # self.e4= Entry(self, textvariable=self.ISBN_text)
        # self.e4.grid(row=1, column=3)

        self.list1 = Listbox(self, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        # self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # now we need to attach a scrollbar to the listbox, and the other direction,too
        sb1 = ttk.Scrollbar(self)
        sb1.grid(row=2, column=2, rowspan=6)
        self.list1.config(yscrollcommand=sb1.set)
        sb1.config(command=self.list1.yview)

        # b1 = Button(self, text="View all", width=12, command=self.view_command)
        # b1.grid(row=2, column=3)

        # b2 = Button(self, text="Search entry", width=12, command=self.search_command)
        # b2.grid(row=3, column=3)

        # b3 = Button(self, text="Add entry", width=12, command=self.add_command)
        # b3.grid(row=4, column=3)

        # b4 = Button(self, text="Update selected", width=12, command=self.update_command)
        # b4.grid(row=5, column=3)

        b5 = ttk.Button(self, text="Delete selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        button6 = ttk.Button(self, text ="to_GraphPage", command = lambda : controller.show_frame(GraphPage)) 
        button6.grid(row = 7, column = 3) 
        # b6 = Button(self, text="Top searched", width=12, command=lambda:self.show_graph(Graph))
        # b6.grid(row=7, column=3)

        # b7 = Button(self, text="Close", width=12, command=self.destroy)
        # b7.grid(row=8, column=3)



        def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
            try:
                index = self.list1.curselection()[0]
                self.selected_tuple = self.list1.get(index)
                self.e1.delete(0,END)
                self.e1.insert(END,self.selected_tuple[1])
                self.e2.delete(0, END)
                self.e2.insert(END,self.selected_tuple[2])
                self.e3.delete(0, END)
                self.e3.insert(END,self.selected_tuple[3])
                self.e4.delete(0, END)
                self.e4.insert(END,self.selected_tuple[4])
            except IndexError:
                pass                #in the case where the listbox is empty, the code will not execute



        def view_command(self):
            self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
            for row in database.view():
                self.list1.insert(END, row)

        def search_command(self):
            self.list1.delete(0, END)
            counts = {}
            for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()):
                if self.title_text.get() in counts:
                    counts[title_text.get()] += 1
                else:
                    counts[title_text.get()] = 1
                #conn.close()
                self.list1.insert(END, row)
            return counts

        def add_command(self):
            database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
            self.list1.delete(0, END)
            self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()))

        def delete_command(self):
            database.delete(self.selected_tuple[0])
            self.view_command()

        def update_command(self):
            #be careful for the next line ---> we are updating using the texts in the entries, not the selected tuple
            database.update(self.selected_tuple[0],self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
            self.view_command()



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


# app = tkinterApp() 
# app.mainloop() 


###########################################

import tkinter as tk
from tkinter import *
from backend import  Database
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

class Window(object):
    def __init__(self,window):
        self.window = window
        self.window.wm_title("The Book Store")



        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.e2 = Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.e3 = Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.ISBN_text = StringVar()
        self.e4= Entry(window, textvariable=self.ISBN_text)
        self.e4.grid(row=1, column=3)

        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # now we need to attach a scrollbar to the listbox, and the other direction,too
        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)
        self.list1.config(yscrollcommand=sb1.set)
        sb1.config(command=self.list1.yview)

        b1 = Button(window, text="View all", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Search entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update selected", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        # button6 = ttk.Button(self, text ="Page1", command = lambda : controller.show_frame(GraphPage)) 
        # button6.grid(row = 7, column = 3) 
        b6 = Button(window, text="Top searched", width=12, command=self.animate)
        b6.grid(row=7, column=3)

        b7 = Button(window, text="Close", width=12, command=window.destroy)
        b7.grid(row=8, column=3)

    # def show_graph(self):
    #     top = Toplevel()
    #     top.title("Top searched")

    def testmatpl(self):
        names = ['group_a', 'group_b', 'group_c']
        values = [1, 10, 100]

        plt.figure(figsize=(9, 3))

        plt.subplot(131)
        plt.bar(names, values)
        plt.subplot(132)
        plt.scatter(names, values)
        plt.subplot(133)
        plt.plot(names, values)
        plt.suptitle('Categorical Plotting')
        plt.show()

    def animate(self):
        cur.execute("CREATE TABLE IF NOT EXISTS top_book (book_name VARCHAR(255), counter INTEGER)")
        sql = "INSERT INTO top_book (book_name, counter) VALUES (%s, %d)"

        val = [("new world", 21),
                ("adventures", 15),              
                ("hello", 13),
                ("adventures2", 10),
                ("adventures4", 35)
               ]
        cur.executemany('INSERT INTO top_book VALUES(?, ?)'.format(sql.replace('"', '""')), val)
        
        cur.execute("SELECT COUNT(DISTINCT book_name) FROM top_book;")
        num_of_books = cur.fetchall()
        dist_books = num_of_books[0][0]
        #book_num = list(cursor.fetchall())
        xs = []
        x_book_name=[]
        ys = []
        cur.execute("SELECT book_name from top_book")

        for i in range(dist_books):
            xs.append(i+1)

        for i in range(dist_books):
            one_book=cur.fetchone()
            x_book_name.append(one_book[0])

        cur.execute("SELECT counter from top_book")
        for i in range(dist_books):
            one_book_occur=cur.fetchone()
            ys.append(one_book_occur[0])


        plt.figure(figsize=(9, 3))
        plt.suptitle('Categorical Plotting')
        plt.plot(x_book_name, ys)

      #  ani = animation.FuncAnimation(fig, animate, interval=1000)  
        conn.commit()
        plt.show()


        ####################3
        # cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute("SELECT name, category FROM animal")
        # result_set = cursor.fetchall()
        # for row in result_set:
        # print "%s, %s" % (row["name"], row["category"])
        ######################
               


    def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute



    def view_command(self):
        self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, tk.END)
        print(self.title_text.get())
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        #be careful for the next line ---> we are updating using the texts in the entries, not the selected tuple
        database.update(self.selected_tuple[0],self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get())
        self.view_command()



if __name__ == "__main__":
    window = Tk()
    Window(window)
    window.mainloop()





      



