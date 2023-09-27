---
toc: false
comments: false
layout: post
title: Web Programming Code Feedback
description: Different feedback sources for web programming codes
courses: {compsci: {week: 6}}
type: tangibles
---

# Web Programming Code Feedback

---

## ChatGPT feedback on Codes

### Object Personal Representation

Comment and Code Structure:

The code starts with a comment indicating what it's about: assigning key-value objects. This is a good practice to provide context.
Object Creation:

The code creates an object named obj with various key-value pairs representing information about a person.
The object contains attributes like name, age, classes, interests, siblings, ethnicOrigin, instrumentExperience, and passionProject.
Logging Object:

The console.log(obj) statement logs the obj object to the console, displaying its properties and values.
Modifying Classes Property:

The code modifies the classes property by changing the value of the second element in the array.
Logging Modified Property:

The console.log('modified', obj.classes) statement logs the modified classes property to the console.
Defining a String Variable:

A string variable named passionProj is defined, representing a question about hours of practice.
Logging Variable Types:

The code logs the types of the obj and passionProj variables using typeof and outputs the results to the console.
Overall, the code seems to be a simple demonstration of creating and modifying an object in JavaScript, and it logs relevant information to the console. It's clear and well-structured, but providing comments for the purpose of certain operations or explaining the structure of the object could enhance readability and understanding. Additionally, adhering to consistent coding conventions and formatting can further improve code maintainability.


### Code With If Statements and Operators

Comment and Code Structure:

The code begins with a comment indicating what it's about: using if statements and operators. This is a good practice to provide context.
Generating Random Numbers:

Two random numbers, a and b, are generated using Math.random() and Math.floor() to get integers between 0 and 100 (inclusive).
The random numbers are then logged to the console.
If-Else Statements:

The code uses an if-else if-else statement to compare the values of a and b.
If a is greater than b, it prints "a is more than b".
If a is equal to b, it prints "a is the same as b".
If neither condition is true (i.e., a is less than b), it prints "a is less than b".
Overall, the code effectively demonstrates the usage of if statements and comparison operators to handle different scenarios based on the values of a and b. It's clear, concise, and achieves its intended purpose of showcasing conditional logic in JavaScript. However, adding comments within the if-else statements to explain the logic or the purpose of each block could enhance the code's readability and understanding.

## Team Grading

### Bella and Eun's Scoring

2/2.5; The DOM Hack for switching the links did not run. All other hacks were well done and ran without errors. There was a few extra elements added to the hacks that did work.

The link switch didn't work, so I made some changes to the code to allow it to work. Everything else ran smoothly, and I explained the cause of the errors appearing in the 'problems' tab. The magic command was causing problems in VSCode, but the cells did not run otherwise (ignorable error).

