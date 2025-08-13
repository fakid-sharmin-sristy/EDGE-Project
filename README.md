# EDGE-Project
Programming with Basic Python course

**Title:**

Implementation of Chemistry-Related Calculators Using Basic Python**

Introduction:

This assignment applies fundamental Python programming concepts to solve simple chemistry problems. Four small tools have been designed:

i.	Molar Mass Calculator

ii.	pH & pOH Calculator

iii.	Periodic Table Information Search

iv.	Temperature Unit Converter
Each tool works independently, takes user input, processes the data, and displays the result.


**i.	Molar Mass Calculator**

**Purpose:**

To calculate the molar mass of a given chemical compound.
Useful for laboratory calculations such as preparing solutions.

**Approach:**

Store atomic masses of common elements in a data structure.
Take the chemical formula as input.
Multiply each element’s atomic mass by the number of atoms present and sum them.

Example:

Input:
Enter chemical formula: H2O
Output:
Molar mass of H2O = 18.015 g/mol

**ii.	 pH & pOH Calculator**

**Purpose:**

To calculate pH and pOH from either hydrogen ion concentration ([H⁺]) or hydroxide ion concentration ([OH⁻]). To classify the solution as acidic, basic, or neutral.

**Approach:**

Ask the user whether they have [H⁺] or [OH⁻].
Use formulas:
pH = −log₁₀[H⁺]
pOH = −log₁₀[OH⁻]
pH + pOH = 14
Classify based on pH value.

Example:

Do you have [H+] or [OH-]? H
Enter [H+] concentration (mol/L): 0.001
Output:
pH = 3.00, pOH = 11.00 → Acidic solution

**iii.	 Periodic Table Information Search

Purpose:**

To display information about a chemical element based on its symbol or atomic number.
Useful for quick reference in chemistry studies.

**Approach:**

Store element data (symbol, name, atomic number, atomic mass) for a set of elements.
Allow the user to search by entering either symbol or atomic number.
Display the matching element’s details.

Example:
Input:
Enter element symbol or atomic number: O
Output:
Element: Oxygen (O)
Atomic Number: 8
Atomic Mass: 15.999

**iv.	 Temperature Unit Converter**

**Purpose:**

To convert a given temperature between Celsius, Kelvin, and Fahrenheit.
Useful in laboratory and thermodynamic calculations.

**Approach:**
Ask for the current unit (C/F/K) and the temperature value.
Apply the correct conversion formulas to find the other two units.

Example:
Input:
Enter unit (C/F/K): C
Enter temperature: 25
Output:
25.0°C = 298.15K, 77.00°F

**Conclusion**
This assignment demonstrates the use of Python for basic chemical calculations and information retrieval.
Molar Mass Calculator helps in stoichiometric computations. pH & pOH Calculator quickly classifies solutions. Periodic Table Search allows instant reference to element data. Temperature Converter facilitates quick unit conversions.
These small programs can be combined into a single chemistry toolkit for more efficient use in academic or laboratory environments.

