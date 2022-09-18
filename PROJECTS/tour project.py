import mysql.connector
import datetime
murugesh=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="sri_thirupathi_tour_manegement",
)
mycursor=murugesh.cursor()
#mycursor.execute("create database sri_thirupathi_tour_manegement")
#mycursor.execute("create table tour_details (customers_name varchar(225),place varchar(225),days int,budjet int)")
#murugesh.commit()
#print("completed")
print("\n")
sql="SELECT * FROM tour_details ORDER BY customers_name DESC"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for i in myresult:
        print(i)
print("\n")
print("\t\t\t WELCOME TO SRI THIRUPATHI TRAVEL AGENCY \t\t\t") 
print("\n")

print("1.Tiruvannamalai") 

print("2.Yercurd") 

print("3.Kotagiri") 

print("4.Kodaikkanal") 

print("5.Ooty")

print("6.Thirupathi")

print("7.Dhanuskodi")

print("8.Coimbatore")

print("9.Thanjavur")

print("10.Vellore")

print("\n")


def Tiruvannamalai(name,place,days,budjet):

    if days>=1 and budjet>=1000: 
        print("Enjoy the travel")
        sql="insert into tour_details (customers_name,place,days,budjet) values (%s,%s,%s,%s)"
        val=(name,place,days,budjet)
        mycursor.execute(sql,val)
        murugesh.commit()
    else: 
        print("travel start 1000 RS above")  

def Yercurd(name,place,days,budjet):

    if days>=1 and budjet>=1000: 
        print("Enjoy the travel")
        sql="insert into tour_details (customers_name,place,days,budjet) values (%s,%s,%s,%s)"
        val=(name,place,days,budjet)
        mycursor.execute(sql,val)
        murugesh.commit() 
    else: 
        print("travel start 1000 RS above")  

def Kotagiri(name,place,days,budjet):

    if days>=1 and budjet>=1000: 
        print("Enjoy the travel")
        sql="insert into tour_details (customers_name,place,days,budjet) values (%s,%s,%s,%s)"
        val=(name,place,days,budjet)
        mycursor.execute(sql,val)
        murugesh.commit()
    else: 
        print("travel start 1000 RS above")  

def Kodaikkanal(name,place,days,budjet):

    if days>=1 and budjet>=1000: 
        print("Enjoy the travel") 
        sql="insert into tour_details (customers_name,place,days,budjet) values (%s,%s,%s,%s)"
        val=(name,place,days,budjet)
        mycursor.execute(sql,val)
        murugesh.commit()
    else: 
        print("travel start 1000 RS above") 

def Ooty(name,place,days,budjet):

    if days>=1 and budjet>=1000: 
        print("Enjoy the travel")
        sql="insert into tour_details (customers_name,place,days,budjet) values (%s,%s,%s,%s)"
        val=(name,place,days,budjet)
        mycursor.execute(sql,val)
        murugesh.commit()
    else: 
        print("travel start 1000 RS above")  

def Thirupathi(name,place,days,budjet):

    if days>=1 and budjet>=1000: 
        print("Enjoy the travel")
        sql="insert into tour_details (customers_name,place,days,budjet) values (%s,%s,%s,%s)"
        val=(name,place,days,budjet)
        mycursor.execute(sql,val)
        murugesh.commit()
    else: 
        print("travel start 1000 RS above")  

def Dhanuskodi(name,place,days,budjet):

    if days>=1 and budjet>=1000: 
        print("Enjoy the travel")
        sql="insert into tour_details (customers_name,place,days,budjet) values (%s,%s,%s,%s)"
        val=(name,place,days,budjet)
        mycursor.execute(sql,val)
        murugesh.commit()
    else: 
        print("travel start 1000 RS above")  

