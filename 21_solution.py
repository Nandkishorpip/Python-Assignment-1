import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://data.fixer.io/api/latest"

    def get_exchange_rate(self, from_currency, to_currency):
        try:
            # Make the API call to get live exchange rates
            response = requests.get(f"{self.base_url}?access_key={self.api_key}")
            data = response.json()

            if not data.get("success", False):
                raise Exception(data.get("error", {}).get("info", "Failed to fetch exchange rates"))

            rates = data.get("rates", {})
            if from_currency not in rates or to_currency not in rates:
                raise ValueError(f"Currency codes '{from_currency}' or '{to_currency}' are not valid.")

            # Calculate the exchange rate
            from_rate = rates[from_currency]
            to_rate = rates[to_currency]
            exchange_rate = to_rate / from_rate
            return exchange_rate
        except Exception as e:
            print(f"Error: {e}")
            return None

    def convert_currency(self, amount, from_currency, to_currency):
        rate = self.get_exchange_rate(from_currency, to_currency)
        if rate is not None:
            converted_amount = amount * rate
            return converted_amount
        else:
            return None


# Example Usage
if __name__ == "__main__":
    # Replace with your Fixer.io API key
    API_KEY = "YOUR_API_KEY"

    # Create the converter object
    converter = CurrencyConverter(API_KEY)

    # User input
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the source currency (e.g., USD): ").upper()
        to_currency = input("Enter the target currency (e.g., INR): ").upper()

        # Perform conversion
        converted_amount = converter.convert_currency(amount, from_currency, to_currency)
        if converted_amount is not None:
            print(f"Converted Amount: {converted_amount:.2f} {to_currency}")
        else:
            print("Currency conversion failed.")
    except ValueError as e:
        print(f"Invalid input: {e}")
