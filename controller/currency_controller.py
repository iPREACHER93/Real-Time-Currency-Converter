
# CURRENCY CONTROLLER - Connects Model ↔ View and handles logic


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
            self.view.update_status("Rates loaded successfully ✅")
        else:
            self.view.show_error("Connection Error", 
                               "Failed to fetch currency rates. Check your internet connection.")

    def handle_convert(self):
        """Handles conversion logic when 'Convert' is clicked."""
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

        rate = self.model.get_rate(from_curr, to_curr)
        if rate is None:
            self.view.show_error("Error", 
                               f"Could not retrieve rate for {from_curr} → {to_curr}.")
            return

        result = amount * rate
        self.view.display_result(amount, from_curr, to_curr, result, rate)
        self.view.update_status(f"Last updated: {self.model.last_updated}")

    def handle_swap(self):
        """Swap selected currencies."""
        self.view.swap_currencies()