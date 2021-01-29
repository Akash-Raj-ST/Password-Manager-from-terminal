import db_sql as db
import getpass
import pyperclip

# KEYS
CODE = ''  #access to sensitive data
KEY = ''    #initial access to app

print("-"*47)
print("-"*15,"Password Manager","-"*15)
print("-"*47)

# encryption of password
def encrypt(password):
    #Your encrpyting method

#decrypting
def decrypt(password):
    #Your decrpyting method

    
# Function to add info:
def add_info():
    site = input("Enter the name of the website:").lower()
    user = input("Enter the user_name:")
    gmail = input("Enter the gmail:")
    password = input("Enter the password:")
    password = encrypt(password)
    command = input("Enter commands of the account:")
    db.cursor.execute('''INSERT INTO INFO VALUES (NULL,?,?,?,?,?)''',(site,user,gmail,password,command))
    print("Cred added successfully!")
    db.conn.commit()


# Function to view details
def view_info(website=None,index=None,delete=False,edit=False):
    if index is None:
        code = getpass.getpass(prompt="Enter ENCRYPT key to continue:")
    else:
        code=CODE   
    if code == CODE:
        
        if index is None:
            db.cursor.execute('''SELECT * FROM INFO WHERE Website=(?)''',(website,))
        else:
            db.cursor.execute('''SELECT * FROM INFO WHERE No=(?)''',(index,))

        info = db.cursor.fetchall()
        if info:
            record = info
            if delete:
                print("NO".center(5,' '),'|',"SITE".center(15,' '),'|',"USER".center(15,' '),'|',"GMAIL".center(25,' '),)
                print("-"*66)
            else:
                print("NO".center(5,' '),'|',"SITE".center(15,' '),'|',"USER".center(15,' '),'|',"GMAIL".center(25,' '),'|',"PASSWORD".center(25,' '),'|',"COMMANDS".center(25,' '))
                print("-"*120)
                
            for i in info:
                if delete:
                    print(str(i[0]).center(5,' '),'|',i[1].center(15,' '),'|',i[2].center(15,' '),'|',i[3].center(25,' '),)
                    print("-"*66)
                else:  
                    print(str(i[0]).center(5,' '),'|',i[1].center(15,' '),'|',i[2].center(15,' '),'|',i[3].center(25,' '),'|',i[4].center(25,' '),'|',i[5].center(25,' '))
                    print("-"*120)
                
                if delete==False and edit==False:
                    dec = input("Do u want to view or copy decrypted password[v/c/n]:").lower()
                    if dec == 'v':
                        password = decrypt(i[4])
                        print("-"*120)
                        st = f"   Original Password: {password}   "
                        print(st.center(120,'/'))
                        print("-"*120)
                        pyperclip.copy(password)
                    elif dec== 'c':
                        pyperclip.copy(decrypt(i[4]))
                        print("Password copied to clipboard")
                        
            if edit:
                print("\n")
                print("EDIT SECTION".center(120,'-'))
                print("\n")
            return record
        
        else:
            record = False
            print("No such website cred stored")
            return record
        
    else:
        print("WRONG ENCRYPT CODE!!!")
        view_info(website,index,delete)  


# Function to edit details
def edit_info(website):
    records = view_info(website,edit=True)
    if records:
        for record in records:
            view_info(index=record[0])
            chc = input("Do you want to edit this[y/n]:")
            if chc=='y':
                pyperclip.copy(record[1])
                site = input("Enter the website to update  :")
                pyperclip.copy(record[2])
                user      = input("Enter the user_name to update  :")
                pyperclip.copy(record[3])
                gmail     = input("Enter the gmail to update      :")
                pyperclip.copy(decrypt(record[4]))
                password  = input("Enter the password to update   :")
                password  = encrypt(password)
                pyperclip.copy(record[5])
                command   = input("Enter commands of the account to update:")
                db.cursor.execute('''UPDATE INFO SET Website=?,username=?,Gmail=?,Password=?,info=? where No=?''',(site,user,gmail,password,command,record[0]))
                print("Update Successfull!!!")
                db.conn.commit()


# Function to delete record
def delete_info(num):
        db.cursor.execute('''DELETE FROM INFO WHERE No=(?)''',(num,))
        db.conn.commit()
        print("DELETED!!!")


# Function to view all websites only
def website_view():
    db.cursor.execute('''SELECT No,Website,username,gmail FROM INFO''')
    res = db.cursor.fetchall()

    if res:
        print("NO".center(5,' '),'|',"SITE".center(15,' '),'|',"USER".center(15,' '),'|',"GMAIL".center(25,' '),)
        print("-"*66)
        for i in res:
         
            print(str(i[0]).center(5,' '),f"|{i[1].center(17,' ')}|{i[2].center(17,' ')}|{i[3].center(27,' ')}")
            print("-"*66)

    else:
        print("No credentials stored")

        
# Choices
access = False
for i in range(5):
    if i==0:
        key = getpass.getpass(prompt="Hi buddy,Enter the key:")
    else:
        # key = input("Kya bhai,Try once more:")
        key = getpass.getpass(prompt="Kya bhai,Try once more:")
    if key==KEY:
        print("\nYOU-ARE-IN!!!\n")
        access = True
        break
    else:        
        print("Wrong Code")


print("1.Add Credentials")
print("2.View Credentials")
print("3.Edit Credentials")
print("4.Delete Credentials")
print("5.View basic credentials")
print("6.Close")


while access:
    choice = int(input("\nEnter your choice:"))

    if choice==1:
        pyperclip.copy('')
        print("ADD".center(25,"="))
        add_info()
        
    elif choice==2:
        pyperclip.copy('')
        print("VIEW".center(25,"="))      
        website = input("Enter the name of website to view:").lower()
        view_info(website)
        
    elif choice==3:
        pyperclip.copy('')
        print("EDIT".center(25,"="))      
        website = input("Enter the name of the website to edit:").lower()
        edit_info(website)
        
    elif choice==4:
        pyperclip.copy('')
        print("DELETE".center(25,"="))      
        website_view()

        num = input("Enter spaced int to delete['n' to cancel]:").split()
        if num[0] == 'n':
            print("Deletion cancelled")
            continue
        else:
            num1 = map(int,num)
            
        for i in num1:
                view_info(website=None,index=i,delete=True)
                ans = input("Do you want to delete it:[y/n]")
                if ans.lower()=='y':
                    delete_info(i)

    elif choice==5:
        pyperclip.copy('')
        website_view()
        
    elif choice==6:
        pyperclip.copy('')
        print("Program closed BYE!!!")
        break
    
    else:
        pyperclip.copy()
        print("No such choice!!!")

db.conn.commit()
db.conn.close()
