colours = (
    ("Red", (255, 0, 0)),
    ("Green", (0, 255, 0)),
    ("Blue", (0, 0, 255)),
    ("Yellow", (255, 255, 0)),
    ("Cyan", (0, 255, 255)),
    ("Magenta", (255, 0, 255)),
    ("White", (255, 255, 255)),
    ("Black", (0, 0, 0))
)

print("Available Colours:")
for colour in colours:
    print(colour[0])

choice = input("Please enter the name of the colour you want to pick: ").strip().title()
for name, rgb in colours:
    if name == choice:
        print(f"The RGB values for {name} are: {rgb}")
        break
    else:
        print("Colour not found. Please choose from the available colours.")