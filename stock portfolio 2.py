import tkinter as tk
from tkinter import messagebox 


portfolio = {}

def add_stock():
    symbol = entry_symbol.get().upper()
    try:
        shares = int(entry_shares.get())
    except ValueError:
        messagebox.showerror("Error", "Shares must be an integer.")
        return

    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares

    entry_symbol.delete(0, tk.END)
    entry_shares.delete(0, tk.END)
    update_display()

def remove_stock():
    symbol = entry_symbol.get().upper()
    if symbol in portfolio:
        del portfolio[symbol]
    update_display()

def update_display():
    output.delete("1.0", tk.END)
    total_value = 0
    for symbol, shares in portfolio.items():
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        price = data["Close"].iloc[-1]
        value = price * shares
        total_value += value
        output.insert(tk.END, f"{symbol} - {shares} shares @ ${price:.2f} = ${value:.2f}\n")
    output.insert(tk.END, f"\nTotal Portfolio Value: ${total_value:.2f}")

# GUI setup
root = tk.Tk()
root.title("Stock Portfolio Tracker")

tk.Label(root, text="Stock Symbol:").grid(row=0, column=0)
entry_symbol = tk.Entry(root)
entry_symbol.grid(row=0, column=1)

tk.Label(root, text="Shares:").grid(row=1, column=0)
entry_shares = tk.Entry(root)
entry_shares.grid(row=1, column=1)

tk.Button(root, text="Add Stock", command=add_stock).grid(row=2, column=0)
tk.Button(root, text="Remove Stock", command=remove_stock).grid(row=2, column=1)

output = tk.Text(root, height=15, width=50)
output.grid(row=3, column=0, columnspan=2)

root.mainloop()




