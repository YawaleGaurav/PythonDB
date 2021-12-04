import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()

try:
    bcd = int(input('Enter Book Code : '))
    curs.execute("Select * from Books where Book_Id = %d" %bcd)
    data = curs.fetchall()
    if data:
        print()
        print('Book Id     : %d' %bcd)
        print('Book Name   : %s' %data[0][1])
        print('Category    : %s' %data[0][2])
        print('Author      : %s' %data[0][3])
        print('Publication : %s' %data[0][4])
        print('Edition     : %s' %data[0][5])
        print('Price       : %.2f' %data[0][6])

        choice=input("Do you want to Delete Book - Yes/No  : ")
        if choice.upper()== 'YES':
            curs.execute("delete from Books wheree Book_Id=%d" %bcd)
            con.commit()
            print("Book Is Deleted")

        else:
            print("Thank You")
    else:
        print("Book Is Not Found")
except:
    print("Invalid Input")

con.close()
