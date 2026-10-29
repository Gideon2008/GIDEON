import random

OUNCES_PER_POUND = 16
DEFAULT_MOOD = "content"
mood = DEFAULT_MOOD

feedings = 0
drinks = 0


def introduce_baby(name, age, weight_oz):
    funny_things = [
        "dance with my socks.",
        "have staring contests with the teddy bear.",
        "pretend my toes are tiny snacks.",
        "make silly noises at the ceiling.",
    ]
    funny_thing = random.choice(funny_things)

    print("Hello! My name is", name + ".")
    print("I am", age, "years old and weigh", weight_oz, "ounces.")
    print("I like to", funny_thing)


baby_name = input("What is the baby's name?: ")
age = input("How old is the baby in years?: ")
birthdate = input("What is the baby's birthdate?: ")
ounces = int(input("What is the baby's weight in ounces?: "))
height = float(input("What is the baby's height in inches?: "))

print()
introduce_baby(baby_name, age, ounces)

pounds = ounces / OUNCES_PER_POUND

print()
print("--- BABY STATUS ---")
print("Name:", baby_name)
print("Birthdate:", birthdate)
print("Weight:", ounces, "oz")
print("Weight in pounds:", pounds, "lb")
print("Height:", height, "in")
print("Mood:", mood)
print("")


def eat(current_weight_oz, feedings, mood):
    print("Num Num Num Nom Num")
    current_weight_oz += 11
    feedings += 1
    mood = "happy"
    return current_weight_oz, feedings, mood


def drink(current_weight_oz, drinks, mood):
    print("gulp, gulp, gulp, burp, gulp")
    current_weight_oz += 8
    drinks += 1
    mood = "content"
    return current_weight_oz, drinks, mood

def poop(current_weight_oz):
    print("Baby Poops")
    current_weight_oz -= 5
    return current_weight_oz

def pee(current_weight_oz):
    print("Baby Pees")
    current_weight_oz -= 4
    return current_weight_oz

def sleep(mood):
    mood = "content"
    print("ZZZZZZZZZZZZZZZZZZZzzzzzzzzzz")
    print("")
    return mood

def cry(mood):
    mood = "sad"
    print("Wahhh wah wah bahahahahah wahhhawah")
    print("")
    return mood

def display_status(baby_name, current_weight_oz, mood, feedings, drinks):
    current_pounds = current_weight_oz / OUNCES_PER_POUND
    print("Baby Name:", baby_name)
    print("Current Weight in oz:", current_weight_oz)
    print("Current Weight in decimal pounds:", current_pounds, "lbs")
    print("Mood:", mood)
    print("Feedings:", feedings)
    print("Drinks:", drinks)


action = ""
current_weight_oz = ounces
poop_count = 0
pee_count = 0
burp_count = 0

while action != "home":
    action = input("What action would you like your baby to do (eat, drink, sleep, cry, laugh, status, home)?: ").lower()
    if action == "eat":
        current_weight_oz, feedings, mood = eat(current_weight_oz, feedings, mood)
        poop_count += 1
        burp_count += 1
        if(poop_count % 3 == 0):
            current_weight_oz =poop(current_weight_oz)
        if(burp_count % 3 ==0):
            print("*Baby burps*")
        print("")

    elif action == "drink":
        current_weight_oz, drinks, mood = drink(current_weight_oz, drinks, mood)
        pee_count += 1
        burp_count += 1
        if(pee_count % 3 == 0):
            current_weight_oz = pee(current_weight_oz)
        if(burp_count % 3 ==0):
            print("*Baby burps*")
        print("")

    elif action == "sleep":
        mood = sleep(mood)

    elif action == "cry":
        mood = cry(mood)

    elif action == "status":
        print("")
        display_status(baby_name, current_weight_oz, mood, feedings, drinks)
        print("")

    elif action == "laugh":
        print("Baby laughs")
        mood = "happy"
        print("")

    elif action == "home":
        print("Going Home")
        print("")

    else:
        print("Unknown action — try again.")
        print("")

current_pounds = current_weight_oz / OUNCES_PER_POUND
print("-- Final Baby Status Report --")
print("Baby Name:", baby_name)
print("Current Weight in oz:", current_weight_oz)
print("Current Weight in decimal pounds:", current_pounds, "lbs")
print("Mood:", mood)
print("Feedings:", feedings)
print("Drinks:", drinks)