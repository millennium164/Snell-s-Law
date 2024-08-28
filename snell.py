import math

ITALIC_START = '\x1B[3m'
ITALIC_END = '\x1B[0m'

def main():
    print("Snell's Law is: n1.sin(\u03B81) = n2.sin(\u03B82)")
    print(f"\u03B8 being an angle {ITALIC_START}a{ITALIC_END}")
    v = input("which variable would you like to calculate?\nn1, n2, a1 or a2?\n")
    dict = {'n1': 1, 'n2': 1, 'a1': 1, 'a2': 1}
    list = []
    i = 0
    for key in dict.keys():
        list.append(key)
        if key == v:
            rm = list[i]
        i += 1
    dict = get_variables(dict)
    for key, value in dict.items():
       print(f"{key}: {value}")

def get_variables(dict_):
  while True:
    try:
        for key in dict_:
            x = f'{key}'
            a = float(input(f"{x}: "))
            dict_[x] = a
        return dict_
    except ValueError:
        print("Not a float")



main()