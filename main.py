class Person:
    def __init__(self, name, age, experience, working_now, req_salary):
        self.name = name
        self.age = age
        self.experience = experience  # experience in years
        self.req_salary = req.salary  # requested salary in dollars

    def say_hi(self):
        print(
            "Hi! Im",
            self.name,
            self.age,
            "yo, my experience, I request a salary of",
            self.req_salary,
        )


class Worker(Person):
    def __init__(
        self, name, age, experience, req_salary, working_now, position, current_salary
    ):
        super().__init__(name, age, experience, req_salary)
        self.working_now = working_now.name  # company name
        self.position = position
        self.current_salary = current_salary

    def say_hi(self):
        super().say_hi()
        print(
            "Im work in",
            self.working_now,
            "My position",
            self.position,
            "and current salary",
            self.current_salary,
            "$",
        )


class Company:
    def __init__(self, name, description, max_staff, salary, work_group):
        self.name = name
        self.description = description
        self.max_staff = max_staff  # max count of staff
        self.salary = salary  # staring salary for [junior, middle, senior] in dollars
        self.work_group = work_group  # team workers in this company

    # contest among applicants
    def contest(self, applicants, count_places):
        people = sorted(
            applicants, key=lambda applicant: applicant.experience, reverse=True
        )
        while len(people) and count_places > 0:
            self.work_group.append(people[0])
            count_places -= 1
            del people[0]

    # print current work group
    def current_group(self):
        print("Current workers group:", *[i.name for i in self.work_group])

    # print all information about company
    def about_company(self):
        print("Company name: ", self.name)
        print("Company description: ", self.description)
        print("Company max count staff : ", self.max_staff)
        print(
            "Company salary for \n\tjunior: ",
            self.salary[0],
            "\n\tmiddle: ",
            self.salary[1],
            "\n\tsenior: ",
            self.salary[2],
        )

    # employ without contest in company
    def employ(self, person):
        self.work_group.append(person)
        self.current_group()

    # fire person
    def fire(self, person):
        group = self.work_group
        for i in range(len(group)):
            if group[i] == person:
                del group[i]
                break
        self.work_group = group
        self.current_group()


"""
class Person  - default person -> (name, age, experience, req_salary)
class Worker  - currently working person in some company -> (name, age, experience, req_salary, working_now, position, current_salary)
class Company - company -> (name, description, max_staff, salary, work_group)
"""

# * companies
some_ceo = Company("Some comp", "...", 30, [1000, 3000, 4500], [])

# * people
dan = Person("Dan", 25, 0, 1200)
jacob = Person("Jacob", 20, 0, 700)
ben = Person("Ben", 24, 1, 950)
john = Person("John", 27, 3, 1200)
wilson = Person("Wilson", 39, 17, 6600)

# * workers
jack = Worker("Jack", 29, 7, 3200, some_ceo, "middle", 3700)
alex = Worker("Alex", 32, 10, 5000, some_ceo, "senior", 6000)

# * testing

# john.say_hi()
# jack.say_hi()

# some_ceo.employ(jack.name)
# some_ceo.employ(john.name)
# some_ceo.employ(ben.name)
# some_ceo.fire(john.name)

some_ceo.contest([jack, john, ben, wilson, jacob], 3)
some_ceo.current_group()
