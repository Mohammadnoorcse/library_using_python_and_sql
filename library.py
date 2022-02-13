
import mysql.connector as mysql
from tabulate import tabulate
import os #it is cleaning import function

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') # it is using console clearning


db = mysql.connect(host="localhost",
                   user = "root",
                   password = "",
                   database = "library"
                   )
command_handler = db.cursor(buffered = True)

# add the book in library

def add_book():
    clearConsole()
    
    print("\t\t**********Add the book in library*************\n")
    username = input("\t\t\tEnter your username : ")
    title = input("\t\t\tEnter your's book title : ")
    price = int(input("\t\t\tEnter your price : "))
    total = int(input("\t\t\tEnter your same book add : "))

    query = "insert into book(username,title,price,stutes,total) values('{}','{}',{},'{}',{})".format(username,title,price,'unsell',total)
    command_handler.execute(query)
    db.commit()

# update the book

def update():
    clearConsole()
    print("\t\t*********update in your's book item in library**********\n")
    id = int(input("\n\t\t\tEnter your's book id number: "))
    query = "select * from book where book_id = {}".format(id)
    command_handler.execute(query)
    res = command_handler.fetchall()
    h = ['username','book_id','title','price','stutes','total']
    
    if res == []:
        print("\t\t\tcan not find out this item")
    
    else:
        print(tabulate(res,headers=h))
        
        print("\n")
        print('\t\t\t1.username\n\t\t\t2.title\n\t\t\t3.price\n\t\t\t4.stutes')
        ch = int(input('\t\t\tEnter Choice to update : '))
        
        if ch == 1:
            name = input('\t\t\tEnter New name : ')
            query = "update book set username = '{}' where book_id = {}".format(name,id)
            command_handler.execute(query)
            db.commit()
            print("\t\tSuccessfully update Username...")
        elif ch == 2:
            title = input('\t\t\tEnter New book title : ')
            query = "update book set title = '{}' where book_id = {}".format(title,id)
            command_handler.execute(query)
            db.commit()
            print("\t\t\tSuccessfully update Title...")
            
        elif ch == 3:
            price = int(input('\t\t\tEnter New price : '))
            query = "update book set price = {} where book_id = {}".format(price,id)
            command_handler.execute(query)
            db.commit()
            print("\t\t\tSuccessfully update Price...")
            
        elif ch == 4:
            stutes = input('\t\tEnter New stutes : ')
            query = "update book set stutes = '{}' where book_id = {}".format(stutes,id)
            command_handler.execute(query)
            db.commit()
            print("\t\t\tSuccessfully update Stutes...")
        
        else:
            print('\t\t\tInvaild your name and try again...')
            
# delete the item in library

        
def delete():
    clearConsole()
    print("\t\t***************delete the book item*************")
    id = int(input("\t\t\tEnter your's book id number: "))
    query = "select * from book where book_id = {}".format(id)
    command_handler.execute(query)
    res = command_handler.fetchall()
    h = ['username','book_id','title','price','stutes','total']
    
    if res == []:
        print("\t\t\tcan not find out this item")
    
    else:
        print(tabulate(res,headers=h))
        
        ch = input("\t\t\tAre you sure to delete customer...Y/N : ")
        if ch in ['y','Y']:
            query = "delete from book where book_id = {}".format(id)
            command_handler.execute(query)
            db.commit()
            print('\n\t\t\tSuccessfully Deleted book from Database')
            

#search the book item in library


def search():
    clearConsole()
    print("\t\t***************search the book item****************\n")
    id = int(input("\t\t\tEnter your's book id number: "))
    query = "select * from book where book_id = {}".format(id)
    command_handler.execute(query)
    res = command_handler.fetchall()
    h = ['username','book_id','title','price','stutes','total']
    
    if res == []:
        print("\t\t\tcan not find out this item\n")
    
    else:
        print(tabulate(res,headers=h))

# book deatails in library
        
def book_deatail():
    clearConsole()
    print("\t\t****************book_deatails**********\n")
    query = "select * from book"
    command_handler.execute(query)
    res = command_handler.fetchall()
    h = ['username','book_id','title','price','stutes','total']
    
    if res == []:
        print("\t\t\tcan not find out this item")
    
    else:
        print(tabulate(res,headers=h))
            
    
    

# sign in  using id,username and password

def sign_in():
    clearConsole()
    print("\t\t************sign_in*************\n")
    id = int(input('\t\t\tEnter your id : '))
    name = input("\t\t\tEnter your name : ")
    password = input('\t\t\tEnter your password: ')
    query = "select * from login where id = {}".format(id)
    command_handler.execute(query)
    res = command_handler.fetchall()
    if res == []:
        print('\t\tcan not find this data')
    else:
        if res[0][1] == name and res[0][2] == password:
            
            while True:
               clearConsole()
                
               print('\t\t*********Welcome to library function*************')
               
               
               print("\t\t\t1.Add Book")
               print("\t\t\t2.update Book")
               print("\t\t\t3.Search")
               print("\t\t\t4.Remove")
            #    print("5.Returns a book")
               print("\t\t\t5.Books details")
        
               user_option = input("\t\tOption : ")
               if user_option == "1":
                  add_book()
               elif user_option == "2":
                   update()
               elif user_option == "3":
                   search()
               elif user_option == "4":
                   delete()
               elif user_option == "5":
                   book_deatail()
               
                
        
               else:
                   
                 print("\t\tNo valid option was selected")
        
               ch=int(input('\n\t\tPress 0 to continue...Any other key to Exit : '))
    
               if ch!=0:
                  break
            
            
        
        else:
            print('\t\tWrong the username and password')
            

# create a account 

def sign_up():
    clearConsole()
    print("\t\t*********sign up***********\n")
    id = int(input("\t\t\tEnter your id : "))
    name = input("\t\t\tEnter your username:  ")
    pas = input("\t\t\tEnter your password : ")
    phone = input("\t\t\tEnter your phone number : ")
    address = input("\t\t\tEnter your address : ")
    privilege  = input("\t\t\tEnter your privilege : ")
    
    query = "insert into login(id,username,password,phone,address,privilege) values({},'{}','{}','{}','{}','{}')".format(id,name,pas,phone,address,privilege)
    command_handler.execute(query)
    db.commit()
    
    print("\t\t"+name + " has been registered as a " +privilege)
    

# main function

  

def main():
    clearConsole()
    print("\t\t**************main*****************\n")
    while 1:
        print("\t\t\tWelcome to the library system\n")
        print("\t\t\t\t1.sign in")
        print("\t\t\t\t2.sign up")
        
        user_option = input("\t\t\tOption : ")
        if user_option == "1":
            sign_in()
        elif user_option == "2":
            sign_up()
        
        else:
            print("\t\tNo valid option was selected")
        
        ch=int(input('\n\t\tPress 0 to continue...Any other key to Exit : '))
    
        if ch!=0:
         break

main()
        