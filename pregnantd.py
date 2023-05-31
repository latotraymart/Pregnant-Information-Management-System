import os, sys
import random
import tempfile
from datetime import datetime
from logging import info
from time import strftime
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector
from PIL import Image, ImageTk


class Pregnantdetails_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Record Management System     | Developed By Group 2 ")
        self.root.geometry("1400x1400+0+225")
        style=ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=50,
        fieldbackground="#D3D3D3"
        
        )
        style.configure("Treeview.Heading", font=('Arial', 11,'bold'))
        style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 11))
        style.map('Treeview',background=[('selected','green')])
       



        #======variabless=====
        self.var_Lmens=StringVar()
        self.var_fcheck=StringVar()
        self.var_Pstat=StringVar()
        self.var_followup=StringVar()
        self.var_lastcheckupstat=StringVar()
        self.var_medfindings=StringVar()
        self.var_reccommendation=StringVar()
        self.var_nextcheckup=StringVar()
        self.var_healthcard=StringVar()
        self.var_dbframe=StringVar()
        self.var_details=StringVar()





         #======title===============
        lbl_title=Label(self.root,text="PREGNANT MEDICAL INFORMATION",font=("times new roman",20,"bold"),bg="green",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1400,height=40)


   
     
       
         #=====logo==================
        img2=Image.open(r"C:\Users\LATOT\Desktop\Pregnant System\images\preglogo.webp")
        img2=img2.resize((90,45),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=90,height=45)

        #===========Room labelframe======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Pregnant Medical Details", font=("times new roman",10,"bold"),padx=2)
        labelframeleft.place(x=0,y=50,width=425,height=430)

        #=======labels and entry===========
        #==customer contact
        lbl_healthcard=Label(labelframeleft,text="Patient HealthCard",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_healthcard.grid(row=0,column=0,sticky=W)


        enty_health=ttk.Entry(labelframeleft,textvariable=self.var_healthcard,font=("times new roman",13,"bold"),width=19)
        enty_health.grid(row=0,column=1,sticky=W)

        


        #==fetch data button
        btn_fetchdata=Button(labelframeleft,command=self.fetch_contact,text="fetch data",font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btn_fetchdata.place(x=330,y=4)





        #==check_in date
        lbl_lms=Label(labelframeleft,text="Last Menstruation" ,font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_lms.grid(row=1,column=0,sticky=W)

        txt_lms=ttk.Entry(labelframeleft,textvariable=self.var_Lmens,width=29,font=("times new roman",13,"bold"))
        txt_lms.grid(row=1,column=1)

        #==check_out date
        lbl_fcheck=Label(labelframeleft,text="First Checkup",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_fcheck.grid(row=2,column=0,sticky=W)

        txt_fcheck=ttk.Entry(labelframeleft,textvariable=self.var_fcheck,width=29,font=("times new roman",13,"bold"))
        txt_fcheck.grid(row=2,column=1)

        lbl_pregstats=Label(labelframeleft,text="Pregnant Status",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_pregstats.grid(row=3,column=0,sticky=W)

        txt_regstats=ttk.Entry(labelframeleft,textvariable=self.var_Pstat,width=29,font=("times new roman",13,"bold"))
        txt_regstats.grid(row=3,column=1)


        lbl_followup=Label(labelframeleft,text="Follow up",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_followup.grid(row=4,column=0,sticky=W)

        txt_lastcheckup=ttk.Entry(labelframeleft,textvariable=self.var_followup,width=29,font=("times new roman",13,"bold"))
        txt_lastcheckup.grid(row=4,column=1)

        lbl_lastcheckup=Label(labelframeleft,text="Last Checkup Status",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_lastcheckup.grid(row=5,column=0,sticky=W)

        txt_lastcheckup=ttk.Entry(labelframeleft,textvariable=self.var_lastcheckupstat,width=29,font=("times new roman",13,"bold"))
        txt_lastcheckup.grid(row=5,column=1)


        lbl_Medfinding=Label(labelframeleft,text="Medical Findings",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_Medfinding.grid(row=6,column=0,sticky=W)

        txt_medf=ttk.Entry(labelframeleft,textvariable=self.var_medfindings,width=29,font=("times new roman",13,"bold"))
        txt_medf.grid(row=6,column=1)

        lbl_reccomend=Label(labelframeleft,text="Reccomendation",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_reccomend.grid(row=7,column=0,sticky=W)

        txt_reccomend=ttk.Entry(labelframeleft,textvariable=self.var_reccommendation,width=29,font=("times new roman",13,"bold"))
        txt_reccomend.grid(row=7,column=1)


        lbl_nxtcheck=Label(labelframeleft,text="Next Checkup",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_nxtcheck.grid(row=8,column=0,sticky=W)

        txt_nxtcheck=ttk.Entry(labelframeleft,textvariable=self.var_nextcheckup,width=29,font=("times new roman",13,"bold"))
        txt_nxtcheck.grid(row=8,column=1)










      
       
        
        
    

       

   
        
        #========buttons========
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=340,width=420,height=40)
        
        btnadd=Button(btn_frame,text="Save",command=self.add_data,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        btnprint=Button(btn_frame,text="Print",command=self.printb,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btnprint.grid(row=0,column=4,padx=1)


      
       

        
      



         #=======search table frame system============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and  Search", font=("arial",12,"bold"),padx=2)
        table_frame.place(x=455,y=250,width=900,height=200)

        lbl_searchby=Label(table_frame,text="Search By: ",font=("times new roman",12,"bold"),bg="green",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)


        self.serch_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_search["value"]=("Healthcard","First_checkup")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,font=("times new roman",13,"bold"),width=20)
        txt_search.grid(row=0,column=2,padx=2)


        btn_search=Button(table_frame,text="Search",command=self.search_data,font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btn_search.grid(row=0,column=3,padx=1)

        btn_show=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btn_show.grid(row=0,column=4,padx=1)

       

         #======show data table======

        view_table=Frame(table_frame,bd=2,relief=RIDGE)
        view_table.place(x=0,y=50,width=900,height=120)

        scrollx=ttk.Scrollbar(view_table,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(view_table,orient=VERTICAL)

        self.room_details_table=ttk.Treeview(view_table,column=("Healthcard","Last_Menstruation","First_checkup","Pregnant_status","Follow_up","Last_checkup_Status","Medical_Findings","Recommendation","Next_Checkup"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)


        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.room_details_table.xview)
        scrolly.config(command=self.room_details_table.yview)

        self.room_details_table.heading("Healthcard",text="Healthcard")
        self.room_details_table.heading("Last_Menstruation",text="Last_Menstruation")
        self.room_details_table.heading("First_checkup",text="First_checkup")
        self.room_details_table.heading("Pregnant_status",text="Pregnant_status")
        self.room_details_table.heading("Follow_up",text="Follow_up")
        self.room_details_table.heading("Last_checkup_Status",text="Last_checkup_Status")
        self.room_details_table.heading("Medical_Findings",text="Medical_Findings")
        self.room_details_table.heading("Recommendation",text="Recommendation")
        self.room_details_table.heading("Next_Checkup",text="Next_Checkup")
        
        
        self.room_details_table["show"]="headings"

        self.room_details_table.column("Healthcard",width=150)
        self.room_details_table.column("Last_Menstruation",width=150)
        self.room_details_table.column("First_checkup",width=150)
        self.room_details_table.column("Pregnant_status",width=150)
        self.room_details_table.column("Follow_up",width=150)
        self.room_details_table.column("Last_checkup_Status",width=150)
        self.room_details_table.column("Medical_Findings",width=150)
        self.room_details_table.column("Recommendation",width=150)
        self.room_details_table.column("Next_Checkup",width=150)
   
        
        self.room_details_table.pack(fill=BOTH,expand=1)
        self.room_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        
        #==add data===
    def add_data(self):
        if self.var_healthcard.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into pregnantd values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_healthcard.get(),
                                                                            self.var_Lmens.get(),
                                                                            self.var_fcheck.get(),
                                                                            self.var_Pstat.get(),
                                                                            self.var_followup.get(),
                                                                            self.var_lastcheckupstat.get(),
                                                                            self.var_medfindings.get(),
                                                                            self.var_reccommendation.get(),
                                                                            self.var_nextcheckup.get(),
                                                                            
                                                                            
                                                                        ))
                                                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Pregnant Medical Record Save",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Pregnant Has No Record:{str(es)}",parent=self.root)


        
        #=============room AVAILABILITY========
        

            #===fetch data=====
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pregnantd order by First_checkup asc")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #===get cursor data
    def get_cursor(self,events=""):
        cursor_rows=self.room_details_table.focus()
        content=self.room_details_table.item(cursor_rows)
        row=content["values"]

        self.var_healthcard.set(row[0])
        self.var_Lmens.set(row[1])
        self.var_fcheck.set(row[2])
        self.var_Pstat.set(row[3])
        self.var_followup.set(row[4])
        self.var_lastcheckupstat.set(row[5])
        self.var_medfindings.set(row[6])
        self.var_reccommendation.set(row[7])
        self.var_nextcheckup.set(row[8])

        #update===
    
    def update(self):
        if self.var_healthcard.get()=="":
            messagebox.showerror("Error","Please Enter HealthCard Number",parent=self.root)
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            my_cursor.execute("update pregnantd set Last_Menstruation=%s,First_checkup=%s,Pregnant_status=%s,Follow_up=%s,Last_Checkup_Status=%s,Medical_Findings=%s,Recommendation=%s,Next_Checkup=%s where Healthcard=%s",(

                                                                                                                    
                                                                                                                    self.var_Lmens.get(),
                                                                                                                    self.var_fcheck.get(),
                                                                                                                    self.var_Pstat.get(),
                                                                                                                    self.var_followup.get(),
                                                                                                                    self.var_lastcheckupstat.get(),
                                                                                                                    self.var_medfindings.get(),
                                                                                                                    self.var_reccommendation.get(),
                                                                                                                    self.var_nextcheckup.get(),
                                                                                                                    self.var_healthcard.get()
                                                                                                                   

                                                                                                                                                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Pregnant Medical Record has been updated successfully",parent=self.root)


            
   


    def reset(self):
        
        self.var_healthcard.set("")
        self.var_Lmens.set("")
        self.var_fcheck.set("")
        self.var_Pstat.set("")
        self.var_followup.set("")
        self.var_lastcheckupstat.set("")
        self.var_medfindings.set("")
        self.var_reccommendation.set("")
        self.var_nextcheckup.set("")
     
       

        






    
    def fetch_contact(self):
     
        if self.var_healthcard.get()=="":
            messagebox.showerror("Error","please Enter Healtcard Number",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  FamilyId from tblpatient where Healthcard_id =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            

            if row==None:
                messagebox.showerror("Error","This Patient Not Found",parent=self.root)
            else:
               
                conn.commit()
                conn.close()




                
                
                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=455,y=50,width=440,height=200)
                
                scrol_y=Scrollbar(showdataframe,orient=VERTICAL)
                self.txtarea=Text(showdataframe,yscrollcommand=scrol_y.set)
                scrol_y.pack(side=RIGHT,fill=Y)
                scrol_y.config(command=self.txtarea.yview)
                self.txtarea.pack(fill=BOTH,expand=1)


                #--FAMILY ID--
                
                result=row[0]
                self.txtarea.insert(END,f"Family ID: {result}")
                



                    #FNAME----
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  FName from tblpatient where Healthcard_id =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            result=row[0]
            self.txtarea.insert(END,f"\nFirst Name: {result}")
                

           
            #-----LNAME----

            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  LName from tblpatient where Healthcard_id =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            result=row[0]
            self.txtarea.insert(END,f"\nLast Name: {result}")

           
            
            #---LAST MENSTRUATION
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  Last_Menstruation from pregnantd where Healthcard =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            result=row[0]
            self.txtarea.insert(END,f"\nLast Menstruation: {result}")


           

            #---FIRST CHECKUP
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  First_checkup from pregnantd where Healthcard =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            result=row[0]
            self.txtarea.insert(END,f"\nLast Check-up: {result}")

            
           

            #---PREGNANT STATUS

            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  Pregnant_status from pregnantd where Healthcard =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            result=row[0]
            self.txtarea.insert(END,f"\nPregnant Status: {result}")
            
           


            #=====Followup====================

            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  Follow_up from pregnantd where Healthcard =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            result=row[0]
            self.txtarea.insert(END,f"\nFollow up: {result}")
            



           #======lastcheckup status========

            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  Last_Checkup_Status from pregnantd where Healthcard =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            result=row[0]
            self.txtarea.insert(END,f"\nLast Check-up: {result}")
            
            
            


            #=======Medical Findings====

            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  Medical_Findings from pregnantd where Healthcard =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            result=row[0]
            self.txtarea.insert(END,f"\nMedical Findings: {result}")
            
            
           

            #====Reccomendations====
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  Recommendation from pregnantd where Healthcard =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            result=row[0]
            self.txtarea.insert(END,f"\nReccomendations: {result}")
            
            
            #====nextcheckup=======

            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select  Next_checkup from pregnantd where Healthcard =%s")
            value=(self.var_healthcard.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            result=row[0]
            self.txtarea.insert(END,f"\nNext-Checkup: {result}")
            
           






           
            


                
    
            #====searh system==========

    def search_data(self):

        if self.txt_search.get()=="":
            messagebox.showerror("Error","Enter Healthcard Id or First Checkup Date",parent=self.root)

        else:

        
                  
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            my_cursor.execute('select * from pregnantd where ' +str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get()+"%'"))
            rows=my_cursor.fetchall()
            if len (rows)!=0:
                 self.room_details_table.delete(*self.room_details_table.get_children())
                 for i in rows:
                    self.room_details_table.insert("",END,values=i)
                    conn.commit()
                    conn.close()

            else:
                messagebox.showerror("Error","Health Card Not Found")

    def printb(self):
        q=self.txtarea.get('1.0','end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w', encoding='utf-8').write(q)
        os.startfile(filename,'Print')


   








if __name__=="__main__":
    root=Tk()
    obj=Pregnantdetails_window(root)
    root.mainloop()

