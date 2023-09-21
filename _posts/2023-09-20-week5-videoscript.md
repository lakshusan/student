---
toc: false
comments: false
layout: post
title: Team Test Video Script
description: The codes we included in our team test video (Bella, Eun, Avanthika, Lakshanya)
courses: {compsci: {week: 5}}
type: plans
---

## Team Test Video Script

---

### Introduction

Lakshanya: Hi, my name is Lakshanya and I’m the Scrum Master. Our team name is LEIA. 
Eun: I’m Eun and I’m the Frontend developer.
Bella: I’m Bella and I’m a Backend developer.
Avanthika: I’m Avanthika and I’m also a Backend developer.


### Project 1

Eun: Our first program is a Python Quiz. It is a program with output, input and output, a list, iteration, with a selection and condition. The purpose of this program is to conduct a quiz, gather user responses, and calculate their scores. 
Bella: Eun and I used Mr Mortensen’s code-we added new questions, used lists, made it iterable, added exceptions, and were able to calculate percentage scores. 
Eun: In class, while we were  going  over our goals for the day in our  meeting and establishing what we hoped to accomplish, Bella and I  decided to use this piece of code from our earlier hacks because it already had elements we needed. For our first block of code, I added a visual element that prints “Python Quiz” to let the user know that there was a quiz.
Bella: Then I left the original code for the first two functions, question_and_answer and question_with_response as well as the greeting to the user and the variables. 
Eun: I identified an error. One thing I noticed in the original program is the “Are you ready to take a test” input only returned the response-even if we typed in no, the code still ran. So I decided to make an exception for that code-the quiz would only run if the user responded yes. So, we had to put the quiz code in a function to call for it and so that it won’t run on it’s own, and created an if statement.conditional-if the answer was yes, the program would run. If the answer was no, the program wouldn’t run.  I sent this code over Slack. Here is a flowchart that we made for this conditional:
Bella: To use lists and make the code iterable, I made the questions one list and the answers on list. Then I used a for loop to run through each element of the questions list. Thanks to everything starting from a 0 index and ending with 8, with a total of nine elements in each list, I was able to use the same for loop to run over both lists, thus making the code more efficient.  I left the correct variable as is because it worked fine, as well as the score out of questions. Try testing out the quiz and seeing if it works.
Eun: To calculate the percent, we divided the number of correct questions by the total amount of questions and multiplied it by 100. We also created an exception relating to the issue I mentioned earlier about the user wanting to take the test or not. I created the error InvalidTesterAnswer and used a try and except block-if the answer was not yes or no, then “It seems like your answer wasn't a clear yes or no. Please try running again!” would be printed out. Try pausing the video and typing in a random number.
Bella: We also tried a tester function for the whole program.
Eun: We tried importing unittest in a different module. However, this did not work as well as we thought and we decided to scrap it and use it for a project that would be more useful, which brings us to our next project.


### Project 2

Lakshanya: Our second program is an ‘about us’ using a dictionary code. We use it to define different things including our names, our date of birth, where we live, our siblings, and where we’ve been.
Avanthika: The purpose of this code is to more easily represent data. We enter data, and data is organized in categories that are easy to understand.
Lakshanya: It also allows us to speed up the process; instead of writing full sentences, our data is shown in a straightforward manner with less to read and consumes less storage.
Avanthika: This code is based on the code with similar information about Mr. Mortensen  and Mr. Lopez that was given to us in an earlier code.
Lakshanya: This information is similar to what we originally used on our home pages at the beginning of the year. Instead of Markdown format, we successfully used python for the code, displayed on Jupyter Notebooks using an .ipynb file in the python cell. 
Avanthika: We used this data and changed some of the information so it matches better. Lakshanya: We had one error where there was no ‘=’ sign between the variable and the data, so the object was not callable.
Avanthika: In our third code, we made an average calculator code. It takes numbers from a data set and takes the average.
Lakshanya: The code had different types of inputs with different numbers and amount of numbers. Each time, the calculator outputs the arithmetic mean of the data set.
Avanthika: We also included an additional code which tested each type of data set calculations; this shows the accuracy of the calculations.
Lakshanya: The last commented line allows for the test to run, but blocks the output from being displayed, so we left it as a comment unless we wanted to see the answer.