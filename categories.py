import re
from utils import filter_instock, sort_items
from urllib.parse import quote
from display import show_category_navigation_menu, show_sort_menu, display_items, display_categories, display_brands
from product_catalog import product_brands, my_categories
from scraper_utils import handle_request,scrape_category_product_data

def refresh_items(url,page):
    #This works

    response=handle_request(url)
    product_data=scrape_category_product_data(response,url)
    display_items(product_data,page)
    return product_data



def select_category(my_categories):
    while True:

        display_categories(my_categories)

        try:
            category_number=int(input(("Enter category number: ")))
        
            if category_number == len(my_categories) + 1:
                return "BACK"        
        except ValueError:
            print("Please Enter a number ❗")
            continue
        
        if category_number in my_categories:
                category_name=my_categories[category_number]
                return category_name
        else:
            print("Invalid Number ❗ ")
        
    

def build_product_url(category_name,page):
    category_slug = category_name.replace(" ", "-").lower()
    
    if category_slug.lower() == "tv-&-home-appliances":
            
            category_slug=category_slug.replace("&","")
            name = re.sub(r'-+', '-', category_slug)
            category_slug=quote(name,safe="-").lower()

    url=f"https://priceoye.pk/{category_slug}?page={page}"
    return url,category_slug


def select_brands(brand_list,page,category_slug,category_name):
    while True:
        try:

            brand_number=int(input("Enter brand number: "))
        except ValueError:
            print("Enter a Number ! Please Try again...")
            display_brands(product_brands,category_name)
            continue
        
        if brand_number == len(brand_list) + 1:
            return "BACK"
        
        elif brand_number>=1 and brand_number<=len(brand_list):
            brand_name=brand_list[brand_number].lower().strip()
            url=f"https://priceoye.pk/{category_slug}/{brand_name}"
            brand_items=refresh_items(url,page)
            return brand_items
            
        else:
            print("Invalid Brand Name ! Please Try again...")
            display_brands(product_brands,category_name)
            continue


def get_categories():
    MIN_PAGE=1
    MAX_PAGE=26
    page=MIN_PAGE
    category_name=select_category(my_categories)
    if category_name == "BACK":
        return
    #go back to main navigation
    url,category_slug=build_product_url(category_name,page)
    product_data=refresh_items(url,page)
    while True:

        choice=show_category_navigation_menu()
    
        if choice=="1":
                #Next Page
                if page<MAX_PAGE:
                        page+=1
                        product_data=refresh_items(url,page)
                else:
                        print("❗ Limit Exceeded")
        elif choice == "2":
                # Previous Page
                if page>MIN_PAGE:
                    page-=1
                    product_data=refresh_items(url,page)
                else:
                    print("❗ Already at the first page.")
        elif choice=="3":
            #filter brands.
            brands_list=display_brands(product_brands,category_name)

            brand_choice=select_brands(brands_list,page,category_slug,category_name)
            if brand_choice == "BACK":
                continue
             # return to the nav menu

        elif choice=="4":
            filtered_items=filter_instock(product_data)
            if filtered_items=="Not instock":
                print("Sorry No stock available right now... :(")
            else:
                print("Filtering In-Stock...")
                display_items(filtered_items,page)
        elif choice=="5":
                choice=show_sort_menu()
                if choice=="1":
                    print("Sorting from Low to High...")
                    asc_sorted_items=sort_items(product_data,order="asc")
                    display_items(asc_sorted_items,page)

                elif choice=="2":
                    print("Sorting From High to Low...")
                    dec_sorted_items=sort_items(product_data,order="dec")
                    display_items(dec_sorted_items,page)

                elif choice=="3":
                    print("Returning to Navigation Menu...")
                    show_category_navigation_menu()

        elif choice=="6":
            return get_categories() 
            
        elif choice=="7":
            return 

    