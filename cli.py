import argparse

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import validate_inputs
from bot.logging_config import setup_logger


def main():

    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)

    parser.add_argument("--side", required=True)

    parser.add_argument("--type", required=True)

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:

        validate_inputs(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        client = BinanceFuturesClient().get_client()

        # set leverage
        client.futures_change_leverage(
            symbol=args.symbol.upper(),
            leverage=10
        )

        manager = OrderManager(client)

        print("\n=== ORDER REQUEST SUMMARY ===")

        print(f"Symbol      : {args.symbol}")
        print(f"Side        : {args.side}")
        print(f"Order Type  : {args.type}")
        print(f"Quantity    : {args.quantity}")

        if args.price:
            print(f"Price       : {args.price}")

        response = manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n=== ORDER RESPONSE ===")

        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Avg Price     : {response.get('avgPrice')}")

        print("\nOrder placed successfully.")

    except Exception as e:

        print(f"\nOrder failed: {e}")


if __name__ == "__main__":
    main()