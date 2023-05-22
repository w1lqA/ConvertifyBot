## ConvertifyBot

This Python Telegram bot allows users to convert currency values using real-time exchange rates. It utilizes the `requests` library to make API calls to retrieve exchange rate data and the `python-telegram-bot` library to interact with the Telegram Bot API.

### Features

1. **Start Command**: The `/start` command initializes the bot and displays a welcome message to the user along with a menu of available currencies for conversion.

2. **Currency Selection**: The bot presents a menu of currencies to choose from, including both fiat currencies (RUB, USD, EUR, CNY) and cryptocurrencies (BTC, ETH). Users can select the currency they want to convert from.

3. **Conversion Selection**: After selecting the base currency, the bot presents another menu where users can choose the currency they want to convert to.

4. **Amount Input**: Once the conversion currencies are selected, users can input the amount they want to convert. The bot validates the input and ensures it is a valid number.

5. **Conversion Calculation**: The bot retrieves the real-time exchange rate for the selected currency pair and performs the conversion calculation. It then displays the converted amount to the user.

6. **Further Actions**: After the conversion is complete, the bot offers further actions to the user. They can choose to start a new conversion with different currencies or convert another amount using the current currency pair.

7. **User Tracking**: The bot tracks user interactions by storing user data, such as user ID, first name, last name, username, and bot status (is_bot), in a CSV file named `user_data.csv`.

8. **Error Handling**: The bot handles errors gracefully, such as invalid user inputs or API failures, and provides appropriate error messages to the user.

### Dependencies

The bot requires the following dependencies to be installed:

- `requests`: A library for making HTTP requests to retrieve exchange rate data.
- `python-telegram-bot`: A library for interacting with the Telegram Bot API.

### API Integration

The bot integrates with two external APIs to retrieve exchange rate data:

1. `exchangerate-api.com`: Used to retrieve exchange rates for fiat currencies (RUB, USD, EUR, CNY).

2. `alphavantage.co`: Used to retrieve exchange rates for cryptocurrencies (BTC, ETH).

You need to obtain an API key from `alphavantage.co` and replace `'H8FN4INZUM35FMF1'` with your own API key in the `get_crypto_exchange_rate` function.

### Usage

To use the bot, you need to create a Telegram bot and obtain an API token from the BotFather. Replace `'YOUR_BOT_TOKEN'` with your own token in the `Updater` initialization.

Once you have set up the bot, you can run the script, and it will start listening for incoming messages and commands from users. Users can interact with the bot by sending commands, selecting options from the provided menus, and entering the amount they want to convert.

Developed by w1lqA.
