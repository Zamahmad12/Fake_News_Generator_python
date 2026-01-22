import random

# -------- SPORTS DATA --------
sports_subjects = ["Cricketer", "Footballer", "Team India", "Coach", "Barcelona"]
sports_actions = ["wins", "loses", "breaks", "sets", "joins"]
sports_objects = ["World Cup", "IPL match", "record", "final match", "trophy"]
sports_places = ["in India", "in England", "in Australia", "in Dubai"]

# -------- TECHNOLOGY DATA --------
tech_subjects = ["Google", "Apple", "Microsoft", "Tesla", "Startup"]
tech_actions = ["launches", "tests", "bans", "upgrades", "develops"]
tech_objects = ["AI robot", "new smartphone", "electric car", "app", "website"]
tech_places = ["in India", "in USA", "in China", "in Japan"]

# -------- FUNCTIONS --------
def sports_news():
    subject = random.choice(sports_subjects)
    action = random.choice(sports_actions)
    obj = random.choice(sports_objects)
    place = random.choice(sports_places)
    return subject + " " + action + " " + obj + " " + place

def tech_news():
    subject = random.choice(tech_subjects)
    action = random.choice(tech_actions)
    obj = random.choice(tech_objects)
    place = random.choice(tech_places)
    return subject + " " + action + " " + obj + " " + place

def create_news():
    print("\nCreate Your Own Fake News")
    subject = input("Enter subject: ")
    action = input("Enter action: ")
    obj = input("Enter object: ")
    place = input("Enter place: ")

    return subject + " " + action + " " + obj + " " + place

# -------- MAIN PROGRAM --------
while True:
    print("\n--- Fake News Generator ---")
    print("1. Sports News")
    print("2. Technology News")
    print("3. Create Your Own Fake News")
    print("4. Generate Multiple Headlines")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        headline = sports_news()
        print("\nSports News:", headline)

    elif choice == "2":
        headline = tech_news()
        print("\nTechnology News:", headline)

    elif choice == "3":
        headline = create_news()
        print("\nYour Fake News:", headline)

    elif choice == "4":
        number = int(input("How many headlines? "))
        category = input("sports / tech / random: ")

        print()
        for i in range(number):
            if category == "sports":
                news = sports_news()
            elif category == "tech":
                news = tech_news()
            else:
                if random.choice([1, 2]) == 1:
                    news = sports_news()
                else:
                    news = tech_news()

            print(str(i+1) + ".", news)

    elif choice == "5":
        print("\nThanks for using Fake News Generator!")
        break

    else:
        print("\nInvalid choice!")
