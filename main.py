import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',port = '3306',user = 'root',password = 'HasnainSid@786',database = 'pythontest')

        query = 'create table if not exists user(userID int primary key,userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)

    # Insert
    def insert_user(self,userID,userName,phone):
        query = "insert into user(userID,userName,phone) values({},'{}','{}')".format(userID,userName,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    # fectch all
    def fectch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User ID: ", row[0])
            print("User Name: ", row[1])
            print("User Phone: ", row[2])
            print()
            print()

    # fectch requried
    def fectch_requried(self,req_id):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            if req_id == row[0]:
              print("User ID: ", row[0])
              print("User Name: ", row[1])
              print("User Phone: ", row[2])
              print()
              print()
        else:
            print("Not found")
            print()


    def delete_user(self,userID):
        query = "delete from user where userID = {}".format(userID)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("Delete user")

    def update_user(self,userID,userName,userPhone):
        query = "update user set userName = '{}',phone = '{}' where userID = {}".format(userName,userPhone,userID)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Update user")




# main coding
helper = DBHelper()
helper.insert_user(4,"Boss","720786")
# helper.insert_user(2,"Akhtar","722786")
# helper.insert_user(5,"Siddique","726786")
# helper.delete_user(4)

helper.fectch_all()
helper.update_user(4,"Hilo","00786")
helper.fectch_all()

# helper.fectch_requried(3)
