"""
Main Entry Point - Currency Converter Application
"""
import tkinter as tk
from model.currency_model import CurrencyModel
from view.currency_view import CurrencyView
from view.splash_screen import SplashScreen  
from controller.currency_controller import CurrencyController


def main():
    """Main entry point with splash screen"""
    # Show splash screen first (change duration here: 3 seconds default)
    # For 1 minute, use: splash = SplashScreen(duration=60)
    splash = SplashScreen(duration=6)  # 6 seconds for testing
    splash.show()
    
    # After splash screen closes, show main application
    root = tk.Tk()
    model = CurrencyModel()
    view = CurrencyView(root)
    controller = CurrencyController(model, view)
    root.mainloop()


if __name__ == "__main__":
    main()