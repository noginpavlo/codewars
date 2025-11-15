from abc import ABC, abstractmethod


class EmployeeFactory(ABC):
    """Abstract factory for families creation."""

    @abstractmethod
    def create_manager(self): ...

    @abstractmethod
    def create_developer(self): ...


class FullTimeEmployeeFactory(EmployeeFactory):
    """Concrete factroy for Full-time employees creation."""

    def create_manager(self, name, email, salary, team_name) -> Manager:
        salary_strategy = FullTimePayment(salary)
        return Manager(name, email, salary_strategy, team_name)

    def create_developer(self, name, email, salary, programming_language) -> Developer:
        salary_strategy = FullTimePayment(salary)
        return Developer(name, email, salary_strategy, programming_language)


class PartTimeEmployeeFactory(EmployeeFactory):
    """Concrete factroy for Part-time employees creation."""

    def create_manager(self, name, email, hourly_rate, hours_worked, team_name):
        salary_strategy = PartTimePayment(hourly_rate, hours_worked)
        return Manager(name, email, salary_strategy, team_name)

    def create_developer(self, name, email, hourly_rate, hours_worked, programming_language):
        salary_strategy = PartTimePayment(hourly_rate, hours_worked)
        return Developer(name, email, salary_strategy, team_name)


class Payment(ABC):

    @abstractmethod
    def process_payment(self): ...


class FullTimePayment(Payment):

    def __init__(self, salary):
        self.salary = salary

    def process_payment(self, fixed_salary):
        return salary


class PartTimePayment(Payment):

    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def process_payment(self, fixed_salary):
        return self.hours * self.hourly_rate


class Employee:
    """
    This is a base class for regular employees
    (who work full-time on a long term basis and have a fixed salary)
    """

    def __init__(self, email, salary_strategy):
        self.salary_strategy = salary_strategy

    def calculate_payment(self):
        return self.salary_strategy.process_payment()


class Developer(Employee):
    """This is a class for regular developers"""

    def __init__(self, name, email, programming_language):
        super().__init__(name, email, salary_strategy)
        self.programming_language = programming_language
        self.tasks = []  # fifo queue

    def add_task(self, task):
        self.tasks.append(task)
        print(f"{self.name} accepted the task: {task}")

    def process_tasks(self):
        for task in self.tasks:
            print(f"{self.name} is writing code for task: {task}")

        self.tasks.clear()
        print(f"{self.name} completed all tasks")


class Manager(Employee):
    """This is a class to regulrar managers"""

    def __init__(self, name, email, salary, team_name):
        super().__init__(name, email, salary)
        self.team_name = team_name
        self.developers = []
        self.team_tasks = []

    def add_task_to_team(self, task):
        self.team_tasks.append(task)
        print(f"Task: {task} is added to the team {self.team_name}")

    def add_developer_to_team(self, regular_developer):
        self.developers.append(regular_developer)
        print(f"{regular_developer.name} is added to the team {self.team_name}")

    def assign_tasks_to_developers(self):
        print(f"Team {self.team_name} is working on the following tasks: {self.team_tasks}")
        for task, developer in zip(self.team_tasks, self.developers):
            developer.add_task(task)

    def start_sprint(self):
        print(f"Team {self.team_name} is starting a new sprint")
        for developer in self.developers:
            developer.process_tasks()

    def finish_sprint(self):
        print(f"Team {self.team_name} has finished the sprint")
        self.team_tasks.clear()


# TODO: add support for contractor employees (developers and managers) !!!


if __name__ == "__main__":
    # create regular manager
    regular_manager = RegularManagerEmployee("Alice Brown", "alice@brown.com", 2000, "team_name")

    # add tasks to team
    regular_manager.add_task_to_team("Task 1")
    regular_manager.add_task_to_team("Task 2")

    # create regular developers
    regular_developer_1 = RegularDeveloperEmployee("John Doe", "jogn@doe.com", 1000, "Python")
    regular_developer_2 = RegularDeveloperEmployee("Mike Smith", "mike@smith.com", 1200, "C++")

    # add developers to team
    regular_manager.add_developer_to_team(regular_developer_1)
    regular_manager.add_developer_to_team(regular_developer_2)

    # assign tasks to developers
    regular_manager.assign_tasks_to_developers()

    # start a new sprint
    regular_manager.start_sprint()

    # finish the sprint once all the tasks are complenetd
    regular_manager.finish_sprint()

    # pay employtees for their work
    print(f"{regular_manager.name} got payment: {regular_manager.calculate_payment()}")
    print(f"{regular_developer_1.name} got payment: {regular_developer_1.calculate_payment}")
    print(f"{regular_developer_2.name} got payment: {regular_developer_2.calculate_payment}")
