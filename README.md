# Data Scraper GUI Application

Empower your web scraping needs by leveraging the versatility of this tool. While the provided code demonstrates scraping from a specific website, users can effortlessly adapt it to harvest data from their preferred web sources.

The Data Scraper GUI Application is a tool that allows users to fetch and scrape data from either an API or a web page. It provides a user-friendly interface to input the source, URL, and desired output format (JSON or CSV) for the scraped data. The application is built using the Python `tkinter` library for the graphical user interface, and it uses `requests` for making HTTP requests, `BeautifulSoup` for web scraping, and `pandas` for handling data.

## Preview

## Data Scrapped from Web (Based on Written Code from specific website)
<p align="center">
   <img src="https://github.com/Dev-Hooman/data-scrapper/assets/80707427/c7298b25-505f-46d3-be7e-f541b1eccc9a" alt="from web" />
</p>

## Scrapped Data in JSON:

<p align="center">
   <img src="https://github.com/Dev-Hooman/data-scrapper/assets/80707427/653f943b-db99-4e7f-aa1b-705234ccfbc2" alt="JSON show case" />
</p>

## Data fetched from API

<p align="center">
      <img src="https://github.com/Dev-Hooman/data-scrapper/assets/80707427/7494540b-cc1f-4771-8939-5f07c0470a3a" alt="from API" />
</p>



## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Data Scraper GUI Application simplifies the process of data scraping from web sources by providing an easy-to-use graphical interface. Users can choose between fetching data from an API or scraping data from a web page. The application supports saving the scraped data in either JSON or CSV format.

## Features

- Choose between API and web scraping as data sources.
- Input the URL of the API or the web page to scrape.
- Select the desired output format: JSON or CSV.
- Fetch data from the specified source and URL.
- Display a progress bar to indicate the scraping process.
- Handle errors and display status messages.
- Save the scraped data in the selected format.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/data-scraper.git
   cd data-scraper
## Usage

1. Run the application by executing the following command:
   ```bash
      python run.py
2. The graphical user interface (GUI) will open. Here's how to use the application:

- Choose the data source by selecting "API" or "Web".
- Enter the URL of the API or web page you want to scrape.
- Select the output format as either "JSON" or "CSV".
- Click the "Scrap" button to initiate the scraping process.
- The progress bar will show the progress of the scraping.
- Once the scraping is complete, the status label will display the result.
  
3. The scraped data will be saved in the selected format (JSON or CSV) in a location of your choice.


## Customization
  
  You can customize this application to suit your needs. Some possible improvements include:

- Adding more data sources or web scraping targets.
- Enhancing the user interface with more styling and design.
- Adding options to customize the data scraping process further.
- Handling additional errors and edge cases.
- Implementing multi-threading for smoother user experience.
  
## Contributing
- Contributions are welcome! If you have any suggestions, bug fixes, or enhancements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

