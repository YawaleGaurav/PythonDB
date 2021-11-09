import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()

au = input('Enter the Name of Author : ')
pu = input('Enter the Name of Publication : ')

curs.execute("select Book_Name from Books where Author = '%s' AND Publication = '%s'" %(au, pu))
data = curs.fetchall()

if data:
    print()
    no = 0
    for rec in data:
        no += 1
        print('%d) %s' %(no, rec[0]))

else:
    print()
    print('No Book have these Author and Publication combination')

con.close()