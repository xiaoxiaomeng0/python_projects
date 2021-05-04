class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        print(self.question_list[self.question_number]["text"])
        self.question_number += 1
        answer = input("What is the answer? Type 'true' or 'false': ")
        self.check_answer(answer, self.question_list[self.question_number]["answer"])

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong.")
        print(f"The current score is {self.score}/{self.question_number}")






