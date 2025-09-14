questions=[
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["What is 2 + 2?", "3", "4", "5", "6", 2],
    ["What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Saturn", 3],
    ["Who wrote 'Hamlet'?", "Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen", 3],
    ["What is the boiling point of water?", "90°C", "100°C", "110°C", "120°C", 2],
    ["Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Silver", "Iron", 2],
    ["What is the currency of Japan?", "Yen", "Dollar", "Euro", "Won", 1],
    ["Who painted the Mona Lisa?", "Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
    ["What is the smallest prime number?", "0", "1", "2", "3", 3],
    ["Which ocean is the largest?", "Atlantic", "Indian", "Arctic", "Pacific", 4],
    ['What is the hardest natural substance on Earth?', 'Gold', 'Iron', 'Diamond', 'Platinum', 3],
    ['Who is known as the "Father of Computers"?', 'Charles Babbage', 'Alan Turing', 'John von Neumann', 'Steve Jobs', 1],
    ['What is the main ingredient in traditional Japanese miso soup?', 'Rice', 'Soybeans', 'Fish', 'Seaweed', 2],
]


for question in questions:
    print(question[0])
    print(question[1], question[2], question[3], question[4], sep="\n")
    user=int(input("Enter your answer (1-4): "))
    if user == question[5]:
        print("Correct!\n")
       
    else:
        print(f"Wrong! The correct answer is option {question[5]}.\n")
        print("Game Over! You lost the game., you can try again.")
        break
    
