Process.md — Assignment 4(CFCP)
📌 Project Overview
  This document explains the entire process of creating a Python-based calculator, initializing Git, committing changes, and pushing the project to a GitHub repository using VS Code and the terminal.

✅ 1. Create the Project Folder
->Create a new folder, for example:
  Assignment 4(CFCP)

  Open this folder in VS Code.

✅ 2. Create the Python Calculator
->Inside VS Code, create a file named:
  Calculator.py

Wrote a simple calculator program,

print("Hello, user!")
#Enter the numbers:
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

#Choices for arithematic calculations
print("Select 1 for addition")
print("Select 2 for subtraction")
print("Select 3 for multiplicaion")
print("Select 4 for division")
choices=int(input("Enter your selected choice:"))
#conditions
if choices=='1' :
    sum=num1+num2
    print("On adding numbers we get:",sum)

elif(choices=='2'):
    diff=num1-num2
    print("On subtracting numbers we get:",diff)

elif(choices=='3'):
    product=num1*num2
    print("On multiplying numbers we get:",product)

elif(choices=='4'):
    quotient=num1//num2
    print("On dividing numbers we get:",quotient)

else:
    print("INVALID CHOICE!! Please select from above choices")

    
✅ 3. Initialize Git Repository
->Open the VS Code terminal:
  Ctrl + `

->Run:
  git init
  This creates a .git folder and initializes the repository.

✅ 4. Configure Git (only first time)
  git config --global user.name "Your Name"
  git config --global user.email "your-email@example.com"

✅ 5. Add Files to Staging Area
  git add .

->Or add specific file:
  git add calculator.py

✅ 6. Commit the Code
  git commit -m "Added calculator program"

If it says nothing to commit, it means no file was changed after last commit.

✅ 7. Create a GitHub Repository
  Go to GitHub → New Repository
  Give a name, for example: Assignment 4 CFCP by Aadit Prashar
  Create repository

✅ 8. Connect Local Repo to GitHub
->Copy the commands GitHub gives:
  git remote add origin https://github.com/yourusername/python-calculator.git

->Verify:
  git remote -v

✅ 9. Push Code to GitHub
->For first push:
  git branch -m main
  git push -u origin main

->For future pushes:
  git push


⭐ Summary
-->Step	Description
1.	Created project folder
2.	Wrote calculator program in Python
3.	Initialized Git using VS Code terminal
4.	Staged file using git add
5.	Committed changes
6.	Created GitHub repo
7.	Connected VS Code Git → GitHub
8.	Pushed code successfully
🎉 Your Calculator Project Is Now Live on GitHub!

You can now share your repository link or keep updating your project with more commits.
