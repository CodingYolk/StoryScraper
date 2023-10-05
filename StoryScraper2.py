import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup

def scrape_wattpad_reading_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the HTML content from the file
        html_content = file.read()

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the story links in the reading list
    story_links = soup.find_all('a', {'class': 'cover cover-sm pull-left on-navigate'})

    # Extract the URLs from the story links
    urls = [link['href'] for link in story_links]

    return urls

# Create the Tkinter root window
root = tk.Tk()
root.withdraw()

# Ask the user to select the input HTML file
input_file_path = filedialog.askopenfilename(title="Select HTML file", filetypes=(("HTML files", "*.html"), ("All files", "*.*")))

# Scrape the story URLs
story_urls = scrape_wattpad_reading_list(input_file_path)

# Ask the user to select the output file path
output_file_path = filedialog.asksaveasfilename(title="Save output file", defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

# Save the links in a text file
with open(output_file_path, 'w') as file:
    for url in story_urls:
        file.write(url + '\n')

print("Links saved to", output_file_path)
