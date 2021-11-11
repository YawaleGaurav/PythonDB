import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()

try:
    bcd = int(input('Enter Book Code : '))
    rew = input('Enter Review for the Book : ')
    curs.execute("Select * from Books where Book_Id = %d" %bcd)
    data = curs.fetchall()
    if data:
        curs.execute("update Books set Review = '%s' where Book_Id = %d" %(rew, bcd))
        con.commit()

        print()
        print('Book review is added')

    else:
        print()
        print('Book does not exist')

except:
    print()
    print('Invalid input')

con.close()