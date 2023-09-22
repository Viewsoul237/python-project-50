from gendiff import generate_diff, arguments_parser


def main():
    file_one, file_two, format = arguments_parser()
    print(generate_diff(file_one, file_two, format))


if __name__ == "__main__":
    main()
