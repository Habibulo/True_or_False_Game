# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.foydalanuvchi = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers +=1
#         self.following +=1
#
# user_1 = User("001", "khabibullo")
# user_2 = User("002", "Ali")
# # print(user_2.followers)
# user_1.follow(user_2)
#
# print(user_2.followers)
# class Car:
#     def enter_race_mode():
#         self.seats = 2
# my_car = Car()
# print(my_car.enter_race_mode)


# #
# class Talaba:
#     def __init__(self, ism, familya, t_yil):
#         self.ism = ism
#         self.familya = familya
#         self.t_yil = t_yil
#     def get_name(self):
#         return self.ism
#     def get_age(self, yil):
#         return yil - self.t_yil
#     def intro(self):
#         return f"{self.ism} {self.familya} tugilgan yilim {self.t_yil}"
# talaba1 = Talaba('Khabibullo', 'Khalmjonov', 1997)
# print(talaba1.ism)
# print(talaba1.familya)
# print(talaba1.t_yil)
# talaba1.intro()
# print(talaba1.get_age(2023))
#
#

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

"""for question in question_bank:
    print(question)"""

quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()
print(f"you have completed the quiz\nYour final score was {quiz.score}/{len(question_bank)}")