# Course: CS3642
# Student name: Sammy Hasan-Silva
# Student ID: 000917482
# Assignment #: 1
# Due Date: Sept 16th 2022
# Signature:Sammy Hasan-Silva
# Score:


# blueprint of the People
class Person:
    def __init__(self, attractive):
        self.attractive = attractive


# blueprint of our agent
class SimpleReflexAgent(Person):  # TODO agent needs to scan Person objects
    def __init__(self, person):

        if person.attractive:
            print("allowed")
        else:
            print("not allowed")


# CREATE objects
p1 = Person(attractive=False)
p2 = Person(attractive=True)
p3 = Person(attractive=True)
# CREATE our queue
queue = [p1, p2, p3]


# have our agent scan each person in the queue and take action based on conditions

# agent1 = SimpleReflexAgent(queue.__getitem__(0))
# queue.pop(0)
# agent1 = SimpleReflexAgent(queue.__getitem__(0))
# queue.pop(0)
# agent1 = SimpleReflexAgent(queue.__getitem__(0))
# queue.pop(0)

# loop
# todo:
#  if they are attractive they can be placed into the club
while bool(queue):
    SimpleReflexAgent(queue.__getitem__(0))
    queue.pop(0)

