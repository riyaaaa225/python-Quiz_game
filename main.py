from question_model import question
from data import question_data
from quiz_brain import quizBrain

Question_bank= []
for q in question_data:
    question_text = q["text"]
    question_answer = q["answer"]
    new_question = question(question_text, question_answer)
    Question_bank.append(new_question)

quiz = quizBrain(Question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
