from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    for i, guitar in enumerate(guitars):
        print("Name:", guitar.name)
        print("Year:", guitar.year)
        print("Cost:", guitar.cost)
        print("{} ({}) : {} added.".format(guitar.name, guitar.year, guitar.cost))
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        print("Guitar {}: {} ({}), worth ${:10,.2f} ({})".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                 guitar.is_vintage()))


if __name__ == '__main__':
    main()