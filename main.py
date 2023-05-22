import requests
import csv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, User
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import datetime

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][to_currency]

def get_crypto_exchange_rate(from_currency, to_currency):
    api_key = 'ALPHAVANTAGE_API'
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    return exchange_rate

def write_user_data(user_id, first_name, last_name, username, is_bot):
    with open('user_data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([f'ID: {user_id}, Firstname: {first_name}, Lastname: {last_name}, Username: {username}, IsBOT?: {is_bot}'])


def start(update, context):
    user: User = update.message.from_user
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    is_bot = user.is_bot

    write_user_data(user_id, first_name, last_name, username, is_bot)

    keyboard = [
        [
            InlineKeyboardButton(" RUB 🇷🇺 ", callback_data='fromRUB'),
            InlineKeyboardButton(" USD 🇺🇸 ", callback_data='fromUSD'),
            InlineKeyboardButton(" EUR 🇪🇺 ", callback_data='fromEUR'),
            InlineKeyboardButton(" CNY 🇨🇳 ", callback_data='fromCNY'),
        ],
        [
            InlineKeyboardButton(" BTC ₿ ", callback_data='fromBTC'),
            InlineKeyboardButton(" ETH Ξ ", callback_data='fromETH'),
        ]
    ]
    context.user_data.clear()

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f"Hello, {first_name}! My name is Convertify💱! I'm a bot🤖 that can convert currencies! \nPlease choose the currency you want to convert from:", reply_markup=reply_markup)

    
def from_rub(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton(" USD 🇺🇸 ", callback_data='RUB_USD'),
            InlineKeyboardButton(" EUR 🇪🇺 ", callback_data='RUB_EUR'),
            InlineKeyboardButton(" CNY 🇨🇳 ", callback_data='RUB_CNY'),
        ],
        [
            InlineKeyboardButton(" ETH Ξ ", callback_data='BTC_ETH'),
            InlineKeyboardButton(" BTC ₿ ", callback_data='ETH_BTC'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('You have chosen RUB 🇷🇺!\nNow select the currency you want to convert to:💱', reply_markup=reply_markup)

def from_usd(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton(" RUB 🇷🇺 ", callback_data='USD_RUB'),
            InlineKeyboardButton(" EUR 🇪🇺 ", callback_data='USD_EUR'),
            InlineKeyboardButton(" CNY 🇨🇳 ", callback_data='USD_CNY'),
        ],
        [
            InlineKeyboardButton(" ETH Ξ ", callback_data='BTC_ETH'),
            InlineKeyboardButton(" BTC ₿ ", callback_data='ETH_BTC'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('You have chosen USD 🇺🇸!\nNow select the currency you want to convert to:💱', reply_markup=reply_markup)

def from_eur(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton(" RUB 🇷🇺 ", callback_data='EUR_RUB'),
            InlineKeyboardButton(" USD 🇺🇸 ", callback_data='EUR_USD'),
            InlineKeyboardButton(" CNY 🇨🇳 ", callback_data='EUR_CNY'),
        ],
        [
            InlineKeyboardButton(" ETH Ξ ", callback_data='BTC_ETH'),
            InlineKeyboardButton(" BTC ₿ ", callback_data='ETH_BTC'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('You have chosen EUR 🇪🇺!\nNow select the currency you want to convert to:💱', reply_markup=reply_markup)

def from_cny(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton(" RUB 🇷🇺 ", callback_data='CNY_RUB'),
            InlineKeyboardButton(" EUR 🇪🇺 ", callback_data='CNY_EUR'),
            InlineKeyboardButton(" USD 🇺🇸 ", callback_data='CNY_USD'),
        ],
        [
            InlineKeyboardButton(" ETH Ξ ", callback_data='BTC_ETH'),
            InlineKeyboardButton(" BTC ₿ ", callback_data='ETH_BTC'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('You have chosen CNY 🇨🇳!\nNow select the currency you want to convert to:💱', reply_markup=reply_markup)

def from_btc(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton(" RUB 🇷🇺 ", callback_data='BTC_RUB'),
            InlineKeyboardButton(" USD 🇺🇸 ", callback_data='BTC_USD'),
            InlineKeyboardButton(" EUR 🇪🇺 ", callback_data='BTC_EUR'),
            InlineKeyboardButton(" CNY 🇨🇳 ", callback_data='BTC_CNY'),
        ],
        [
            InlineKeyboardButton(" ETH Ξ ", callback_data='BTC_ETH'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('You have chosen BTC ₿!\nNow select the currency you want to convert to:💱', reply_markup=reply_markup)

def from_eth(update, context):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton(" RUB 🇷🇺 ", callback_data='ETH_RUB'),
            InlineKeyboardButton(" USD 🇺🇸 ", callback_data='ETH_USD'),
            InlineKeyboardButton(" EUR 🇪🇺 ", callback_data='ETH_EUR'),
            InlineKeyboardButton(" CNY 🇨🇳 ", callback_data='ETH_CNY'),
        ],
        [
            InlineKeyboardButton(" BTC ₿ ", callback_data='ETH_BTC'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('You have chosen ETH Ξ!\nNow select the currency you want to convert to:💱', reply_markup=reply_markup)


def restart(update, context):
    keyboard = [
        [
            InlineKeyboardButton(" RUB 🇷🇺 ", callback_data='fromRUB'),
            InlineKeyboardButton(" USD 🇺🇸 ", callback_data='fromUSD'),
            InlineKeyboardButton(" EUR 🇪🇺 ", callback_data='fromEUR'),
            InlineKeyboardButton(" CNY 🇨🇳 ", callback_data='fromCNY'),
        ],
        [
            InlineKeyboardButton(" BTC ₿ ", callback_data='fromBTC'),
            InlineKeyboardButton(" ETH Ξ ", callback_data='fromETH'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.edit_text('Please select a NEW currency🆕 you want to convert to:💱', reply_markup=reply_markup)

    

def button_action(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'fromRUB':
        context.user_data.clear()
        from_rub(update, context)
    elif query.data == 'fromUSD':
        context.user_data.clear()
        from_usd(update, context)
    elif query.data == 'fromEUR':
        context.user_data.clear()
        from_eur(update, context)
    elif query.data == 'fromCNY':
        context.user_data.clear()
        from_cny(update, context)
    elif query.data == 'fromBTC':
        context.user_data.clear()
        from_btc(update, context)
    elif query.data == 'fromETH':
        context.user_data.clear()
        from_eth(update, context)
    elif query.data == 'restart':
        context.user_data.clear()
        restart(update, context)
    elif query.data == 'reconversion':
        conversion = context.user_data.get('conversion')
        if conversion:
            context.user_data.clear()
            context.user_data['conversion'] = conversion
            query.edit_message_text(text="Enter a NEW amount for conversion💱:")
        else:
            query.edit_message_text(text="Sorry, failed❌ to find previous currency values.")
    else:
        context.user_data['conversion'] = query.data
        query.edit_message_text(text="Enter the amount you want to convert💱:")

currency_names = {
    'RUB': 'RUB🇷🇺',
    'USD': 'USD🇺🇸',
    'EUR': 'EUR🇪🇺',
    'CNY': 'CNY🇨🇳',
    'BTC': 'BTC₿',
    'ETH': 'ETHΞ'
}


def convert(update, context):
    amount = float(update.message.text)
    conversion = context.user_data['conversion']
    from_currency, to_currency = conversion.split('_')
        
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y.%m.%d %H:%M ")


    if from_currency in ('BTC', 'ETH') or to_currency in ('BTC', 'ETH'):
        exchange_rate = get_crypto_exchange_rate(from_currency, to_currency)
    else:
        exchange_rate = get_exchange_rate(from_currency, to_currency)

    converted_amount = round(amount * exchange_rate, 1)

    from_currency_name = currency_names.get(from_currency, from_currency)
    to_currency_name = currency_names.get(to_currency, to_currency)

    update.message.reply_text(f"At the moment( {formatted_datetime}):\n{amount} {from_currency_name} equals {converted_amount} {to_currency_name}")

    keyboard = [
        [
            InlineKeyboardButton("⏪Other currencies", callback_data='restart'),
        ],
        [
            InlineKeyboardButton("Continue with the current pair⏩", callback_data='reconversion'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Choose what to do next🤔:", reply_markup=reply_markup)


updater = Updater('TELEGRAM_BOT_API', use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button_action))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, convert))

updater.start_polling()
updater.idle()