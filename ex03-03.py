score = input ("Enter a grade betwenn 0.0 and 1.0 ")
try:
    score=float(score)
except:
    print("Bad score")
    quit()
if score>1.0 or score<0.0:
    print("Bad Score")
else:
    if score>= 0.9:
        print("A")
    if score>= 0.8 and score<0.9:
        print("B")
    if score>= 0.7 and score<0.8:
        print("C")
    if score>= 0.6 and score<0.7:
        print("D")
    if score< 0.6 and score>=0.0:
        print("F")