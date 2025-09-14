#Test 1
# def greet(name):
#     print(f"Hellow, {name}")
#     print(f"how are you, {name}?")
#     print(f"How is the weather, {name}?")
# greet("Kyn Quarie")

#Test 2
# def life_in_weeks(age):
#     left_year = 90 - age
#     left_week = 52 * left_year
#     print(f"You have {left_week} weeks left.")
# life_in_weeks(23)

#Test 3
# def greet2(name, location):
#     print(f"Hello, {name} how are you in the {location}?")

# greet2(location = "Philippines", name = "Kyn")

#Test 4
def calculate_love_score(name1, name2):
    one = list(name1.lower())
    two = list(name2.lower())

    true = ["t", "r", "u", "e"]
    love = ["l", "o", "v", "e"]

    firstDigit = 0
    secondDigit = 0

    for check in one:
        if check in true:
            firstDigit += 1
        if check in love:
            secondDigit += 1

    for check in two:
        if check in true:
            firstDigit += 1
        if check in love:
            secondDigit += 1

    print(str(firstDigit) + str(secondDigit))


calculate_love_score("Sunny", "Neph")
