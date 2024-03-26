import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

def check_assets():
    def go_back():
        assets_window.destroy()  # Destroy the assets window

    def refresh_treeview():
        # Clear existing items in the treeview
        for item in tree.get_children():
            tree.delete(item)

        # Fetch updated data from the database
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="K@rtik2004",
                database="assettracking"
            )

            cursor = connection.cursor()

            cursor.execute("SELECT Asset_id, Asset_Types, Category, No_of_assets, Purchase_date, Api_value, Asset_value FROM assets")
            assets = cursor.fetchall()

            for asset in assets:
                asset_value = float(asset[6])  # Convert to float
                if isinstance(asset_value, str):
                    try:
                        asset_value = float(asset_value)
                    except ValueError:
                        messagebox.showwarning("Warning", f"Invalid asset value: {asset_value}")
                        continue
                api_value_with_dollar = "${:.2f}".format(float(asset[5]))  # Format Api value with dollar sign and 2 decimal places
                asset_value_with_dollar = "${:.2f}".format(asset_value)  # Format Asset value with dollar sign and 2 decimal places
                tree.insert("", "end", values=(asset[0], asset[1], asset[2], asset[3], asset[4], api_value_with_dollar, asset_value_with_dollar))

            connection.commit()
            connection.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    assets_window = tk.Toplevel()
    assets_window.title("Assets")
    assets_window.attributes("-fullscreen", True)  # Make the window fullscreen

    # Create the back button
    back_button = tk.Button(assets_window, text="Back", command=go_back)
    back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    # Create the treeview with increased height
    tree = ttk.Treeview(assets_window, columns=("Asset ID", "Asset Types", "Category", "No of Assets", "Purchase Date", "Api Value", "Asset Value"), height=35)
    tree.heading("Asset ID", text="Asset ID")  # Align the heading text to the left
    tree.heading("Asset Types", text="Asset Types")
    tree.heading("Category", text="Category")
    tree.heading("No of Assets", text="No of Assets")
    tree.heading("Purchase Date", text="Purchase Date")
    tree.heading("Api Value", text="Api Value")
    tree.heading("Asset Value", text="Asset Value")

    tree.column("Asset ID", anchor="w", width=100)  # Set width for Asset ID column

    # Create vertical scrollbar
    scrollbar = ttk.Scrollbar(assets_window, orient="vertical", command=tree.yview)
    scrollbar.grid(row=1, column=1, sticky='ns')

    tree.configure(yscrollcommand=scrollbar.set)

    refresh_treeview()  # Initially populate the treeview

    # Adjust the width of the "Asset Types" column
    total_width_except_column = sum(tree.column(c)["width"] for c in tree["columns"] if c != "Asset Types")
    remaining_width = assets_window.winfo_width() - total_width_except_column
    tree.column("Asset Types", width=max(200, remaining_width))

    # Place the treeview in the middle of the window
    tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    assets_window.mainloop()
