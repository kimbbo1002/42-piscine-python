"""
When you store an object in a list, 
you are storing a reference to that specific instance. 
This allows you to loop through the list and access 
any attribute or method defined in that object's class hierarchy.
"""

## Class
Think of a Class as a blueprint or a recipe, and an Instance (Object) as the actual house or cake built from that blueprint.

If you have a blueprint for a house, you can't live in the blueprint itself. You use it to build many houses. Each house can have different colors or owners, but they all share the same structure (walls, roof, doors).

### The Blueprint (`class`) and the Object (`instance`)
In Python, we define a class to group data (attributes) and actions (methods) together.
```python
class Dog:
    # The Constructor: This is where we define the "data" for each dog
    def __init__(self, name, breed):
        self.name = name   # Attribute
        self.breed = breed # Attribute

    # A Method: This is an "action" the dog can do
    def bark(self):
        print(f"{self.name} says: Woof!")

# Creating "Objects" (Instances) from the class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Poodle")

dog1.bark() # Output: Buddy says: Woof!
```

### Understanding `self`
The word `self` is often the most confusing part. Think of `self` as a way for the object to point to itself.

When you say dog1.bark(), Python internally does this: Dog.bark(dog1).
- `self` becomes `dog1`
- That's how the code knows to print "Buddy" and not "Max"

### Inheritance (The Family Tree)
Inheritance allows one class to take all the attributes and methods of another class. This prevents you from writing the same code over and over.

Imagine we have a general `Animal` class, and we want a specific `Cat` class.
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating...")

class Cat(Animal): # Cat inherits from Animal
    def meow(self):
        print(f"{self.name} says: Meow!")

my_cat = Cat("Whiskers")
my_cat.eat()  # Works because of inheritance!
my_cat.meow() # Specific to the Cat class
```

## Nesting a Class (Inner Classes)
Nesting a class simply means defining one class inside another. In module01 ex6, you have `GardenStats` inside `GardenManager`.

**Why ??**
- **Logical Grouping**: If `GardenStats` is only ever used by the `GardenManager` to process garden data, it makes sense to keep it "inside" so your code stays organized.
- **Namespace Control**: It tells other programmers, "This class is a helper specifically for the Manager."
- **Relationship**: It represents a "part-of" relationship. The stats are part of the management system.

**Important Note**: Even though `GardenStats` is inside `GardenManager`, it cannot automatically see `self.plants`.

## **`@classmethod` vs `@staticmethod`**
This is about what data the method can see automatically.

### **`@classmethod`** (The "Global" View)
- **Automatic Argument**: It always receives `cls` (the Class itself) as the first argument.
- **Use Case**: When you need to interact with things that affect every instance of that class.
- **In project**: `create_garden_network`. It needs to look at `total_garden` (a class-level variable) to see how many gardens exist in the whole system. It doesn't care about Alice or Bob specifically; it cares about the "Manager" blueprint.

### **`@staticmethod`** (The "Independant" View)
- **Automatic Argument**: None. It doesn't get `self` or `cls`.
- **Use Case**: When a function is related to the class topic but doesn't need to change or read any data from the class or the objects. It's just a utility tool.
- **In project**: `validate_height`(height). This is just a math check (is the number >0?). It doesn't need to know the garden's name or how many plants there are. It just does its job and returns `True` or `False`.

## Class Polymorphism
In programming, polymorphism refers to the ability of different classes to be treated as instances of the same parent class through the same interface (method name), even though each class implements that method differently.
It is the reason why, in your garden project, you can call `.get_info()` on every plant in your list without needing to know if it's a regular plant or a prize flower.

**How Polymorphism Works**
When you have a parent class and several child classes, they can all have a method with the exact same name. When you call that method on an object, Python "dynamically" figures out which version to run based on the object's actual type.

## Action vs Method
In the context of programming and Object-Oriented Design, these two terms represent the "**What**" versus the "**How**."
1. The Action (The Conceptual Idea)
An Action is a high-level description of what an object can do in the real world or in your program's logic. It is the "verb."

- Examples: "Grow," "Add a Plant," "Bark," "Calculate Score."

- Context: You talk about actions when you are planning your code or explaining it to a human. "The Garden Manager needs an action to help all plants grow at once."

2. The Method (The Code Implementation)
A Method is the actual block of code (the def) inside a class that performs that action. It is the machine that makes the action happen.

- Examples: def grow(self):, def add_plant(self, plant):.

- Context: You talk about methods when you are writing the syntax. "I will implement the grow action using an instance method so it can access the plant's height."