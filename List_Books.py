import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()

curs.execute("Select Book_Name from Books")
data = curs.fetchall()

no = 0
for rec in data:
    no += 1
    print('%d) %s' %(no, rec[0]))

con.close()