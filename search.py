from scraper_utils import handle_request, scrape_search_product_data
from utils import sort_items
from utils import filter_instock
from display import show_search_navigation_menu
from urllib.parse import quote_plus
from display import display_items
from display import show_sort_menu

def refresh_items(product_name,page):
    url=built_product_url(product_name,page)
    response=handle_request(url)
    items=scrape_search_product_data(response,product_name)
    display_items(items,page)
    return items

   
def built_product_url(user_input,page):
    url =f"https://priceoye.pk/search?q={quote_plus(user_input)}"
    
    if page==2:
        url =f"https://priceoye.pk/search?q={quote_plus(user_input)}&page={page}"

    print(url)
    return url

def search_data():
            page=1
            MAX_LIMIT=10
            MIN_LIMIT=1
            product_name=input("🔍 Enter product to search: ").strip().lower()

            items=refresh_items(product_name,page)
            while True:
                choice=show_search_navigation_menu()
                if choice == "1":
                # Next Page
                    if page<MAX_LIMIT:
                        page+=1
                        refresh_items(product_name,page)
                    else:
                        print("❗ Limit Exceeded")
                
                elif choice == "2":
                    # Previous Page
                    if page>MIN_LIMIT:
                        page-=1
                        refresh_items(product_name,page)

                    else:
                        print("❗ Already at the first page.")

                elif choice == "3":
                    # Sort by Price
                    choice=show_sort_menu()
                    if choice=="1":
                        print("Sorting from Low to High...")
                        asc_sorted_items=sort_items(items,order="asc")
                        display_items(asc_sorted_items,page)

                    elif choice=="2":
                        print("Sorting From High to Low...")
                        dec_sorted_items=sort_items(items,order="dec")
                        display_items(dec_sorted_items,page)
            
                elif choice == "4":
                    # Filter In-Stock Only
                    filtered_items=filter_instock(items)
                    print("Filtering In-Stock...")
                    display_items(filtered_items,page)

                elif choice == "5":
                    #change products
                    search_data()
                
                elif choice == "6":
                    # Quit
                    return 
                    
