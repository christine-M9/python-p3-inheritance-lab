#!/usr/bin/env python

# teacher.py
import random
from user import User

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge  # Initializing knowledge with predefined values

    def teach(self):
        if self.knowledge:
            return random.choice(self.knowledge)
        else:
            return "I have no knowledge to teach"
