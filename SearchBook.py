import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()
try:
    bcd = int(input('Enter Book Code : '))
    curs.execute("Select * from Books where Book_Id = %d" %bcd)
    data = curs.fetchone()
    if data:
        print("Book Name   : %s" %data[1])
        print("Category    : %s" %data[2]) 
        print("Author      : %s" %data[3])
        print("Publication : %s" %data[4])
        print("Edition     : %s" %data[5])
        print("Price       : %.2f" %data[6])
    else:
        print("Book is not found")

except:
    print("Invalid Book Code")
con.close()