def Coimbatore(name,place,days,budjet):

    if days>=1 and budjet>=1000: 
        print("Enjoy the travel")
        sql="insert into tour_details (customers_name,place,days,budjet) values (%s,%s,%s,%s)"
        val=(name,place,days,budjet)
        mycursor.execute(sql,val)
        murugesh.commit() 
    else: 
        print("travel start 1000 RS above")  

def Thanjavur(name,place,days,budjet):

    if days>=1 and budjet>=1000: 
        print("Enjoy the travel")
        sql="insert into tour_details (customers_name,place,days,budjet) values (%s,%s,%s,%s)"
        val=(name,place,days,budjet)
        mycursor.execute(sql,val)
        murugesh.commit()
    else: 
        print("travel start 1000 RS above")  

def Vellore(name,place,days,budjet):

    if days>=1 and budjet>=1000: 
        print("Enjoy the travel")
        sql="insert into tour_details (customers_name,place,days,budjet) values (%s,%s,%s,%s)"
        val=(name,place,days,budjet)
        mycursor.execute(sql,val)
        murugesh.commit() 
    else: 
        print("travel start 1000 RS above")  

try:

    m=datetime.datetime.now()
    print(m)
    print("\n")

    user=int(input("Where do you go on HOLIDAYS in the list above:"))

    if user==1:

        print("Tiruvannamalai")
        name=input("Enter your name:").lower().strip()
        place="Tiruvannamalai"
        days=int(input("Enter how many days:"))
        budjet=int(input("Enter your budjet:"))
        Tiruvannamalai(name,place,days,budjet)

    elif user==2:

        print("Yercurd")
        name=input("Enter your name:").lower().strip()
        place="Yercurd"
        days=int(input("Enter how many days:"))
        budjet=int(input("Enter your budjet:"))
        Yercurd(name,place,days,budjet)

    elif user==3:

        print("Kotagiri")
        name=input("Enter your name:").lower().strip()
        place="Kotagiri"
        days=int(input("Enter how many days:"))
        budjet=int(input("Enter your budjet:"))
        Kotagiri(name,place,days,budjet)

    elif user==4:

        print("Kodaikkanal")
        name=input("Enter your name:").lower().strip()
        place="Kodaikkanal"
        days=int(input("Enter how many days:"))
        budjet=int(input("Enter your budjet:"))
        Kodaikkanal(name,place,days,budjet)

    elif user==5:

        print("Ooty")
        name=input("Enter your name:").lower().strip()
        place="Ooty"
        days=int(input("Enter how many days:"))
        budjet=int(input("Enter your budjet:"))
        Ooty(name,place,days,budjet)

    elif user==6:

        print("Thirupathi")
        name=input("Enter your name:").lower().strip()
        place="Thirupathi"
        days=int(input("Enter how many days:"))
        budjet=int(input("Enter your budjet:"))
        Thirupathi(name,place,days,budjet)

    elif user==7:

        print("Dhanuskodi")
        name=input("Enter your name:").lower().strip()
        place="Dhanuskodi"
        days=int(input("Enter how many days:"))
        budjet=int(input("Enter your budjet:"))
        Dhanuskodi(name,place,days,budjet)

    elif user==8:

        print("Coimbatore")
        name=input("Enter your name:").lower().strip()
        place="Coimbatore"
        days=int(input("Enter how many days:"))
        budjet=int(input("Enter your budjet:"))
        Coimbatore(name,place,days,budjet)

    elif user==9:

        print("Thanjavur")
        name=input("Enter your name:").lower().strip()
        place="Thanjavur"
        days=int(input("Enter how many days:"))
        budjet=int(input("Enter your budjet:"))
        Thanjavur(name,place,days,budjet)

    elif user==10:

        print("Vellore")
        name=input("Enter your name:").lower().strip()
        place="Vellore"
        days=int(input("Enter how many days:"))
        budjet=int(input("Enter your budjet:"))
        Vellore(name,place,days,budjet)

    else:

        print("choice only 1 to 10")

except:
    print("give me numbers only")
