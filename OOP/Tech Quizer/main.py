from question_model import  Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q["question"], q["correct_answer"]))

new_q = QuizBrain(question_bank)

while new_q.still_has_questions():
    new_q.new_question()

