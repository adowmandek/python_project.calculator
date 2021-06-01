
print ("DEKS hotel###")
print ("DEKSMenu\n1 Break fast\n2.lunch\n3.dinner")

opt="x"
bal=0
while(opt is "x"):
    opt1=int (input("please enter your choice(1,2,3)"))
if(opt1==1):
     print("welcome to breakfast menu")
     print ("1.chai sh 40\n2.coffe sh 30")
     opt_1=int(raw_input("please select an option(1,2)"))
     if(opt_1==1):
         print("you have selected chai enjoy! ")
         bal+=30
elif(opt1==2):
    print("you have selected coffe")
    bal+=35
else:
    print("invalid option")
elif(opt1==2):
    print("welcome to lunch lunch menu")
    print("1.rice and soup sh 60\n 2. chapati and soup sh 50")
    opt_2=int(raw_input("please select an option(1,2)"))
    if(opt_2==1):
        print(" you have selected rice and soup enjoy!")
        bal+=80
    elif(opt_2==2):
        print("you have selected chapati and vegetables")
        bal+=35
   
    else:
        "invalid option"
    elif(opt1==3):
        print("welcome to dinner menu")
        print("1.chicken and soup sh 100\n 2. vegetables sh 200")
        opt_2=int(raw_input("please select an option(1,2)"))
        if(opt_2==1):
        print(" you have selected chicken")
        bal+=180
    elif(opt_2==2):
        print(" you have selected vegetables")
        bal+=70
  
    else:
        print("invalid option")
        opt=raw_input("Do you want another orer(n/s)?"))
        print("dear customer your bill is ",bal)
        print("Thanks for coming here")