from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Room_booking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1370x460+160+330")

        #=========================variable============================
        self.var_contact=StringVar()
        self.var_check_in=StringVar()
        self.var_check_out=StringVar()
        self.var_room_type=StringVar()
        self.var_available_room=StringVar()
        self.var_meal=StringVar()
        self.var_no_of_days=StringVar()
        self.var_paid_tax=StringVar()
        self.var_sub_total=StringVar()
        self.var_total_cost=StringVar()

        
        #=========================title================================
        lbl_title=Label(self.root,text="Room Booking Details",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1370,height=50)
        
        #=========================label frame=============================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Booking Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=410,height=407)

        #Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,)

        entry_contact=Entry(labelframeleft,width=24,textvariable=self.var_contact,font=("arial",13))
        entry_contact.grid(row=0,column=1,sticky=W)

        

        #Check_in date
        check_in_date=Label(labelframeleft,text="Check_in Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=Entry(labelframeleft,width=24,textvariable=self.var_check_in,font=("arial",13))
        txtcheck_in_date.grid(row=1,column=1)

        #check_out
        lbl_check_out=Label(labelframeleft,text="Check_out Date",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)

        txt_check_out=Entry(labelframeleft,width=24,textvariable=self.var_check_out,font=("arial",13))
        txt_check_out.grid(row=2,column=1)

        #Room_Type
        label_Room_Type=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        label_Room_Type.grid(row=3,column=0,sticky=W)

        combo_Room_Type=ttk.Combobox(labelframeleft,textvariable=self.var_room_type,font=("arial",12,),width=22,state="readonly")
        combo_Room_Type["value"]=("Single","Double","Luxury")
        combo_Room_Type.grid(row=3,column=1)

        #Available_room
        lblAvailable_room=Label(labelframeleft,text="Available Room.",font=("arial",12,"bold"),padx=2,pady=6)
        lblAvailable_room.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
        my_cursor=conn.cursor()     
        my_cursor.execute("select Room_No from details")
        rows=my_cursor.fetchall()

        combo_Room_No=ttk.Combobox(labelframeleft,textvariable=self.var_available_room,font=("arial",12,),width=22,state="readonly")
        combo_Room_No["value"]=rows
        combo_Room_No.grid(row=4,column=1)

        
        #Meal
        lblMeal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        txtMeal=Entry(labelframeleft,width=24,textvariable=self.var_meal,font=("arial",13))
        txtMeal.grid(row=5,column=1)

        #No_of_Days
        lblNo_of_Days=Label(labelframeleft,text="No of Days",font=("arial",12,"bold"),padx=2,pady=6)
        lblNo_of_Days.grid(row=6,column=0,sticky=W)

        txtNo_of_Days=Entry(labelframeleft,width=24,textvariable=self.var_no_of_days,font=("arial",13))
        txtNo_of_Days.grid(row=6,column=1)
        
        #Paid_tax
        lblPaid_tax=Label(labelframeleft,text="Paid Tax",font=("arial",12,"bold"),padx=2,pady=6)
        lblPaid_tax.grid(row=7,column=0,sticky=W)
        
        txtPaid_tax=Entry(labelframeleft,width=24,textvariable=self.var_paid_tax,font=("arial",13))
        txtPaid_tax.grid(row=7,column=1)
        
        
        #Sub_total
        lblSub_total=Label(labelframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        lblSub_total.grid(row=8,column=0,sticky=W)

        txtSub_total=Entry(labelframeleft,width=24,textvariable=self.var_sub_total,font=("arial",13))
        txtSub_total.grid(row=8,column=1)

        #Total_cost
        lblTotal_cost=Label(labelframeleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
        lblTotal_cost.grid(row=9,column=0,sticky=W)

        txtTotal_cost=Entry(labelframeleft,width=24,textvariable=self.var_total_cost,font=("arial",13))
        txtTotal_cost.grid(row=9,column=1)

        #=========================bill button==============================
        btnBill=Button(labelframeleft,text="BILL",command=self.total,font=("arial",11,"bold"),bg="black",fg="white",width=10,cursor="hand2")
        btnBill.grid(row=10,column=0,sticky=W)

        #=========================btn frame=================================
        btn_frame=Frame(self.root,bd=2,relief=RIDGE)
        btn_frame.place(x=415,y=57,width=75,height=405)

        btnFetchData=Button(btn_frame,command=self.Fetch_contact,text="Fetch",font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnFetchData.place(x=0,y=20,width=72,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnAdd.place(x=0,y=100,width=72,height=40)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnUpdate.place(x=0,y=180,width=72,height=40)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnDelete.place(x=0,y=260,width=72,height=40)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnReset.place(x=0,y=340,width=72,height=40)

        #=============================img=============================
        img5=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\room 3.JPG")
        img5=img5.resize((465,200),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(self.root,image=self.photoimg5,bd=0,relief=RIDGE)
        lblimg.place(x=900,y=50,width=465,height=200)

        #============================table frame=======================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Details and Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=495,y=220,width=870,height=407)


        lblSearchBy=Label(Table_Frame,text="Search By",font=("arial",12,),bg="black",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.grid(row=0,column=1)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=29,font=("arial",13))
        txtSearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnsearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnShowAll.grid(row=0,column=4,padx=1)

        #========================data table===================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=43,width=860,height=170)
        

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Room_Table=ttk.Treeview(details_table,column=("contact","check_in","check_out","room_type","available_room",
        "meal","no_of_days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)
        
        self.Room_Table.heading("contact",text="Contact")
        self.Room_Table.heading("check_in",text="Check-in")
        self.Room_Table.heading("check_out",text="Check-out")
        self.Room_Table.heading("room_type",text="Room Type")
        self.Room_Table.heading("available_room",text="Available Room")
        self.Room_Table.heading("meal",text="Meal")
        self.Room_Table.heading("no_of_days",text="No of Days")
       
        
        self.Room_Table["show"]="headings"

        self.Room_Table.column("contact",width=100)
        self.Room_Table.column("check_in",width=100)
        self.Room_Table.column("check_out",width=100)
        self.Room_Table.column("room_type",width=100)
        self.Room_Table.column("available_room",width=100)
        self.Room_Table.column("meal",width=100)
        self.Room_Table.column("no_of_days",width=100)
        self.Room_Table.pack(fill=BOTH,expand=1)

        self.Room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #=================================================================================
    def add_data(self):
        if (self.var_contact.get()=="" or self.var_check_in.get()=="" or self.var_check_out.get()=="" or
           self.var_room_type.get()=="" or self.var_available_room.get()=="" or self.var_meal.get()==""):
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_contact.get(),
                                                                                        self.var_check_in.get(),
                                                                                        self.var_check_out.get(),
                                                                                        self.var_room_type.get(),
                                                                                        self.var_available_room.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_no_of_days.get()
                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong:{str(es)}",parent=self.root) 
   
   #================================fetch data=====================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
        my_cursor=conn.cursor()     
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #===============================cursor============================================
    def get_cursor(self,event=""):
        cursor_row=self.Room_Table.focus()
        content=self.Room_Table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_check_in.set(row[1]),
        self.var_check_out.set(row[2]),
        self.var_room_type.set(row[3]),
        self.var_available_room.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_no_of_days.set(row[6])
        self.var_paid_tax.set(""),
        self.var_sub_total.set(""),
        self.var_total_cost.set("")
        

    #====================================update====================================
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
            my_cursor=conn.cursor()     
            my_cursor.execute("update room set Check_in=%s,Check_out=%s,Room_Type=%s,Available_Room=%s,Meal=%s,No_of_Days=%s where Contact=%s",(       
                                                                                        self.var_check_in.get(),
                                                                                        self.var_check_out.get(),
                                                                                        self.var_room_type.get(),
                                                                                        self.var_available_room.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_no_of_days.get(),
                                                                                        self.var_contact.get(),
                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you really want to delete",parent=self.root)
        if (mDelete>0):
            conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
            my_cursor=conn.cursor()     
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_check_in.set(""),
        self.var_check_out.set(""),
        self.var_room_type.set(""),
        self.var_available_room.set(""),
        self.var_meal.set(""),
        self.var_no_of_days.set("")
        
    #====================================All data===================================
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact details",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=500,y=55,width=350,height=165)

        #=====================================Name==========================================
                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

        #===================================Gender========================================
                conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblName.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

        #===================================Email========================================
                conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblName.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)
        
        #===================================Nationality========================================
                conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblName.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=90)

        #===================================Address========================================
                conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblName.place(x=0,y=120)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=120)

        #====================================search======================================
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def total(self):
        inDate=self.var_check_in.get()
        outDate=self.var_check_out.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_no_of_days.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="breakfast" and self.var_room_type.get()=="Single"):
            q1=float(200)
            q2=float(1000)
            q3=float(self.var_no_of_days.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%(q5))
            Total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_sub_total.set(ST)
            self.var_total_cost.set(Total)
        if(self.var_meal.get()=="lunch" and self.var_room_type.get()=="Single"):
            q1=float(700)
            q2=float(1000)
            q3=float(self.var_no_of_days.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%(q5))
            Total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_sub_total.set(ST)
            self.var_total_cost.set(Total)
        if(self.var_meal.get()=="dinner" and self.var_room_type.get()=="Single"):
            q1=float(200)
            q2=float(1000)
            q3=float(self.var_no_of_days.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%(q5))
            Total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_sub_total.set(ST)
            self.var_total_cost.set(Total)
        if(self.var_meal.get()=="breakfast" and self.var_room_type.get()=="Double"):
            q1=float(200)
            q2=float(2000)
            q3=float(self.var_no_of_days.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%(q5))
            Total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_sub_total.set(ST)
            self.var_total_cost.set(Total)
        if(self.var_meal.get()=="lunch" and self.var_room_type.get()=="Double"):
            q1=float(700)
            q2=float(2000)
            q3=float(self.var_no_of_days.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%(q5))
            Total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_sub_total.set(ST)
            self.var_total_cost.set(Total)
        if(self.var_meal.get()=="dinner" and self.var_room_type.get()=="Double"):
            q1=float(800)
            q2=float(2000)
            q3=float(self.var_no_of_days.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%(q5))
            Total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_sub_total.set(ST)
            self.var_total_cost.set(Total)
        if(self.var_meal.get()=="breakfast" and self.var_room_type.get()=="Luxury"):
            q1=float(200)
            q2=float(3500)
            q3=float(self.var_no_of_days.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%(q5))
            Total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_sub_total.set(ST)
            self.var_total_cost.set(Total)
        if(self.var_meal.get()=="lunch" and self.var_room_type.get()=="Luxury"):
            q1=float(700)
            q2=float(3500)
            q3=float(self.var_no_of_days.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%(q5))
            Total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_sub_total.set(ST)
            self.var_total_cost.set(Total)
        elif(self.var_meal.get()=="dinner" and self.var_room_type.get()=="Luxury"):
            q1=float(800)
            q2=float(3500)
            q3=float(self.var_no_of_days.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%(q5))
            Total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_sub_total.set(ST)
            self.var_total_cost.set(Total)

              


if __name__ == "__main__":
    root=Tk()
    obj=Room_booking(root)
    root.mainloop() 

