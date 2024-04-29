from modules import accounts
from tkinter import *
import tkinter.ttk  as tkk
#import mysql.connector


#connection  = mysql.connector.connect(
#     user='root',
#     password='test1234',
#     database='bank_database'
#     )
#cursor = connection.cursor()
#addData = ("INSERT INTO account_info (account_name, account_email, account_pin,account_balence) VALUES (test,teste,11111111)")
#cursor.execute(addData)
#connection.commit()
#cursor.close()

root = Tk()
root.title("Online Bank system")
root.geometry("500x800")
#root.configure(background='#706e6c')
ac = accounts
wigit_index = ac.wigit_index
ac_index = []
ac_index.append(ac.info(root,"testinfo","ian","12345678"))


#resets program to base(does not affect local index)
def log_out():
     global login_state
     global account_login_location
     account_login_location = int 
     login_state = False
     main()

#removes account
def delete(location):
     con = ac.messagebox.askquestion("Delete Account",f"Do you want to delete {ac_index[account_login_location].name_account()}")
     if con =='yes':
          ac_index.remove(ac_index[location])
          log_out()
     else:
          ac.messagebox.showinfo
#directs to account modual info function
def create():
     ac.forget_wigit()
     global ac_index_size
     global ac_created
     ac_created = True
     ac_index.append(ac.info(root))
  
     return_b = Button(root,text="return",command=lambda:main()& return_b.grid_forget())
     return_b.grid(row=19,column=0)
     wigit_index.append(return_b)


def check_info(locat,t):
     check_info_text = Label(locat,text=t)
     check_info_text.grid(row=2,column=0)
     wigit_index.append(check_info_text)


# checks the inputed login and compare to the database
def login_check(frame,name,pin):
     global login_state

     if len(name)<=0 or len(pin)<8 or any(inter.isalpha() for inter in pin):
          if len(name)<=0 :
               error_name = Label(frame,text="-must have login email or name",fg="red")
               error_name.grid(row=2,column=0)
               wigit_index.append(error_name)

          if any(inter.isalpha() for inter in pin):
               error_pin = Label(frame,text="Please no charecters in account pin.",fg="red")
               error_pin.grid(row=10,column=0)
               wigit_index.append(error_pin)

          if len(pin)<8:
               error_pin = Label(frame,text="-pin length must be at least 8 long",fg="red")
               error_pin.grid(row=5,column=0)
               wigit_index.append(error_pin)

     else:
          for x in range(len(ac_index)):
               if (ac_index[x].account_info.get("name") == name or ac_index[x].account_info.get("email")== name) and ac_index[x].account_info.get("pin") == pin:
               
                    global account_login_location
                    account_login_location= x
                    login_state=True
                    main()

          if login_state == False:
               failed_login_text=Label(frame,text="Invalid login",fg="red")
               failed_login_text.grid(row=0,column= 0)
               wigit_index.append(failed_login_text)



#takes in input to get login info 
def login():
     global login_state
     ac.forget_wigit()

                    
     frame = LabelFrame(root,padx=10,pady=10)
     frame.grid(row=0,column=0,columnspan=10)
     wigit_index.append(frame)

     name_text = Label(frame,text ="Please enter account name or email")
     name_text.grid(row=1,column=0,columnspan=4)
     wigit_index.append(name_text)

     name = Entry(frame, width=40)
     name.grid(row=3,column=0,columnspan=4)
     name.insert(0,"ian")
     wigit_index.append(name)

     pin_text = Label(frame,text="please enter account pin")
     pin_text.grid(row=4,column=0,columnspan=4)
     wigit_index.append(pin_text)

     pin = Entry(frame,width=40)
     pin.grid(row=6,column=0,columnspan=4)
     wigit_index.append(pin)
     pin.insert(0,"12345678")

     #when clicked checks the information for errors and then checks database
     next = Button(frame,text="next",command=lambda:login_check(frame,name.get(),pin.get()))
     next.grid(row=8,column=0)
     wigit_index.append(next)

     

     

                    
