"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   * Encapsulation:
        Data and its behaviors "live" close together, so it's easy to see what
        data can do/how it can be acted upon.

    * Abstraction:
        Details can be "hidden" from the user. For example, when we were using
        that graphics program, we knew which methods we could use with various
        shapes, like .setBackgroundColor(), but we didn't need to know how those
        methods worked under the hood.

    * Polymorphism:
        Interchangeability of components. Classes that call the same methods
        should pass the same number of arguments, so that you can loop over
        heterogeneous types.

2. What is a class?

    Classes are a way of storing data and its behaviors. The data structures
    we've encountered previously, like lists, tuples, etc., are specific types
    of classes; that's why they have their own methods.

3. What is an instance attribute?

    An instance attribute is an attribute that is specific to a particular
    instance, rather than shared with all instances of that class.

4. What is a method?

    A method is a function that is defined in the class or inherited from parent
    classes. These methods are called with dot notation, e.g., fido.speak().

5. What is an instance in object orientation?

    An instance is a specific, individual occurrence of a class. For example,
    fido is an instance of the class Dog.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is shared among all instances of that class. For example,
   the class Dog can have color = 'brown' as a class attribute, so that dog
   instances don't need to have their color specified within them, as they can
   look up their class attribute. But if I want to make a particular
   dog black, I can give it an instance attribute of fido.color = 'black'.
   Instances look at themselves first, and if they don't have an instance
   attribute, they look up at their class to see if it's stored there.

"""


# Parts 2 through 5:
# Create your classes and class methods
