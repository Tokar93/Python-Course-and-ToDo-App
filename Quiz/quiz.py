import json

with open('questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)
a = 0
solutions = []
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question['alternatives']):
        print(index+1, '-', alternative)
    user_choice = int(input('Enter your answer: '))
    question['user_choice'] = user_choice
    if question['correct_answer'] == question['user_choice']:
        a =+ 1
    else:
        a = a
print(f'Your score is {a}/{len(data)} points')
