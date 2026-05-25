

#Purpose:
#A program that quizzes the user on networking and cybersecurity topics. 

#Inputs:
#User text input for answers.

#Outputs:
#Final score
#Feedback on correct/incorrect answers

#Uses random number library to randomize question order.
import random

print("Welcome to the quiz! Let's test your knowledge.")
print("To answer, simply type the letter corresponding to your choice, and hit Enter.")
print()


#List of all required answers and options per question
#Each element in the list is a dictionary with keys "question", "answer", and "options".
questionList = [
    {
    "question": "What layer of the OSI model do routers operate on?",
    "answer": "C",
    "options": [
        "A. Session Layer",
        "B. Data Link Layer",
        "C. Network Layer",
        "D. Application Layer"
        ]
    },

    {
    "question": "What is the primary function of a switch in a network?",
    "answer": "B",
    "options": [
        "A. Route packets between different networks",
        "B. Forward data within the same network segment",
        "C. Amplify signals in a network",
        "D. Store and forward data packets"
        ]
    },

    {
        "question": "Which protocol is used to resolve IP addresses to MAC addresses?",
        "answer": "A",
        "options": [
            "A. ARP",
            "B. DNS",
            "C. HTTP",
            "D. TCP"
        ]
    },

    {
        "question": "What is the primary function of a hub in a network?",
        "answer": "A",
        "options": [
            "A. Broadcast data to all devices on the network",
            "B. Forward data within the same network segment",
            "C. Route packets between different networks",
            "D. Store and forward data packets"
        ]
    },

    {
    "question": "What is the primary function of a router in a network?",
    "answer": "C",
    "options": [
        "A. Broadcast data to all devices on the network",
        "B. Forward data within the same network segment",
        "C. Route packets between different networks",
        "D. Store and forward data packets"
        ]
    },

    {
    "question": "What is 128 in binary?",
    "answer": "A",
    "options": [
        "A. 10000000",
        "B. 10000001",
        "C. 10000010",
        "D. 10000011"
        ]
    },

    {
    "question": "What is the primary function of a firewall in a network?",
    "answer": "B",
    "options": [
        "A. Amplify signals in a network",
        "B. Monitor and control incoming and outgoing network traffic",
        "C. Route packets between different networks",
        "D. Store and forward data packets"
        ]
    },

    {
    "question": "What does the Triple A Triad stand for in cybersecurity?",
    "answer": "A",
    "options": [
        "A. Authentication, Authorization, Accounting",
        "B. Availability, Auditing, Access Control",
        "C. Access Control, Audit Trail, Actualization",
        "D. Threat Detection, Response, Recovery"
        ]
    },

    {
    "question": "What type of attack was the recent Canvas LMS attack?",
    "answer": "A",
    "options": [
        "A. Ransomware",
        "B. Phishing",
        "C. Keylogging",
        "D. Spyware"
        ]
    },

    {
    "question": "What is ethical hacking?",
    "answer": "A",
    "options": [
        "A. Legitimate penetration testing",
        "B. Unauthorized access to systems",
        "C. Creating malware",
        "D. Stealing sensitive information"
        ]
    },
]



#Function that prompts the user with questions and checks their answers
#It takes the list, and outputs the question and options, then validates it and updates the score

#Parameter questionOrder is a list of indices that determines the order of questions asked. 

def askQuestions(questionOrder): 
    score = 0   #variable local to function, but outside the loop to keep track of score
    for i in range(len(questionOrder)):
        print(questionList[questionOrder[i]]["question"])    
        #Nested for loop cycles the list, for the options inside each dictionary, and prints them out
        for option in questionList[questionOrder[i]]["options"]:
            print(option)
        answer = input("YOUR Answer:")

        if answer.upper() == questionList[questionOrder[i]]["answer"]:  
            #Upper function is used to make sure user input is unaffected by case sentitivity
            print("Correct!")
            score += 1
            print("Your Score:", score)
            print()
        else:
            print("Incorrect! The correct answer was:", questionList[questionOrder[i]]["answer"])
            print("Your Score:", score)
            print()


def main():
    #List is made for randomization. It uses the indices of questionList for easy comprehension
    quizOrder = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(quizOrder)
    askQuestions(quizOrder)


#Call to main function
main()