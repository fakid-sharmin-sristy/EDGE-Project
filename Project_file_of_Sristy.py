import math

#  Periodic Table Data (Symbol: (Name, Atomic Mass))
elements = {
    "H": ("Hydrogen", 1.008),
    "He": ("Helium", 4.0026),
    "Li": ("Lithium", 6.94),
    "Be": ("Beryllium", 9.0122),
    "B": ("Boron", 10.81),
    "C": ("Carbon", 12.011),
    "N": ("Nitrogen", 14.007),
    "O": ("Oxygen", 15.999),
    "Na": ("Sodium", 22.989),
    "Mg": ("Magnesium", 24.305),
    "Al": ("Aluminium", 26.982),
    "Si": ("Silicon", 28.085),
    "P": ("Phosphorus", 30.974),
    "S": ("Sulfur", 32.06),
    "Cl": ("Chlorine", 35.45),
    "K": ("Potassium", 39.098),
    "Ca": ("Calcium", 40.078)}

#  1. Molar Mass Calculator
def molar_mass(formula):
    total_mass = 0
    i = 0
    while i < len(formula):
        elem = formula[i]
        if i + 1 < len(formula) and formula[i+1].islower():
            elem += formula[i+1]
            i += 1
        i += 1

        qty = ''
        while i < len(formula) and formula[i].isdigit():
            qty += formula[i]
            i += 1
        qty = int(qty) if qty else 1

        if elem in elements:
            total_mass += elements[elem][1] * qty
        else:
            print(f"Unknown element: {elem}")
            return None
    return total_mass

#  2. pH & pOH Calculator
def calculate_ph():
    choice = input("Calculate (1) pH from [H+], (2) pOH from [OH-]: ")
    if choice == '1':
        h_conc = float(input("Enter [H+] concentration (mol/L): "))
        ph = -math.log10(h_conc)
        poh = 14 - ph
        print(f"pH = {ph:.2f}, pOH = {poh:.2f}")
    elif choice == '2':
        oh_conc = float(input("Enter [OH-] concentration (mol/L): "))
        poh = -math.log10(oh_conc)
        ph = 14 - poh
        print(f"pOH = {poh:.2f}, pH = {ph:.2f}")
    else:
        print("Invalid choice!")

#  3. Periodic Table Info Search
def search_element():
    query = input("Enter element symbol: ").capitalize()
    if query in elements:
        name, mass = elements[query]
        print(f"Symbol: {query}\nName: {name}\nAtomic Mass: {mass} g/mol")
    else:
        print("Element not found!")

# 4. Temperature Unit Converter
def convert_temperature():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    choice = input("Choose conversion: ")

    if choice == '1':
        c = float(input("Enter Celsius: "))
        print(f"Fahrenheit: {c * 9/5 + 32:.2f}")
    elif choice == '2':
        f = float(input("Enter Fahrenheit: "))
        print(f"Celsius: {(f - 32) * 5/9:.2f}")
    elif choice == '3':
        c = float(input("Enter Celsius: "))
        print(f"Kelvin: {c + 273.15:.2f}")
    elif choice == '4':
        k = float(input("Enter Kelvin: "))
        print(f"Celsius: {k - 273.15:.2f}")
    elif choice == '5':
        f = float(input("Enter Fahrenheit: "))
        k = (f - 32) * 5/9 + 273.15
        print(f"Kelvin: {k:.2f}")
    elif choice == '6':
        k = float(input("Enter Kelvin: "))
        f = (k - 273.15) * 9/5 + 32
        print(f"Fahrenheit: {f:.2f}")
    else:
        print("Invalid choice!")

# Main Menu
while True:
    print("\n--- Chemistry Toolkit ---")
    print("1. Molar Mass Calculator")
    print("2. pH & pOH Calculator")
    print("3. Periodic Table Info Search")
    print("4. Temperature Unit Converter")
    print("5. Exit")

    option = input("Choose an option: ")
    if option == '1':
        formula = input("Enter chemical formula (e.g., H2O): ")
        mass = molar_mass(formula)
        if mass:
            print(f"Molar Mass of {formula} = {mass:.3f} g/mol")
    elif option == '2':
        calculate_ph()
    elif option == '3':
        search_element()
    elif option == '4':
        convert_temperature()
    elif option == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid option! Try again.")