"""
Day 14 - Abstraction in Python (ABC - Abstract Base Classes)
Demonstrates abstraction by hiding implementation details and exposing only functionality.
Abstraction provides access to functionality but hides the underlying implementation.
This module covers:
- Abstract Base Class (ABC)
- Abstract methods using @abstractmethod decorator
- Creating concrete classes that implement abstract methods
"""

# Abstraction Principle:
# Giving access to functionality but hiding implementation details

# ABC - Abstract Base Class
# Used to define a blueprint for other classes without providing implementation details

# Example: Abstract class and concrete implementation

from abc import ABC, abstractmethod

# Abstract class (blueprint/interface)
class Vehicle(ABC):
    """
    Abstract base class for vehicles.
    Defines methods that must be implemented by concrete subclasses.
    """

    @abstractmethod
    def start(self):
        """
        Abstract method - must be implemented by subclasses.
        Defines the start functionality for any vehicle.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Abstract method - must be implemented by subclasses.
        Defines the stop functionality for any vehicle.
        """
        pass


# Concrete class (implements abstract methods from abstract class)
class Car(Vehicle):
    """
    Concrete implementation of Vehicle abstract class.
    Provides specific implementation for car's start and stop methods.
    """

    def start(self):
        """Implement start method for Car."""
        print("Car engine started...")

    def stop(self):
        """Implement stop method for Car."""
        print("Car engine stopped...")


# Usage
# v = Vehicle()  # ERROR: Cannot create object for abstract class
# TypeError: Can't instantiate abstract class Vehicle with abstract methods start, stop

# Create object from concrete class
c = Car()
c.start()  # Output: Car engine started...
c.stop()   # Output: Car engine stopped...
