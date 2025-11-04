
# CURRENCY MODEL - Handles API data, rates, and logic


import requests
from datetime import datetime

class CurrencyModel:
    """Model: Handles data and business logic"""

    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"
        self.rates = {}
        self.base_currency = "USD"
        self.last_updated = None

        # Currency display names
        self.currency_names = {
            'USD': 'US Dollar', 'EUR': 'Euro', 'GBP': 'British Pound',
            'JPY': 'Japanese Yen', 'AUD': 'Australian Dollar', 'CAD': 'Canadian Dollar',
            'CHF': 'Swiss Franc', 'CNY': 'Chinese Yuan', 'INR': 'Indian Rupee',
            'MXN': 'Mexican Peso', 'BRL': 'Brazilian Real', 'ZAR': 'South African Rand',
            'SGD': 'Singapore Dollar', 'HKD': 'Hong Kong Dollar', 'NZD': 'New Zealand Dollar',
            'SEK': 'Swedish Krona', 'NOK': 'Norwegian Krone', 'KRW': 'South Korean Won',
            'TRY': 'Turkish Lira', 'RUB': 'Russian Ruble', 'THB': 'Thai Baht',
            'PLN': 'Polish Zloty', 'DKK': 'Danish Krone', 'CZK': 'Czech Koruna',
            'HUF': 'Hungarian Forint', 'RON': 'Romanian Leu', 'ISK': 'Icelandic Króna',
            'PHP': 'Philippine Peso', 'MYR': 'Malaysian Ringgit', 'IDR': 'Indonesian Rupiah',
            'ILS': 'Israeli Shekel', 'AED': 'UAE Dirham', 'SAR': 'Saudi Riyal',
            'QAR': 'Qatari Riyal', 'KWD': 'Kuwaiti Dinar', 'BHD': 'Bahraini Dinar',
            'OMR': 'Omani Rial', 'JOD': 'Jordanian Dinar', 'EGP': 'Egyptian Pound',
            'MAD': 'Moroccan Dirham', 'NGN': 'Nigerian Naira', 'KES': 'Kenyan Shilling',
            'GHS': 'Ghanaian Cedi', 'UGX': 'Ugandan Shilling', 'TZS': 'Tanzanian Shilling',
            'CLP': 'Chilean Peso', 'ARS': 'Argentine Peso', 'COP': 'Colombian Peso',
            'PEN': 'Peruvian Sol', 'VND': 'Vietnamese Dong', 'PKR': 'Pakistani Rupee',
            'BDT': 'Bangladeshi Taka', 'LKR': 'Sri Lankan Rupee', 'NPR': 'Nepalese Rupee'
        }

    def fetch_rates(self, base: str = "USD") -> bool:
        """Fetch latest currency rates from API and update model state"""
        try:
            response = requests.get(f"{self.api_url}{base}", timeout=10)
            response.raise_for_status()
            data = response.json()

            if "rates" not in data:
                raise ValueError("Invalid response: 'rates' key missing")

            self.rates = data["rates"]
            self.base_currency = base
            self.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True

        except (requests.RequestException, ValueError) as e:
            print(f"[API ERROR] Could not fetch rates: {e}")
            self.rates = {}
            return False

    def get_rate(self, from_curr: str, to_curr: str) -> float:
        """Get exchange rate between two currencies - FIXED METHOD"""
        if not self.rates:
            print("[WARNING] No rates available")
            return None
        
        try:
            # Both currencies must exist in rates
            if from_curr not in self.rates and from_curr != self.base_currency:
                print(f"[ERROR] Unknown currency: {from_curr}")
                return None
            
            if to_curr not in self.rates:
                print(f"[ERROR] Unknown currency: {to_curr}")
                return None
            
            # Calculate rate: from_curr -> USD -> to_curr
            if from_curr == self.base_currency:
                rate = self.rates[to_curr]
            else:
                rate = self.rates[to_curr] / self.rates[from_curr]
            
            return round(rate, 6)
        
        except Exception as e:
            print(f"[ERROR] Rate calculation failed: {e}")
            return None

    def convert(self, amount: float, from_curr: str, to_curr: str) -> float:
        """Convert a given amount between two currencies"""
        rate = self.get_rate(from_curr, to_curr)
        if rate is None:
            return 0.0
        return round(amount * rate, 2)

    def get_currency_list(self) -> list:
        """Return sorted list of all available currencies with display names"""
        if self.rates:
            available = self.rates.keys()
        else:
            available = self.currency_names.keys()
        
        # Return formatted list: "USD - US Dollar"
        formatted_list = []
        for code in sorted(available):
            name = self.currency_names.get(code, code)
            formatted_list.append(f"{code} - {name}")
        
        return formatted_list

    def get_currency_display_name(self, code: str) -> str:
        """Return formatted currency display name"""
        name = self.currency_names.get(code, code)
        return f"{code} - {name}"
