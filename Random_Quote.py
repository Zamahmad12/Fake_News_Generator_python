import random

# -------- MOTIVATIONAL QUOTES --------
motivational_quotes = [
    "Believe in yourself.",
    "Hard work always pays off.",
    "Never give up.",
    "Dream big and work hard.",
    "Success comes to those who try.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dont stop when you are tired. Stop when you are done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Little things make big days.",
    "It is going to be hard, but hard does not mean impossible.",
    "Your only limit is your mind.",
    "Stay focused and never quit.",
    "Do something today that your future self will thank you for.",
    "Believe you can and you are halfway there.",
    "Doubt kills more dreams than failure ever will.",
    "Success doesnot come to you. You go to it.",
    "The harder you work for something, the greater you will feel when you achieve it."
]

# -------- FUNNY QUOTES --------
funny_quotes = [
    "I am on a seafood diet. I see food and I eat it.",
    "Why dont scientists trust atoms? Because they make up everything.",
    "I am not lazy, I am on energy saving mode.",
    "My bed is a magical place where I suddenly remember everything I forgot.",
    "I put my phone on airplane mode, but it is not flying.",
    "I am not superstitious, but I am a little stitious.",
    "Why dont eggs tell jokes? They had crack each other up.",
    "I told my computer I needed a break, and it said: No problem  I Will go to sleep.",
    "I started with nothing, and I still have most of it.",
    "Why did the math book look sad? Because it had too many problems.",
    "I used to think I was indecisive, but now I am not too sure.",
    "I asked my dog whats two minus two. He said nothing.",
    "Why dont skeletons fight each other? They dont have the guts.",
    "I am so good at sleeping, I can do it with my eyes closed.",
    "I tried to be normal once. Worst two minutes of my life.",
    "Why dont programmers like nature? It has too many bugs.",
    "I put my phone on silent, but my mind is still loud."
]

# -------- LOVE QUOTES --------
love_quotes = [
    "Love is not about how much you say, but how much you prove.",
    "You are my today and all of my tomorrows.",
    "Love is when the other persons happiness matters more than yours.",
    "I fell in love the way you fall asleep: slowly, then all at once.",
    "Every love story is beautiful, but ours is my favorite.",
    "You are my sunshine on a cloudy day.",
    "I still fall for you every single day.",
    "Love is composed of a single soul inhabiting two bodies.",
    "You are the reason I smile a little more.",
    "I love you more than yesterday but less than tomorrow.",
    "Where there is love, there is life.",
    "You had me at hello.",
    "I love you not only for what you are, but for what I am when I am with you.",
    "You make my heart smile.",
    "I found my home in your heart.",
    "To love and be loved is to feel the sun from both sides.",
    "I choose you. And I will choose you over and over."
]

custom_quotes = []

# -------- FUNCTIONS --------
def show_menu():
    print("\n--- Random Quote Generator ---")
    print("1. Motivational Quotes")
    print("2. Funny Quotes")
    print("3. Love Quotes")
    print("4. Create Your Own Quote")
    print("5. Exit")

def get_random_quote(quotes_list):
    return random.choice(quotes_list)

# -------- MAIN PROGRAM --------
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        quote = get_random_quote(motivational_quotes)
        print("\nMotivational Quote:")
        print(quote)

    elif choice == "2":
        quote = get_random_quote(funny_quotes)
        print("\nFunny Quote:")
        print(quote)

    elif choice == "3":
        quote = get_random_quote(love_quotes)
        print("\nLove Quote:")
        print(quote)

    elif choice == "4":
        user_quote = input("\nEnter your own quote: ")
        custom_quotes.append(user_quote)
        print("Your quote has been added!")

    elif choice == "5":
        print("\nThanks for using Random Quote Generator! 👋")
        break

    else:
        print("\nInvalid choice. Please try again.")

    if len(custom_quotes) > 0:
        show_custom = input("\nDo you want to see a custom quote? (yes/no): ")
        if show_custom == "yes":
            quote = get_random_quote(custom_quotes)
            print("\nYour Custom Quote:")
            print(quote)
