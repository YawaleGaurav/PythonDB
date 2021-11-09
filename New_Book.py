import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()

try:
    id = int(input('Enter the book id : '))
    nm = input('Enter Book name : ')
    ct = input('Enter the category of Book : ')
    au = input('Enter the Author name of Book : ')
    pu = input('Enter publication of Book : ')
    ed = input('Enter the edition of Book : ')
    pr = float(input('Enter the price of Book > 0 : '))
    re = input('Enter review for book : ')

    curs.execute("insert into Books values(%d, '%s', '%s', '%s', '%s', '%s', %.1f, '%s')" %(id, nm, ct, au, pu, ed, pr, re))
    con.commit()

    print()
    print('Your Book is added into the database')

except:
    print()
    print('Invalid input')
    print("We can't add new book into database")
    print()

con.close()