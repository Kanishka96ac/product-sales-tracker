# 🛒 Product Sales Tracker

A lightweight Python automation project that reads product sale IDs from a text file, fetches details from a predefined dataset, appends the current date and unique sale ID, and generates a clean CSV sales report.

## 📌 Features

* Tracks sales based on product IDs from a `.txt` file.
* Automatically assigns a sale ID and current date to each transaction.
* Looks up product details (name and price) using a predefined dictionary.
* Exports data to a structured CSV report.
* Uses standard Python libraries only (no external dependencies).

## 🧰 Tech Stack

* Python 3.x
* Built-in modules: `csv`, `datetime`

## 📂 Project Structure

```
.
├── product_sales.txt          # Input file containing product IDs (one per line)
├── product_sales_tracker.py   # Main script
└── product_sale_report.csv    # Generated CSV report
```

## 📄 Sample Input (`product_sales.txt`)

```
P001
P003
P006
P009
```

## 📄 Output (`product_sale_report.csv`)

| current\_date | sale\_id | product\_id | name                | price |
| ------------- | -------- | ----------- | ------------------- | ----- |
| 9/5/2025      | 1        | P001        | Wireless Headphones | 100   |
| 9/5/2025      | 2        | P003        | Bluetooth Speaker   | 50    |
| 9/5/2025      | 3        | P006        | Wireless Mouse      | 30    |
| 9/5/2025      | 4        | P009        | Smartphone          | 600   |

> 🗓 Date format is automatically generated based on your current system date (DD/MM/YYYY).

## 🚀 How to Run

1. **Clone this repository:**

   ```bash
   git clone https://github.com/your-username/product-sales-tracker.git
   cd product-sales-tracker
   ```

2. **Ensure you have Python installed** (Python 3.6 or above).

3. **Prepare the input file**:
   Make sure `product_sales.txt` contains one product ID per line using predefined keys like `P001`, `P003`, etc.

4. **Run the script:**

   ```bash
   python product_sales_tracker.py
   ```

5. **Check the output:**
   A file named `product_sale_report.csv` will be created with the sale records.

## 📌 Notes

* This script assumes all product IDs in the input file exist in the `product_data` dictionary.
* Customise the `product_data` dictionary to include more products if needed.

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to fork, contribute, or suggest improvements. Happy tracking!

## 👨‍💻 Author

Made with ❤️ by Kanishka Peramunugama
