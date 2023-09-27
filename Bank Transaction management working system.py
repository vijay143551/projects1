# Banking Transaction management  system:-


customer_names=['VIJAY PALEM','MAHESH .Y','HAMEEDH Y','HARI ','DHARMA']
customer_pins=['5121','1432','1234','7891','4321']
customer_balance=[20000,30000,40000,50000,6000]
deposit=0
withdraw=0
balance=0
counter_1=1
counter_2=5
i=0

# this is hlps the prgrm to run contiuesly:-

while True:
    print('=============================================================')
    print('-------------welcome to STATE BANK OF INDIA -----------------')
    print('==============================================================')
    print('1.open new bank')
    print('2.withdraw money')
    print('3.Deposit money')
    print('4. check customers and balance')
    print('Exit/Quit')
    print(20*'-')

# the below statement takes choice numbers of users:-
    
    choice_numbers = input('select your choic numbers from above menu :')
    if choice_numbers =='1':
        print('choice number  1 is selected by the customer')

# the line below will take np.of customers from user

        noc=eval(input('Number of customers:'))
        i=i+noc


# the if condition will restrict the no.of new account to 5:

        if i > 5:
            print('\n')
            print('customers registration Exceed reached')
            i=i-noc
        else:
            while counter_1<=i:
                name=input('INPUT FULLNAME :')
                customer_names.append(name)
                pin=str(input("please enter a pin :"))
                customer_pins.append(pin)
                balance=0
                deposit=eval(input('please deposit a min amount to create a new account :')) 
                balance=balance+deposit
                customer_balance.append(balance)
                print('name=',end='')
                print(customer_names[counter_2])
                print('pin=',end='')
                print(customer_pins[counter_2])
                print('Balance=',end='')
                print(customer_balance[counter_2], end=" ")       
                print('-\Rs')
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1 
                print('\your name is added to the customer system:-')
                print('\your pin is added to the customer system:-')
                print('\your Balance is added to the customer system:-')
                print('--------New account is created Successfull-------')
                print('your name is available in the customers list below:-')
                print(customer_names)
                print('\n')
                print('please note your name and pin')
                print(20*'=')
        mainmenu=input('please press enter key to go back to main menu to perform another function or EXIT : ')
    elif choice_numbers == '2':
         j=0
         print("choice number 2 is selected by the customer")
         while j<1:
              k = -1
              name = input('Enter input name:')
              pin = input('Enter input pin:')
              while k < len(customer_names) - 1:
                  k = k + 1
                  if name == customer_names[k]:
                     if pin == customer_pins[k]:
                        j = j + 1
                        print("your current balance:",end='')
                        print('-/Rs',customer_balance[k])
                        # print("-Rs\n")
                        balace=customer_balance[k]
                        withdraw=eval(input("input a amount to withdraw:"))
                        if withdraw > balance:
                            deposit=eval(input("your account Balance is Low please deposit a higher value of amount:"))
                            balance=balance+deposit
                            print("your current balance:",end='')
                            print(balance,end='')
                            print("-/Rs\n")
                            balance=balance-withdraw
                            print('\n')
                            print("---------withdraw successfull!-------")
                            customer_balance[k]=balance
                            print("your new balance:",balance,end='')
                            print("-Rs\n\n")

                        else:  #balance > withdraw
                            balance=balance-withdraw
                            print("\n")
                            print("----------withdraw Successfull!---------")
                            customer_balance[k]=balance
                            print("your new balance:",balance,end='')
                            print("-Rs\n\n")
              if j < 1: # when name/pin is wrong:-
                     print('your name and pin dors not match with our record:-')
                     break
         mainmenu=input('please press enter key to go back to main menu to perform another function or EXIT')
    elif choice_numbers == '3':
         print("choice 3 is selected by the customer:")
         n=0
         while n < 1: # when pin/name is wrong:-
               k=-1
               name=input('enter input name:')
               pin=input('enter input pin:')
               while k < len(customer_names)-1:
                  k=k+1
                  if name == customer_names[k]:
                     if pin == customer_pins[k]:
                        n=n+1
                        print("your current balance:",end='')
                        print(customer_balance[k])
                        print("-Rs\n")
                        balace=customer_balance[k]
                        deposit=eval(input("enter the amount yuou want to deposit into your accoint:-"))
                        balance=balance+deposit
                        customer_balance[k]=balance
                        print('\n')
                        print("--------deposit Successfull!--------")
                        print("your new balnace:", balance,end="")
                        print("-/Rs\n\n")
               if n < 1:
                  print("your name / pin does not match:-")
                  break                  
         mainmenu=input('please press enter key to go back to main menu to perform another function or EXIT')
    
    elif choice_numbers == '4': #(check customer and balace)
         print("choice number 4 is selected by the customer:")
         k=0
         print("customer name list and balance mentioned below:")
         print('\n')
         while k <= len(customer_names) - 1:
               print("customer=",customer_names[k])
               print('Balance=',customer_balance[k])
               print('-/Rs')
               print("\n")
               k=k+1
         mainmenu=input('please press enter key to go back to main menu to perform another function or EXIT') 
    elif choice_numbers == '5':
         print("choice number 5 is selected by customer:")
         print('Thank you for using our BANKING system:')
         print('\n')
         print('Come again')
         break
    else: # when wrong function is choosen:-
         print("INVALID option selected by customer")
         print("please try again:")
         mainmenu=input('please press enter key to go back to main menu to perform another function or EXIT')

        
 

        

                 








