from search import search_data
from display import show_main_menu
from mail import mail
from categories import get_categories

def main():
    while True:
        user_input=show_main_menu()

        if user_input=="1":
            search_data()
         
        elif user_input=="2":
            get_categories()
            
        elif user_input=="3":
            mail()
            
            
        elif user_input=="4":
            print("Good bye 😊")
            exit()
    
        
        
if __name__ == "__main__":
    main()







