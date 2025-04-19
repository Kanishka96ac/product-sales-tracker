import csv
import datetime

product_data = {
    "P001" : ['Wireless Headphones' , 100],
    "P002" : ['Laptop Backpack ', 60],
    "P003" : ['Bluetooth Speaker' , 50],
    "P004" : ['USB Flash Drive' , 20],
    "P005" : ['Mobile Phone Case' , 15],
    "P006" : ['Wireless Mouse' , 30],
    "P007" : ['Laptop Stand' , 40],
    "P008" : ['HDMI Cable' , 15],
    "P009" : ['Smartphone' , 600],
    "P010" : ['External Hard Drive' , 100]
}

def date_formatter():
    today = datetime.date.today()
    day = today.strftime('%d').lstrip("0")
    month = today.strftime('%m').lstrip("0")
    year = today.strftime('%Y')
    formatted_date = f"{day}/{month}/{year}"
    return formatted_date

product_details = []
headers = ['current_date' , 'sale_id' , 'product_id' , 'name' , 'price']

with open('product_sales.txt' , 'r') as text_file:
    product_ids = text_file.readlines()

    for index, product_id in enumerate(product_ids) :
        product_id = product_id.strip()
        product_details.append([date_formatter() , (index+1) , product_id , product_data[product_id][0] , product_data[product_id][1]])

print(product_details)

with open('product_sale_report.csv' , 'w' , newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(headers)
    csv_writer.writerows(product_details)