import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from rich.panel import Panel

console = Console()

def show_main_menu():
    valid_choices=["1","2","3","4","5","6","7"]
    while True:
        menu_text = Text()
        menu_text.append("[1] Search for a Product by Name\n", style="bold white")
        menu_text.append("[2] Browse by Category (Mobiles, etc.)\n", style="bold white")
        menu_text.append("[3] Toggle Email Alerts\n", style="bold white")
        menu_text.append("[4] Quit\n", style="bold red")

        panel = Panel(
        menu_text,
        title="[bold white]💰 Welcome to PriceCheck[/]",
        title_align="center",
        border_style="bright_yellow",
        expand=False, 
        padding=(1, 5) 
        )
        console.print(panel)
        
        choice=input("🔸 Enter your choice (1-6): ")
        if choice in valid_choices:
            return choice
        else:
            print("❌ Invalid choice. Please select a number from 1 to 6.\n")

def show_search_navigation_menu():
    valid_choices=["1","2","3","4","5","6"]
    while True:
    
        menu_text=Text()
        menu_text.append("[1] Next Page\n", style="bold white")
        menu_text.append("[2] Previous Page\n", style="bold white")
        menu_text.append("[3] Sort by Price\n",style="bold white")
        menu_text.append("[4] Filter In-Stock Only\n",style="bold white")
        menu_text.append("[5] Change Product\n",style="bold white")
        menu_text.append("[6] Back to Main Menu\n",style="bold white")
        panel = Panel(
                menu_text,
                title="🧭 Search Navigation Menu",
                title_align="center",
                border_style="bright_yellow",
                expand=False,  
                
                    )
        console.print(panel)
        choice=input("🔸 Enter your choice (1-7): ")
        if choice in valid_choices:
            return choice
        else:
            print("❌ Invalid choice. Please select a number from 1 to 6.\n")
    

def show_category_navigation_menu():
        while True:
            valid_choices=["1","2","3","4","5","6","7"]
            menu_text=Text()

            menu_text.append("[1] Next Page\n")
            menu_text.append("[2] Previous Page\n")
            menu_text.append("[3] Filter by Brand\n")
            menu_text.append("[4] Filter In-Stock Only\n")
            menu_text.append("[5] Sort by Price\n")
            menu_text.append("[6] Change Category\n")
            menu_text.append("[7] ", style="red")
            menu_text.append("Back to Main Menu\n", style="red")
            panel = Panel(
                menu_text,
                title="🧭 Category Navigation Menu",
                title_align="left",
                border_style="bright_yellow",
                expand=False
            )

            console.print(panel)

            choice=input("🔸 Enter your choice (1-7): ")
            if choice in valid_choices:
                return choice
            else:
                print("❌ Invalid choice. Please select a number from 1 to 7.\n")
                
def show_sort_menu():
    valid_choice=["1","2","3"]
    while True:
        console.print("""
                    📊 Sort Options:
                    [1] Price: Low to High
                    [2] Price: High to Low
                    [3] Back to Navigation Menu
                    """)
        choice = input("Enter your choice (1-3): ")

        if choice in valid_choice:
            return choice
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.\n")

def display_items(my_items,page,MAX_LIMIT=36):
    console.print(f"Displaying Page [bold green]{page}/{MAX_LIMIT}...")
    
    if my_items:
        console.print(f"[bold green]✅ Results found![/]\n")
        time.sleep(5)
        
    else:
        console.print(f"[bold red]❌ No results found ! ")
        
    for index, item in enumerate(my_items, start=1):
        console.print(f"🛒 [bold white]Title[/]: {index}. {item['Title']}")
        console.print(f"💰 [bold green]Price[/]: {item['Price']}")
        console.print(f"🔗 [blue underline]Link[/]: {item['Link']}")
        console.print(f"📦 [bold white]Stock[/]: {item['Status']}")
        console.print("-" * 60)  # separator between items

def display_categories(my_categories):

        category_text = Text()
        for idx, value in my_categories.items():
                category_text.append(f"[{idx}] ", style="cyan")
                category_text.append(f"{value}\n",style="bold bright_white")

        back_option = len(my_categories) + 1
        category_text.append(f"[{back_option}] ", style="cyan")
        category_text.append("Back to Main Menu", style="bold red")

        panel = Panel(
            category_text,
            title="Categories",
            border_style="bright_yellow",
            box=box.ROUNDED,
            expand=False
        )
        console.print(panel)
    


def display_brands(product_brands,category_name):
        brands_text=Text()
        brands_list={}
        category_list=product_brands[category_name] #Gets the list of items
        back_option = len(category_list) + 1

        for i,brand_names in enumerate(category_list):
            brands_text.append(f"[{i+1}] ", style="cyan")
            brands_text.append(f"{brand_names}\n",style="bold bright_white")
            brands_list[i+1]=brand_names

        brands_text.append(f"[{back_option}] ", style="cyan")
        brands_text.append("Back to Category Menu", style="bold red")

        panel = Panel(
            brands_text,
            title="Brands List",
            border_style="bright_yellow",
            box=box.ROUNDED,
            expand=False
        )
        console.print(panel)
        return brands_list