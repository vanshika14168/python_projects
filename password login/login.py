c_pass="vanshu123"

for i in range(1,4):
    
    password=input("enter password:")
    if password==c_pass:
        print("right password")
        print("login successfully")
        break
        
    else:
        print("wrong password")
        print("you have only ",3-i," attempt\nplease try again.")