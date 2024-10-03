
# Amazon Web Scraping 🚀

A Python project that scrapes product details (titles, prices, and links) from locally stored HTML files using BeautifulSoup and exports the data to a CSV file. This project demonstrates web scraping techniques and handling HTML data.

## 🗂 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 📖 Overview

This project processes locally saved Amazon product pages, extracting the following details:
- **Product Title**: Scraped from the `<h2>` tag.
- **Product Price**: Extracted from the `<span>` tag with class `a-price-whole`.
- **Product Link**: Extracted from the `<a>` tag inside the title and combined with the base URL.

The final data is stored in a CSV file (`data.csv`), which contains the titles, prices, and links of the products.

## 🛠️ Project Structure

```bash
amazon-web-scrapping/
│
├── data/                   # Directory containing the HTML files to scrape
├── main.py                 # Main Python script for scraping
├── data.csv                # Output file with the scraped data
├── .gitignore              # Specifies files and directories ignored by Git
└── README.md               # Project documentation
```

## ✅ Prerequisites

Ensure you have the following installed:
- **Python 3.x**
- **Pandas**: For exporting data to CSV.
- **BeautifulSoup** (bs4): For parsing HTML content.

You can install the required Python packages using:

```bash
pip install pandas beautifulsoup4
```

## ⚙️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Git-abby/amazon-web-scrapping.git
   cd amazon-web-scrapping
   ```

2. **Install Dependencies**:

   Ensure all dependencies are installed by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Add Your Data**:

   Add your HTML files (to scrape) into the `data` directory. The script processes all HTML files in this directory.

## 💻 Usage

Run the Python script to scrape product data from the local HTML files and export it to a CSV file:

```bash
python main.py
```

After running, a file named `data.csv` will be created in the project root directory with the following columns:
- **Title**: The name of the product.
- **Price**: The product price (whole number).
- **Link**: The URL to the product page.

## 🛡️ Error Handling

The script includes basic error handling:
- If a product title, price, or link is missing in the HTML file, it catches the exception and logs the error with the specific file name where the error occurred.

To improve the logging mechanism, you can replace `print()` with proper logging using the `logging` module for more detailed error tracking.

## 🔧 Technologies Used

- **Python**: Main language used for writing the script.
- **BeautifulSoup (bs4)**: For parsing HTML content and extracting product details.
- **Pandas**: To structure data in tabular format and export it as a CSV file.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
