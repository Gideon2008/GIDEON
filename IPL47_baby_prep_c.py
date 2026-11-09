OUNCES_PER_POUND = 16
DEFAULT_MOOD = "content"

class Baby:
    def __init__(self, name, birthdate, ounces = 130, height = 20):
        self.name = name
        self.birthdate = birthdate
        self.weight_oz = ounces
        self.height_in = height
        self.mood = DEFAULT_MOOD
        self.feedings = 0
        self.drinks = 0
        self.eats = 0
    def eat(self, food = "vegetables"):
        print("Num Num Num Nom Num")
        self.weight_oz += 11
        self.feedings += 1
        self.eats += 1
        if food == "vegetables":
            print("Baby eats vegetables")
            baby.cry()
        elif food == "cereal":
            print("Baby eats cereal")
            baby.sleep()
        else:
            print("Baby eats", food)
            baby.laugh()
    def drink(self):
        print("gulp, gulp, gulp, burp, gulp")
        self.weight_oz += 8
        self.drinks += 1
        self.feedings += 1
        self.mood = "content"
    def poop(self):
        print("Baby Poops")
        self.weight_oz -= 5
    def pee(self):
        print("Baby Pees")
        self.weight_oz -= 4
    def laugh(self):
        print("Baby laughs")
        self.mood = "happy"
    def cry(self):
        print("Wahhh wah wah bahahahahah wahhhawah")
        self.mood = "sad"
    def sleep(self):
        print("ZZZZZZZZZZZZZZZZZZZzzzzzzzzzz")
        self.mood = "content"
    def scream(self):
        print("Ahhhhhhhhhhhhhhhhhhhhhh")
    def display_status(self):
        print("Baby Name:", self.name)
        print("Birthdate:", self.birthdate)
        print("Current Weight in oz:", self.weight_oz)
        print("Current Weight in decimal pounds:", self.weight_oz / OUNCES_PER_POUND, "lbs")
        print("Height:", self.height_in, "in")
        print("Mood:", self.mood)
        print("Feedings:", self.feedings)
        print("Eats:", self.eats)
        print("Drinks:", self.drinks)

baby_name = input("What is the baby's name?: ")
birthdate = input("What is the baby's birthdate?: ")
ounces = int(input("What is the baby's weight in ounces?: "))
height = float(input("What is the baby's height in inches?: "))

starting_weight_oz = ounces

baby = Baby(baby_name, birthdate, ounces, height)
baby2 = Baby("John", "3/19/2017", 40, 32)


print()
print("--- BABY STATUS ---")
baby.display_status()
print()
baby2.display_status()
print()


action = ""
poop_count = 0
pee_count = 0
burp_count = 0

while action != "home":
    action = input("What action would you like your baby to do (eat, drink, sleep, cry, laugh, scream, status, home)?: ").lower()
    if action == "eat":
        food = input("What would you like your baby to eat (vegetables, cereal, or other)?: ").lower()
        baby.eat(food)
        poop_count += 1
        burp_count += 1
        
        if(poop_count % 3 == 0):
            baby.poop()
            
        if(burp_count % 3 ==0):
            print("*Baby burps*")
            baby.mood = "happy"
        print()

    elif action == "drink":
        baby.drink()
        pee_count += 1
        burp_count += 1

        if(pee_count % 3 == 0):
            baby.pee()
            
        if(burp_count % 3 ==0):
            print("*Baby burps*")
            baby.mood = "happy"
        print()

    elif action == "sleep":
        baby.sleep()

    elif action == "cry":
        baby.cry()

    elif action == "status":
        print()
        baby.display_status()
        print()

    elif action == "laugh":
        baby.laugh()
        print()

    elif action == "home":
        print("Going Home")
        print()

    elif action == "scream":
        baby.scream()
        print()

    else:
        print("Unknown action — try again.")
        print()


    if (baby.weight_oz >= starting_weight_oz * 2):
        print("Baby has become too fat to be considered a baby anymore! Congratulations! Welcome to having a toddler!")
        print()
        break


print("-- Final Baby Status Report --")
baby.display_status()