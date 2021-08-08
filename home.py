from background import foodapp
def home1():
    print("EDYODA RESTAURANT")
    print("\n")
    hmtst=True
    while hmtst:        
        print("Press 1 for admin login")
        print("Press 2 for user login")
        print("Press 3 for new user registration")
        print("Press 4 to exit application")
        tol=input()
        if tol not in ['1','2','3','4']:
            print("Invalied input")
        elif tol=='1':
            foodapp.administrator()
        elif tol=='2':
            foodapp.memberside()
        elif tol=='3':
            foodapp.register()
        elif tol=='4':
            hmtst=False

def main():
    foo = home1()
    

if __name__ == "__main__":
    main()            