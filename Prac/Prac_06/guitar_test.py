from guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922)
    another = Guitar("Another Guitar", 2012)
    print(gibson, gibson.get_age(), gibson.is_vintage())
    print(another, another.get_age(), another.is_vintage())


if __name__ == '__main__':
    main()