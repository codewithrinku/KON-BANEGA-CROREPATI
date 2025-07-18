import random
print("\t\t\t\tThis is a game")
print("\t\t\t     KON BANEGA CROREPATI\n\n")

print("If you want to enter this game, please enter some information.")
print("IMPORTANT NOTICE:")
print("You can play this game only if your age is 18 or above.\n")

name = input("Enter your name: ").capitalize()
age = int(input("Enter your Age: "))

if age >= 18:  # If user 18 ka hai to
    print(f"\nCongratulations {name}, you can play the game.")
    
    print("Do you want to play this game?")
    print("a. Yes\t\tb. No")
    response = input("What is your response a or b: ")
    response = response.lower()
    questions = {"Who was the first Prime Minister of India? (a) Jawaharlal Nehru (b) Indira Gandhi (c) Mahatma Gandhi (d) Sardar Vallabhbhai Patel)": "a",
                 " Which empire was known for its vast network of roads called the Silk Road? (a) Roman Empire (b) Mongol Empire (c) Han Dynasty (d) Ottoman Empire":"c",
                 "When did World War II end? (a) 1943 (b) 1945 (c) 1947 (d) 1950 ": "b",
                 "Who painted the Mona Lisa? (a) Vincent van Gogh (b) Leonardo da Vinci (c) Pablo Picasso (d) Michelan":"b",
                 "What historical event is commemorated on Bastille Day? (a) The French Revolution (b) The American Revolution (c) The Russian Revolution (d) The English Civil War ":"a",
                 "Who was the leader of the Indian independence movement against British rule? (a) Subhas Chandra Bose (b) Jawaharlal Nehru (c) Mahatma Gandhi (d) Bhagat Singh ":"c",
                 "What major event in 1989 signified the end of the Cold War? (a) The Vietnam War (b) The fall of the Berlin Wall (c) The Korean War (d) The Cuban Missile Crisis " :"b"}
    level = [100000,700000,3100000,5100000]
    print(level)
    rand = random.choice(list(questions.keys()))
    answer = questions[rand].lower()
    if response == "a":
        print("\nOkay! Let's start the game \n")
        
        total_profit = 0
        print(rand)
        answer1 = input("Enter your answer : ").lower()

        if answer == answer1:
            total_profit = 100000
            print(f"Congratulations {name}! You won {total_profit} 🏆")

            continue_game = input("Do you want to play the next question? (yes/no): ")
            continue_game = continue_game.lower()
            if continue_game == "yes":
                rand = random.choice(list(questions.keys()))
                answer = questions[rand].lower()
                print(rand)
                answer1 = input("Enter your answer : ").lower()
                

                if answer == answer1:
                    total_profit = 700000
                    print(f"🎉 Congratulations {name}! You jeet gaye {total_profit} 🏆")
                    continue_game = input("Do you want to play the next question? (yes/no): ")
                    continue_game = continue_game.lower()
                    if continue_game == "yes":
                        rand = random.choice(list(questions.keys()))
                        answer = questions[rand].lower()
                        print(rand)
                        answer1 = input("Enter your answer : ").lower()
                        

                        if answer == answer1:
                            total_profit = 3100000
                            print(f"🎉 Congratulations {name}! You tum jeet gaye {total_profit} 🏆")
                            continue_game = input("Do you want to play the next question? (yes/no): ")
                            # question 4
                            continue_game = continue_game.lower()
                            if continue_game == "yes":
                                rand = random.choice(list(questions.keys()))
                                answer = questions[rand].lower()
                                print(rand)
                                answer1 = input("Enter your answer : ").lower()
                            

                                if answer == answer1:
                                    total_profit = 5100000
                                    print(f"🎉 Congratulations {name}! You now won {total_profit} 🏆")
                        else:
                            print(f"Wrong answer.this is correct answer {answer}")
                            print(f"Tum ab tak {total_profit} rupe jeet chuke ho ")
                else:
                    print(f"Wrong answer. this is correct answer {answer}")
                    print(f"Tum ab tak {total_profit} rupe jeet chuke ho ")
            else:
                print(f"Okay {name}₹{total_profit}. rupe jeet chuke ho")
        else:
            print(f"sorry sir Wrong answer, this is correct answer {answer}")
            print("aap ab tak 0 rupe jeet chuke ho")

    elif response == "b":
        print(f"No problem {name}")
    else:
        print("Invalid input. Please restart kro.")

else:
    print(f"Sorry {name}, you are not 18+ so game is not start ")
