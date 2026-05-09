# Binance Futures Testnet Trading Bot

## Features

- MARKET and LIMIT orders
- BUY and SELL support
- Binance Futures Testnet integration
- CLI argument support
- Logging and exception handling

---

## Setup

### Clone Repository

```bash
git clone <your_repo_url>
cd binance-trading-bot
```

---

### Install Requirements

```bash
pip install -r requirements.txt
```

---

### Create .env

```env
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
```

---

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Assumptions

- Binance demo/testnet account already created
- Futures permissions enabled
- Uses Binance Futures Testnet environment