#!/usr/bin/env python3
import os
os.chdir('/home/student/mycode/')

question1 =" Someone's rattling the garbage can outside your ideal back door. Who is it likely to be?"
answer1 = ["a raccoon", "a homeless person, looking for your leftovers from the fancy restaurant you visited last night.", "the little old lady who lives next door, she collects glass bottles"]

question2 = "It's midnight. What are you doing?"
answer2 = ["lying on my back on the grass", "tcked in bed,fast asleep","dancing at a club"]

question3 = "which is more important to you?"
answer3 = ["knowling the names of all your neighbors", "having a wide variety of restaurants in your neighborhood", "not having a neighbourhood at all"]

question4 = "when it comes to outdoor space, i'm happy if..."
answer4 = ["I have a place to park", "I have a patio to sit on.", "I have full-grown trees"]

questions =[question1, question2, question3, question4]
answers = [answer1, answer2, answer3, answer4]
score = 0
questionNum = 0

while(questionNum < 4):
    
    print(questions[questionNum])
    num = 1
    for x in answers[questionNum]:
        print(str(num) + ". " + x + "\n")
        num += 1
    answerInput = input("which do you choose? (1,2,3)\n")
    while int(answerInput) < 1 or int(answerInput) >=4:
        answerInput = input("please choose among (1,2,3)\n")
   
    if answerInput == 1:
        score += 1
    elif answerInput == 2:
        score += 2
    else:
        score += 3
    questionNum += 1

if (score <= 4):
    print("you belong to city!")
elif (score > 4 and score < 16):
    print("your belong to country!")
else:
    print("your belong to county and city!")



