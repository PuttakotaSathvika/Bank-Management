from create import insert
from read import read
from update import update
from delete import delete

obj = insert()
objread = read()
objupdate = update()
objdelete = delete()

print("------------------Bank Management System--------------------")
print("For Inserting data press 1:")
print("For Reading data press 2:")
print("For Updating data press 3:")
print("For Deleting data press 4:")
opr=int(input(" please enter your operation:"))

def myopr():
    print("-------For Personal Details press 1---------- ")
    print("-------For Bank Details press 2--------- ")
    print("-------For  Transaction Details press 3--------- ")
    print("-------For Account Details press 4---------- ")
    vr=int(input("please select the table:"))
    if vr==1:
        return'personal_details'
    elif vr==2:
        return'bank_details'
    elif vr==3:
        return'transaction_details'
    elif vr==4:
        return'account_details'
    
if opr==1:
    h = myopr()
    if h=='personal_details':
        cid = int(input("please enter customer id:"))
        fname = input("please enter customer first name:")
        lname = input("please enter customer last name:")
        addr = input("please eneter customer address:")
        pn = int(input("please enter customer phone number:"))
        an = input("please enter customer aadhar number:")
        pan = input("please enter customer pan number:")
        obj.personal_details(cid,fname,lname,addr,pn,an,pan)
    elif h=='bank_details':
        acn = int(input("please enter account number:")) 
        cid = int(input("please enter customerid:"))
        ifsc = input("please enter ifsc code:")
        actype = input("please enter account type:")
        obj.bank_details(acn,cid,ifsc,actype)
    elif h=='transaction_details':
        tid = int(input("please enter transcationid:"))
        sacc = int(input("please enter sender account:"))
        racc = int(input("please enter recevier account:"))
        amt = int(input("please enter amount:"))
        mthd = input("please enter method:") 
        obj.transaction_details(tid,sacc,racc,amt,mthd)
    elif h=='account_details':
        acn = int(input("please enter account number:"))
        tid = int(input("please enter transcationid:"))
        amt = int(input("please enter amount:"))
        cbal = int(input("please enter closing balance:"))
        ttype=input("please enter transaction type: ")
        obj.account_details(acn,tid,amt,cbal,ttype)  

if opr==2:     #user wanted to read the data
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    objread.specific_info(cusid,j)
    

if opr==3:       #user want to update the data
    k = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    colname = input("please enter column name:")
    newval = input("please enter new values:") # 500 str # 'jhon'
    objupdate.myupdate(j,colname,newval,cusid)

if opr==4:
    p = myopr()
    cusid = int(input("please enter the customer id to delete the data:"))
    objdelete.specific_del(p,cusid)    




     





