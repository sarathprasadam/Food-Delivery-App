class foodapp:
    admin_dict={'admin':'admin'}
    member_dict={}
    food_dict={'f1':['Tandoori Chicken','4 pieces',240,5,5],
           'f2':['Vegan Burger','1 piece',320,6,3],
          'f3':['Truffle Cake','500 gm',900,8,4]}
    food_count=3
    @classmethod
    def register(cls):
        print("------NEW USER REGISTRATION------")                   
        s=0
        while(s!=10):
            s=0
            k=input("Mobile number= ")
            if len(k)==0:
                print("Enter any value")
            else:                    
                for i in k:
                    if ord(i) not in range(48,58):
                        print("Character not allowed in no")
                        break
                else:
                    k=int(k)
                    m=k
                    while(m!=0):
                        m=m//10            
                        s+=1
                    if s!=10:
                        print("Enter number correctly")
        mobile_no=str(k)
        if mobile_no in cls.member_dict.keys():
            print("Mobile no already registered.Login and enjoy fooding")
        else:            
            mail=input("Enter email id: ")
            name=input("Name: ")
            password=input("Enter password: ")
            ad1=input("Enter house name: ")
            ad2=input("Enter Street name: ")
            ad3=input("Enter place: ")
            ad4=[ad1,ad2,ad3]
            cls.member_dict[mobile_no]=[password,name,mail,ad4,{}]
    
    @classmethod
    def administrator(cls):
        id1=input("Enter username: ")
        if id1 in cls.admin_dict.keys():
            id2=input("Enter password: ")
            if cls.admin_dict[id1]==id2:
                print("Login successfull")
                tst1=True
                while tst1:
                    print("--------------------------")
                    print("Enter 1 to add new item")
                    print("Enter 2 to view list of item")
                    print("Enter 3 to remove a food item")
                    print("Enter 4 to Edit food item")
                    print("Enter 5 to logout")
                    inp1=input()
                    if inp1 not in ['1','2','3','4','5']:
                        print("Invalied entry")
                    elif inp1=='1':
                        print("----New food details----")
                        fd_name=input("Enter food name: ")
                        fd_quan=input("Enter food Quantity: ")
                        tst2=True
                        while tst2:
                            fd_price=input("Enter price: ")
                            for i in fd_price:
                                        if ord(i) not in range(48,58):
                                            print("Character not allowed in no of copies")
                                            break
                                        else:
                                            tst2=False
                                            fd_price=int(fd_price)                        
                        tst6=True
                        while tst6:
                            fd_disc=input("Enter discount for food: ")
                            for ww in fd_disc:
                                if ord(ww) not in range(48,58):
                                    print("Character not allowed in no of copies")
                                    break
                                else:
                                    tst6=False
                                    fd_disc=int(fd_disc)
                        tst7=True
                        while tst7:
                            fd_stock=input("Enter stock: ")
                            for ww in fd_stock:
                                if ord(ww) not in range(48,58):
                                    print("Character not allowed in no of copies")
                                    break
                                else:
                                    tst7=False
                                    fd_stock=int(fd_stock)

                        
                        cls.food_count+=1
                        cls.food_dict['f'+str(cls.food_count)]=[fd_name,fd_quan,fd_price,fd_disc,fd_stock]
                        print("Item added successfully")
                    elif inp1=='2':
                        print("---Menu of Restaurant---")
                        for fd in cls.food_dict.keys():
                            print("Food id: ",fd)
                            print("Name: ",cls.food_dict[fd][0])
                            print("Quantity: ",cls.food_dict[fd][1])
                            print("Price: ",cls.food_dict[fd][2])
                            print("Discount given: ",cls.food_dict[fd][3])
                            prafdsa=cls.food_dict[fd][2]-((cls.food_dict[fd][2] * cls.food_dict[fd][3])/100)
                            print("Price after discount: ",prafdsa)
                            print("Stock: ",cls.food_dict[fd][4])
                            print("------------------------------------")
                    elif inp1=='3':
                        print("FOOD DELETION PAGE")
                        dltid=input("Enter food id: ")
                        if dltid in cls.food_dict.keys():
                            print("Do you want to remove ",cls.food_dict[dltid][0])
                            print("If so press 1 else press any other key")
                            dltst=input()
                            if dltst=='1':
                                cls.food_dict.pop(dltid)
                                print("Food item removed successfully")
                            else:
                                print("Food deletion cancelled")
                        else:
                            print("Wrong food id")
                    elif inp1=='4':
                        print("----FOOD EDITING PAGE----")
                        fdeditid=input("Enter food id: ")
                        if fdeditid not in cls.food_dict.keys():
                            print("Invalied Food id")
                        else:
                            print("Food details")
                            print("Food id: ",fdeditid)
                            print("Name: ",cls.food_dict[fdeditid][0])
                            print("Quantity: ",cls.food_dict[fdeditid][1])
                            print("Price: ",cls.food_dict[fdeditid][2])
                            print("Discount given: ",cls.food_dict[fdeditid][3])
                            print("Stock: ",cls.food_dict[fdeditid][4])
                            edttst=True
                            while edttst:                                
                                print("------------------------------------")
                                print("Press 1 to edit food name")
                                print("Press 2 to edit food Quantity")
                                print("Press 3 to edit food Price")
                                print("Press 4 to edit food Discount")
                                print("Press 5 to edit food Stock")                                
                                print("Press 6 if you finished editing")
                                edt=input()
                                if edt not in ['1','2','3','4','5','6']:
                                    print("Invalied entry")
                                elif edt=='1':
                                    newfdn=input("Enter food name: ")
                                    cls.food_dict[fdeditid][0]=newfdn                                    
                                elif edt=='2':
                                    newfdq=input("Enter quantity: ")
                                    cls.food_dict[fdeditid][1]=newfdq
                                elif edt=='3':
                                    tst10=True
                                    while tst10:
                                        newfdp=input("Enter price: ")
                                        for i in newfdp:
                                                    if ord(i) not in range(48,58):
                                                        print("Character not allowed in no of copies")
                                                        break
                                                    else:
                                                        tst10=False
                                                        newfdp=int(newfdp)          
                                    #newfdp=input("Enter Price: ")
                                    cls.food_dict[fdeditid][2]=newfdp
                                    
                                elif edt=='4':
                                    tst11=True
                                    while tst11:
                                        newfdd=input("Enter discount for food: ")
                                        for ww in newfdd:
                                            if ord(ww) not in range(48,58):
                                                print("Character not allowed in no of copies")
                                                break
                                            else:
                                                tst11=False
                                                newfdd=int(newfdd)
                                    #newfdd=input("Enter Discount: ")
                                    cls.food_dict[fdeditid][3]=newfdd
                                    
                                elif edt=='5':
                                    tst12=True
                                    while tst12:
                                        newfds=input("Enter stock: ")
                                        for ww in newfds:
                                            if ord(ww) not in range(48,58):
                                                print("Character not allowed in no of copies")
                                                break
                                            else:
                                                tst12=False
                                                newfds=int(newfds)
                                    #newfds=input("Enter stock: ")
                                    cls.food_dict[fdeditid][4]=newfds                                 
                                
                                   
                                elif edt=='6':
                                    print("Food editing completed")
                                    edttst=False
                            
                            
                                  
                            
                    elif inp1=='5':
                        tst1=False
                        print("Logged out successfully")                                             
                    
              
            else:
                print("Wrong password")            
        else:
            print("Invalied username")
    
    @classmethod
    def memberside(cls):
        minp1=input("Enter mobile no: ")
        if minp1 in cls.member_dict.keys():
            minp2=input("Enter password: ")
            if cls.member_dict[minp1][0]==minp2:
                mtst=True
                while mtst:
                    
                    print("Print 1 to place new order")
                    print("Press 2 to see order history")
                    print("Press 3 to update Profile")
                    print("Press 4 to log out")
                    minp3=input()
                    if minp3 not in ['1','2','3','4']:
                        print("Invalied input")
                    elif minp3=='1':
                        print("List of food available at restaurant")
                        for l in cls.food_dict.keys():
                            fdno=l[1]
                            print("Food no: ",fdno,"Name: ",cls.food_dict[l][0])
                            print("Quantity: ",cls.food_dict[l][1])
                            print("Price: ",cls.food_dict[l][2])
                            print("Discount given: ",cls.food_dict[l][3])
                            print("Stock: ",cls.food_dict[l][4])
                            print("---------------------------")
                        print("Enter food item no  you want to order in [1,2,3.....] format")                        
                        fd_ord1=input()
                        fd_ord=[]
                        m=len(fd_ord1)
                        k=1
                        hmt=0
                        while(k<m):
                            fd_ord.append(fd_ord1[k])
                            k+=2
                        #print("List of item selected")
                        to=0
                        for ad in fd_ord:
                            print("List of item selected")
                            fd_ordid='f'+ad
                            if fd_ordid in cls.food_dict.keys():
                                if cls.food_dict[fd_ordid][4]>0:
                                    print("Name: ",cls.food_dict[fd_ordid][0])
                                    print("Quantity: ",cls.food_dict[fd_ordid][1])
                                    print("Price: ",cls.food_dict[fd_ordid][2])
                                    print("Discount given: ",cls.food_dict[fd_ordid][3])
                                    prafds=cls.food_dict[fd_ordid][2]-((cls.food_dict[fd_ordid][2] * cls.food_dict[fd_ordid][3])/100)
                                    print("Price after discount: ",prafds)
                                    to=to+prafds
                                else:
                                    print("Food out of stock")
                                    hmt=1
                                    break
                            else:
                                print("Incorrect format")
                                hmt=1
                                break
                            print("-----------------------------------")
                        if hmt==0:
                            print("Total Price: ",to)
                            print("Press 1 to confirm order")
                            ordrinp=input()
                            if ordrinp=='1':
                                print("Food ordered successfully")
                                gb=[]
                                for ak in fd_ord:
                                    fd_ord1='f'+ak
                                    gb.append(fd_ord1)
                                    cls.food_dict[fd_ord1][4]-=1

                                lenfod=len(cls.member_dict[minp1][4])
                                cls.member_dict[minp1][4][lenfod+1]=gb
                        else:
                            print("Food ordering cancelled")
                                
                            
                    elif minp3=='2':
                        print("-----FOOD ORDER HISTORY-----")                        
                        for his in cls.member_dict[minp1][4].keys():
                            lll=1
                            print("Order NO: ",his)
                            for chi in cls.member_dict[minp1][4][his]:
                                print(lll,'.',cls.food_dict[chi][0])
                                lll+=1
                    elif minp3=='3':                        
                        prof=True
                        while prof:
                            print("--------------------")
                            print("Press 1 to edit Name")
                            print("Press 2 to edit Email")
                            print("Press 3 to edit Password")
                            print("Press 4 to edit Address")
                            print("Press 5 to exit editing")

                            editinp=input()
                            if editinp not in ['1','2','3','4','5']:
                                print("Invalied input")
                            elif editinp=='1':
                                nmnew=input("Enter name: ")
                                cls.member_dict[minp1][1]=nmnew
                            elif editinp=='2':
                                emnew=input("Enter email: ")
                                cls.member_dict[minp1][2]=emnew
                                
                            elif editinp=='3':
                                pwnew=input("Enter New Password: ")
                                cls.member_dict[minp1][0]=pwnew
                                pass
                            elif editinp=='4':
                                a1new=input("Enter House name: ")
                                a2new=input("Enter Street name: ")
                                a3new=input("Enter Place: ")
                                cls.member_dict[minp1][3]=[a1new,a2new,a3new]                                
                            elif editinp=='5':
                                prof=False
                                print("Editing completed")
                        
                       
                    elif minp3=='4':
                        mtst=False
                        print("Logged out successfully")
                        
                
            else:
                print("Wrong password")
        else:
            print("Invalied mobile no")
            
      
        
        
def main():
    foo = foodapp()
    foo.foodapp()

if __name__ == "__main__":
    main()