def bill( kilo):
     pay=0
     if(kilo<=5):
        pay=25
     print(pay)
 else:
     pay=5*25+(kilo-5)*17
     print(pay)
print("1.avadi")
print("2.parthipattu")
print("3.melpakkam")
print("4.sekkadu")
print("5.porur")
 a=input("enter destination")
if(a==1):
    print("1.avadi")
    bill(5)
elif(a==2):
    print("porur")
    pay(11)
elif(a==3):
    print("avadi")
    pay(11)
