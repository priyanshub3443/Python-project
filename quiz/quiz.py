question = [
    "What is your name?",
    "What is the capital of India?",
    "What is the capital of Uttar Pradesh?",
    "What is the capital of Uttarakhand?"
]

answer = [
    "Priyanshu",
    "Delhi",
    "Lucknow",
    "Dehradun"
]

score = 0

for i in range(len(question)):
    print(question[i])
    userAnswer = input("Answer: ")

    if userAnswer.strip().lower() == answer[i].strip().lower():
        print("Correct")
        score += 1
    else:
        print("Incorrect")

print(f"Score: {score}")
