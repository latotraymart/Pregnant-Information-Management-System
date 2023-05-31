from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile



class Patient_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Ensofttech Phonebook Management System     | Developed By Group 2 ")
        self.root.geometry("1400x1400+0+225")
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=50,
        fieldbackground="#D3D3D3"
       
        

        )
        style.configure("Treeview.Heading", font=('Arial', 12,'bold'))
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 12))
        style.map('Treeview',background=[('selected','green')])
       
        #===========variables=====================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


        self.var_cust_name=StringVar()
        self.var_last_name=StringVar()
        self.var_address=StringVar()
        self.var_contact=StringVar()
        self.var_bmi=StringVar()
        self.var_health=StringVar()
       
        




        #======title===============
        lbl_title=Label(self.root,text="Phonebook Management System",font=("times new roman",20,"bold"),bg="green",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1400,height=50)
         #=====logo==================
       
       

        #===========labelframe======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Pregnant Personal Details", font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=425)

      


        


        #===Patient name==========
        lbl_cust_name=Label(labelframeleft,text="First Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        txt_cname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("times new roman",13,"bold"))
        txt_cname.grid(row=1,column=1)

        #lastname=====
        lbl_last_name=Label(labelframeleft,text="Last Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_last_name.grid(row=2,column=0,sticky=W)

        txt_lname=ttk.Entry(labelframeleft,textvariable=self.var_last_name,width=29,font=("times new roman",13,"bold"))
        txt_lname.grid(row=2,column=1)

        #====== address=========
        lbl_cust_address=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_address.grid(row=3,column=0,sticky=W)

        txt_add=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("times new roman",13,"bold"))
        txt_add.grid(row=3,column=1)

        #===contact=====

        lbl_contact=Label(labelframeleft,font=("arial",12,"bold"),text="Contact No.",padx=2,pady=6)
        lbl_contact.grid(row=4,column=0,sticky=W)

        txt_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=29,font=("times new roman",13,"bold"))
        txt_contact.grid(row=4,column=1)


      
     
       
         
        
        #========buttons========
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=412,height=40)
        
        btnadd=Button(btn_frame,text="Save",command=self.add_data,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)
        
        btndel=Button(btn_frame,text="Delete",command=self.mdelete_data,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btndel.grid(row=0,column=4,padx=1)


        #=======search table frame system============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and  Search", font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=905,height=490)

        lbl_searchby=Label(table_frame,text="Search By: ",font=("times new roman",12,"bold"),bg="green",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)


        self.serch_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_search["value"]=("lname","ContactNo")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,font=("times new roman",13,"bold"),width=20)
        txt_search.grid(row=0,column=2,padx=2)


        btn_search=Button(table_frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="green",fg="gold",width=5)
        btn_search.grid(row=0,column=3,padx=1)

        btn_show=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btn_show.grid(row=0,column=4,padx=1)

        #======show data table======

        view_table=Frame(table_frame,bd=2,relief=RIDGE)
        view_table.place(x=0,y=50,width=900,height=350)

        scrollx=ttk.Scrollbar(view_table,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(view_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(view_table,column=("FName","LName","Address","ContactNo",
        ),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)


        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.cust_details_table.xview)
        scrolly.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("FName",text="FirstName")
        self.cust_details_table.heading("LName",text="LastName")
        self.cust_details_table.heading("Address",text="Address")
        self.cust_details_table.heading("ContactNo",text="Contact_No")
       
        self.cust_details_table["show"]="headings"

       
        self.cust_details_table.column("FName",width=150)
        self.cust_details_table.column("LName",width=150)
        self.cust_details_table.column("Address",width=150)
        self.cust_details_table.column("ContactNo",width=150)
       
       

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        
        
        if self.var_contact.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
               
                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into tblpatient values(%s,%s,%s,%s)",(
                                                                          
                                                                            self.var_cust_name.get(),
                                                                            self.var_last_name.get(),
                                                                            self.var_address.get(),
                                                                            self.var_contact.get(),
                                                                           
                                                                           
                                                                        ))
                                                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Record Has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from tblpatient")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,events=""):
        cursor_rows=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_rows)
        row=content["values"]

   
        self.var_cust_name.set(row[0])
        self.var_last_name.set(row[1])
        self.var_address.set(row[2])
        self.var_contact.set(row[3])
       
        

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            my_cursor.execute("update tblpatient set FName=%s,LName=%s,Address=%s where ContactNo=%s",(

                                                                                                                    
                                                                                                                    self.var_cust_name.get(),
                                                                                                                    self.var_last_name.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_contact.get()
                                                                                                                   

                                                                                                                                                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Record details has been updated successfully",parent=self.root)


    

    def reset(self):
        #self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_last_name.set("")
        self.var_address.set("")
        #self.var_gender.set("")
        self.var_contact.set("")
       
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search(self):

        if self.txt_search.get()=="":
            messagebox.showerror("Error","Fields are Required",parent=self.root)
        
        

        
        
        else:
    
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            my_cursor.execute('select * from tblpatient where ' +str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get()+"%'"))
            rows=my_cursor.fetchall()
            if len (rows)!=0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
                for i in rows:
                    self.cust_details_table.insert("",END,values=i)
               
                conn.commit()
                conn.close()
            else:
                messagebox.showerror("Error","Record  Not Found")
    
    def mdelete_data(self):
        mdelete_data=messagebox.askyesno("Phonebook Management System","Do you want to delete this Record",parent=self.root)
        if mdelete_data>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query="delete from tblpatient  where ContactNo=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

   
        
            



if __name__=="__main__":
    root=Tk()
    obj=Patient_window(root)
    root.mainloop()

        
