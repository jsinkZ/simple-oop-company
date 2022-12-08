class Person:
    def __init__(self, name, age, experience, req_salary, looking_position):
        self.name = name
        self.age = age
        self.experience = experience  # experience in years
        self.req_salary = req_salary  # requested salary in dollars
        self.looking_position = (
            looking_position  # looking for this position in next company
        )

    def say_hi(self):
        print(
            "Hi! Im",
            self.name,
            self.age,
            "yo, my experience",
            self.experience,
            "years, I request a salary of",
            self.req_salary,
            "$. Im looking for",
            self.looking_position,
            "position in next company",
        )


class Worker(Person):
    def __init__(
        self,
        name,
        age,
        experience,
        req_salary,
        looking_position,
        working_now,
        position,
        current_salary,
    ):
        super().__init__(name, age, experience, req_salary, looking_position)
        self.working_now = working_now.name  # company name
        self.position = position
        self.current_salary = current_salary

    def say_hi(self):
        super().say_hi()
        print(
            "Im work in",
            self.working_now,
            "my position",
            self.position,
            "and current salary",
            self.current_salary,
            "$",
        )


class Company:
    def __init__(
        self, name, description, max_staff, salary, work_group, ratio_over_salary
    ):
        self.name = name
        self.description = description
        self.max_staff = max_staff  # max count of staff
        self.salary = salary  # staring salary for [junior, middle, senior] in dollars
        self.work_group = work_group  # team workers in this company
        self.ratio_over_salary = (
            ratio_over_salary  # the coefficient of overpayment of salary
        )

    # contest among applicants
    def contest(self, applicants, count_places):
        # if applicants require salary more than min of his position * 0.3 * max coefficient of overpayment of salary he will skipped

        people = sorted(
            applicants, key=lambda applicant: applicant.experience, reverse=True
        )

        while len(people) and count_places > 0:
            applicant_position_index = 0

            # get applicant position index
            for position_index in range(len(self.salary)):
                if people[0].looking_position == "junior":
                    applicant_position_index = position_index
                if people[0].looking_position == "middle":
                    applicant_position_index = position_index
                if people[0].looking_position == "senior":
                    applicant_position_index = position_index

            if (
                people[0].req_salary
                <= self.salary[applicant_position_index] * 0.3 * self.ratio_over_salary
            ):
                self.work_group.append(people[0])
                count_places -= 1

            del people[0]

    # print current work group
    def current_group(self):
        print("Current workers group:", *[i.name for i in self.work_group])

    # print all information about company
    def about_company(self):
        print("Company name:", self.name)
        print("Company description:", self.description)
        print("Company max count staff: ", self.max_staff)
        print(
            "Company salary for \n\tjunior:",
            self.salary[0],
            "\n\tmiddle:",
            self.salary[1],
            "\n\tsenior:",
            self.salary[2],
        )

    # employ without contest in company
    def employ(self, person):
        self.work_group.append(person)

    # fire person
    def fire(self, person):
        group = self.work_group
        for i in range(len(group)):
            if group[i] == person:
                del group[i]
                break
        self.work_group = group


"""
class Person  - default person -> (name, age, experience, req_salary)
class Worker  - currently working person in some company -> (name, age, experience, req_salary, working_now, position, current_salary)
class Company - company -> (name, description, max_staff, salary, work_group)
"""

# * companies
VVS_company = Company(
    "VVS company", "Best solve for your business", 30, [1000, 3000, 4500], [], 1.45
)
Diamonds_crime_company = Company(
    "Diamonds crime", "Design UI", 12, [800, 2200, 3700], [], 1.25
)

# * people
dan = Person("Dan", 25, 0, 1200, "junior")
jacob = Person("Jacob", 20, 0, 700, "junior")
ben = Person("Ben", 24, 3, 950, "middle")
john = Person("John", 27, 5, 1200, "senior")
wilson = Person("Wilson", 39, 17, 6600, "senior")

# * workers
bruce = Worker("Bruce", 23, 3, 1800, "middle", Diamonds_crime_company, "junior", 1200)
jack = Worker("Jack", 29, 7, 3900, "senior", Diamonds_crime_company, "middle", 3700)
alex = Worker("Alex", 32, 10, 6400, "senior", Diamonds_crime_company, "senior", 6000)

# * testing

# john.say_hi()
# jack.say_hi()
# wilson.say_hi()
# alex.say_hi()

# VVS_company.about_company()
# Diamonds_crime_company.about_company()

Diamonds_crime_company.employ(bruce)
Diamonds_crime_company.employ(jack)
Diamonds_crime_company.employ(alex)

Diamonds_crime_company.current_group()

VVS_company.current_group()
VVS_company.contest([dan, jacob, ben, john, wilson, bruce, jack, alex], 5)
VVS_company.current_group()
