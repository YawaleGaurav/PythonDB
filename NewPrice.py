import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()
try:
    bcd=int(input("Enter A Book Code : "))
    prc=float(input("Enter A New Price : "))
    curs.execute("select * from Books where Book_Id=%d" %bcd)
    data=curs.fetchone()
    if data:
        curs.execute("update Books set Price=%.2f where Book_Id=%d" %(prc,bcd))
        con.commit()
        print("New Price Is Updated Successfuly")
    else:
        print("Book Is Not Found")
except:
    print("Invalid Input")

con.close()