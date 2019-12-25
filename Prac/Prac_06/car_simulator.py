from car import Car


def main():
    print("Let's drive!")
    name = input("Enter your car name:")
    car = Car(name, 100)
    print(car)
    print("""Menu:
d) drive
r) refuel
q) quit""")
    choice = input("Enter your choice:").lower()
    while choice != "q":
        if choice == "d":
            distance = int(input("How many km do you wish to drive? "))
            while distance < 0:
                print("Distance must be >= 0")
                distance = int(input("How many km do you wish to drive? "))
            distance = car.drive(distance)
            if distance < car.fuel:
                print("The car drove {}km.".format(distance))
            else:
                print("The car drove {}km and ran out of fuel.".format(distance))
        elif choice == "r":
            fuel_added = int(input("How many units of fuel do you want to add to the car?"))
            while fuel_added < 0:
                print("Fuel amount must be >= 0")
                fuel_added = int(input("How many units of fuel do you want to add to the car?"))
            car.add_fuel(fuel_added)
            print("Added {} units of fuel.".format(fuel_added))
        else:
            print("Invalid choice")
        print()
        print(car)
        print("""Menu:
d) drive
r) refuel
q) quit""")
        choice = input("Enter your choice: ").lower()
    print()
    print("Good bye {}'s driver.".format(car.name))


if __name__ == '__main__':
    main()