import tkinter as tk
from tkinter import filedialog, messagebox
import requests
from bs4 import BeautifulSoup
import csv
import os
from urllib.parse import urljoin


def fetch_and_save_urls():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Input Error", "Please enter a URL.")
        return

    try:
        # Fetch content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all clickable URLs from anchor tags
        urls = set()  # Use a set to avoid duplicates

        # Extract links from <a> tags
        for a_tag in soup.find_all('a', href=True):
            full_url = urljoin(url, a_tag['href'])
            urls.add(full_url)

        # Extract links from <form> tags with an "action" attribute
        for form_tag in soup.find_all('form', action=True):
            full_url = urljoin(url, form_tag['action'])
            urls.add(full_url)

        # Extract links from <img> tags with a "src" attribute if they are wrapped in anchors
        for img_tag in soup.find_all('img', src=True):
            parent = img_tag.parent
            if parent and parent.name == 'a' and parent.get('href'):
                full_url = urljoin(url, parent['href'])
                urls.add(full_url)

        # Ask the user where to save the CSV file
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return  # User cancelled the file save dialog

        # Write URLs to the CSV file
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["URL"])
            for link in urls:
                writer.writerow([link])

        messagebox.showinfo("Success", f"URLs have been saved to {os.path.basename(file_path)}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the GUI
app = tk.Tk()
app.title("URL Extractor")
app.geometry("400x200")

tk.Label(app, text="Enter URL:").pack(pady=10)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

fetch_button = tk.Button(app, text="Fetch and Save URLs", command=fetch_and_save_urls)
fetch_button.pack(pady=20)

app.mainloop()
