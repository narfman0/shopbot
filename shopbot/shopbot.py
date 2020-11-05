import argparse

from shopbot import amazon, bhphoto, newegg


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Consume.')
    parser.add_argument('--merchant', help='from which merchant do you wish to buy: amazon, bhphoto, newegg')
    args = parser.parse_args()
    if args.merchant == "amazon":
        amazon.attempt_purchase()
    elif args.merchant == "bhphoto":
        bhphoto.attempt_purchase()
    elif args.merchant == "newegg":
        newegg.attempt_purchase()