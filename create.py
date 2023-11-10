# installed library mysql-connector-python
import mysql.connector


#creating connection 
class insert:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Nandu@22",
                database = "bank"
            )
    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO PERSONAL_DETAILS VALUES({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
        self.conn.commit() 
        print("----------------------personal details has been saved successfully----------------------:")


    def bank_details(self,acn,cid,ifsc,actype):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO BANK_DETAILS VALUES({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("----------------------bank details as been successfully saved----------------------------:")  

    def transaction_details(self,tid,sacc,racc,amt,mthd):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO TRANSACTION_DETAILS VALUES({tid},{sacc},{racc},{amt},'{mthd}')")
        self.conn.commit()
        print("---------------transaction details as been saved successfully-----------------:")

    def account_details(self,acn,tid,amt,cbal,ttype):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO ACCOUNT_DETAILS VALUES({acn},{tid},{amt},{cbal},'{ttype}')")
        self.conn.commit()
        print("-----------------account details as been saved successfully-----------:")     







