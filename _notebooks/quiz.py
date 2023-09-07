

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def display_py_file():
    # Read the content of your .py file
    with open('"\\wsl.localhost\Ubuntu\home\lakshusan\vscode\student\_notebooks\quiz.py"', 'r') as py_file:
        py_content = py_file.read()

    # Define an HTML template
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python File Content</title>
    </head>
    <body>
        <h1>Content of your Python file:</h1>
        <pre>{{ py_content }}</pre>
    </body>
    </html>
    """

    # Render the HTML template with the Python file content
    return render_template_string(html_template, py_content=py_content)

if __name__ == '__main__':
    app.run(debug=True)

import getpass, sys

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 3
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
answer = input("Are you ready to take a test?")

rsp = question_with_response("What's my name?")
if rsp == "Lakshanya":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What is an interest I mentioned in my data tables?")
if rsp == "books":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

rsp = question_with_response("What day is today?")
if rsp == "Thursday":
    print(rsp + " is correct!")
    correct += 1
else:
    print(rsp + " is incorrect!")

print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))