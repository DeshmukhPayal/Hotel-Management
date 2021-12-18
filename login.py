from hotel import HotelManagementSystem
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

def main():
    win=Tk()
    obj=Login_System(win)
    
    win.mainloop()

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        #----------------------------------------------------------------------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #==================================img1======================================
        img0=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\login.JPG")
        img0=img0.resize((1550,800),Image.ANTIALIAS)
        self.photoimg0=ImageTk.PhotoImage(img0)

        lblimg=Label(self.root,image=self.photoimg0)
        lblimg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\login5.JPG")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #===========================labels===========================
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        img2=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\login5.JPG")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)


        img3=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\pass.JPG")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=395,width=25,height=25)

    #=================================btns==============================
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn=Button(frame,text="New User Register",command=self.register_win,font=("calibri",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=20,y=350,width=160)

        pwbtn=Button(frame,text="Forgot Password ",command=self.forgot_password,font=("calibri",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        pwbtn.place(x=15,y=375,width=160)

    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.obj=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields are required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Logged in successfully")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                self.var_email.get(),
                                                                self.var_pass.get()
            ))
            row=my_cursor.fetchall()
            if row==None:
                messagebox.showerror("Error","Invalid Username or password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.obj=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #===================================reset pass func======================================
    def reset_pass(self):
        if self.txt_combo_security_Q.get()=="select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security_A_entry.get()=="":
            messagebox.showerror("Error","Enter Answer",parent=self.root2)
        if self.txt_new_password_entry.get()=="":
            messagebox.showerror("Error","Enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.txt_combo_security_Q.get(),self.txt_security_A_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password reset successfully",parent=self.root2)
                self.root2.destroy()


    #===================================forgot password=======================================
    def forgot_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Enter valid username to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Reset Password",font=("times new roman",20,"bold"),fg="white",bg="black")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                self.txt_combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15),state="readonly")
                self.txt_combo_security_Q["value"]=("Select","Birth Place","Pet name","Favourite colour")
                self.txt_combo_security_Q.place(x=50,y=110,width=250)
                self.txt_combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
                security_A.place(x=50,y=150)

                self.txt_security_A_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security_A_entry.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_new_password_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_new_password_entry.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="white")
                btn.place(x=120,y=280)




            

#===========================================================================================================================================
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

    #==================================variables===========================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
   
   
    #============================images=====================================
        img1=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\register1.JPG")
        img1=img1.resize((1550,800),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(self.root,image=self.photoimg1)
        lblimg1.place(x=0,y=0,relwidth=1,relheight=1)

    #===============================frame==================================
        frame=Frame(self.root,bg="white")
        frame.place(x=400,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",20,"bold"),fg="brown",bg="white")
        register_lbl.place(x=20,y=20)

    #==============================label==================================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250,)

        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.txt_lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname_entry.place(x=370,y=130,width=250)
#------------------------------------------------------------------------------------------------------------
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact_entry.place(x=50,y=200,width=250,)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email_entry.place(x=370,y=200,width=250)
#---------------------------------------------------------------------------------------------------------------
        security_Q=Label(frame,text="Security Question",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.txt_combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15),state="readonly")
        self.txt_combo_security_Q["value"]=("Select","Birth Place","Pet name","Favourite colour")
        self.txt_combo_security_Q.place(x=50,y=270,width=250)
        self.txt_combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.txt_security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.txt_security_A_entry.place(x=370,y=270,width=250)
#----------------------------------------------------------------------------------------------------------------
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd_entry.place(x=50,y=340,width=250,)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd_entry.place(x=370,y=340,width=250)

    #===================================check btn=================================================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Confirm",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=390)

    #===================================buttons==================================================

        img2=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\register 1.PNG")
        img2=img2.resize((100,50),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(frame,image=self.photoimg2,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=10,y=420,width=300)

        img3=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\login 1.JPG")
        img3=img3.resize((100,50),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b2=Button(frame,image=self.photoimg3, command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
        b2.place(x=330,y=420,width=300)

    #====================================functions===========================
    def register_data(self):
        if (self.var_fname.get()=="" or self.var_email.get()=="" or self.txt_combo_security_Q.get()=="Select"):
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Please confirm your password")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","You need to check 'I Confirm' ")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            rows=my_cursor.fetchone()
            if rows!=None:
                messagebox.showerror("Error","User already exists")
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
                messagebox.showinfo("Success","You are successfully registered",parent=self.root)

    def return_login(self):
        self.destroy()

if __name__ == "__main__":
    main() 