

# CURRENCY VIEW - UI Components


import tkinter as tk
from tkinter import ttk, messagebox


class CurrencyView:
    """View: Elegant, Responsive, with  Navigation Bar"""

    def __init__(self, root):
        self.root = root
        self.root.title("💱 Cellusys Build Up Currency Converter")
        self.root.geometry("950x720")
        self.root.minsize(600, 550)
        self.root.configure(bg="#0a2342")

        self.current_size = "large"
        self.active_tab = "Convert"
        self.root.bind('<Configure>', self.on_window_resize)

        self.setup_styles()
        self.create_widgets()

    def on_window_resize(self, event):
        if event.widget == self.root:
            width = self.root.winfo_width()
            if width < 700:
                size = "small"
            elif width < 900:
                size = "medium"
            else:
                size = "large"
            if size != self.current_size:
                self.current_size = size
                self.adjust_layout()

    def adjust_layout(self):
        width = self.root.winfo_width()
        if self.current_size == "small":
            self.title_main.config(font=("Arial", 18, "bold"))
            self.amount_entry.config(font=("Arial", 14, "bold"))
            self.card.place_configure(width=min(480, width - 40), height=470)
        elif self.current_size == "medium":
            self.title_main.config(font=("Arial", 22, "bold"))
            self.amount_entry.config(font=("Arial", 16, "bold"))
            self.card.place_configure(width=min(600, width - 60), height=500)
        else:
            self.title_main.config(font=("Arial", 26, "bold"))
            self.amount_entry.config(font=("Arial", 18, "bold"))
            self.card.place_configure(width=650, height=520)

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')

        style.configure(
            'Round.TButton',
            padding=(12, 8),
            font=('Arial', 11, 'bold'),
            background='#007bff',
            foreground='white',
            borderwidth=0
        )
        style.map(
            'Round.TButton',
            background=[('active', '#0056b3')],
            foreground=[('active', 'white')]
        )

        style.configure('TCombobox',
                        fieldbackground='white',
                        background='white',
                        padding=5)

    def create_widgets(self):
        # HEADER BAR
        header = tk.Frame(self.root, bg="#06172d")
        header.pack(fill="x")

        tk.Label(
            header, text="💱", font=("Arial", 28),
            bg="#06172d", fg="#00d4ff"
        ).pack(side="left", padx=20, pady=10)

        title_label = tk.Label(
            header,
            text="Cellusys Build Up Currency Converter",
            font=("Arial", 18, "bold"),
            fg="white", bg="#06172d"
        )
        title_label.pack(side="left", padx=10, pady=10)

        tk.Button(
            header, text="Login", font=("Arial", 10, "bold"),
            bg="#0a2342", fg="white", relief="flat", cursor="hand2",
            activebackground="#00bfff"
        ).pack(side="right", padx=15, pady=10)

        tk.Button(
            header, text="Register", font=("Arial", 10, "bold"),
            bg="#00bfff", fg="white", relief="flat", cursor="hand2",
            activebackground="#00a3e0"
        ).pack(side="right", padx=5, pady=10)

        # NAVIGATION BAR
        self.navbar = tk.Frame(self.root, bg="#0b2a52", height=45)
        self.navbar.pack(fill="x", pady=(0, 5))

        self.nav_buttons = {}
        tabs = ["Convert", "Send", "Charts", "Alerts"]
        for name in tabs:
            btn = tk.Label(
                self.navbar,
                text=name,
                font=("Arial", 11, "bold"),
                bg="#0b2a52",
                fg="#cbd9ff" if name != self.active_tab else "#00d4ff",
                cursor="hand2",
                padx=20,
                pady=8
            )
            btn.pack(side="left", padx=(15, 5))
            btn.bind("<Enter>", lambda e, b=btn: self.on_nav_hover(b))
            btn.bind("<Leave>", lambda e, b=btn: self.on_nav_leave(b))
            btn.bind("<Button-1>", lambda e, n=name: self.set_active_tab(n))
            self.nav_buttons[name] = btn

        # TITLE AREA
        title_frame = tk.Frame(self.root, bg="#0a2342")
        title_frame.pack(pady=(25, 15))

        self.title_main = tk.Label(
            title_frame,
            text="Exchange Rates • Convert Instantly",
            font=("Arial", 26, "bold"),
            fg="white",
            bg="#0a2342"
        )
        self.title_main.pack()

        self.title_sub = tk.Label(
            title_frame,
            text="Reliable, real-time foreign exchange updates",
            font=("Arial", 12),
            fg="#d3e0ff",
            bg="#0a2342"
        )
        self.title_sub.pack()

        # MAIN CARD
        card_container = tk.Frame(self.root, bg="#0a2342")
        card_container.pack(expand=True, fill="both")

        shadow = tk.Label(card_container, bg="#07152c")
        shadow.place(relx=0.5, rely=0.5, anchor="center", width=660, height=530)

        self.card = tk.Frame(
            card_container, bg="white",
            relief="raised", bd=0, highlightthickness=0
        )
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=650, height=520)

        content = tk.Frame(self.card, bg="white")
        content.pack(fill="both", expand=True, padx=25, pady=25)

        # Amount Section
        tk.Label(
            content, text="Enter Amount", font=("Arial", 10, "bold"),
            bg="white", fg="#2c3e50"
        ).pack(anchor="w", pady=(10, 2))

        self.amount_var = tk.StringVar(value="1.00")
        self.amount_entry = tk.Entry(
            content,
            textvariable=self.amount_var,
            font=("Arial", 18, "bold"),
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightcolor="#007bff"
        )
        self.amount_entry.pack(fill="x", ipady=6, pady=(0, 10))

        # Currency Selection
        selector = tk.Frame(content, bg="white")
        selector.pack(fill="x", pady=10)

        tk.Label(selector, text="From", bg="white", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
        tk.Label(selector, text="To", bg="white", font=("Arial", 10, "bold")).grid(row=0, column=2, sticky="w")

        self.from_combo = ttk.Combobox(selector, state="readonly", font=("Arial", 11))
        self.from_combo.grid(row=1, column=0, sticky="ew", padx=(0, 5))

        self.to_combo = ttk.Combobox(selector, state="readonly", font=("Arial", 11))
        self.to_combo.grid(row=1, column=2, sticky="ew", padx=(5, 0))

        selector.grid_columnconfigure(0, weight=1)
        selector.grid_columnconfigure(1, weight=0)
        selector.grid_columnconfigure(2, weight=1)

        # Swap Button
        self.swap_btn = tk.Button(
            selector,
            text="⇄",
            font=("Arial", 18, "bold"),
            bg="#e3f2fd",
            fg="#007bff",
            width=3,
            relief="flat",
            cursor="hand2"
        )
        self.swap_btn.grid(row=1, column=1, padx=10)

        # Result Section
        result_frame = tk.Frame(content, bg="#f6fbff", relief="groove", bd=1)
        result_frame.pack(pady=20, fill="x")

        self.result_label = tk.Label(
            result_frame,
            text="Enter amount and press Convert",
            font=("Arial", 16, "bold"),
            bg="#f6fbff",
            fg="#007bff",
            wraplength=500
        )
        self.result_label.pack(pady=15)

        self.rate_label = tk.Label(
            result_frame,
            text="",
            font=("Arial", 10),
            bg="#f6fbff",
            fg="#444"
        )
        self.rate_label.pack(pady=(0, 10))

        # Convert button
        self.convert_btn = ttk.Button(
            content, text="💱 Convert Now", style="Round.TButton", cursor="hand2"
        )
        self.convert_btn.pack(fill="x", pady=(10, 20), ipady=4)

        # Status Bar
        self.status_label = tk.Label(
            content,
            text="Waiting for connection...",
            font=("Arial", 9),
            fg="#666",
            bg="white"
        )
        self.status_label.pack(side="bottom", pady=5)

    def on_nav_hover(self, btn):
        if btn.cget("text") != self.active_tab:
            btn.config(fg="#00bfff")

    def on_nav_leave(self, btn):
        if btn.cget("text") != self.active_tab:
            btn.config(fg="#cbd9ff")

    def set_active_tab(self, tab_name):
        self.active_tab = tab_name
        for name, btn in self.nav_buttons.items():
            btn.config(
                fg="#00d4ff" if name == tab_name else "#cbd9ff",
                font=("Arial", 11, "bold")
            )
        self.update_status(f"Switched to {tab_name} tab")

    def populate_currencies(self, currencies: list):
        self.from_combo['values'] = currencies
        self.to_combo['values'] = currencies
        if currencies:
            self.from_combo.set("USD - US Dollar")
            self.to_combo.set("EUR - Euro")

    def get_amount(self) -> float:
        try:
            value = self.amount_var.get().replace(',', '').strip()
            return float(value)
        except ValueError:
            return None

    def get_from_currency(self):
        value = self.from_combo.get()
        return value.split(' - ')[0] if value else "USD"

    def get_to_currency(self):
        value = self.to_combo.get()
        return value.split(' - ')[0] if value else "EUR"

    def display_result(self, amount, from_c, to_c, result, rate):
        self.result_label.config(
            text=f"{amount:,.2f} {from_c} = {result:,.2f} {to_c}",
            fg="#27ae60"
        )
        self.rate_label.config(
            text=f"1 {from_c} = {rate:.6f} {to_c}"
        )

    def update_status(self, msg):
        self.status_label.config(text=msg)

    def show_error(self, title, message):
        messagebox.showerror(title, message)

    def show_info(self, title, message):
        messagebox.showinfo(title, message)

    def swap_currencies(self):
        from_val, to_val = self.from_combo.get(), self.to_combo.get()
        self.from_combo.set(to_val)
        self.to_combo.set(from_val)
