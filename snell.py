import math

ITALIC_START = '\x1B[3m'
ITALIC_END = '\x1B[0m'

def main():
    # Information and variable of choice
    print("Snell's Law is: n1.sin(\u03B81) = n2.sin(\u03B82)")
    print(f"\u03B8 being an angle {ITALIC_START}a{ITALIC_END}, in degrees")
    while True:
        v = input("which variable would you like to calculate?\nn1, n2, a1 or a2?\n")
        if v in ("n1", "n2", "a1", "a2"):
            break
        else:
            print("Invalid answer, try again.")
    dict = {'n1': 1, 'n2': 1, 'a1': 1, 'a2': 1}
    for key in dict.keys():
        if key == v:
            dict[key] = 0
    # Prompt for other variables
    dict = get_variables(dict)
    for key in dict.keys():
        # Take angle's sine
        if key in ("a1", "a2"):
            dict[key] = math.sin(math.radians(dict[key]))
    # Calculate the variable of choice, in each case
    if dict["n1"] == 0:
        n1 = (dict["n2"] * dict["a2"]) / dict["a1"]
        print(f"refractive index of medium 1: {n1}")
    elif dict["n2"] == 0:
        n2 = (dict["n1"] * dict["a1"]) / dict["a2"]
        print(f"refractive index of medium 2: {n2}")
    elif dict["a1"] == 0:
        a1 = math.degrees(math.asin((dict["n2"] * dict["a2"]) / dict["n1"]))
        print(f"angle of incidence: {a1}°")
    elif dict["a2"] == 0:
        a2 = (dict["n1"] * dict["a1"]) / dict["n2"]
        if a2 <= 1:
            a2 = math.degrees(math.asin(a2))
            print(f"angle of refraction: {a2}°")
        else:
            print("total internal reflection of light")

def get_variables(dict_):
  while True:
    try:
        for key in dict_:
            if dict_[key] != 0:
                a = float(input(f"{key}: "))
                dict_[key] = a
        return dict_
    except ValueError:
        print("Not a float")

main()