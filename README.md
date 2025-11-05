# Telegram Crypto Price Bot

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram)](https://core.telegram.org/bots)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg?logo=docker)](https://www.docker.com/)
[![CoinMarketCap](https://img.shields.io/badge/CoinMarketCap-API-blue.svg)](https://coinmarketcap.com/api/)

A Telegram bot that provides real-time cryptocurrency prices directly in your Telegram chats, powered by CoinMarketCap API.

## Features

- 🚀 Real-time cryptocurrency price fetching
- 💰 Support for all cryptocurrencies available on CoinMarketCap
- ⚡ Fast and lightweight
- 🐳 Docker support for easy deployment
- 🔒 Secure API key management using environment variables

## Setup

### Prerequisites
- Python 3.11 or higher
- Docker (optional, for containerized deployment)

### Environment Variables

Create a `.env` file in the root directory of the project with the following variables:

```env
TELEGRAM_TOKEN=your_telegram_bot_token_here
CMC_API_KEY=your_coinmarketcap_api_key_here
```

- **`TELEGRAM_TOKEN`**: Your Telegram Bot API token. Get this from [@BotFather](https://t.me/botfather) on Telegram.
- **`CMC_API_KEY`**: Your CoinMarketCap API key. Obtain one from the [CoinMarketCap API portal](https://pro.coinmarketcap.com/signup).

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

Once the bot is running, open your Telegram app and start a chat with your bot. Use the `/price` command followed by the cryptocurrency symbol:

```
/price BTC
/price ETH
/price DOGE
/price ADA
```

The bot will respond with the current USD price of the requested cryptocurrency.

## Technologies Used

- **Python 3.11+** - Core programming language
- **python-telegram-bot** - Telegram Bot API wrapper
- **CoinMarketCap API** - Cryptocurrency price data
- **Docker** - Containerization for deployment
- **python-dotenv** - Environment variable management

## Project Structure

```
telegram-crypto-price-bot/
├── bot.py              # Main bot application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
├── .env               # Environment variables (create this)
└── README.md          # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Mukhammad Imam Fahrudin**

- GitHub: [@imamfahrudin](https://github.com/imamfahrudin)

## Acknowledgments

- [CoinMarketCap](https://coinmarketcap.com/) for providing the cryptocurrency price API
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for the excellent Telegram Bot framework

## Support

If you find this project helpful, please give it a ⭐ on GitHub!