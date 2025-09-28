# PriceWatcherBot

A simple service to track product prices on major e-commerce platforms (Amazon, Ozon, AliExpress, Wildberries, MercadoLibre).  
You provide a product URL, the bot periodically checks the price, stores the history, and notifies you when the price drops.

## Features
- Add a product to watchlist with target price or drop percentage.
- Periodically fetch current prices from supported stores.
- Store price history in a local SQLite database.
- Send alerts via Telegram or Discord when price conditions are met.
- View simple charts of price history.

## Quickstart
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pricewatcher-bot.git
   cd pricewatcher-bot
