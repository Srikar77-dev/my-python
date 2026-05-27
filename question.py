from Question1 import Question as q

question_s = [
    "what anime is about freedom among the options?\na. Attack on Titan\nb. One Piece\nc. Naruto",
    "who is the opposit of god?\na.adolf hitler\nb.mamata benerji\nc.rahul gandhi",
    "who is the worst person alive?\na.Shehbaz sharif\nb. donald trump\nc. kim jong"
]

question= [ q(question_s[0],"a"),
            q(question_s[1],"a"),
            q(question_s[2],"b")
          ]

def test():
    score = 0
    for q in question:
        answer = input(q.question_text+"\n")
        if answer == q.answer:
            score +=1
    print("your got is "+str(score)+"/"+str(len(question))+ " correct")
test()        