import requests,time
from bs4 import BeautifulSoup
import urllib.parse
def handle_request(url):
    API_TOKEN = "69aa72a0e0f945e2bd467f2193aa8c2969e9d465fe4"
    USE_PROXY = True   #Change to True to Turn on Proxy
    try:
        if USE_PROXY:
            encoded_url = urllib.parse.quote(url, safe="")
            proxy_url = f"http://api.scrape.do/?token={API_TOKEN}&url={encoded_url}"
            response = requests.get(proxy_url, timeout=30)

        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                      }

        response=requests.get(url,headers=headers,timeout=10)

        response.raise_for_status()
        print("Searching...")
        time.sleep(5)
        return response

    except requests.exceptions.ConnectionError as e:
            print(f"Network Problem.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")  

    except TimeoutError:
        print("Request Timeout")

def scrape_category_product_data(response,url):
    page=BeautifulSoup(response.content,"html.parser")
    products=page.find_all("div",class_="productBox b-productBox")
    my_items=[]
    
    for product in products:

        out_of_stocks=product.find("div",id="stock-badge") #Fetches Out of stocks
        if out_of_stocks:
            out_of_stocks.img["alt"]
            status="❌🔴 Out of Stock"
        else:
            status="✅🟢 In Stock"

        if "tv-home-appliances" not in url:
            title_tag=product.find("div",class_="p-title p-title-center bold h5")
        else:
            title_tag=product.find("div",class_="p-title bold h5")
        title = title_tag.getText(strip=True) if title_tag else "No title found"
        price_tag=product.find("div",class_="price-box p1")
        price=price_tag.getText(strip=True) if price_tag else "No title found"
        link=product.a["href"]
        
        my_items.append(
            {
        "Title": title,
        "Price": price,
        "Link": link,
        "Status":status
                        })
    return my_items

def scrape_search_product_data(response,product_name):
    page=BeautifulSoup(response.content,"lxml")
    products=page.find_all("div",class_="productBox b-productBox")
    my_items=[]

    for product in products:
        out_of_stocks=product.find("div",id="stock-badge") 
        if out_of_stocks:
            out_of_stocks.img["alt"]
            status="❌🔴 Out of Stock"
        else:
            status="✅🟢 In Stock"
         
        title=product.find("div",class_="p-title bold h5").getText(strip=True)
        price=product.find("div",class_="price-box p1").getText(strip=True)
        link=product.a["href"]
        
        if product_name in title.lower():
    
            my_items.append({
            "Title": title,
            "Price": price,
            "Link": link,
            "Status":status
        })

        
        
    return my_items
