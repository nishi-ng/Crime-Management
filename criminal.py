from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector



class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        #variables
        self.var_CaseId=StringVar()
        self.var_CriminalNo=StringVar()
        self.var_Name=StringVar()
        self.var_Nickname=StringVar()
        self.var_ArrestDate=StringVar()
        self.var_DateOfCrime=StringVar()
        self.var_Address=StringVar()
        self.var_Age=StringVar()
        self.var_Occupation=StringVar()
        self.var_BirthMark=StringVar()
        self.var_CrimeType=StringVar()
        self.var_FathersName=StringVar()
        self.var_Gender=StringVar()
        self.var_Wanted=StringVar()


        lbl_title=Label(self.root,text="CRIMINAL MANAGEMENT SYSTEM SOFTWARE",font=('times new roman',30,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1355,height=60)

        #HEAD LOGO
        img_logo=Image.open('images/logo.png') 
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=140,y=5,width=50,height=50)

        #Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        img_frame.place(x=0,y=60,width=1355,height=150)

        #Image 1
        img_1=Image.open('images/p7.jpg') 
        img_1=img_1.resize((450,150),Image.ANTIALIAS)
        self.photo_1=ImageTk.PhotoImage(img_1)

        self.img_1=Label(img_frame,image=self.photo_1)
        self.img_1.place(x=0,y=0,width=450,height=150)
        
        #Image 2
        img_2=Image.open('images/police5.jpg') 
        img_2=img_2.resize((450,150),Image.ANTIALIAS)
        self.photo_2=ImageTk.PhotoImage(img_2)

        self.img_2=Label(img_frame,image=self.photo_2)
        self.img_2.place(x=452,y=0,width=450,height=150)

        #image 3
        img_3=Image.open('images/police6.jpg') 
        img_3=img_3.resize((450,150),Image.ANTIALIAS)
        self.photo_3=ImageTk.PhotoImage(img_3)

        self.img_3=Label(img_frame,image=self.photo_3)
        self.img_3.place(x=904,y=0,width=450,height=150)

        #main frame
        Main_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Main_Frame.place(x=3,y=215,width=1352,height=480)

        #upper frame
        upper_Frame=LabelFrame(Main_Frame,bd=2,relief=RIDGE,bg="white",text="CRIMINAL INFORMATION",font=('times new roman',11,'bold'),fg='red')
        upper_Frame.place(x=4,y=2,width=1339,height=240)

        #LABELS
        #CASE ID
        case_id=Label(upper_Frame,text='Case ID:',font=('arial',10,'bold'),bg='white')
        case_id.grid(row=0,column=0,padx=2,sticky=W)
        case_entry=ttk.Entry(upper_Frame,textvariable=self.var_CaseId,width=22,font=('arial',10,'bold'))
        case_entry.grid(row=0,column=1,padx=2,sticky=W)

        #Criminal No
        criminal_no=Label(upper_Frame,text='Criminal No.:',font=('arial',10,'bold'),bg='white')
        criminal_no.grid(row=0,column=2,padx=2,pady=5,sticky=W)
        txt_crimianl_no=ttk.Entry(upper_Frame,textvariable=self.var_CriminalNo,width=22,font=('arial',10,'bold'))
        txt_crimianl_no.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #CRIMINAL name
        criminal_name=Label(upper_Frame,text='Criminal Name:',font=('arial',10,'bold'),bg='white')
        criminal_name.grid(row=1,column=0,padx=2,sticky=W,pady=5)
        txt_criminal_name=ttk.Entry(upper_Frame,textvariable=self.var_Name,width=22,font=('arial',10,'bold'))
        txt_criminal_name.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #NICKNAME
        nick_name=Label(upper_Frame,text='NickName:',font=('arial',10,'bold'),bg='white')
        nick_name.grid(row=1,column=2,padx=2,sticky=W,pady=5)
        txt_nick_name=ttk.Entry(upper_Frame,textvariable=self.var_Nickname,width=22,font=('arial',10,'bold'))
        txt_nick_name.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #Arrest Date
        Arrest_Date=Label(upper_Frame,text='Arrest Date:',font=('arial',10,'bold'),bg='white')
        Arrest_Date.grid(row=2,column=0,padx=2,sticky=W,pady=5)
        txt_Arrest_Date=ttk.Entry(upper_Frame,textvariable=self.var_ArrestDate,width=22,font=('arial',10,'bold'))
        txt_Arrest_Date.grid(row=2,column=1,padx=2,pady=5,sticky=W)
        
        #Date Of Crime
        Date_Of_Crime=Label(upper_Frame,text='Date Of Crime:',font=('arial',10,'bold'),bg='white')
        Date_Of_Crime.grid(row=2,column=2,padx=2,sticky=W,pady=5)
        txt_Date_Of_Crime=ttk.Entry(upper_Frame,textvariable=self.var_DateOfCrime,width=22,font=('arial',10,'bold'))
        txt_Date_Of_Crime.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        #ADDRESS
        Address=Label(upper_Frame,text='Address:',font=('arial',10,'bold'),bg='white')
        Address.grid(row=3,column=0,padx=2,sticky=W,pady=5)
        txt_Address=ttk.Entry(upper_Frame,textvariable=self.var_Address,width=22,font=('arial',10,'bold'))
        txt_Address.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        #AGE
        Age=Label(upper_Frame,text='Age:',font=('arial',10,'bold'),bg='white')
        Age.grid(row=3,column=2,padx=2,sticky=W,pady=5)
        txt_Age=ttk.Entry(upper_Frame,textvariable=self.var_Age,width=22,font=('arial',10,'bold'))
        txt_Age.grid(row=3,column=3,padx=2,pady=5,sticky=W)

        #OCCUPATION
        Occupation=Label(upper_Frame,text='Occupation:',font=('arial',10,'bold'),bg='white')
        Occupation.grid(row=4,column=0,padx=2,sticky=W,pady=5)
        txt_Occupation=ttk.Entry(upper_Frame,textvariable=self.var_Occupation,width=22,font=('arial',10,'bold'))
        txt_Occupation.grid(row=4,column=1,padx=2,pady=5,sticky=W)

        #Birth_Mark
        Birth_Mark=Label(upper_Frame,text='Birth Mark:',font=('arial',10,'bold'),bg='white')
        Birth_Mark.grid(row=4,column=2,padx=2,sticky=W,pady=5)
        txt_Birth_Mark=ttk.Entry(upper_Frame,textvariable=self.var_BirthMark,width=22,font=('arial',10,'bold'))
        txt_Birth_Mark.grid(row=4,column=3,padx=2,pady=5,sticky=W)

        #Crime Type
        Crime_type=Label(upper_Frame,text='Crime Type:',font=('arial',10,'bold'),bg='white')
        Crime_type.grid(row=0,column=4,padx=2,sticky=W,pady=5)
        txt_Crime_type=ttk.Entry(upper_Frame,textvariable=self.var_CrimeType,width=22,font=('arial',10,'bold'))
        txt_Crime_type.grid(row=0,column=5,padx=2,pady=5,sticky=W)

        #Father Name
        Fathers_Name=Label(upper_Frame,text='Father\'s Name:',font=('arial',10,'bold'),bg='white')
        Fathers_Name.grid(row=1,column=4,padx=2,sticky=W,pady=5)
        txt_Father_Name=ttk.Entry(upper_Frame,textvariable=self.var_FathersName,width=22,font=('arial',10,'bold'))
        txt_Father_Name.grid(row=1,column=5,padx=2,pady=5,sticky=W)

        #Gender
        Gender=Label(upper_Frame,text='Gender:',font=('arial',10,'bold'),bg='white')
        Gender.grid(row=2,column=4,padx=2,sticky=W,pady=5)
        
        #radio button gender
        radio_frame_gender=Frame(upper_Frame,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=630,y=70,width=165,height=25)

        male=Radiobutton(radio_frame_gender,text="Male",variable=self.var_Gender,value='male',font=('arial',9,'bold'),bg='white')
        male.grid(row=0,column=0,padx=4,pady=0,sticky=W)

        Female=Radiobutton(radio_frame_gender,variable=self.var_Gender,text="Female",value='Female',font=('arial',9,'bold'),bg='white')
        Female.grid(row=0,column=1,padx=4,pady=0,sticky=W)

        #Wanted
        Most_Wanted=Label(upper_Frame,text='Most Wanted:',font=('arial',10,'bold'),bg='white')
        Most_Wanted.grid(row=3,column=4,padx=2,sticky=W,pady=5)
        
        #radio button wanted
        radio_frame_wanted=Frame(upper_Frame,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=630,y=100,width=165,height=20)

        Yes=Radiobutton(radio_frame_wanted,variable=self.var_Wanted,text="Yes",value='Yes',font=('arial',9,'bold'),bg='white')
        Yes.grid(row=0,column=0,padx=4,pady=0,sticky=W)

        No=Radiobutton(radio_frame_wanted,variable=self.var_Wanted,text="No",value='No',font=('arial',9,'bold'),bg='white')
        No.grid(row=0,column=1,padx=4,pady=0,sticky=W)

        #buttons
        Buttons_frame=Frame(upper_Frame,relief=RIDGE,bg='white',bd=2)
        Buttons_frame.place(x=4,y=165,width=630,height=45)

        #Add_Button
        btn_add=Button(Buttons_frame,text='Record Save',command=self.add_data,font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        #Update_Button
        btn_update=Button(Buttons_frame,text='Record Update',command=self.Update,font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete_Button
        btn_delete=Button(Buttons_frame,command=self.Delete_Data,text='Record Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear_Button
        btn_clear=Button(Buttons_frame,command=self.Clear_Data,text='Record Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        #background right image
        img_crime=Image.open('images/police1.jpg') 
        img_crime=img_crime.resize((445,210),Image.ANTIALIAS)
        self.photo_crime=ImageTk.PhotoImage(img_crime)

        self.img_crime=Label(upper_Frame,image=self.photo_crime)
        self.img_crime.place(x=880,y=1,width=445,height=210)


        #lower frame
        lower_Frame=LabelFrame(Main_Frame,bd=2,relief=RIDGE,bg="white",text="CRIMINAL INFORMATION TABLE",font=('times new roman',11,'bold'),fg='red')
        lower_Frame.place(x=4,y=245,width=1339,height=225)
        
        #search frame
        Search_Frame=LabelFrame(lower_Frame,bd=2,relief=RIDGE,bg="white",text="SEARCH CRIMINAL RECORD",font=('times new roman',8,'bold'),fg='red')
        Search_Frame.place(x=2,y=0,width=1330,height=55)

        Search_By=Label(Search_Frame,text='Search By:',font=('arial',12,'bold'),bg='Red',fg='white')
        Search_By.grid(row=0,column=0,padx=4,sticky=W,pady=5)

        self.var_Com_Search=StringVar()
        combo_Search_box=ttk.Combobox(Search_Frame,textvariable=self.var_Com_Search,width=22,font=('arial',10,'bold'),state='readonly')
        combo_Search_box['value']=('Select Options','case_id','criminal_no')
        combo_Search_box.current(0)
        combo_Search_box.grid(row=0,column=1,sticky=W,padx=5)

        self.var_Search=StringVar()
        Search_Txt=ttk.Entry(Search_Frame,textvariable=self.var_Search,width=18,font=('arial',12,'bold'))
        Search_Txt.grid(row=0,column=2,padx=5,sticky=W)

        #Search_Button
        btn_search=Button(Search_Frame,command=self.Search_Data,text='Search',font=('arial',11,'bold'),width=15,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        #All_Button
        btn_All=Button(Search_Frame,command=self.Fetch_Data,text='Show All',font=('arial',11,'bold'),width=15,bg='blue',fg='white')
        btn_All.grid(row=0,column=4,padx=5)

        Crime_Agency=Label(Search_Frame,text='NATIONAL CRIME AGENCY',font=('Times new Roman',22,'bold'),bg='white',fg='crimson')
        Crime_Agency.grid(row=0,column=5,padx=150,sticky=W)       
        

        #table frame
        table_frame=Frame(lower_Frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=60,width=1322,height=140)
        
        #Scroll Bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='CaseId')
        self.criminal_table.heading('2',text='Crime No.')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5',text='Arrest Date')
        self.criminal_table.heading('6',text='Date Of Crime')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father\'s Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=100)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=100)

        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind('<ButtonRelease>',self.get_cursor)

        self.Fetch_Data()
    
    #Add Function
    def add_data(self):
        if self.var_CaseId.get()=="":
            messagebox.showerror("Error","All fiels Required")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user="root",password="Nishing20.",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute('insert into crime values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.var_CaseId.get(),
                            self.var_CriminalNo.get(),
                            self.var_Name.get(),
                            self.var_Nickname.get(),
                            self.var_ArrestDate.get(),
                            self.var_DateOfCrime.get(),
                            self.var_Address.get(),
                            self.var_Age.get(),
                            self.var_Occupation.get(),
                            self.var_BirthMark.get(),
                            self.var_CrimeType.get(),
                            self.var_FathersName.get(),
                            self.var_Gender.get(),
                            self.var_Wanted.get()
                            ))
                conn.commit()
                self.Fetch_Data()
                self.Clear_Data()
                conn.close()
                messagebox.showinfo("Success","Criminal Record has been added successfully.")
            except Exception as E:
                messagebox.showerror("Error",f"Due To {str(E)}")

    #Fetch Data 
    def Fetch_Data(self):
        conn=mysql.connector.connect(host='localhost',user="root",password="Nishing20.",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute('select * from crime')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()
    
    #get Cursor
    def get_cursor(self,event=""):
        cursur_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursur_row)
        data=content['values']

        self.var_CaseId.set(data[0])
        self.var_CriminalNo.set(data[1])
        self.var_Name.set(data[2])
        self.var_Nickname.set(data[3])
        self.var_ArrestDate.set(data[4])
        self.var_DateOfCrime.set(data[5])
        self.var_Address.set(data[6])
        self.var_Age.set(data[7])
        self.var_Occupation.set(data[8])
        self.var_BirthMark.set(data[9])
        self.var_CrimeType.set(data[10])
        self.var_FathersName.set(data[11])
        self.var_Gender.set(data[12])
        self.var_Wanted.set(data[13])

    #Update
    def Update(self):
        if self.var_CaseId.get()=="":
            messagebox.showerror("Error","All fiels Required")
        else:
            try:
                update=messagebox.askyesno('update','Are you sure you want to update record?')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',user="root",password="Nishing20.",database="management")
                    my_cursor=conn.cursor()
                    my_cursor.execute('update crime set Criminal_no=%s,criminal_name=%s,nick_name=%s,Arrest_Date=%s,Date_Of_Crime=%s,Address=%s,Age=%s,Occupation=%s,Birth_Mark=%s,Crime_type=%s,Fathers_Name=%s,Gender=%s,Most_Wanted=%s where case_id=%s',(
                                                    self.var_CriminalNo.get(),
                                                    self.var_Name.get(),
                                                    self.var_Nickname.get(),
                                                    self.var_ArrestDate.get(),
                                                    self.var_DateOfCrime.get(),
                                                    self.var_Address.get(),
                                                    self.var_Age.get(),
                                                    self.var_Occupation.get(),
                                                    self.var_BirthMark.get(),
                                                    self.var_CrimeType.get(),
                                                    self.var_FathersName.get(),
                                                    self.var_Gender.get(),
                                                    self.var_Wanted.get(),
                                                    self.var_CaseId.get()
                                                     ))
                else:
                    if not update:
                        return 
                conn.commit()
                self.Fetch_Data()
                self.Clear_Data()
                conn.close()
                messagebox.showinfo("Success","Criminal Record has been updated successfully.")
            except Exception as E:
                messagebox.showerror("Error",f"Due To {str(E)}")
    
    #Delete Data
    def Delete_Data(self):
        if self.var_CaseId.get()=="":
            messagebox.showerror("Error","All fiels Required")
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure you want to delete record?')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',user="root",password="Nishing20.",database="management")
                    my_cursor=conn.cursor()
                    sql='delete from crime where case_id=%s'
                    value=(self.var_CaseId.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.Fetch_Data()
                self.Clear_Data()
                conn.close()
                messagebox.showinfo('Success','Criminal record Successfully deleted')
            except Exception as E:
                messagebox.showerror('Error',f'Due to {str(E)}')
    
    #clear
    def Clear_Data(self):
        
        self.var_CaseId.set("")
        self.var_CriminalNo.set("")
        self.var_Name.set("")
        self.var_Nickname.set("")
        self.var_ArrestDate.set("")
        self.var_DateOfCrime.set("")
        self.var_Address.set("")
        self.var_Age.set("")
        self.var_Occupation.set("")
        self.var_BirthMark.set("")
        self.var_CrimeType.set("")
        self.var_FathersName.set("")
        self.var_Gender.set("")
        self.var_Wanted.set("")

    def Search_Data(self):
        if self.var_Com_Search.get()=="":
            messagebox.showerror('Error','All Fields are Required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user="root",password="Nishing20.",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute('select * from crime where ' +str(self.var_Com_Search.get())+ " LIKE'%"+str(self.var_Search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as E:
                messagebox.showerror('Error',f'Due to {str(E)}')
                    
               
if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
