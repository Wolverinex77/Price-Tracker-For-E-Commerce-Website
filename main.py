from search import search
from categories import categories
from display import show_main_menu

def main():
    while True:
        user_input=show_main_menu()

        if user_input=="1":
            search()
        
        elif user_input=="2":
            categories()
            
        elif user_input=="3":
            #send email
            print("To be done in the future 😊 ")
            
            
        elif user_input=="4":
                print("Good bye 😊")
                exit()
    
        
        
if __name__ == "__main__":
            main()







