class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def new_question(self):
        question = self.question_list[self.question_number]
        self.answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False) ")
        self.validate_answer()
        self.is_correct()

    def validate_answer(self):
        validation = self.answer in ["True", "False"]
        while not validation:
            print("Please enter a valid answer between True or False")
            self.answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False) ")
            validation = self.answer in ["True", "False"]

    def is_correct(self):
        correct_answer = self.question_list[self.question_number].answer
        if self.answer == correct_answer:
            self.score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! The correct answer was: {correct_answer}")
        self.question_number += 1
        print(f"Your current score is: {self.score}/{self.question_number}\n")
