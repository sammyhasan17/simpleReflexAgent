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
#  if they are attractive they can be placed into the club
while bool(queue):
    SimpleReflexAgent(queue.__getitem__(0))
    queue.pop(0)

