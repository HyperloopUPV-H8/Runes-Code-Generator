import re
import pandas as pd

pinout = pd.read_csv("code-generators/data/pinout.csv")
f = open("code-generators/code-generated/pinout.txt", "w")
for index, row in pinout.iterrows():
    pin_name = row["Name"]
    alternate_function = row["Signal"]
    alt_functions = list(row[4:])

    if not re.search(r"^P[A-H]\d\d?$", pin_name): continue 

    counter = 0
    found = False
    for alt_function in alt_functions:
        if alt_function == alternate_function:
            found = True
            break
        counter += 1

    if found:
        f.write(f"Pin {pin_name}(PORT_{pin_name[1]}, PIN_{pin_name[2:]}, AF{counter});\n")
    else:
        f.write(f"Pin {pin_name}(PORT_{pin_name[1]}, PIN_{pin_name[2:]});\n")

