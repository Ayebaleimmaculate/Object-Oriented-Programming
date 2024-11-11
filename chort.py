class Cohort4:
    # Constructor to initialize cohort name, number of students, description, start date, and end date
    def __init__(self, name, num_students, description, start_date, end_date):
        self.name = name
        self.num_students = num_students
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
     
    # Method to print cohort name, number of students, description, start date, and end date
    def print_cohort4_info(self):
        print(f"Cohort name: {self.name}")
        print(f"Total number of students: {self.num_students}")
        print(f"Description: {self.description}")
        print(f"Start date: {self.start_date}")
        print(f"End date: {self.end_date}")

#a new instance of the Cohort4 class with additional attributes
my_cohort = Cohort4("Cohort3", 25, "Object-Oriented Programming", "2024-01-10", "2024-05-20")
  
# Calling the method to print cohort4 information
my_cohort.print_cohort4_info()
