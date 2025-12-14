#Calculating Grades

from js import document

def calculate_grade(event):

    English = float(document.getElementById("English").value or 0)
    Math = float(document.getElementById("Math").value or 0)
    Science = float(document.getElementById("Science").value or 0)
    SocialStudies = float(document.getElementById("SocialStudies").value or 0)
    Filipino = float(document.getElementById("Filipino").value or 0)
    Pe = float(document.getElementById("Pe").value or 0)


    total = English + Math + Science + SocialStudies + Filipino + Pe

    average = total / 6

    document.getElementById("display").innerText = f"Your average grade is: {average:.2f}"

