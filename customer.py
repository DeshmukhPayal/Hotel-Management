from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1370x460+160+330")

    #==========================variables===========================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()
        self.var_post=StringVar()

    #=========================title================================
        lbl_title=Label(self.root,text="Personal Details",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1370,height=50)

    #=========================label frame=============================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=410,height=407)

    #=========================labels and entries========================

        #Ref
        lbl_cust_ref=Label(labelframeleft,text="Reference No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13),state="readonly")
        entry_ref.grid(row=0,column=1)

        #name
        cname=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13))
        txtcname.grid(row=1,column=1)

        #age
        lblAge=Label(labelframeleft,text="Age",font=("arial",12,"bold"),padx=2,pady=6)
        lblAge.grid(row=2,column=0,sticky=W)

        txtAge=Entry(labelframeleft,textvariable=self.var_age,width=29,font=("arial",13))
        txtAge.grid(row=2,column=1)

        #gender
        label_gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.grid(row=3,column=1)

        

        #mobile
        lblMobile=Label(labelframeleft,text="Mobile No.",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=4,column=0,sticky=W)

        txtMobile=Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13))
        txtMobile.grid(row=4,column=1)

        #mail
        lblEmail=Label(labelframeleft,text="Email",font=("arial",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=5,column=0,sticky=W)

        txtEmail=Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",13))
        txtEmail.grid(row=5,column=1)

        #nationality
        lblnationality=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblnationality.grid(row=6,column=0,sticky=W)

        combo_nat=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,),width=27,state="readonly")
        combo_nat["value"]=("India","America","Other")
        combo_nat.grid(row=6,column=1)

        #id
        lblIdProof=Label(labelframeleft,text="ID Proof Type",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=7,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12),width=27,state="readonly")
        combo_id["value"]=("PAN","Aadhar","Passport","Driving Licence")
        combo_id.grid(row=7,column=1)

        #id no.
        lblIdNumber=Label(labelframeleft,text="ID number",font=("arial",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=8,column=0,sticky=W)

        txtIdNumber=Entry(labelframeleft,textvariable=self.var_idnumber,width=29,font=("arial",13))
        txtIdNumber.grid(row=8,column=1)

        #adress
        lblAddress=Label(labelframeleft,text="Address",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=9,column=0,sticky=W)

        txtAddress=Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13))
        txtAddress.grid(row=9,column=1)

        #postcode
        lblPostCode=Label(labelframeleft,text="PostCode",font=("arial",12,"bold"),padx=2,pady=6)
        lblPostCode.grid(row=10,column=0,sticky=W)

        txtPostCode=Entry(labelframeleft,textvariable=self.var_post,width=29,font=("arial",13))
        txtPostCode.grid(row=10,column=1)

        #=========================btn frame=================================
        btn_frame=Frame(self.root,bd=2,relief=RIDGE)
        btn_frame.place(x=415,y=57,width=75,height=405)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnAdd.place(x=0,y=15,width=72,height=40)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnUpdate.place(x=0,y=125,width=72,height=40)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnDelete.place(x=0,y=235,width=72,height=40)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnReset.place(x=0,y=345,width=72,height=40)
        
        #============================table frame=======================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Details and Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=495,y=50,width=870,height=407)


        lblSearchBy=Label(Table_Frame,text="Search By",font=("arial",12,),bg="black",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
        combo_search["value"]=("Mobile No.","Name","Reference No.")
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
        details_table.place(x=0,y=43,width=860,height=340)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","age","gender","mobile",
        "email","nationality","idproof","idnumber","address","post"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("age",text="Age")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="ID Proof")
        self.Cust_Details_Table.heading("idnumber",text="ID Number")
        self.Cust_Details_Table.heading("address",text="Address")
        self.Cust_Details_Table.heading("post",text="PostCode")
        
        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("age",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        self.Cust_Details_Table.column("post",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        


    def add_data(self):
        if (self.var_mobile.get()=="" or self.var_gender.get()=="" or self.var_ref.get()=="" or
           self.var_cust_name.get()=="" or self.var_email.get()=="" or self.var_nationality.get()=="" or
           self.var_idproof.get()=="" or self.var_idnumber.get()=="" or self.var_address.get()=="" or 
           self.var_post.get()=="" ):
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_ref.get(),
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_age.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_idproof.get(),
                                                                                        self.var_idnumber.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_post.get()
                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong:{str(es)}",parent=self.root)             



    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
        my_cursor=conn.cursor()     
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_age.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_nationality.set(row[6]),
        self.var_idproof.set(row[7]),
        self.var_idnumber.set(row[8]),
        self.var_address.set(row[9]),
        self.var_post.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
            my_cursor=conn.cursor()     
            my_cursor.execute("update customer set Name=%s,Age=%s,Gender=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s,PostCode=%s where Ref=%s",(       
                                                                                        self.var_cust_name.get(),
                                                                                        self.var_age.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_mobile.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_nationality.get(),
                                                                                        self.var_idproof.get(),
                                                                                        self.var_idnumber.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_post.get(),
                                                                                        self.var_ref.get()))
            conn.commit()

            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Data updated successfully",parent=self.root)

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you really want to delete",parent=self.root)
        if (mDelete>0):
            conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
            my_cursor=conn.cursor()     
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_age.set(""),
        self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set(""),
        self.var_idproof.set(""),
        self.var_idnumber.set(""),
        self.var_address.set(""),
        self.var_post.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()







if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop() 