account_login_location = int
login_state = False
ac_created = False
def main():
     global login_state 
     global account_login_location
     global ac_created 

     ac.forget_wigit()

     blank1 = Label(root,text="").grid(row=3,column=10)
     quit = Button(root,text= "Exit program",command=lambda:root.destroy()).grid(row=20,column=0)

     if not login_state :
          if ac_created:
               account_create_text = Label(root,text="account created, please log to access your account")
               account_create_text.grid(row=0,column=0)
               wigit_index.append(account_create_text)
          print("check1")
          #if a account has been created pose this prompt 
               
          prompt= Label(root, text="welcome to the online bank system\n-please log or create account to continue " )
          prompt.grid(row=1,column=0,columnspan=4,sticky=W+E)
          wigit_index.append(prompt)

          login_button = Button(root,text="login",command= login,padx=20)
          login_button.grid(row=2,column=0)
          wigit_index.append(login_button)

          create_button = Button(root,text="Create account",padx=20,command= create)
          create_button.grid(row=2,column=1)
          wigit_index.append(create_button)
                         
     elif login_state:
          change = StringVar()
          loged_in_prompt= Label(root,text=f"Welcome {ac_index[account_login_location].name_account()} to the online banking system")
          loged_in_prompt.grid(row=0,column=0,pady=20,columnspan=10,sticky="NW")
          wigit_index.append(loged_in_prompt)

          #creates blank frames to fill with the information

          #check balence frame
          fram1 = LabelFrame(root,padx=50,pady=15)
          fram1.grid(row=2,column=0,columnspan=10,sticky="NEWS")
          wigit_index.append(fram1)

          #deposit frame
          fram2 = LabelFrame(root,padx=20,pady=15)
          fram2.grid(row=3,column=0,columnspan=4,sticky="NEWS")
          wigit_index.append(fram2)

          #withdraw frame
          fram3 = LabelFrame(root,padx=20,pady=15)
          fram3.grid(row=3,column=5,columnspan=4,sticky="NEWS")
          wigit_index.append(fram3)

          #check detials frame
          fram4 = LabelFrame(root,padx=20,pady=15)
          fram4.grid(row=4,column=0,columnspan=4,sticky="NEWS")
          wigit_index.append(fram4)

          #modify frame
          fram5 = LabelFrame(root,padx=20,pady=15)
          fram5.grid(row=4,column=5,columnspan=4,sticky="NEWS")
          wigit_index.append(fram5)

          #delete frame
          fram6 = LabelFrame(root,padx=20,pady=15)
          fram6.grid(row=6,column=0,columnspan=4,sticky="NEWS")
          wigit_index.append(fram6)

          root.grid_columnconfigure(0,weight = 1)
          root.grid_columnconfigure(5,weight=1)



          #short hand: check, dep, with, mod,log, del  to simplify code names
          #check account funds 
          check_b = Button(fram1,text="Check Account Balance",command=lambda:ac_index[account_login_location].check(fram1))
          check_b.grid(row=0,column=0,columnspan=5,sticky="EW")
          wigit_index.append(check_b)
          #add to the account

          dep_text = Label(fram2,text="How much do you want to deposit?")
          dep_text.grid(row=0,column=0,columnspan=4)
          wigit_index.append(dep_text)

          dep_amount = Entry(fram2,width=20)
          dep_amount.grid(row=2,column=0,columnspan=3)
          wigit_index.append(dep_amount)

          dep_b = Button(fram2,text="Deposit",command=lambda: ac_index[account_login_location].deposit(fram2,int(dep_amount.get())))
          dep_b.grid(row=4,column=0)
          wigit_index.append(dep_b)

          #withdraw from account
          with_text = Label(fram3,text="How much do you want to withdraw?")
          with_text.grid(row=0,column=0,columnspan=3)
          wigit_index.append(with_text)

          with_amount = Entry(fram3,width=20)
          with_amount.grid(row=2,column=0)
          wigit_index.append(with_amount)

          with_b = Button(fram3,text="withdraw",command= lambda:ac_index[account_login_location].withdraw(fram3,int(with_amount.get())))
          with_b.grid(row=4,column=0)
          wigit_index.append(with_b)

          #check account details 
          checkD_text= Label(fram4,text="Check account information")
          checkD_text.grid(row=0,column=0,columnspan=4)
          wigit_index.append(checkD_text)

          checkD_b= Button(fram4,text="select",command=lambda:check_info(fram4,ac_index[account_login_location].info_account()))
          checkD_b.grid(row=3,column=0)
          wigit_index.append(checkD_b)

          #modify account details 
          mod_text = Label(fram5,text="Change information")
          mod_text.grid(row=0,column=0,columnspan=5)
          wigit_index.append(mod_text)

          mod_chamge = Entry(fram5,width=20)
          mod_chamge.grid(row=1,column=0,columnspan=4)
          wigit_index.append(mod_chamge)


          mod_name = Radiobutton(fram5,text="Name",variable=change, value="name")
          mod_name.grid(row=2,column=0)
          wigit_index.append(mod_name)

          mod_email = Radiobutton(fram5,text="Email",variable=change, value="email")
          mod_email.grid(row=2,column=1)
          wigit_index.append(mod_email)

          mod_pin = Radiobutton(fram5,text="Pin",variable=change, value="pin")
          mod_pin.grid(row=2,column=2)
          wigit_index.append(mod_pin)


          mod_b = Button(fram5,text="select",command=lambda:ac_index[account_login_location].mod_info(fram5,change.get(),mod_chamge.get()))
          mod_b.grid(row=6,column=0)
          wigit_index.append(mod_b)

          #delete account
          del_text = Label(fram6,text="delete account")
          del_text.grid(row=0,column=0)
          wigit_index.append(del_text)

          del_b = Button(fram6,text="delete",command=lambda:delete(account_login_location))
          del_b.grid(row=1,column=0)
          wigit_index.append(del_b)
          #log out/ resets the program
          log_b = Button(root,text="logout",command=log_out)
          log_b.grid(row=9,column=0,padx=10,pady=10)
          wigit_index.append(log_b)
               

                    

                    
               
     else:
          print("fatil error")               
     
main()
root.mainloop()