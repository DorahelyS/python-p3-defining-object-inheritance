'''

Intro to Object Inheritance:

Key Vocab
Inheritance: a tool that allows us to recycle code by creating a class that "inherits" the attributes and methods 
of a parent class.
Composition: a tool that enables you to recycle code by adding objects to other objects. Rather than building on a 
base class as in inheritance, composition leverages the attributes and methods of an instance of another class.
Subclass: a class that inherits from another class. Colloquially called a "child" class.
Superclass: a class that is inherited by another class. Colloquially called a "parent" class.
Child: another name for a subclass.
Parent: another name for a superclass.
super(): a built-in Python function that allows us to manipulate the attributes and methods of a superclass from 
the body of its subclass.
Decorator: syntax that allows us to add functionality to an object without modifying its structure.

Introduction:
The concept of inheritance in Python works similarly to the real world — A prince can inherit a kingdom and 
everything within it; a baby can inherit genetic traits from a parent. In Python, a class can inherit the 
behaviors of another class, referred to as the superclass.


Defining Object Inheritance:
In the real-world, different entities (people, animals, cars, you name it) are related in various ways. 
Within a single entity or group, there exist systems of classification. For example, the "dogs" entity or 
category includes pugs, corgis, labs, etc. All of these breeds share common features because they are all dogs. 
But they all have certain unique traits as well.

Another example: you are writing a web application in which users are either admins, instructors or students. 
All of these entities are "users" and have common features, but they all have some unique traits as well.

How can our code reflect that fact that these different categories of things all share some, or even many, 
characteristics but all have some unique attributes as well? Well, we could write separate Admin, Instructor 
and Student classes that each contain repetitious code to lend each of these classes shared attributes and behaviors. 
We know, however, that repetitive code is always something to be avoided. Not only is it time consuming, but what 
happens when we need to make a change to this shared behavior? We'd have to code the same change in three places.

Instead, we can use inheritance. The use of inheritance allows us to create a family of classes with shared 
behavior, while still differentiating those classes. With inheritance, we could inherit the Admin, Instructor and 
Student classes from a User class. Then, any changes made to the User class would apply to the other class.

While you may not write your own classes that use inheritance very frequently, you will encounter it frequently 
as a developer, particularly when working with other libraries (such as SQLAlchemy, which you'll learn later in 
this phase). Once we introduce the use of databases and the challenge of connecting our programs to our database, 
you'll encounter inheritance in nearly every program you write for the web. More on that later.

What is Inheritance?

In Python, classes can inherit from one another. This means that they acquire all of the attributes and 
behaviors (i.e. all of the methods) of the parent, also called the superclass. An object can directly access 
public inherited attributes and methods. However, since private attributes are only visible in the defining class, 
the private inherited attributes must be accessed through public inherited methods.

In this exercise, we'll be building our own chain of inheritance.

