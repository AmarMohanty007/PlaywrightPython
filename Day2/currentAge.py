"""
Python fundamentals lesson covering input, data types, operators, deletion, and simple calculations. This file focuses on currentAge.
"""


from datetime import datetime


# Define generation ranges
def check_generation(birth_year):
    if 1928 <= birth_year <= 1945:
        return "Silent"
    elif 1946 <= birth_year <= 1964:
        return "Baby Boomers"
    elif 1965 <= birth_year <= 1980:
        return "Gen X"
    elif 1981 <= birth_year <= 1996:
        return "Millennial"
    elif 1997 <= birth_year <= 2010:
        return "Gen Z"
    elif 2011 <= birth_year <= 2025:
        return "Alpha"
    elif 2026 <= birth_year <= 2040:
        return "Beta"
    else:
        return "Other Generation"

current_year = datetime.now().year

Birth_year= int(input("Enter your Birth Year in 4 digits😎: "))

generation = check_generation(Birth_year)

age = current_year-Birth_year

print(f'You are {age} years old.😊')
print(f"you belong to the {generation} generation.🎉")
