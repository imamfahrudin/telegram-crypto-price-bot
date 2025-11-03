# Import necessary libraries
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Retrieve API tokens from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CMC_API_KEY = os.getenv("CMC_API_KEY")

# Asynchronous function to handle the /price command
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if a cryptocurrency symbol is provided
    if not context.args:
        await update.message.reply_text("Usage: /price <symbol>. Example: /price btc")
        return

    # Get the symbol from the command arguments and convert to uppercase
    symbol = context.args[0].upper()
    
    # CoinMarketCap API endpoint for latest cryptocurrency quotes
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    
    # Headers for API request, including the API key
    headers = {"X-CMC_PRO_API_KEY": CMC_API_KEY}
    
    # Parameters for the API request, specifying the cryptocurrency symbol
    params = {"symbol": symbol}

    # Make the GET request to the CoinMarketCap API
    response = requests.get(url, headers=headers, params=params)
    
    # Parse the JSON response
    data = response.json()

    try:
        # Extract the price of the cryptocurrency from the response
        price = data["data"][symbol]["quote"]["USD"]["price"]
        # Reply with the formatted price
        await update.message.reply_text(f"{symbol} price: ${price:,.2f}")
    except KeyError:
        # Handle cases where the symbol is invalid or an API error occurs
        await update.message.reply_text("Invalid symbol or API error.")

# Main entry point of the script
if __name__ == "__main__":
    # Build the Telegram Application with the bot token
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    # Add a command handler for the /price command, linking it to the price function
    app.add_handler(CommandHandler("price", price))
    
    # Start polling for updates from Telegram
    app.run_polling()
