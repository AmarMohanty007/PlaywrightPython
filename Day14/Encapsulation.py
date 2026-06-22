"""
Day 14 - Encapsulation in Python
Demonstrates encapsulation through private variables and getter/setter methods.
Encapsulation hides internal details and controls access to object attributes.
This module covers:
- Private variables using __ (double underscore)
- Getter methods for read access
- Setter methods for write access with validation
- Data protection and integrity
"""

# Example 1: Student class with encapsulation

class Student:
    """
    Student class demonstrating encapsulation.
    - name: public attribute (accessible directly)
    - __marks: private attribute (hidden from direct access)
    """

    def __init__(self, name):
        """
        Constructor to initialize student.

        Args:
            name: Student's name (public)
        """
        self.name = name
        self.__marks = 0  # Private variable - prefixed with __

    def get_marks(self):
        """
        Getter method to read private marks attribute.

        Returns:
            The student's marks
        """
        return self.__marks

    def set_marks(self, marks):
        """
        Setter method to write to private marks attribute with validation.
        Validates that marks are not exceeding 100.

        Args:
            marks: Marks to set
        """
        if marks <= 100:
            self.__marks = marks  # Set only if valid
        else:
            print("Invalid marks. Marks Must be <=100")


# Usage
stu = Student("John")
stu.set_marks(90)  # Use setter method to set marks
print(stu.get_marks())  # Output: 90 - Use getter method to get marks

# Benefits of Encapsulation:
# 1. Data Protection: Direct access to __marks is prevented
# 2. Validation: Setter method can validate data before storing
# 3. Flexibility: Can change internal implementation without affecting external access
# 4. Maintainability: Hide complexity from users of the class
