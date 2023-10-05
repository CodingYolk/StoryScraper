import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
import os

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

# Ask the user to select the folder containing HTML files
folder_path = filedialog.askdirectory(title="Select Folder")

# Create a list to store all extracted URLs
all_story_urls = []

# Get a list of all HTML files in the selected folder
html_files = [f for f in os.listdir(folder_path) if f.endswith('.html')]

# Process each HTML file and append the links to the list
for html_file in html_files:
    input_file_path = os.path.join(folder_path, html_file)
    story_urls = scrape_wattpad_reading_list(input_file_path)
    all_story_urls.extend(story_urls)

# Ask the user to select the output file path
output_file_path = filedialog.asksaveasfilename(title="Save output file", defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))

# Save all the links in a single text file
with open(output_file_path, 'w') as file:
    for url in all_story_urls:
        file.write(url + '\n')

print(f"All links saved to {output_file_path}")
