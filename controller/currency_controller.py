
# ============================================================================
# FILE 7: controller/currency_controller.py
# ============================================================================

"""
Currency Controller - Connects Model ↔ View and handles application logic
"""

import threading
import time


class CurrencyController:
    """Controller: Manages interactions between Model and View"""

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.convert_btn.config(command=self.handle_convert)
        self.view.swap_btn.config(command=self.handle_swap)
        self.initialize_app()

    def initialize_app(self):
        """Fetch rates and populate currencies"""
        if self.model.fetch_rates():
            currency_list = self.model.get_currency_list()
            self.view.populate_currencies(currency_list)
            
            if self.model.is_offline:
                self.view.update_status("⚠️ OFFLINE MODE - Using cached rates from " + self.model.last_updated)
            else:
                self.view.update_status("✅ ONLINE - Rates loaded successfully")
        else:
            self.view.show_error("Connection Error", 
                               "Failed to fetch currency rates and no cached data available.")

    def handle_convert(self):
        """Handles conversion logic with spinner animation"""
        amount = self.view.get_amount()
        from_curr = self.view.get_from_currency()
        to_curr = self.view.get_to_currency()

        if amount is None or amount <= 0:
            self.view.show_error("Invalid Input", 
                               "Please enter a valid amount greater than zero.")
            return

        if not from_curr or not to_curr:
            self.view.show_error("Missing Selection", "Please select both currencies.")
            return

        # Show spinner
        self.view.show_spinner()
        self.view.update_status("Converting...")
        
        # Simulate processing delay (remove in production or keep for UX)
        def perform_conversion():
            time.sleep(0.5)  # Simulated delay
            
            rate = self.model.get_rate(from_curr, to_curr)
            
            # Update UI in main thread
            self.view.root.after(0, lambda: self.finish_conversion(amount, from_curr, to_curr, rate))
        
        # Run conversion in background thread
        threading.Thread(target=perform_conversion, daemon=True).start()

    def finish_conversion(self, amount, from_curr, to_curr, rate):
        """Complete the conversion and update UI"""
        self.view.hide_spinner()
        
        if rate is None:
            self.view.show_error("Error", 
                               f"Could not retrieve rate for {from_curr} → {to_curr}.")
            self.view.update_status("Conversion failed")
            return

        result = amount * rate
        self.view.display_result(amount, from_curr, to_curr, result, rate)
        
        if self.model.is_offline:
            self.view.update_status(f"⚠️ OFFLINE MODE - Using cached rates from {self.model.last_updated}")
        else:
            self.view.update_status(f"✅ Last updated: {self.model.last_updated}")

    def handle_swap(self):
        """Swap selected currencies."""
        self.view.swap_currencies()