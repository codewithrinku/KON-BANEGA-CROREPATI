import random
print("\t\t\t\tThis is a game")
print("\t\t\t     KON BANEGA CROREPATI\n\n")

print("If you want to enter this game, please enter some information.")
print("IMPORTANT NOTICE:")
print("You can play this game only if your age is 18 or above.\n")

name = input("Enter your name: ").capitalize()
age = int(input("Enter your Age: "))

if age >= 18:
    print(f"\nCongratulations {name}, you can play the game.")
    
    print("Do you want to play this game?")
    print("a. Yes\t\tb. No")
    response = input("What is your response a or b: ").lower()

    questions = {
        "Who was the first Prime Minister of India? (a) Jawaharlal Nehru (b) Indira Gandhi (c) Mahatma Gandhi (d) Sardar Vallabhbhai Patel)": "a",
        "Which empire was known for its vast network of roads called the Silk Road? (a) Roman Empire (b) Mongol Empire (c) Han Dynasty (d) Ottoman Empire": "c",
        "When did World War II end? (a) 1943 (b) 1945 (c) 1947 (d) 1950 ": "b",
        "Who painted the Mona Lisa? (a) Vincent van Gogh (b) Leonardo da Vinci (c) Pablo Picasso (d) Michelan": "b",
        "What historical event is commemorated on Bastille Day? (a) The French Revolution (b) The American Revolution (c) The Russian Revolution (d) The English Civil War ": "a",
        "Who was the leader of the Indian independence movement against British rule? (a) Subhas Chandra Bose (b) Jawaharlal Nehru (c) Mahatma Gandhi (d) Bhagat Singh ": "c",
        "What major event in 1989 signified the end of the Cold War? (a) The Vietnam War (b) The fall of the Berlin Wall (c) The Korean War (d) The Cuban Missile Crisis ": "b"
    }

    level = [100000, 700000, 3100000, 5100000, 10000000]  # Last is 1 crore
    total_profit = 0

    if response == "a":
        print("\nOkay! Let's start the game \n")

        for i in range(len(level)):
            rand = random.choice(list(questions.keys()))
            answer = questions[rand].lower()
            print(rand)
            user_answer = input("Enter your answer: ").lower()

            if user_answer == answer:
                total_profit = level[i]
                print(f"🎉 Congratulations {name}! You won ₹{total_profit} 🏆")
                if i != len(level) - 1:
                    continue_game = input("Do you want to play the next question? (yes/no): ").lower()
                    if continue_game != "yes":
                        print(f"Okay {name}, you have won ₹{total_profit}. Thank you for playing!")
                        break
                else:
                    print(f"🎊🎊 Superb {name}! You have become a CROREPATI 🪙🪙! Total Winnings: ₹{total_profit}")
            else:
                print(f"Wrong answer! The correct answer was: {answer}")
                print(f"{name}, you won ₹{total_profit} till now. Better luck next time!")
                break

    elif response == "b":
        print(f"No problem {name}, maybe next time!")
    else:
        print("Invalid input. Please restart the game.")

else:
    print(f"Sorry {name}, you are not 18+ so game cannot start.")
