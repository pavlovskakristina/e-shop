import json
import tkinter as tk
# import tkinter.simpledialog as sd
from tkinter import messagebox
from body import Product, products, orders
from storage import save_products_to_file

PRODUCTS_FILE = "products.json"


def load_products():
    products.clear()
    try:
        with open(PRODUCTS_FILE, "r") as f:
            data = json.load(f)
            for item in data:
                p = Product(
                    name=item["name"],
                    brand=item["brand"],
                    amount=item["amount"],
                    price=item["price"]
                )
                products.append(p)
    except FileNotFoundError:
        pass


class EShopGUI(tk.Tk):
    def __init__(self, customer):
        super().__init__()
        self.customer = customer  # klient z CLI
        self.cart = []
        self.title("E-Shop")
        self.geometry("600x400")

        # Lista produktów
        tk.Label(self, text="Products").grid(row=0, column=0, padx=10, pady=5)
        self.lb_products = tk.Listbox(self, width=40, height=15)
        self.lb_products.grid(row=1, column=0, padx=10, pady=5)

        # Lista koszyka
        tk.Label(self, text="Cart").grid(row=0, column=1, padx=10, pady=5)
        self.lb_cart = tk.Listbox(self, width=25, height=15)
        self.lb_cart.grid(row=1, column=1, padx=10, pady=5)

        # Przyciski
        btn_frame = tk.Frame(self)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(btn_frame, text="Add to Cart →", command=self.add_to_cart).pack(side="left", padx=5)
        tk.Button(btn_frame, text="← Remove from Cart", command=self.remove_from_cart).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Purchase", command=self.purchase).pack(side="left", padx=5)
        tk.Button(btn_frame, text="History", command=self.show_history).pack(side="left", padx=5)

        self.refresh_products()

    def refresh_products(self):
        """Przeładuj listę produktów w Listboxie."""
        self.lb_products.delete(0, tk.END)
        for idx, p in enumerate(products, start=1):
            display = f"{idx}. {p.name} ({p.brand}) — {p.amount} pcs @ {p.price:.2f}$"
            self.lb_products.insert(tk.END, display)

    def add_to_cart(self):
        sel = self.lb_products.curselection()
        if not sel:
            return
        idx = sel[0]
        p = products[idx]
        if p.amount <= 0:
            messagebox.showwarning("Out of stock", f"{p.name} is out of stock.")
            return
        # dodajemy do koszyka (tylko etykietę)
        self.cart.append(p)
        self.lb_cart.insert(tk.END, f"{p.name} — {p.price:.2f}$")

    def remove_from_cart(self):
        sel = self.lb_cart.curselection()
        if not sel:
            return
        idx = sel[0]
        del self.cart[idx]
        self.lb_cart.delete(idx)

    def purchase(self):
        if not self.cart:
            return
        total = sum(p.price for p in self.cart)
        # zmniejszamy stan magazynu
        for p in self.cart:
            p.amount -= 1
        save_products_to_file(products)
        self.cart.clear()
        self.lb_cart.delete(0, tk.END)
        self.refresh_products()
        messagebox.showinfo("Thank you!", f"Purchase complete!\nTotal: {total:.2f}$")

    def show_history(self):
        """Wyświetla historię zamówień dla zalogowanego klienta."""
        user_orders = [o for o in orders if o.customer.id == self.customer.id]
        if not user_orders:
            messagebox.showinfo("History", "You have no past orders.")
            return

        text = ""
        for o in user_orders:
            items = ", ".join(f"{k}x{v}" for d in o.orders for k, v in d.items())
            text += f"Order #{o.id_n} on {o.date}: {items} — Total {o.total_orders:.2f}$\n\n"

        messagebox.showinfo("Your Orders", text.strip())


if __name__ == "__main__":
    load_products()
    # importuj Customer do testu
    from body import Customer
    # utwórz „dummy” klienta
    test_customer = Customer("Test", "User", "pw")
    app = EShopGUI(test_customer)
    app.mainloop()
