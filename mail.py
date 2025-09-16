import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from scraper import scrape_full_category
import validators
load_dotenv()


# Gmail credentials
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def mail():
    email=input("Enter your email: ").strip()
    valid=validators.email(email)
    if valid==True: 
        to_email = email
    else:
        print("Invalid Email.")
        return #Returns to Main
    if not EMAIL or not APP_PASSWORD:
        print("Error: Environment variables for email are not set.")
        return
    
    all_prod_data,category_name = scrape_full_category()
    if category_name=="BACK":
        return
    email_body=""
    for product in all_prod_data:
        if product['Discount']>=30 and product['Status']=='✅🟢 In Stock':
                  
            email_body += (
    f"\n"
    f"🛒 {product['Title']}\n"
    f"💰 Price: {product['Price']}\n"
    f"🔥 {product['Discount']}% OFF (Original: {product['Original Price']})\n"
    f"📦 Stock: {product['Status']}\n"
    f"🔗 Link: {product['Link']}\n\n"
        )
            
    # Email 
    
    subject = f"🔥 Big Discounts: 30%+ OFF on {category_name}!"
    body = email_body

    # Create message
    msg = MIMEText(body, 'plain')
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    # Connect to Gmail SMTP server and send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()
    


  
