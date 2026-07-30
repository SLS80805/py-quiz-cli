questions = [
    {
        "question": "Which programming language is known for snake logo?",
        "options": ["1. Java", "2. C++", "3. Python", "4. HTML"],
        "answer": 3
    },
    {
        "question": "What does CPU stand for?",
        "options": ["1. Central Processing Unit", "2. Computer Personal Unit", "3. Central Performance Utility", "4. Control Program Unit"],
        "answer": 1
    },
    {
        "question": "Which data structure follows First-In, First-Out (FIFO)?",
        "options": ["1. Stack", "2. Queue", "3. Array", "4. Tree"],
        "answer": 2
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["1. func", "2. function", "3. def", "4. define"],
        "answer": 3
    }
]

score = 0
print("=== WELCOME TO THE QUIZ APP ===\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}: {q['question']}")
    for opt in q["options"]:
        print(f"  {opt}")
    
    while True:
        ans = input("Your answer (1-4): ")
        if ans in ["1", "2", "3", "4"]:
            break
        print("Invalid! Enter 1, 2, 3, or 4.")
    
    if int(ans) == q["answer"]:
        print("✓ Correct!\n")
        score += 1
    else:
        print(f"✗ Wrong! Correct answer: {q['options'][q['answer'] - 1]}\n")

total = len(questions)
pct = (score / total) * 100
print("=== QUIZ FINISHED ===")
print(f"Score: {score}/{total} ({pct:.0f}%)")