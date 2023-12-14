#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    pass
    def __init__(self, name="None", job=""):
        self._name = name
        self._job = job

        if not name:
            print("Name must be string between 1 and 25 characters.")
        elif not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
        elif not 1 <= len(name) <= 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name.title()
        if job and job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self._job = None
        else:
            self._job = job
        

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value.title()

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, value):
        if value != "" and value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value





    job = property(get_job, set_job)
