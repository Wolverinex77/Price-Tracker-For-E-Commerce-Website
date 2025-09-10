import time


def sort_items(items,order):
    if order=="asc":
        sorted_items=sorted(items,key=lambda x: int(x["Price"].replace("Rs", "").replace(",", "").strip()))
    else:
        sorted_items=sorted(items,key=lambda x: int(x["Price"].replace("Rs", "").replace(",", "").strip()),reverse=True)
    return sorted_items
  
def filter_instock(items):

    my_filter_stocks=[]
    for item in items:
        if item["Status"]=="✅🟢 In Stock":
            my_filter_stocks.append(item)
    
    #If all-stocks are empty
    if not my_filter_stocks:
        return "Not instock"
    else:
        return my_filter_stocks
