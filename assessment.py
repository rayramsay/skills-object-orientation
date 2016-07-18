"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   * Encapsulation:
        Data and its behaviors "live" close together, so it's easy to see what
        data can do/how it can be acted upon.

    * Abstraction:
        Details can be "hidden" from the user. For example, when we were using
        that graphics program, we knew which methods we could use with various
        shapes, like .setBackgroundColor(), but we didn't--and didn't need to--
        know how those methods worked under the hood.

    * Polymorphism:
        Interchangeability of components. Classes that call the same methods
        should pass the same number of arguments. 

2. What is a class?

    Classes are a way of storing data and its behaviors. The data structures
    we've encountered previously, like lists, tuples, etc., are specific types
    of classes; that's why they have their own methods.

3. What is an instance attribute?

    An instance attribute is an attribute that is specific to a particular
    instance, rather than shared with all instances of that class.

4. What is a method?

    A method is a function that is defined in the class or inherited from parent
    classes. These methods are called with dot notation, e.g., fido.speak().

5. What is an instance in object orientation?

    An instance is a specific, individual occurrence of a class. For example,
    fido is an instance of the class Dog.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is shared among all instances of that class. For example,
   the class Dog can have color = 'brown' as a class attribute, so that dog
   instances don't need to have their color specified within them, as they can
   look up their class attribute. But if I want to make a particular
   dog black, I can give it an instance attribute of fido.color = 'black'.
   Instances look at themselves first, and if they don't have an instance
   attribute, they look up at their class to see if it's stored there.

"""


# Part 2: Classes and Init Methods
# Part 3: Methods

class Student(object):

    def __init__(self, first_name, last_name, address):
        """Initializes new student."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):
        """Initializes new question."""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Asks user the question and compares their response to the correct
        answer; returns a boolean."""

        answer = raw_input("{} > ".format(self.question))
        return answer.lower() == self.correct_answer.lower()
        # User's answer doesn't have to match the capitalization of correct
        # answer in order to be marked correct.


class Exam(object):

    def __init__(self, name):
        """Initializes new exam with blank list of questions."""

        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Adds new question to the list of questions."""

        self.questions.append(Question(question, correct_answer))

    def administer(self):
        """Loops over exam's questions, returns score."""

        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():  # if that returns True then
                score += 1
        return score


# Part 4: Create an actual exam!

def take_test(exam, student):
    """Given an exam and a student, administers exam and records student's
    score."""

    student.score = exam.administer()


def example():
    """Creates an exam, adds a few questions to it, creates a student,
    administers the test for that student."""

    exam = Exam("exam")

    exam.add_question("Who received the first IBM PC delivered in New York "
                      "City?", "Edie Windsor")

    exam.add_question("Who headed the team that wrote the software for the "
                      "Apollo Guidance Computer?", "Margaret Hamilton")

    student = Student("Nicey", "Goodcoder", "123 Computer St")

    student.score = exam.administer()

    if student.score == len(exam.questions):
        print "Great job! Your score is {}.".format(student.score)
    else:
        print "Your score is {}.".format(student.score)


# Part 5: Inheritance

class Quiz(Exam):
    """It's like an exam, only pass/fail."""

    def administer(self):
        score = super(Quiz, self).administer()
        return score / float(len(self.questions)) >= 0.5
        # If you answer at least half of the questions correctly, you pass the
        # quiz. Length (i.e., number) of questions converted to a float due to
        # Python 2's counterintuitive implementation of the '/' operator.
