import splitter

from .config import config


def main():
    # Your program
    print(config.app_name)

    words = splitter.split("entityculling")
    print(words)


if __name__ == "__main__":
    main()
