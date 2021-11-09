import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()

try:
    id = int(input('Enter Book id : '))
    pr = float(input('Enter the new price of Book : '))
    curs.execute("Select Price from Books where Book_Id = %d" %id)
    data = curs.fetchall()

    if data:
        curs.execute("update Books set Price = %.1f where Book_Id = %d" %(pr, id))
        con.commit()

        print()
        print('Price of Book is changed')

    else:
        print()
        print('Book does not exist')

except:
    print()
    print('Invalid input')

con.close()