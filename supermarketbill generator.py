# spermarket bill generator:-
from datetime import datetime
print()
print("==========================welcome=============================")
print()
name=input("enter your name:")
#lists of items:-
lists='''
rice     Rs 20/kg
dal      Rs 30/kg
sugar    Rs 40/kg
oil      Rs 50/kg
'''

# declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

# rates for items
items={'rice':20,'dal':30,'sugar':40,'oil':50}

option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items")
        quantity=int(input("enter quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,item,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        price("you entered wrong number")     

    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(30*"=","vijay supermarket",30*"=")
            print(25*" ","kadapa")
            print("name:",name,30*" ","date:",datetime.now())
            print(80*"=")
            print("sno",8*" ",'item',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,9*' ',9*' ',ilist[i],5*' ',qlist[i],plist[i])
                print(80*" ")
                print(60*" ",'TOTAL AMOUNT;' ,'Rs',totalprice)
                print(60*" ",'TOTAL AMOUN:','Rs',totalprice)




                    