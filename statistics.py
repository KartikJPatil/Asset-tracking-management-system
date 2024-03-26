import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector

# Function to fetch data from the database
def fetch_portfolio_data():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="K@rtik2004",
            database="assettracking"
        )

        cursor = connection.cursor()

        # Fetch data for stocks
        cursor.execute("SELECT Category, SUM(No_of_assets) FROM assets WHERE Asset_Types = 'Stocks' GROUP BY Category")
        stocks_data = cursor.fetchall()

        # Fetch data for bitcoin
        cursor.execute("SELECT 'Bitcoin', COUNT(*) FROM assets WHERE Asset_Types = 'Bitcoin'")
        bitcoin_data = cursor.fetchall()

        connection.close()

        return stocks_data, bitcoin_data

    except mysql.connector.Error as e:
        print("Error fetching data:", e)
        return None, None

# Function to create the pie chart
def create_pie_chart():
    # Fetch data from the database
    stocks_data, bitcoin_data = fetch_portfolio_data()

    if stocks_data is None or bitcoin_data is None:
        print("Failed to fetch data from the database")
        return

    # Calculate total count of assets
    total_stocks = sum([count for _, count in stocks_data])
    total_assets = total_stocks + bitcoin_data[0][1]

    # Prepare data for plotting
    categories = [item[0] for item in stocks_data] + ['Bitcoin']
    counts = [item[1] for item in stocks_data] + [bitcoin_data[0][1]]

    # Create a new Tkinter window
    pie_chart_window = tk.Tk()
    pie_chart_window.title("Portfolio Overview")
    pie_chart_window.attributes("-fullscreen", True)

    # Create a matplotlib figure and subplot
    fig = Figure(figsize=(8, 8))
    ax = fig.add_subplot(111)

    # Generate pie chart for stocks and Bitcoin
    ax.pie(counts, labels=categories, autopct='%1.1f%%', startangle=140)
    ax.set_title('Portfolio Overview')

    # Create a canvas to display the pie chart
    canvas = FigureCanvasTkAgg(fig, master=pie_chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Function to close the window and go back
    def go_back():
        pie_chart_window.destroy()

    # Create a 'Back' button
    back_button = tk.Button(pie_chart_window, text="Back", command=go_back)
    back_button.place(x=10, y=10)

    # Run the Tkinter event loop
    pie_chart_window.mainloop()

# Call create_pie_chart function to display the pie chart directly
create_pie_chart()
