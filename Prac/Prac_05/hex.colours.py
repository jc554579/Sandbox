Colours = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUAMARINE1": "#7fffd4",
           "AZURE1": "#f0ffff", "BLUE1": "#0000ff", "BLUEVIOLET": "#8a2be2",
           "BROWN1": "#ff4040", "BURLYWOOD": "#deb887", "CHARTREUSE1": "#7fff00",
           "FLORALWHITE": "#fffaf0"}

colour_Name = input("Enter a colour name: ").upper()
while colour_Name != " ":
    if colour_Name in Colours:
        print(colour_Name, "is", Colours[colour_Name])
    else:
        print("Invalid colours!")

    colour_Name = input("Enter a colour name: ").upper()