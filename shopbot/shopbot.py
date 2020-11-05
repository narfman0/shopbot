import argparse

from shopbot import amazon, bhphoto, newegg


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Consume.")
    parser.add_argument(
        "--merchant",
        help="from which merchant do you wish to buy: amazon, bhphoto, newegg",
        default="newegg",
    )
    parser.add_argument("--search_url", help="what base url to use for search results")
    parser.add_argument(
        "--search_link_text",
        help="what snippet of text to search and match to initiate purchase",
        default="AMD RYZEN 9 5900X",
    )
    args = parser.parse_args()
    if args.merchant == "amazon":
        amazon.attempt_purchase(args.search_url, args.search_link_text)
    elif args.merchant == "bhphoto":
        bhphoto.attempt_purchase(args.search_url, args.search_link_text)
    elif args.merchant == "newegg":
        newegg.attempt_purchase(args.search_url, args.search_link_text)
