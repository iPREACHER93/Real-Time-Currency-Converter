# Entry point to start the app.
import tkinter as tk
from model.currency_model import CurrencyModel
from view.currency_view import CurrencyView
from controller.currency_controller import CurrencyController



# MAIN ENTRY POINT


def main():
    root = tk.Tk()
    model = CurrencyModel()
    view = CurrencyView(root)
    controller = CurrencyController(model, view)
    root.mainloop()

if __name__ == "__main__":
    main()