import requests
import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from tkcalendar import DateEntry

root = tk.Tk()

Asset_id_int = tk.IntVar()
Asset_Types_var = tk.StringVar()
Category_var = tk.StringVar()
No_of_assets_var = tk.IntVar()
Purchase_date_var = tk.StringVar()

def go_back():
    root.destroy()
def save_asset():
    Asset_id = Asset_id_int.get()
    Asset_Types = Asset_Types_var.get()
    Category = Category_var.get()
    No_of_assets = No_of_assets_var.get()
    Purchase_date = Purchase_date_var.get()

    if Asset_Types == 'Bitcoin':
        api_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()
            if 'bpi' not in data or 'USD' not in data['bpi']:
                raise ValueError("Price not found in response")
            api_value = data['bpi']['USD']['rate_float']
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch Bitcoin price: {e}")
            return
        except (ValueError, KeyError) as e:
            messagebox.showerror("Error", f"Failed to parse Bitcoin price: {e}")
            return
    elif Asset_Types == 'Stocks':
        api_url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={Category}&apikey=T9WT2SEE3DESWBOX'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            if 'Global Quote' not in data or '05. price' not in data['Global Quote']:
                raise ValueError("Invalid Category")
            api_value = data['Global Quote']['05. price']
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch stock price: {e}")
            return
        except (ValueError, KeyError) as e:
            messagebox.showerror("Error", f"select a valid asset type and category.")
            return
    else:
        api_value = None

    if not all([Asset_id, Asset_Types, Category, No_of_assets, Purchase_date]) or api_value is None:
        messagebox.showwarning("Warning", "Please fill in all the fields or select a valid asset type and category.")
        return
    Asset_value = No_of_assets * float(api_value)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="K@rtik2004",
            database="assettracking"
        )

        cursor = connection.cursor()
        query = "INSERT INTO assets (Asset_id, Asset_Types, Category, No_of_assets, Purchase_date, Asset_value, Api_value) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (Asset_id, Asset_Types, Category, No_of_assets, Purchase_date, Asset_value, api_value)
        cursor.execute(query, values)

        connection.commit()
        connection.close()

        messagebox.showinfo("Success", "Asset details saved successfully!")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error: {e}")

def save_date():
    selected_date = cal.get_date()
    Purchase_date_var.set(selected_date)

# Create the main window
root.title("Asset Management System")
root.attributes('-fullscreen', True)  # Set fullscreen
root.configure(bg="light blue")

# Create a LabelFrame for entering asset details
frame = tk.LabelFrame(root, text="Enter Asset Details", padx=50, pady=50, bg="light blue")
frame.pack(padx=50, pady=50, fill=tk.X)

# Change font size and background color of labels
label_font = ('Helvetica', 12)
label_bg = "light blue"

# Entry widgets for asset details
tk.Label(frame, text="Asset ID:", width=20, height=4, font=label_font, bg=label_bg).grid(row=0, column=0, padx=(0, 10))
tk.Entry(frame, textvariable=Asset_id_int, width=30).grid(row=0, column=1)

# Dropdown menu for selecting title
Asset_Types_options = ['Bitcoin', 'Stocks']
tk.Label(frame, text="Asset Types:", width=20, height=4, font=label_font, bg=label_bg).grid(row=1, column=0, padx=(0, 10))
Asset_Types_dropdown = tk.OptionMenu(frame, Asset_Types_var, *Asset_Types_options)
Asset_Types_dropdown.grid(row=1, column=1)

tk.Label(frame, text="Category:", width=20, height=4, font=label_font, bg=label_bg).grid(row=2, column=0, padx=(0, 10))
tk.Entry(frame, textvariable=Category_var, width=30).grid(row=2, column=1)

tk.Label(frame, text="Number of assets:", width=20, height=4, font=label_font, bg=label_bg).grid(row=3, column=0, padx=(0, 10))
tk.Entry(frame, textvariable=No_of_assets_var, width=30).grid(row=3, column=1)

tk.Label(frame, text="Purchase Date(yy/mm/dd):", width=20, height=4, font=label_font, bg=label_bg).grid(row=4, column=0, padx=(0, 10))
cal = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.grid(row=4, column=1)
cal_button = tk.Button(frame, text="Save Date", command=save_date)
cal_button.grid(row=5, columnspan=2)

# Save button
save_button = tk.Button(frame, text="Save Asset", command=save_asset, width=20)
save_button.grid(row=7, columnspan=2)

# Back button
back_button = tk.Button(root, text="Back", command=go_back)
back_button.place(x=10, y=10)

root.mainloop()
