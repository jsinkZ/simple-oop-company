class Person:
    def __init__(self, name, age, experience, working_now):
        self.name = name
        self.age = age
        self.experience = experience  # exp in years
        self.working_now = working_now  # string company name or ''

    def say_hi(self):
        where_work = ""
        if self.working_now == "":
            where_work = "I dont work!"
        else:
            where_work = "I work in " + self.working_now
        print("Hi! Im ", self.name, self.age, "yo, my experience.", where_work)


class Worker(Person):
    def __init__(self, name, age, experience, working_now, position):
        super().__init__(name, age, experience, working_now)
        self.position = position

    def say_hi(self):
        super().say_hi()
        print("My position ", self.position)

class Company:
    def __init__(self, name, description, max_staff, salary, work_group):
        self.name = name  # company name
        self.description = description  # company description
        self.max_staff = max_staff  # max count of staff
        self.salary = salary  # salary for [junior, middle, senior]
        self.work_group = work_group

    def contest(self, applicants, count_places):
        people = sorted(applicants, key=lambda applicant: applicant.experience, reverse=True)
        while len(people) and count_places > 0:
            self.work_group.append(people[0])
            count_places -= 1
            del people[0]

    def current_group(self):
        print("Current workers group:", *[i.name for i in self.work_group])

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

    def employ(self, person):
        self.work_group.append(person)
        self.current_group()

    def fire(self, person):
        group = self.work_group
        for i in range(len(group)):
            if group[i] == person:
                del group[i]
                break
        self.work_group = group
        self.current_group()


# * companies
some_ceo = Company("Some comp", "...", 30, [10, 20, 30], [])

# * people
jacob = Person('Jacob', 20, 0, "")
ben = Person("Ben", 24, 1, "")
john = Person("John", 27, 3, "")
wilson = Person("Wilson", 39, 17, "")
jack = Worker("Jack", 29, 7, some_ceo.name, "middle")
    
# john.say_hi()
# jack.say_hi()

# some_ceo.employ(jack.name)
# some_ceo.employ(john.name)
# some_ceo.employ(ben.name)
# some_ceo.fire(john.name)

some_ceo.contest([jack, john, ben, wilson, jacob], 3)
some_ceo.current_group()