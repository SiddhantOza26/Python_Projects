questions =[["Which is the biggest continent in the world?","North America","Asia","Africa","Australia",2],
["Which is the longest river in the world?","Great Ganga","Nile","Amazon","Niger",2],
["Which bank is called bankers Bank of India?","Reserve Bank of India","Punjab National Bank","State Bank of India","ICICI Bank",1],
["Which is the largest animal in the world?","Shark","Blue whale","Elephant","Giraffe",2],
["Which is the 29th state of India?","Uttarakhand","Uttar Pradesh","Madhya Pradesh","Telangana",4],
["Which planet in the solar system is known as the “Red Planet”?","Venus","Earth","Mars","Jupiter",3],
["What animal is the national symbol of Australia?","Kangaroo","Koala","Emu","Crocodile",1],
["What chemical element is designated as “Hg”?","Silver","Tin","Copper","Mercury",4],
["What is the largest ocean in the world?","Indian Ocean","Pacific Ocean","Atlantic Ocean","Arctic Ocean",2],
["What is the tallest mountain in the world?","Mount Kilimanjaro","Mount McKinley","Mount Everest","Mount Fuji",3],
["The language of Lakshadweep a Union Territory of India, is","Tamil","Hindi","Malayalam","Telugu",3],
["September 27 is celebrated every year as","World Tourism Day","Teachers' Day","National Integration Day","International Literacy Day",1],
["Pongal is a popular festival of which state?","Karnataka","Kerala","Andhra Pradesh","Tamil Nadu",4],
["World Health Day is observed on","Apr 7","Mar 6","Mat 15","Apr 28",1],
["Bahubali festival is related to","Islam","Hinduism","Buddhism","Jainism",4],
["Which language is used to create facebook?","Python","Php","Javascript","Java",2]
]

levels=[1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

print("\n***** Welcome to KBC *****")

money=0
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(question[0])
    print(f"1.{question[1]}     2.{question[2]}\n3.{question[3]}     4.{question[4]}")
    ans=int(input("Enter your answer (1-4) or 0 to quit:"))

    if(ans==0):
        money=levels[i-1]
        break
    if(ans==question[-1]):
        print(f"Correct answer,you have won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==15):
            money=10000000    

    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money}") 


