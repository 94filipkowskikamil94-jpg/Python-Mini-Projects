
import json

with open("questions.json", "r", encoding="utf-8") as file:
    questions_list = json.load(file)

score = 0

for question_item in questions_list:
    print("Question:", question_item['question'])

    answer_number = 1
    for answer_item in question_item["answers"]:

        print(str(answer_number) + ".", answer_item["text"])
        answer_number += 1

    user_choice = int(input("your answer(1-3): "))

    corrert_answer = question_item["answers"][user_choice - 1]

    if corrert_answer["is_correct"]:
            print("Correct Siusiaku!")
            score += 1

    else:
            print("You sucked")
print("\nQuiz finished! Your score:", score, "/", len(questions_list))