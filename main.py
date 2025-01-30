quiz_questions = [
    "What is the capital of Iran?",
    "What is the capital of Thailand?",
    "What is the capital of Estonia?",
    "Which US state is Memphis located in?",
    "Which US state is Savannah located in?",
    "Which US state is El Paso located in?",
    "Which US state is Baltimore located in?",
    "What is the capital of Finland?",
    "What is the capital of Sweden?",
    "What is the capital of Norway?",
    "What is the capital of Iceland?",
    "Which Canadian province is Halifax located in?",
    "Which Canadian province is Montreal located in?",
    "Which Chinese province is Lhasa located in?",
]
quiz_answers = [
    "tehran", 
    "bangkok",
    "tallinn",
    "tennessee",
    "georgia",
    "texas",
    "maryland",
    "helsinki",
    "stockholm",
    "oslo",
    "reykjavik",
    "nova scotia",
    "quebec",
    "tibet",
]
score = 0
for i in range (14):
    print(quiz_questions[i])
    user_answer = input()
    if user_answer == quiz_answers[i]:
        print("Correct!")
        score += 1
    elif user_answer != quiz_answers[i]:
        print("Incorrect.")
        score += 0
    
