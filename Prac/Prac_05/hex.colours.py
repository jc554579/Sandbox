Colours = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4",
           "azure1": "#f0ffff", "blue1": "#0000ff", "BlueViolet": "#8a2be2",
           "brown1": "#ff4040", "burlywood": "#deb887", "chartreuse1": "#7fff00",
           "FloralWhite": "#fffaf0"}

colour_Name = input("Enter a colour name: ")
while colour_Name != " ":
    if colour_Name in Colours:
        print(colour_Name, "is", Colours[colour_Name])
    else:
        print("Invalid colours!")

    colour_Name = input("Enter a colour name: ")