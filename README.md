# Telegram Crypto Price Bot

This bot provides real-time cryptocurrency prices directly in your Telegram chats.

## Features
- Get the current price of any cryptocurrency supported by CoinMarketCap.

## Setup

### Prerequisites
- Python 3.11 or higher
- Docker (optional, for containerized deployment)

### Environment Variables
Create a `.env` file in the root directory of the project with the following variables:

`TELEGRAM_TOKEN`: Your Telegram Bot API token. Get this from BotFather.
`CMC_API_KEY`: Your CoinMarketCap API key. Obtain one from the CoinMarketCap website.

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/imamfahrudin/telegram-crypto-price-bot.git
   cd telegram-crypto-price-bot
   ```
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   ./venv/Scripts/activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

### Docker Deployment
1. Ensure you have Docker installed.
2. Build and run the Docker container:
   ```bash
   docker-compose up --build -d
   ```

## Usage

Send the `/price` command followed by the cryptocurrency symbol to your bot. For example:

`/price BTC`
`/price ETH`

## Contributing

Feel free to fork the repository, open issues, or submit pull requests.