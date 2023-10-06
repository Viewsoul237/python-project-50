import argparse


def arguments_parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")

    # Positional arguments
    parser.add_argument("first_file", type=str, help="Absolute path to your file")
    parser.add_argument("second_file", type=str, help="Absolute path to your file")

    # Optional arguments
    parser.add_argument('-f', '--format',
                        default="stylish",
                        choices=['stylish', ' plain', ' json'],
                        help='set format of output')

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
