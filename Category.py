import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()
n=0
try:
    cat=input("Enter Category Of Book : ")
    curs.execute("select * from Books where Category= '%s'" %cat)
    data=curs.fetchall()
    
    if data:
        for rec in data:
            n+=1
            print('%d)%s' %(n, rec[1]))
    else:
        print("No Book Is Prsent Of Such Category")
except:
    print("Invalid Input")
con.close()