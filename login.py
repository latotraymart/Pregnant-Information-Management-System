

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from Record import  RecordManagementSystem
import random
import time
import datetime


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        pass
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        
        




        self.bg=ImageTk.PhotoImage(file=r"C:\Users\LATOT\Desktop\Pregnant System\images\buntis3.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


       

        
        


    
        frame=Frame(self.root,bg="#9ccd1a",borderwidth=4,relief="groove")
        frame.place(x=800,y=170,width=500,height=500)

        img1=Image.open(r"C:\Users\LATOT\Desktop\Pregnant System\images\bernabelogo1.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.PhotoImage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.PhotoImage1,bg="#9ccd1a",borderwidth=0)
        lblimg1.place(x=1000,y=185,width=100,height=100)

        get_str=Label(frame,text="Admin Login",font=("times new roman",20,"bold"),fg="white",bg="#9ccd1a")
        get_str.place(x=160,y=100)


        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="#9ccd1a")
        username.place(x=125,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=100,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="#9ccd1a")
        password.place(x=125,y=225)

        self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.txtpass.place(x=100,y=250,width=270)

        #icon image===============

        img2=Image.open(r"C:\login_system\images\login2.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.PhotoImage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.PhotoImage2,bg="#9ccd1a",borderwidth=0)
        lblimg1.place(x=900,y=323,width=25,height=25)

        img3=Image.open(r"C:\login_system\images\lock-icon-transparent-background-10.jpg")
        img3=img3.resize((30,30),Image.ANTIALIAS)
        self.PhotoImage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.PhotoImage3,bg="#9ccd1a",borderwidth=0)
        lblimg1.place(x=900,y=395,width=25,height=25)

        #LOGIN BUTTON==
        loginbtn=Button(frame,text="Login",command=self.login_user,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#9ccd1a",activeforeground="white",activebackground="#007bff")
        loginbtn.place(x=100,y=300,width=120,height=35)
         #signout BUTTON==
        signbtn=Button(frame,text="SignOut",command=self.sign_out,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#9ccd1a",activeforeground="white",activebackground="#007bff")
        signbtn.place(x=250,y=300,width=120,height=35)

        #REGISTER BUTTON====
        #registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="#007bff")
        #registerbtn.place(x=15,y=350,width=160)

        #forget pass button==
        forgetpassbtn=Button(frame,command=self.forgot_password_window,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="#9ccd1a",activeforeground="white",activebackground="#007bff")
        forgetpassbtn.place(x=70,y=370,width=160)

            

        
       



            #=============user login===============

       


    def rigister_window(self):
        if  self.txtpass.get()=="":
            messagebox.showerror("Error","Enter Admin password")
         
        elif  self.txtpass.get()!="admin1":
              messagebox.showerror("Error","Invalid Admin password")
                 
          

        else:
            messagebox.askyesno("YesNo","Create New User Account?")
            self.new_window=Toplevel(self.root)
            self.app=Register(self.new_window)
        


    
   


    def login_user(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields are Required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome Record Management system")
           
        
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                                          ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")

        

            else:
                open_main=messagebox.askyesno("YesNo","Access by Admin")
               
                if open_main>0:
                  
                    self.new_window=Toplevel(self.root)
                    self.app=RecordManagementSystem(self.new_window)
                
                   
                    
                  

                    

                else:
                    if not open_main:
                       
                        return
            conn.commit()
            conn.close()
            
            

        #===================reset password window================
    def reset_pass(self):
        if self.combo_securityQ.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            valeeu=(self.txtuser.get(),self.combo_securityQ.get(),self.txt_security.get(),)
            my_cursor.execute(qury,valeeu)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please Login New password",parent=self.root2)
                self.root2.destroy()




         #=======================forget password window=========   
    
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please Enter the valid username")

            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("500x450+800+200")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="#007bff",bg="white")
                l.place(x=10,y=0,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=130,y=80)

                self.combo_securityQ=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_securityQ["values"]=("select","Your Birth Place","Your Girlfriend name","Your Pet name")
                self.combo_securityQ.place(x=130,y=110,width=250)
                self.combo_securityQ.current(0)

                security_A=Label(self.root2,text=" Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=130,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=130,y=180,width=250)

                newpassword=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                newpassword.place(x=130,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=130,y=250,width=250)

                btnresetpass=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green")
                btnresetpass.place(x=230,y=290)

    def sign_out(self):
        self.root.destroy()




class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

#===============variables=========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        







        #bg image=============
        
        self.bg=ImageTk.PhotoImage(file=r"C:\login_system\images\trr1.jpg")
        bg_label=Label(self.root,image=self.bg)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        #left image

        self.bg1=ImageTk.PhotoImage(file=r"C:\login_system\images\relax.jpg")
        left_label=Label(self.root,image=self.bg1)
        left_label.place(x=170,y=150,width=600,height=500)

        #===Main frame==

        frame=Frame(self.root,bg="white")
        frame.place(x=700,y=150,width=600,height=500)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="#007bff",bg="white")
        register_lbl.place(x=20,y=20)
        
        #====label and entry=======

        #row1==========
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=340,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname ,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=340,y=130,width=250)

        # row 2======

        contact=Label(frame,text="Contact",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=340,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=340,y=200,width=250)

        # row 3===========
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_securityQ=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_securityQ["values"]=("select","Your Birth Place","Your Girlfriend name","Your Pet name")
        self.combo_securityQ.place(x=50,y=270,width=250)
        self.combo_securityQ.current(0)

        security_A=Label(frame,text=" Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=340,y=240,width=250)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=340,y=270,width=250)

        #row 4=======

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_passw=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_passw.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=340,y=310)

        self.txt_confirmpassw=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirmpassw.place(x=340,y=340,width=250)

        #==========check button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #=============buttons=============
        img=Image.open(r"C:\login_system\images\rg.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"C:\login_system\images\logb.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=330,y=420,width=200)

#=============function declaration==========
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")

        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")

            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_fname.get(),
                                                                                self.var_lname.get(),
                                                                                self.var_contact.get(),
                                                                                self.var_email.get(),
                                                                                self.var_securityQ.get(),
                                                                                self.var_securityA.get(),
                                                                                self.var_pass.get()
                                                                                       ))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Register Succesfully")
    
    
    def return_login(self):
        self.root.destroy()

   



    
     
if __name__== "__main__":
    main()
    