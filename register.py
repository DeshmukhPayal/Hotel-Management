from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="Confirm",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
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

        b2=Button(frame,image=self.photoimg3,borderwidth=0,cursor="hand2",bg="white")
        b2.place(x=330,y=420,width=300)

    #====================================functions===========================
    def register_data(self):
        if (self.var_fname.get()=="" or self.var_email.get()=="" or self.txt_combo_security_Q.get()=="Select"):
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Please confirm your password")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","You need to check 'Confirm' ")
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
            

        


if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop() 