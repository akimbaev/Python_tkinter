from tkinter import *
import sqlite3
import tkinter.messagebox


def open_dialog():
    window=Tk()
    window.geometry("450x350")
    window.title("User Registration Form")

    username=StringVar()
    ln=StringVar()
    ps=StringVar()
    DOB=StringVar()
    num=StringVar()
    cit=StringVar()
    c1=StringVar()


    def printt():
        tkinter.messagebox.showinfo("Success", "Successfully Registered!\n \nYou can now click on EXIT to close the application.")


    def exitt():

        exit()


    def database():
        username=username.get()
        password=ps.get()
        name=ln.get()
        date=DOB.get()
        sex=c1.get()
        contact=num.get()
        city1=cit.get()
        conn=sqlite3.connect("Form.db")
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Student(username TEXT,password TEXT,name TEXT,DOB TEXT,Gender TEXT,Contact TEXT,City TEXT,)')
        cursor.execute('INSERT INTO Student(username,password,name,DOB,Gender,Contact,City) VALUES (?,?,?,?,?,?,?)' , (name1,name2,date,sex,contact,city1),)
        conn.commit()


    #HEADER
    Tops = Frame(window,bg="white",width = 1600,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)

    f1 = Frame(window,width = 900,height=700,relief=SUNKEN)
    f1.pack(side=LEFT)

    f2 = Frame(window ,width = 400,height=700,relief=SUNKEN)
    f2.pack(side=RIGHT)
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Registration",fg="black",bd=10,anchor='w')
    lblinfo.grid(row=0,column=0)
    #ENTRYFIELD FOR Username
    label1=Label(f1,text="Username")
    label1.grid(row=0,column=0)
    field1=Entry(f1,textvar=username)
    field1.grid(row=0,column=1)
    #ENTRYFIELD FOR Password
    label2=Label(f1,text="Password")
    label2.grid(row=1,column=0)
    field2=Entry(window,textvar=ps)
    field2.grid(row=1,column=1)
    # #ENTRYFIELD FOR NAME
    label3=Label(f1,text="Name")
    label3.grid(row=2,column=0)
    field3=Entry(window,textvar=ln)
    field3.grid(row=2,column=1)
    # #ENTRY FIELD FOR  DOB
    label4=Label(f1,text="Date of Birth : \n (DD/MM/YYYY) ")
    label4.grid(row=3,column=0)
    field3=Entry(window,textvar=DOB)
    field3.place(x=150, y=210)

    label5=Label(f1,text="City : ")
    label5.grid(row=4,column=0)

    

    

    # #ENTRYFIELD FOR CITY
    # city=Label(window, text="City : ", font=("Arial",14))
    # city.place(x=10, y=270)
    # field4=Entry(textvar=cit)
    # field4.place(x=100, y=275)
    # #ENTRY FIELD FOR GENDER
    # gender=Label(text="Gender: ", font=("Arial",14))
    # gender.place(x=400, y=210)

    # ch1=Radiobutton(window,text="Male", variable=c1, value="Male").place(x=100, y=300)
    # ch2=Radiobutton(window, text="Female", variable=c1, value="Female").place(x=170, y=300)
    # ch3=Radiobutton(window, text="Others", variable=c1, value="Others").place(x=250, y=300)

    # #ENTRYFIELD FOR CONTACT NO.
    # cont=Label(text="Contact No.:      +91 -  ", font=("Arial",14))
    # cont.place(x=10, y=390)
    # field5=Entry(textvar=num)
    # field5.place(x=200, y=395)

    #BUTTONS
    but1 = Button(text=" Submit", width=12, height=2, bg="beige", font=("Arial", 8), command=lambda: [printt(), database()])
    but1.place(x=100, y=650)
    window.bind("<Return>", database)

    but2=Button(text="Exit", width=12, height=2, bg="beige", font=("Arial",8), command=exitt)
    but2.place(x=600, y=650)

    window.mainloop()



if __name__ == "__main__":
    open_dialog()

