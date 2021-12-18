from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Room_booking
from details import Room_details


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #==================================img1======================================
        img1=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\hotel.JPG")
        img1=img1.resize((1550,300),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=300)

        #=================================title=====================================
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #==============================main frame==================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=300,width=1550,height=500)

        #==========================================================================
        img=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\img3.JPG")
        img=img.resize((1365,485),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lblimg=Label(main_frame,image=self.photoimg,bd=4,relief=RIDGE)
        lblimg.place(x=160,y=0,width=1365,height=485)

        #==================================menu====================================
        lbl_title=Label(main_frame,text="MENU",font=("times new roman",15),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=155)

        #==============================btn frame==================================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=155,height=450)

        #=========================================================================
        img2=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\info6.JPG")
        img2=img2.resize((145,75),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(btn_frame,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=145,height=75)

        cust_btn=Button(btn_frame,text="Info",command=self.cust_details,width=25,font=("times new roman",15),bd=4,relief=RIDGE,cursor="hand2")
        cust_btn.place(x=0,y=75,width=145,height=25)

        #=========================================================================
        img3=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\booking2.JPG")
        img3=img3.resize((145,75),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(btn_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=110,width=145,height=75)

        book_btn=Button(btn_frame,text="Booking",command=self.room_booking,width=25,font=("times new roman",15),bd=4,relief=RIDGE,cursor="hand2")
        book_btn.place(x=0,y=185,width=145,height=25)

        #===========================================================================
        img4=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\details1.JPG")
        img4=img4.resize((145,75),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(btn_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=220,width=145,height=75)

        detail_btn=Button(btn_frame,text="Details",command=self.details_room,width=25,font=("times new roman",15),bd=4,relief=RIDGE,cursor="hand2")
        detail_btn.place(x=0,y=305,width=145,height=25)

        #=========================================================================
        img5=Image.open(r"C:\Users\mrunal\Desktop\hotel management\images\info.JPG")
        img5=img5.resize((145,75),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg=Label(btn_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=340,width=145,height=75)

        logout_btn=Button(btn_frame,text="LogOut",command=self.logout,width=25,font=("times new roman",15),bd=4,relief=RIDGE,cursor="hand2")
        logout_btn.place(x=0,y=415,width=145,height=25)
        





    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=Room_booking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=Room_details(self.new_window)


    def logout(self):
        self.root.destroy()












if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop() 
















    