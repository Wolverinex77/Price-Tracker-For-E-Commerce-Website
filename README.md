# CS50 Final Project – PriceOye Product Tracker

#### Video Demo: [https://youtu.be/z-EEepP9CvI](https://youtu.be/z-EEepP9CvI)

#### Description:

## Introduction

This is my final project for **CS50’s Introduction to Programming with Python**.  
It’s a **Product Catalog & Price Tracker** that scrapes product information from **PriceOye**, a popular e-commerce site in Pakistan for electronics (mobiles, laptops, gadgets).

### Users can:
- Search for products by keyword  
- Browse items by category  
- (Coming soon) Receive product info via email  
- Exit the program  

I chose this project because I’m interested in automation and scripting. I wanted to explore how Python can be used to scrape and process real-world data, while also building something practical. With this program, users can enter any product and instantly get real-time data about it.  

This project has the potential to grow into a real-world tool that solves everyday problems, such as comparing prices or tracking sales.

---

## Project Overview

The project runs in the terminal with a **menu-driven interface powered by the `rich` library**.  
Data is scraped in real time using **`requests` + `BeautifulSoup`**.

### Main Features
- **Search for products** – find items by keyword  
- **Browse categories** – explore products grouped into categories/brands  
- **Future Email Support** – send product info via email  
- **Exit** – closes the program  

### Proxy for Geo-Restrictions
Since PriceOye is only accessible from Pakistan, I added a **proxy system** in `scraper.py` (using an API token).  
This allows the program to fetch product data even if it’s run outside Pakistan.

---

## Requirements

- Python 3.8+  
- requests  
- beautifulsoup4  
- rich  
- lxml  

---

## How to Run

You can run the program in two ways:

### Option 1: Clone via Git

1. Make sure you have Python 3 installed.  
2. Clone the repository:  
   ```bash
   git clone https://github.com/Wolverinex77/Price-Tracker-For-E-Commerce-Website.git
   cd Price-Tracker-For-E-Commerce-Website

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt

4. Run the program:
   ```bash
python main.py


### Option 2: Run via IDE

1. Download or clone the repository.

2. Open the folder in your IDE (PyCharm, VS Code, Thonny).

3. Install the requirements.
   ```bash
pip install -r requirements.txt
   
4. Run main.py directly from the IDE.



## File Overview

* `main.py` – entry point; shows the main menu and runs the program
* `scraper.py` – fetches product data from websites
* `product_catalog.py` – manages product information
* `categories.py` – handles product categories
* `search.py` – implements the search function
* `display.py` – displays the menu and product information
* `mail.py` – placeholder for future email feature
* `utils.py` – helper functions used throughout the project
* `requirements.txt` – list of Python libraries

---

## Design Choices

* I split the project into multiple modules instead of one big file, which makes it easier to extend later.
* I used `requests` + `BeautifulSoup` instead of Selenium because they’re faster and lighter for this type of scraping.
* I chose the `rich` library to make the terminal interface cleaner and more user-friendly.

---

## Challenges & Learning

The hardest part of this project was **web scraping**, because I wasn’t familiar with it at all. I had to do a lot of trial and error to figure out how to correctly fetch and parse data from the website.

Another big challenge was **structuring the code into multiple modules**. At first, I tried to keep everything in one place, but that made the program messy and difficult to manage. Splitting logic into `scraper.py`, `search.py`, `display.py`, and other files took more effort, but resulted in much cleaner code.

This project took me **over a month** to complete, because I had to keep testing, fixing, and reorganizing until everything worked properly.

### What I Learned

* How to scrape and parse HTML data with BeautifulSoup
* How to structure a larger Python program across multiple files
* How automation can solve real-world problems

---

## Future Improvements

* **Email support**: Expand `mail.py` so users can receive product data via email
* **More sites**: Add scraping from multiple e-commerce platforms
* **CSV Export**: Save and track historical data
* **GUI**: Add a graphical user interface for non-technical users

---

## Conclusion

This project reflects my interest in automation and web scraping, while also solving a real-world problem: quickly accessing product information.

It’s a foundation that can be expanded into a bigger tool for tracking prices, comparing platforms, or even monitoring sales over time.

```

