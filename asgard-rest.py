from api.api import Rest

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-r", "--run", action="store_true")
parser.add_argument("-c", "--config", action="store", default=".env")

if __name__ == "__main__":
    args = parser.parse_args()

    if args.run:
        r = Rest(args.config)
        r.run()