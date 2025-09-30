# Trading Bot

## Setup

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd Trading\ Bot
   ```

2. **Create a Python virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install python-binance python-dotenv tabulate
   ```

4. **Create a `.env` file**
   ```
   API_KEY=your_binance_api_key
   API_SECRET=your_binance_api_secret
   ```

## Usage

1. **Run the bot**
   ```bash
   python ./src/bot.py
   ```

2. **Follow the prompts** to set buy/sell thresholds and start trading.

3. **Logs**
   - Trading logs and account balances are saved in `trade_logs.txt` after each session or error.

## Dependencies
- [python-binance](https://github.com/sammchardy/python-binance)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- [tabulate](https://pypi.org/project/tabulate/)

## Notes
- This bot uses Binance Testnet by default for safety.
- Make sure your API keys are for the testnet or update the code for live trading.
- For Jupyter Notebook usage, see `bot.ipynb`.
