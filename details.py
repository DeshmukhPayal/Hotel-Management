from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Room_details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1370x460+160+330")

    #=========================title================================
        lbl_title=Label(self.root,text="Room Booking Details",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1370,height=50)
        
    #=========================label frame=============================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Available Room Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        #floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=Entry(labelframeleft,width=24,textvariable=self.var_floor,font=("arial",13))
        entry_floor.grid(row=0,column=1)

        #room no
        lbl_room_no=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_room_no.grid(row=1,column=0,sticky=W)

        self.var_room_no=StringVar()
        entry_room_no=Entry(labelframeleft,width=24,textvariable=self.var_room_no,font=("arial",13))
        entry_room_no.grid(row=1,column=1,sticky=W)

        #room type
        lbl_room_type=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_room_type.grid(row=2,column=0,sticky=W)

        self.var_room_type=StringVar()
        entry_room_type=Entry(labelframeleft,width=24,textvariable=self.var_room_type,font=("arial",13))
        entry_room_type.grid(row=2,column=1,sticky=W)

     #=========================btn frame=================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=200,width=300,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnUpdate.grid(row=0,column=2,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnDelete.grid(row=0,column=4,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="white",width=7,cursor="hand2")
        btnReset.grid(row=0,column=6,padx=1)
    #=========================table frame=============================
        tabelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details",font=("times new roman",12,"bold"),padx=2)
        tabelframeleft.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(tabelframeleft,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabelframeleft,orient=VERTICAL)

        self.Room_Table=ttk.Treeview(tabelframeleft,column=("floor","room_no","room_type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("floor",text="Floor")
        self.Room_Table.heading("room_no",text="Room No")
        self.Room_Table.heading("room_type",text="Room Type")
        
        self.Room_Table["show"]="headings"

        self.Room_Table.column("floor",width=100)
        self.Room_Table.column("room_no",width=100)
        self.Room_Table.column("room_type",width=100)

        self.Room_Table.pack(fill=BOTH,expand=1)
        self.Room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #=================================================================================
    def add_data(self):
        if (self.var_floor.get()=="" or self.var_room_type.get()=="" or self.var_room_no.get()==""):
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                        self.var_floor.get(),
                                                                                        self.var_room_no.get(),
                                                                                        self.var_room_type.get()                                                                                        
                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Success",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong:{str(es)}",parent=self.root) 

    #================================fetch data=====================================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
        my_cursor=conn.cursor()     
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_room_no.set(row[1]),
        self.var_room_type.set(row[2])

    #====================================update====================================
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter Floor",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Payal@14",database="management")
            my_cursor=conn.cursor()     
            my_cursor.execute("update details set Floor=%s,Room_Type=%s,Room_No=%s",(       
                                                                                        self.var_floor.get(),
                                                                                        self.var_room_type.get(),
                                                                                        self.var_room_no.get(),                                                                                        
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
            query="delete from details where Room_No=%s"
            value=(self.var_room_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set(""),
        self.var_room_no.set(""),
        self.var_room_type.set("")
        


if __name__ == "__main__":
    root=Tk()
    obj=Room_details(root)
    root.mainloop() 