import io

class Person:
    APPROVED_JOBS = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management", "Research & Development",
        "Marketing", "Purchasing"
    ]

    def __init__(self, name="", job=""):
        self._name = None
        self._job = None
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string under 25 characters.")
        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in self.APPROVED_JOBS:
            print("Job must be in the list of approved jobs.")
        else:
            self._job = value


captured_out = io.StringIO()


captured_out = io.StringIO()  
person1 = Person(name="", job="Sales")
print(captured_out.getvalue().strip())
assert captured_out.getvalue().strip() == "Name must be a string under 25 characters."



captured_out = io.StringIO()  
person2 = Person(name=123, job='Sales')
print(captured_out.getvalue().strip())
assert captured_out.getvalue().strip() == "Name must be a string under 25 characters."


captured_out = io.StringIO()  
person3 = Person(name="What do Persons do on their day off? Can't lie around - that's their job.", job='Sales')
print(captured_out.getvalue().strip())
assert captured_out.getvalue().strip() == "Name must be a string under 25 characters."


captured_out = io.StringIO()  
person4 = Person(name="John Doe", job='Sales')


captured_out = io.StringIO()  
person5 = Person(job="Benevolent dictator for life")
print(captured_out.getvalue().strip())
assert captured_out.getvalue().strip() == "Job must be in the list of approved jobs."
