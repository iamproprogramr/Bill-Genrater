#This program is written by muhammad yousaf and uploded on https://github.com/iamproprogramr
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageOps
import qrcode
import datetime

def create_bill(shop_name, shop_address, date, manager_name, product_name, product_image_path, price, customer_name, customer_address, cashier_name, discount):
    
    discount_amount = price * (discount / 100)
    total_price = price - discount_amount

    
    width, height = 400, 700
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    
    try:
        font_path = "arial.ttf"
        header_font = ImageFont.truetype(font_path, 24)
        body_font = ImageFont.truetype(font_path, 20)
    except IOError:
        header_font = ImageFont.load_default()
        body_font = ImageFont.load_default()

    
    headers = [
        "CASH RECEIPT",
        shop_name,
        shop_address,
        f"Date: {date}",
        f"Manager: {manager_name}",
    ]
    
    body = [
        f"Customer: {customer_name}",
        f"Address: {customer_address}",
        f"Cashier: {cashier_name}",
        "",
        f"Product: {product_name}",
        f"Original Price: PKR {price:.2f}",
        f"Discount: {discount:.2f}%",
        f"Discount Amount: PKR {discount_amount:.2f}",
        f"Total Price: PKR {total_price:.2f}",
        "",
        "Thank you for shopping with us!"
    ]

    
    y_text = 10
    for header in headers:
        draw.text((10, y_text), header, font=header_font, fill="blue")
        y_text += 35

    y_text += 20

   
    for line in body:
        draw.text((10, y_text), line, font=body_font, fill="black")
        y_text += 30

    
    if product_image_path:
        try:
            product_image = Image.open(product_image_path)
            product_image.thumbnail((150, 150))
            image.paste(product_image, (width - 160, 10))  # Adjust position to right corner
        except Exception as e:
            messagebox.showerror("Error", f"Could not open product image: {e}")

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data("https://github.com/iamproprogramr")
    qr.make(fit=True)
    qr_img = qr.make_image(fill='black', back_color='white')
    qr_img = qr_img.resize((100, 100))

    image.paste(qr_img, (width - 110, height - 110))

    
    image_path = "bill.png"
    image.save(image_path)

   
    image.show()

def generate_bill():
    shop_name = entry_shop_name.get()
    shop_address = entry_shop_address.get()
    date = entry_date.get()
    manager_name = entry_manager_name.get()
    product_name = entry_product_name.get()
    product_image_path = entry_product_image.get()
    price = float(entry_price.get())
    customer_name = entry_customer_name.get()
    customer_address = entry_customer_address.get()
    cashier_name = entry_cashier_name.get()
    discount = float(entry_discount.get())

    create_bill(shop_name, shop_address, date, manager_name, product_name, product_image_path, price, customer_name, customer_address, cashier_name, discount)
    messagebox.showinfo("Success", "Bill has been generated and saved as 'bill.png'.")

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    entry_product_image.delete(0, tk.END)
    entry_product_image.insert(0, file_path)


root = tk.Tk()
root.title("Bill Generator")


tk.Label(root, text="Shop Name:").grid(row=0, column=0, padx=10, pady=5)
entry_shop_name = tk.Entry(root)
entry_shop_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Shop Address:").grid(row=1, column=0, padx=10, pady=5)
entry_shop_address = tk.Entry(root)
entry_shop_address.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Date (MM/DD/YYYY):").grid(row=2, column=0, padx=10, pady=5)
entry_date = tk.Entry(root)
entry_date.insert(0, datetime.datetime.now().strftime("%m/%d/%Y"))
entry_date.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Manager Name:").grid(row=3, column=0, padx=10, pady=5)
entry_manager_name = tk.Entry(root)
entry_manager_name.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Product Name:").grid(row=4, column=0, padx=10, pady=5)
entry_product_name = tk.Entry(root)
entry_product_name.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Product Image:").grid(row=5, column=0, padx=10, pady=5)
entry_product_image = tk.Entry(root)
entry_product_image.grid(row=5, column=1, padx=10, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_image)
browse_button.grid(row=5, column=2, padx=10, pady=5)

tk.Label(root, text="Price:").grid(row=6, column=0, padx=10, pady=5)
entry_price = tk.Entry(root)
entry_price.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Customer Name:").grid(row=7, column=0, padx=10, pady=5)
entry_customer_name = tk.Entry(root)
entry_customer_name.grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="Customer Address:").grid(row=8, column=0, padx=10, pady=5)
entry_customer_address = tk.Entry(root)
entry_customer_address.grid(row=8, column=1, padx=10, pady=5)

tk.Label(root, text="Cashier Name:").grid(row=9, column=0, padx=10, pady=5)
entry_cashier_name = tk.Entry(root)
entry_cashier_name.grid(row=9, column=1, padx=10, pady=5)

tk.Label(root, text="Discount (%):").grid(row=10, column=0, padx=10, pady=5)
entry_discount = tk.Entry(root)
entry_discount.grid(row=10, column=1, padx=10, pady=5)


generate_button = tk.Button(root, text="Generate Bill", command=generate_bill)
generate_button.grid(row=11, columnspan=3, pady=20)


root.mainloop()
