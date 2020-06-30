from tkinter import *
from LibraryBackend import  Database
import os.path
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib
import pylab
matplotlib.use("TkAgg")

# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pylab as pl

import sqlite3
database = Database("books.db")
# with sqlite3.connect('books.db') as conn:
#     cur = conn.cursor()


from models.Item import Item
conn = sqlite3.connect("books.db")
cur = conn.cursor()
from  models.Store import Store
from  models.ShoppingCart import ShoppingCart
cart = ShoppingCart() 



class Window(object):
	class_var = 1
	updated_list=[]
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
		self.list1.grid(row=2, column=0, rowspan=6, columnspan=2,padx=5)

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

		# b6 = Button(window, text="Top searched", width=12, command=self.animate)
		# b6.grid(row=7, column=3)

		b6 = Button(window, text="Top searched", width=12, command=self.animate)
		b6.grid(row=7, column=3)

		b7 = Button(window, text="Close", width=12, command=window.destroy)
		b7.grid(row=8, column=3)
		


		b8 = Button(window, text="Add to cart ", width=12, cursor="hand2", command=self.addItemToCart)
		b8.grid(row=9, column=0)

		b9 = Button(window, text="Go to cart ", width=12, command=self.viewCart)
		b9.grid(row=9, column=1)


	def viewCart(self):   
	    cartWindow = Toplevel()
	    cartWindow.title("The Cart")
	    cartWindow.grab_set()
	    global cart
	    cartItems = cart.getCartItems()

	    cartItemsLabelFrame = LabelFrame(cartWindow,text="Cart Items")
	    cartItemsLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

	    cartItemsFrame = Frame(cartItemsLabelFrame, padx=3, pady=3)
	    cartItemsFrame.pack()
	    index = 0
	    for item in cartItems:
	        itemFrame = Frame(cartItemsFrame,  pady="5")
	        itemFrame.pack(fill="both", expand="yes")

	        nameLabel = Label(itemFrame, text=item.name,font=("Candara",15),fg="blue")
	        priceLabel = Label(itemFrame, text="$ %s"%item.price,font=("Candara",13),fg="red")  
	        addToCartBtn = Button(itemFrame, text="Remove From Cart", font=("Candara",11,"bold"),fg="red",bg="white",cursor="hand2", command=lambda i=index: removeFromCart(i,cartWindow) )

	        nameLabel.pack(side="left")
	        priceLabel.pack(side="left")
	        addToCartBtn.pack(side="right" )
	        index += 1

	    checkOutFrame = Frame(cartWindow, pady="10")
	    totalPriceLabel = Label(checkOutFrame, text="Total Price : $ %s" % cart.getTotalPrice(), font=("Candara",14,"bold"))
	    totalPriceLabel.pack(side="left")
	    buyBtn = Button(checkOutFrame, text="Buy Now", font=("Candara",15,"bold"),bg="white",cursor="hand2", command=lambda : buyCommand(cartWindow))
	    buyBtn.pack(side="left",padx="10")
	    checkOutFrame.pack()

	    backToStoreBtn = Button(cartWindow, text="Back To Store", font=("Candara",15,"bold"),bg="white",cursor="hand2",command=cartWindow.destroy)
	    backToStoreBtn.pack(pady="6")

	    cartWindow.mainloop()
	def addItemToCart(self):
		name1=self.title_text.get()
		store = Store()
		from models.Item import Item
		Item.name=name1
		Item.price=100
		cart.addToCart(Item)
	    # messagebox.showinfo(title="Success" , message="Item %s Added To The Cart !!"%item.name )

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

	def set_const(self, new_var):
		Window.class_var = new_var

	def get_const(self):
		return Window.class_var

	def set_new_list(self, new_list):
		Window.updated_list = new_list

	def get_updated_list(self):
		return Window.updated_list

	def animate(self):
		try:
			val = self.get_updated_list()
			
			sql = "INSERT INTO top_book (title, counter) VALUES (?, ?)"
			cur.executemany(sql, val) 

			cur.execute("SELECT COUNT(DISTINCT title) FROM top_book;")
			num_of_books = cur.fetchall()
			dist_books = num_of_books[0][0]
			xs = []
			x_book_name=[]
			ys = []
			cur.execute("SELECT title from top_book")

			for i in range(dist_books):
				xs.append(i)

			for i in range(dist_books):
				one_book=cur.fetchone()
				x_book_name.append(one_book[0])

			cur.execute("SELECT counter from top_book")
			for i in range(dist_books):
				one_book_occur=cur.fetchone()
				ys.append(one_book_occur[0])

#Type1
			plt.figure(figsize=(8,6))
			plt.suptitle('Categorical Plotting')
			plt.style.use('ggplot')
			plt.plot(x_book_name, ys)
			plt.xticks(rotation=15) 
			conn.commit()
			plt.show()


			conn.commit()
			conn.close()


						
		except:
			print("No data is chosen for building a  graph")
		conn.commit()
		conn.close()
		


	def search_command(self):
		

		self.list1.delete(0, END)
		for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.ISBN_text.get()):
			self.list1.insert(END, row)
		
		
		cur.execute("SELECT title FROM book")
		var = cur.fetchall()
		new_table=[]
		rrr = self.get_updated_list()

		if (len(rrr) == 0) : 
			cur.execute("CREATE TABLE IF NOT EXISTS top_book (title VARCHAR(255), counter INTEGER);")
			get_title  = [i[0] for i in var]
			get_counter = []
			for i in range(len(get_title)):
				if(get_title[i] == self.title_text.get()):
					get_counter.append(1)
				else:
					get_counter.append(0)
			val = list(zip(get_title, get_counter))
			sql = "INSERT INTO top_book (title, counter) VALUES (?, ?)"
			cur.executemany(sql, val) 
			cur.execute('SELECT * FROM top_book')
			self.set_new_list(cur.fetchall())
			print("came here")
			conn.commit()

			
		
		new_table = self.get_updated_list()
	  
		sql = "INSERT INTO top_book (title, counter) VALUES (?, ?)"
		cur.executemany(sql, list(set(new_table)))
			
		cur.execute("SELECT max(counter) FROM top_book WHERE title=?", (self.title_text.get(), ))
		to_increment = cur.fetchall()[0][0]

		cur.execute("""UPDATE top_book 
						SET counter = counter + 1 
						WHERE title = ? and counter=?""", (self.title_text.get(),to_increment))

		cur.execute("SELECT * FROM top_book")
		list_to_save = cur.fetchall()
		self.set_new_list(list(set(list_to_save)))
		print(list(set(list_to_save)))
		conn.commit()
		return list(set(list_to_save))
		conn.close()
		


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




#code for the GUI (front end)
window = Tk()
window.geometry("580x240")
Window(window)

window.mainloop()
