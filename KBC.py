# Simple KBC Game
questions = [
    ["What is the capital of India?", "a. Mumbai", "b. Delhi", "c. Kolkata", "d. Chennai", "b"],
    ["Which planet is known as the Red Planet?", "a. Mars", "b. Venus", "c. Earth", "d. Jupiter", "a"],
    ["Who wrote the Indian National Anthem?", "a. Tagore", "b. Nehru", "c. Gandhi", "d. Tilak", "a"],
    ["which is the best car in the world?", "a. Lamborghini", "b. BMW", "c.Mercedes", "d.Ferrari", "b"],
    ["Who is the current prime minister of india?", "a. Kalam", "b. Rajendra Prasad", "c. Radhakrishnan", "d. Modi", "d"]
]

score = 0
prizes = [1000, 5000, 10000, 50000, 100000]



for i in range(len(questions)):
    q = questions[i]
    print(f"Q{i+1}: {q[0]}")
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])
    answer = input("Your answer (a/b/c/d): ")
    
    if answer.lower() == q[5]:
        print(f"✅ Correct! You won ₹{prizes[i]}\n")
        score += prizes[i]
    else:
        print("❎ Wrong answer!")
        print(f"The correct answer was: {q[5]}")
        break

print(f"Your total winnings: ₹{score}")
print("Thank you for playing!")

