import argparse
import utils

parser = argparse.ArgumentParser()
parser.add_argument("-a", default=0, type=int, help="a variable")
parser.add_argument("-b", default=0, type=int, help="b variable")


def main(a: int, b: int):
    result = utils.squared_euclidean_norm(a, b)

    return result


if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    print(main(a=args.a, b=args.b))
