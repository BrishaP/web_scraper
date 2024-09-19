# print("Hello, World!")
# import requests
# from bs4 import BeautifulSoup

# # Step 1: Send a GET request to the website
# url = "https://en.wikipedia.org/wiki/Marvel_Comics"
# response = requests.get(url)

# # Step 2: Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# # Step 3: Find all the book items on the page
# # books = soup.find_all('article', class_='product_pod')

# # # Step 4: Loop through each book and extract the title and price
# # for book in books:
# #     # Extract the book title
# #     title = book.h3.a['title']
    
# #     # Extract the book price
# #     price = book.find('p', class_='price_color').text
    
# #     # Print the extracted data
# #     print(f"Title: {title}, Price: {price}")

# # Step 5: Find all the header elements (h1, h2, h3, h4, h5, h6)
# header_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
# headers = soup.find_all(header_tags)

# # Step 6: Loop through each header and print the text content
# for header in headers:
#     # Print the header tag name and its text
#     print(f"{header.name}: {header.get_text(strip=True)}")

#     # Step 3: Find all the <p> elements
# paragraphs = soup.find_all('p')

# # Step 4: Loop through each <p> element and print the text content
# for paragraph in paragraphs:
#     # Print the paragraph text
#     print(paragraph.get_text(strip=True))

# import requests
# from bs4 import BeautifulSoup
# from transformers import pipeline

# # Step 1: Fetch HTML content from a webpage
# url = "https://en.wikipedia.org/wiki/The_Rampaging_Hulk"  # Replace with the URL you want to scrape
# response = requests.get(url)
# html_content = response.content

# # Step 2: Parse HTML and extract text
# soup = BeautifulSoup(html_content, "html.parser")
# text = soup.get_text()

# # Optional: Clean and preprocess the text (e.g., remove extra whitespace, etc.)
# clean_text = ' '.join(text.split())

# # Step 3: Load the summarization pipeline from Hugging Face
# summarizer = pipeline("summarization")

# # Step 4: Split the text into smaller chunks
# max_chunk_length = 1024  # Maximum sequence length for the model
# chunks = [clean_text[i:i + max_chunk_length] for i in range(0, len(clean_text), max_chunk_length)]

# # Step 5: Summarize each chunk
# summaries = []
# for chunk in chunks:
#     summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
#     summaries.append(summary[0]['summary_text'])

# # Step 6: Combine and print the summarized text
# combined_summary = ' '.join(summaries)
# print("Summary:")
# print(combined_summary)


import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Step 1: Fetch HTML content from a webpage
url = "https://www.amazon.co.uk/"  # Replace with the URL you want to scrape
response = requests.get(url)
html_content = response.content

# Step 2: Parse HTML and extract text
soup = BeautifulSoup(html_content, "html.parser")
text = soup.get_text()

# Optional: Clean and preprocess the text (e.g., remove extra whitespace, etc.)
clean_text = ' '.join(text.split())

# Step 3: Load the summarization pipeline from Hugging Face
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", revision="a4f8f3e")

# Step 4: Split the text into smaller chunks
max_chunk_length = 1024  # Maximum sequence length for the model
chunks = [clean_text[i:i + max_chunk_length] for i in range(0, len(clean_text), max_chunk_length)]

# Step 5: Summarize each chunk
summaries = []
for chunk in chunks:
    summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False, clean_up_tokenization_spaces=True)
    summaries.append(summary[0]['summary_text'])

# Step 6: Combine and print the summarized text
combined_summary = ' '.join(summaries)
print("Summary:")
print(combined_summary)

