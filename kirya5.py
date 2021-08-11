import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm
import pyodbc

# from visual import *
# import pygame
#conn = pyodbc.connect(
#  'Driver={SQL Server};'
#  'Server=DESKTOP-IM4KUKU\SQLEXPRESS;'
#  'Database=ACDB;'
#  'Trusted_Connection=yes;')



def quit():
        sys.exit()





def mainmenu():
        
        def view():
                def Search():
                                costumer_id=e3.get()

                                conn = pyodbc.connect('Driver={SQL Server};'
                                                        'Server=DESKTOP-IM4KUKU\SQLEXPRESS;'
                                                        'Database=ACDB;'
                                                        'Trusted_Connection=yes;')
                                cursor=conn.cursor()

                                cursor.execute("select * from dbo.customers")

                                row=cursor.fetchone()


                                while costumer_id != "":
                                        try:
                                                if str(row[0]) == costumer_id:
                                                        print_records=""
                                                        print_records+=str("*"+" " +str(row[0])+" " +str(row[1])+" "+str(row[2])+" "+ str(row[3]))+" "+        "\n"
                                                        listbox.insert(END,print_records)
                                                        break
                                        except:
                                                # messagebox.showerror('EROR','Costumer ID does not exist')
                                                print_records="WRONG ID CUSTOMER NOT FOUND"
                                                # print("no")
                                                listbox.insert(END,print_records)
                                                break
                                        row = cursor.fetchone() 
                                e3.delete(0,END)
            
                   
  
                # f.destroy()
                f = tk.Tk()
                f.geometry("{0}x{1}+0+0".format(f.winfo_screenwidth(), f.winfo_screenheight()))
                f.configure(bg="#a5ffa7")
                listbox = Listbox(f, font=40)
                listbox.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.4)
                        
                tk.Label(f, text="customer_id",bg="#a5ffa7").place(relx=0.2,rely=0.3,relwidth=0.1 )
                        
                e3 = tk.Entry(f)
                e3.place(relx=0.3,rely=0.3,relwidth=0.1 )
                        
                tk.Button(f,text='SEARCH',bg="GREY",command=Search).place(relx=0.3,rely=0.4,relwidth=0.1 )
                tk.Button(f,text='RETURN',bg="red", command=mainmenu).place(relx=0.3,rely=0.45,relwidth=0.1 )
                exitt=tk.Button(f,text="EXIT",bg="RED", command=quit).place(relx=0.85,rely=0.85,relwidth=0.1)
        
        
        def packid():
                window.destroy()
                f = tk.Tk()
                f.geometry("{0}x{1}+0+0".format(f.winfo_screenwidth(), f.winfo_screenheight()))
                f.title("sign up")
                f.configure(bg="lightblue")
                tk.Button(f,text='SUBMIT',bg="seagreen").grid(row=7,column=1,sticky=tk.W,pady=4)
                tk.Button(f,text='RETURN',bg="red").grid(row=8,column=1,sticky=tk.W,pady=4)
                tk.Label(f, text="pack id",bg="lightblue").grid(row=0)
                tk.Label(f, text="speed",bg="lightblue").grid(row=1)
                tk.Label(f, text="start date",bg="lightblue").grid(row=2)
                tk.Label(f, text="month payment",bg="lightblue").grid(row=3)
                tk.Label(f, text="sector id",bg="lightblue").grid(row=4)
                tk.Label(f, text="customer id",bg="lightblue").grid(row=5)
                e1 = tk.Entry(f).grid(row=0, column=1)
                e2 = tk.Entry(f).grid(row=1, column=1)
                e3 = tk.Entry(f).grid(row=2, column=1)
                e4 = tk.Entry(f).grid(row=3, column=1)
                e5 = tk.Entry(f).grid(row=4, column=1)
                e6 = tk.Entry(f).grid(row=5, column=1)
                exitt=tk.Button(f,text="EXIT",bg="RED", command=quit).place(relx=0.85,rely=0.85,relwidth=0.1)



        

        def delete():
                def deletee():
                        print_records="YOUR ARE NO LONGER OUR CUSTOMER :( "
                        listbox.insert(END,print_records)

                f = tk.Tk()
                f.geometry("{0}x{1}+0+0".format(f.winfo_screenwidth(), f.winfo_screenheight()))
                f.configure(bg="#ffeeee")
                listbox = Listbox(f, font=40)
                listbox.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.4)
                tk.Label(f, text="First Name",bg="#ffeeee").place(relx=0.2,rely=0.2,relwidth=0.1 )
                tk.Label(f, text="Last Name",bg="#ffeeee").place(relx=0.2,rely=0.25,relwidth=0.1 )
                tk.Label(f, text="customer_id",bg="#ffeeee").place(relx=0.2,rely=0.3,relwidth=0.1 )
                tk.Label(f, text="pack id",bg="#ffeeee").place(relx=0.2,rely=0.35,relwidth=0.1 )
                e1 = tk.Entry(f).place(relx=0.3,rely=0.2,relwidth=0.1 )
                e2 = tk.Entry(f).place(relx=0.3,rely=0.25,relwidth=0.1 )
                e3 = tk.Entry(f).place(relx=0.3,rely=0.3,relwidth=0.1 )
                e4 = tk.Entry(f).place(relx=0.3,rely=0.35,relwidth=0.1 )
                tk.Button(f,text='DELETE',bg="#d84a4a",command=deletee).place(relx=0.3,rely=0.4,relwidth=0.1 )
                tk.Button(f,text='RETURN',bg="gray",command=mainmenu).place(relx=0.3,rely=0.45,relwidth=0.1 )
                print_records = "STATUS:"
                listbox.insert(END, print_records)
                exitt=tk.Button(f,text="EXIT",bg="RED", command=quit).place(relx=0.85,rely=0.85,relwidth=0.1)
        def Add_package():
                        def updatee():
                                print_records="A NEW PACKAGE HAS BEEN ADDED !"
                                listbox.insert(END,print_records)
                                pack_ID=e1.get()
                                Speed=e2.get()
                                Startdate=e3.get()
                                sector=e4.get()
                                Monthlypayment=e5.get()
                                conn = pyodbc.connect('Driver={SQL Server};'
                                        'Server=DESKTOP-IM4KUKU\SQLEXPRESS;'
                                        'Database=ACDB;'
                                        'Trusted_Connection=yes;')
                                cursor.execute('''INSERT INTO packages (pack_id,speed,strt_date,monthly_payment,sector_id) VALUES(?,?,?,?,?)  ''',
                                        (Packege_id, new_speed, start_date, monthly_payment, new_Sector_id))
                                        

                        f = tk.Tk()
                        f.geometry("{0}x{1}+0+0".format(f.winfo_screenwidth(), f.winfo_screenheight()))
                        f.configure(bg="pink")
                        tk.Label(f, text="pack_ID",bg="pink").place(relx=0.2,rely=0.2,relwidth=0.1 )
                        tk.Label(f, text="Speed",bg="pink").place(relx=0.2,rely=0.25,relwidth=0.1 )
                        tk.Label(f, text="Start date",bg="pink").place(relx=0.2,rely=0.3,relwidth=0.1 )
                        tk.Label(f, text="sector",bg="pink").place(relx=0.2,rely=0.35,relwidth=0.1 )
                        tk.Label(f, text="Monthly payment",bg="pink").place(relx=0.2,rely=0.4,relwidth=0.1 )
                        e1 = tk.Entry(f).place(relx=0.3,rely=0.2,relwidth=0.1 )
                        e2 = tk.Entry(f).place(relx=0.3,rely=0.25,relwidth=0.1 )
                        e3 = tk.Entry(f).place(relx=0.3,rely=0.3,relwidth=0.1 )
                        e4 = tk.Entry(f).place(relx=0.3,rely=0.35,relwidth=0.1 )
                        e5 = tk.Entry(f).place(relx=0.3,rely=0.4,relwidth=0.1 )
                        listbox = Listbox(f, font=40)
                        listbox.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.4)
                        print_records = "STATUS:"
                        listbox.insert(END, print_records)
                        exit=tk.Button(f,text="EXIT",bg="RED", command=quit).place(relx=0.85,rely=0.85,relwidth=0.1)
                        re=tk.Button(f,text='RETURN',bg="gray",command=mainmenu).place(relx=0.3,rely=0.45,relwidth=0.1 )
                        tk.Button(f,text='ADD PACKAGE',bg="#5dbb63",command=updatee).place(relx=0.3,rely=0.5,relwidth=0.1 )
                



        def signup():
                def connect():
                        print_records="WELCOME TO OUR COMPANY!"
                        listbox.insert(END,print_records)



                f = tk.Tk()
                f.geometry("{0}x{1}+0+0".format(f.winfo_screenwidth(), f.winfo_screenheight()))
                f.title("sign up")
                tk.Button(f,text='SUBMIT',bg="seagreen", command=connect).place(relx=0.3,rely=0.5,relwidth=0.1 )
                f.configure(bg="lightblue")
                tk.Button(f,text='RETURN',bg="red",command=mainmenu).place(relx=0.3,rely=0.55,relwidth=0.1 )
                tk.Label(f, text="First Name",bg="lightblue").place(relx=0.2,rely=0.2,relwidth=0.1 )
                tk.Label(f, text="Last Name",bg="lightblue").place(relx=0.2,rely=0.25,relwidth=0.1 )
                tk.Label(f, text="birth date",bg="lightblue").place(relx=0.2,rely=0.30,relwidth=0.1 )
                tk.Label(f, text="customer_id",bg="lightblue").place(relx=0.2,rely=0.35,relwidth=0.1 )
                tk.Label(f, text="city",bg="lightblue").place(relx=0.2,rely=0.40,relwidth=0.1 )
                tk.Label(f, text="state",bg="lightblue").place(relx=0.2,rely=0.45,relwidth=0.1 )
                tk.Label(f, text="street",bg="lightblue").place(relx=0.4,rely=0.2,relwidth=0.1 )
                tk.Label(f, text="main num",bg="lightblue").place(relx=0.4,rely=0.25,relwidth=0.1 )
                tk.Label(f, text="second num",bg="lightblue").place(relx=0.4,rely=0.3,relwidth=0.1 )
                tk.Label(f, text="fax",bg="lightblue").place(relx=0.4,rely=0.35,relwidth=0.1 )
                tk.Label(f, text="monthly discount",bg="lightblue").place(relx=0.4,rely=0.4,relwidth=0.1 )
                tk.Label(f, text="pack id",bg="lightblue").place(relx=0.4,rely=0.45,relwidth=0.1 )
                tk.Label(f, text="join date",bg="lightblue").place(relx=0.4,rely=0.5,relwidth=0.1 )
                e1 = tk.Entry(f).place(relx=0.3,rely=0.2,relwidth=0.1 )
                e2 = tk.Entry(f).place(relx=0.3,rely=0.25,relwidth=0.1 )
                e3 = tk.Entry(f).place(relx=0.3,rely=0.3,relwidth=0.1 )
                e4 = tk.Entry(f).place(relx=0.3,rely=0.35,relwidth=0.1 )
                e5 = tk.Entry(f).place(relx=0.3,rely=0.4,relwidth=0.1 )
                e6 = tk.Entry(f).place(relx=0.3,rely=0.45,relwidth=0.1 )
                e7 = tk.Entry(f).place(relx=0.5,rely=0.2,relwidth=0.1 )
                e8 = tk.Entry(f).place(relx=0.5,rely=0.25,relwidth=0.1 )
                e9 = tk.Entry(f).place(relx=0.5,rely=0.3,relwidth=0.1 )
                e10 = tk.Entry(f).place(relx=0.5,rely=0.35,relwidth=0.1 )
                e11 = tk.Entry(f).place(relx=0.5,rely=0.4,relwidth=0.1 )
                e12 = tk.Entry(f).place(relx=0.5,rely=0.45,relwidth=0.1 )
                e13 = tk.Entry(f).place(relx=0.5,rely=0.5,relwidth=0.1 )
                exitt=tk.Button(f,text="EXIT",bg="RED", command=quit).place(relx=0.85,rely=0.85,relwidth=0.1)
                listbox = Listbox(f, font=40)
                listbox.place(relx=0.65, rely=0.2, relwidth=0.3, relheight=0.4)

                window.mainloop()
        def updatepackege():
                def cc():
                        print_records="YOU ARE UP TO DATE \(^o^)/ "
                        listbox.insert(END,print_records)

                

                f = tk.Tk()
                f.geometry("{0}x{1}+0+0".format(f.winfo_screenwidth(), f.winfo_screenheight()))
                f.configure(bg="#ffc53a")
                tk.Label(f, text="First Name",bg="#ffc53a").place(relx=0.2,rely=0.2,relwidth=0.1 )
                tk.Label(f, text="Last Name",bg="#ffc53a").place(relx=0.2,rely=0.25,relwidth=0.1 )
                tk.Label(f, text="PACK ID",bg="#ffc53a").place(relx=0.2,rely=0.3,relwidth=0.1 )
                e1 = tk.Entry(f).place(relx=0.3,rely=0.2,relwidth=0.1 )
                e2 = tk.Entry(f).place(relx=0.3,rely=0.25,relwidth=0.1 )
                e3 = tk.Entry(f).place(relx=0.3,rely=0.3,relwidth=0.1 )
                tk.Button(f,text='UPDATE',bg="#5DBB63", command=cc).place(relx=0.3,rely=0.35,relwidth=0.1 )
                tk.Button(f,text='RETURN',bg="gray",command=mainmenu).place(relx=0.3,rely=0.4,relwidth=0.1 )
                exitt=tk.Button(f,text="EXIT",bg="#D84A4A", command=quit).place(relx=0.85,rely=0.85,relwidth=0.1)
                listbox = Listbox(f, font=40)
                listbox.place(relx=0.45, rely=0.2, relwidth=0.2, relheight=0.2)
                
                f.mainloop()

        w=tk.Tk()
        w.geometry("{0}x{1}+0+0".format(w.winfo_screenwidth(), w.winfo_screenheight()))
        w.configure(bg="BLACK")
        w.title("KIRIYA LTD")
        label1=tk.Label(w,text="welcome! please choose an option", bg='BLACK' ,fg='#f64a8a', font='15' ).place(relx=0.35,rely=0.2,relwidth=0.3 )
        btn = tk.Button(w,text="ADD A NEW CUSTOMER",bg="LIGHTBLUE", command=signup).place(relx=0.35,rely=0.3,relwidth=0.3)
        tk.Button(w,text="DELETE COSTUMER",bg="#FFEEEE", command=delete).place(relx=0.35,rely=0.4,relwidth=0.3)
        tk.Button(w,text="ADD A NEW PACKEGE",bg="PINK", command=Add_package).place(relx=0.35,rely=0.5,relwidth=0.3)
        tk.Button(w,text="UPDATE PACKAGE",bg="#ffc53a", command=updatepackege).place(relx=0.35,rely=0.6,relwidth=0.3)
        tk.Button(w,text="CUSTOMER DETAILS",bg="#a5ffa7", command=view).place(relx=0.35,rely=0.7,relwidth=0.3)
        tk.Button(w,text="EXIT",bg="RED", command=quit).place(relx=0.85,rely=0.85,relwidth=0.1)
        window.destroy()
        w.mainloop()




window=tk.Tk()
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.configure(bg='black')
# signup=tk.Button(window,text="CLICK HERE TO START",bg="#82cbf6", command=mainmenu).place(relx=0.35,rely=0.3,relwidth=0.3)
# label1=tk.Label(text="WELCOME PLEASE CHOOSE AN OPTION", bg='#01002D' ,fg='RED', font='15' ).place(relx=0.35,rely=0.2,relwidth=0.3 )
# photo = PhotoImage(file ='C:/Users/jonatan/Desktop/kiriya/PROLOGO.png') 
# photo=PhotoImage(file='C:/Users/jonatan/Desktop/kiriya/PROLOGO.png') 
# here, image option is used to 
# set image on button 
Button(window, text = 'Click Me !', command=mainmenu).place(relx=0.38,rely=0.3,relwidth=0.249)
window.mainloop()

