from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import ui

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

ui = ui.Interface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
