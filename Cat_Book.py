import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()

ct = input('Enter category of book you want to search : ')

curs.execute("Select Book_Name from Books where Category = '%s'" %ct)
data = curs.fetchall()

if data:
    print()
    no = 0
    for rec in data:
        no += 1
        print('%d) %s' %(no, rec[0]))

else:
    print()
    print('No Book have these category')

print()
con.close()