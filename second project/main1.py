#importing library
import mysql.connector as connector

# connection establishment
class Helper:
    def __init__(self) :

        self.con=con=connector .connect(host='localhost',user='root',password='root123',database='pythontest')# enter your own information
        query='create table if not exists user(userid int primary key not null ,  username varchar(200),  phone varchar(12) not null)'
        cur= self.con.cursor()
        cur.execute(query)
        print("table created successfully")


    # insert into user

    def insert_user(self,userid,username,phone):
        query="insert into user(userid,username,phone) values({},'{}','{}')".format(userid,username,phone)# placeholder is used which will help  to format the specified value and insert them in string
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()  # to save the changes we are making
        print("user saved to database")



    # fetching the data stored in user


    def fetch_all(self):
        query='select * from user'
        cur=self.con.cursor()
        cur.execute(query)
        for x in cur:
            print("userid",x[0])
            print("username",x[1])
            print("user phone",x[2])
            print()


    #delete user record


    def delete_user(self,userid):
        query="delete from user where userid={}".format(userid)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        print("deleted")
        self.con.commit()


    # student details search 
    
    def search(self,userid):
        query="select  * from  user where user name={}".format(userid)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        print("successfully found")
        self.con.commit()
        print("succsfully found")


h=Helper()
while True:
    print("\n ************************** USER MANAGEMENT*************************")
    print("1. INSERT ")
    print("2. VIEW ")
    print("3. DELETE")
    print("4. SEARCH")
    print("5. EXIT")

    choice = input("Enter your choice: ")

    if choice == "1":
        userid = int(input("Enter userid: "))
        username = input("Enter user name: ")
        phone = int(input("Enter phone number: "))
        h.insert_user(userid,username,phone)
        

    elif choice == "2":
        print("\nAll users are:")
        h.fetch_all()

    elif choice == "3":
        name = input("Enter the student id to delete record ")
        h.delete_user(userid)

    elif choice == "4":
        userid = int(input("Enter user ID to search: "))
        h.search(userid)

    elif choice == "5":
        print("Exiting the program.")
        break



    



