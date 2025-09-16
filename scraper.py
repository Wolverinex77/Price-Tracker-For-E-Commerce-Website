from categories import build_product_url, select_category
from product_catalog import my_categories
from scraper_utils import handle_request,scrape_category_product_data
from rich.progress import Progress

def scrape_full_category():
    MAX_PAGE = 12
    MIN_PAGE=  1
    page=MIN_PAGE
    all_prod_data = []


    category_name = select_category(my_categories)
    

    if category_name != 'BACK':
        with Progress() as progress:
            task = progress.add_task("[green]Scraping pages...", total=MAX_PAGE)
            while page != MAX_PAGE :
                url, _ = build_product_url(category_name, page)
                print(url)
                response = handle_request(url)
                product_data = scrape_category_product_data(response, url)
                all_prod_data.extend(product_data)
                page += 1
                progress.update(task, advance=1) 

    return all_prod_data,category_name


