# Question 1: University Course Catalog

# Base class: Course
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        """Initialize Course properties"""
        self.course_name = course_name
        self.course_code = course_code
        self.credit_hours = credit_hours

    def display_course_info(self):
        """Display course details"""
        return f"Course Code: {self.course_code}, Name: {self.course_name}, Credit Hours: {self.credit_hours}"

# Subclass: CoreCourse (inherits from Course)
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        """Initialize CoreCourse properties, including required_for_major"""
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_course_info(self):
        """Display course details including if it's required for a major"""
        requirement_status = "Required" if self.required_for_major else "Not Required"
        return super().display_course_info() + f", Required for Major: {requirement_status}"

# Subclass: ElectiveCourse (inherits from Course)
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        """Initialize ElectiveCourse properties, including elective_type"""
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_course_info(self):
        """Display course details including elective type"""
        return super().display_course_info() + f", Elective Type: {self.elective_type}"


core_course_1 = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course_1 = ElectiveCourse("HIST201", "World History", 2, "liberal arts")
core_course_2 = CoreCourse("ECL543", "Neural Networks", 5, False)
elective_course_2 = ElectiveCourse("ECL541", "Internet of Things", 4, "technical")

print("\n")
print(core_course_1.display_course_info()) 
print(core_course_2.display_course_info())  
print(elective_course_1.display_course_info())   
print(elective_course_2.display_course_info())  
print("\n")

