print("Hello, World!")
import requests
from bs4 import BeautifulSoup

# Step 1: Send a GET request to the website
url = "http://books.toscrape.com/"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Find all the book items on the page
books = soup.find_all('article', class_='product_pod')

# Step 4: Loop through each book and extract the title and price
for book in books:
    # Extract the book title
    title = book.h3.a['title']
    
    # Extract the book price
    price = book.find('p', class_='price_color').text
    
    # Print the extracted data
    print(f"Title: {title}, Price: {price}")
