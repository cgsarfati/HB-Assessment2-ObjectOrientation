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


class Exam(object):

    def __init__(self, name, questions=[]):
        self.name = name.lower()
        self.questions = questions
