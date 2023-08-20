import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import requests
import threading
import json
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import filedialog
from PIL import Image, ImageTk

class DataScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Scraper")
        self.root.geometry("400x400")

        # self.root.configure(bg="white")

        self.background_image = Image.open("./bg/bg.jpeg")  
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.background_label = ttk.Label(root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)


        self.root.resizable(False, False)


        self.style = ttk.Style()
        self.style.theme_use("aqua")

        self.label = ttk.Label(root, text="Select Source", font=('Helvetica', 18, 'bold'))
        self.label.pack(padx=40, pady=10)


        self.source_var = tk.StringVar()
        self.source_var.set("API")

        self.source_radio_api = ttk.Radiobutton(root, text="API", value="API", variable=self.source_var)
        self.source_radio_api.pack(padx=40)

        self.source_radio_web = ttk.Radiobutton(root, text="Web", value="WEB", variable=self.source_var)
        self.source_radio_web.pack()

        self.label_url = ttk.Label(root, text="Enter URL", font=('Helvetica', 12, 'bold'))
        self.label_url.pack(pady=(15, 0))

        self.url_entry = ttk.Entry(root)
        self.url_entry.pack(fill="x", padx=10, pady=(0, 15))

        self.label_format = ttk.Label(root, text="Select Format", font=('Helvetica', 18, 'bold'))
        self.label_format.pack(padx=10)

        self.format_var = tk.StringVar()
        self.format_var.set("json")

        self.format_radio_json = ttk.Radiobutton(root, text="JSON", value="json", variable=self.format_var)
        self.format_radio_json.pack()

        self.format_radio_csv = ttk.Radiobutton(root, text="CSV", value="csv", variable=self.format_var)
        self.format_radio_csv.pack()

        self.scrap_button = ttk.Button(root, text="Scrap", command=self.scrap_data)
        self.scrap_button.pack(pady=(26, 26))

        self.progress_style = ttk.Style()
        self.progress_style.configure("green.Horizontal.TProgressbar", thickness=10, troughcolor="green", background="green")

        self.progress_bar = ttk.Progressbar(root, style="green.Horizontal.TProgressbar", orient="horizontal", mode="determinate", maximum=100, value=0)
        self.progress_bar.pack( padx=40, pady=(10, 0))

        self.status_label = ttk.Label(root, text="", font=("Helvetica", 20, "italic"))
        self.status_label.pack(pady=20)


    def scrap_data(self):
        source = self.source_var.get()
        url = self.url_entry.get()
        output_format = self.format_var.get()

        if not url:
            messagebox.showerror("Error", "Please enter a valid URL.")
            return

        self.progress_bar["value"] = 0
        self.status_label.config(text="Loading...")
        

        thread = threading.Thread(target=self.fetch_data, args=(source, url, output_format))
        thread.start()

    def fetch_data(self, source, url, output_format):
        try:
            if source == "API":
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
            else:
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, "html.parser")
                
                prayers = soup.find_all("div", class_="prayer")
                prayer_data = []

                for prayer in prayers:
                    title = prayer.find("h1", class_="prayer-title").get_text(strip=True)
                    arabic = prayer.find("p", class_="arabic").get_text(strip=True)
                    transliteration = prayer.find("p", class_="transliteration").get_text(strip=True)
                    translation = prayer.find("p", class_="translation").get_text(strip=True)
                    category = prayer["category"]
                    
                    prayer_data.append({
                        "title": title,
                        "arabic": arabic,
                        "transliteration": transliteration,
                        "translation": translation,
                        "category": category
                    })

                data = prayer_data

            self.save_data(data, output_format)
            self.status_label.config(text="Data fetched and saved successfully.")
        except Exception as e:
            self.status_label.config(text="Error while fetching or saving data.")
            messagebox.showerror("Error", str(e))
        finally:
            self.progress_bar["value"] = 100

    def save_data(self, data, output_format):
        file_types = {
            "json": "JSON Files (*.json)",
            "csv": "CSV Files (*.csv)"
        }

        file_extension = "." + output_format
        file_name = filedialog.asksaveasfilename(defaultextension=file_extension, filetypes=[(file_types[output_format], "*" + file_extension)])
        
        if not file_name:
            return

        if output_format == "json":
            with open(file_name, "w") as f:
                json.dump(data, f, indent=4)
        elif output_format == "csv":
            df = pd.DataFrame(data)
            df.to_csv(file_name, index=False)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataScraperApp(root)
    root.mainloop()
