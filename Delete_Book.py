import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()

try:
    id = int(input('Enter Book id : '))
    curs.execute("Select * from Books where Book_Id = %d" %id)
    data = curs.fetchall()
    if data:
        print()
        print('Book Id     : %d' %id)
        print('Book Name   : %s' %data[0][1])
        print('Category    : %s' %data[0][2])
        print('Author      : %s' %data[0][3])
        print('Publication : %s' %data[0][4])
        print('Edition     : %s' %data[0][5])
        print('Price       : %.2f' %data[0][6])

        print()
        ch = input('Do you want remove Book from database - Yes/No : ')
        if ch.upper() == 'YES':
            curs.execute("delete from Books where Book_Id = %d" %id)
            con.commit()
            
            print()
            print('Your Book has been removed from database')

    else:
        print()
        print('Book does not exist')

except:
    print()
    print('Invalid input')

con.close()