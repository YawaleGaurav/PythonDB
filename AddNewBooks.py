import mysql.connector as my

con = my.connect(host='bcraxj52mvogpllhdtex-mysql.services.clever-cloud.com', user='ucnxul09m0vgqoqg', password='5gjqAEl2bEDnJeoiv1rT', database='bcraxj52mvogpllhdtex')
curs=con.cursor()
try:
    bcd=int(input("Enter Book Code    : "))
    bnm=input("Enter Book Name        : ")
    cat=input("Enter Book Category    : ")
    aut=input("Enter Author Name      : ")
    pub=input("Enter Publication Name : ")
    edt=input("Enter Edition          : ")
    prc=float(input("Enter Price      : "))
    rew = input('Enter review for book : ')


    curs.execute("insert into Books values(%d,'%s','%s','%s','%s','%s',%.2f,'%s')" %(bcd,bnm,cat,aut,pub,edt,prc,rew))
    con.commit()
    print("Book Is Successfuly Added")

except:
    print()
    print('Invalid input')
    print("We can't add new book into database")
    print()

con.close()
