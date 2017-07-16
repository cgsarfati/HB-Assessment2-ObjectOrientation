"""
Parts 1-4
Create your classes and class methods here according to the practice instructions.
As you are working on Parts 1, 2, and 4, you can run the test python file
corresponding to that section to verify that you are completing the problem
correctly.
ex: python part_1_tests.py.
"""


class Student(object):
    """ Creates a student. """

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """ Creates a question and answer. """

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """ """

        user_answer = raw_input(self.question + " ")

        return user_answer == self.correct_answer


class Exam(object):
    """ Creates an exam. """

    def __init__(self, name):
        self.name = name.lower()
        self.questions = []
        self.score = None

    def add_question(self, question_set):
        """ """

        self.questions.append(question_set)

    def administer(self):
        """ """

        correct_answers_tally = 0

        for question in self.questions:
            if Question.ask_and_evaluate(question):
                correct_answers_tally += 1

        return float(correct_answers_tally) / len(self.questions)


class StudentExam(object):
    """ """

    def __init__(self, student, exam):
        """ """
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        """ """
        self.score = Exam.administer()
        print self.score


def example():
    """ """

    current_exam = Exam("Midterm")

    set_A = Question("Is Balloonicorn a support staff?", "Yes")
    set_B = Question("What color is Balloonicorn?", "Pink")
    set_C = Question("What floor does Balloonicorn live?", "2nd")

    current_exam.add_question(set_A)
    current_exam.add_question(set_B)
    current_exam.add_question(set_C)

    current_student = Student("Charlotte", "Sarfati", "1200 4th st")

    current_student_exam = StudentExam(current_student, current_exam)
    current_student_exam.take_test()


class Quiz(Exam):
    """ """

    def administer(self):
        """ """

        self.score = super(Quiz, self).administer()

        if self.score >= 0.5:
            return 1
        else:
            return 0


class StudentQuiz(object):
    """ """

    score = 0

    def __init__(self, student, quiz):
        self.student = student
        self.quiz = quiz

    def take_test(self, student, quiz):
        self.score = Quiz.administer()
        print self.score
