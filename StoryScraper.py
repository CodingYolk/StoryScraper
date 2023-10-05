import requests
from bs4 import BeautifulSoup

def scrape_wattpad_reading_list(url):
    # Send a GET request to the reading list URL
    response = requests.get(url)
    response.raise_for_status()

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the story links in the reading list
    story_links = soup.find_all('a', {'class': 'readingListStoryTitle'})

    # Extract the URLs from the story links
    urls = [link['href'] for link in story_links]

    return urls

# Prompt the user for the file path to save the links
file_path = input("Enter the file path to save the links (e.g., C:/path/to/file.txt): ")

# Example reading list URL
reading_list_url = 'https://www.wattpad.com/list/75170794-paranormal-romance'

# Scrape the story URLs
story_urls = scrape_wattpad_reading_list(reading_list_url)

# Save the links in a text file
with open(file_path, 'w') as file:
    for url in story_urls:
        file.write(url + '\n')

print("Links saved to", file_path)
