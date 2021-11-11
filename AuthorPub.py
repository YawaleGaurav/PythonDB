import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()
n=0
try:

    aut = input('Enter the Name of Author : ')
    pub = input('Enter the Name of Publication : ')

    curs.execute("select * from Books where Author = '%s' AND Publication = '%s'" %(aut, pub))
    data = curs.fetchall()
    if data:
        for rec in data:
            n+=1
            print("%d) Book Name : '%s' " %(n,rec[1]))
    else:
        print("Book Is Not Found")

except:
    print("Invalid Input")
con.close()

