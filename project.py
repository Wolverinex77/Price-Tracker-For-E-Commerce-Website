from search import search_data
from display import show_main_menu
from mail import mail
from categories import get_categories


def run_search():
    """Handle the search option."""
    print("Running search...")
    search_data()


def run_categories():
    """Handle categories option."""
    print("Fetching categories...")
    get_categories()


def run_mail():
    """Handle mailing option."""
    print("Sending mail...")
    mail()


def main():
    while True:
        user_input = show_main_menu()

        if user_input == "1":
            run_search()
        elif user_input == "2":
            run_categories()
        elif user_input == "3":
            run_mail()
        elif user_input == "4":
            print("Good bye 😊")
            exit()


if __name__ == "__main__":
    main()
