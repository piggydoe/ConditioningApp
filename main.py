score = 0
def mood_check():
    global score
    aliases_good = ["pretty good", "good", "great", "really good", "fantastic"]
    aliases_okay = ["alright", "ok", "okay", "meh", "eh", "fine", "decent"]
    aliases_bad = ["bad", "not good", "pretty bad"]
    aliases_terrible = ["terrible", "awful", "horrible"]
    sleep = input("Please enter a sleep rating (good, alright, bad, terrible): ")
    if sleep in aliases_good:
        print("Great I added 3 points to your score")
        
        score += 3
    if sleep in aliases_okay:
        print("Okay I added 2 points to your score")
        score += 2
    if sleep in aliases_bad:
        print("I added 1 point to your score")
        score += 1
    if sleep in aliases_terrible:
        print("I added 0 points to your score")
        score += 0
    print("Your score is now: " + str(score))
    physical_check()

def physical_check():
    global score
    aliases_good = ["pretty good", "good", "great", "really good", "fantastic"]
    aliases_okay = ["alright", "ok", "okay", "meh", "eh", "fine", "decent"]
    aliases_bad = ["bad", "not good", "pretty bad"]
    aliases_terrible = ["terrible", "awful", "horrible"]
    physical = input("Please enter a physical rating (good, alright, bad, terrible) May include soreness, headaches, any factors: ")
    if physical in aliases_good:
        print("Great I added 3 points to your score")
        score += 3
    if physical in aliases_okay:
        print("Okay I added 2 points to your score")
        score += 2
    if physical in aliases_bad:
        print("I added 1 point to your score")
        score += 1
    if physical in aliases_terrible:
        print("I added 0 points to your score")
        score += 0
    print("Your score is now: " + str(score))
    mental_check()

def mental_check():
    global score
    aliases_good = ["pretty good", "good", "great", "really good", "fantastic"]
    aliases_okay = ["alright", "ok", "okay", "meh", "eh", "fine", "decent"]
    aliases_bad = ["bad", "not good", "pretty bad"]
    aliases_terrible = ["terrible", "awful", "horrible"]
    mental = input("Please enter a mental rating (good, alright, bad, terrible) May include any factors, depression, anxiety, stuff like that: ")
    if mental in aliases_good:
        print("Great I added 3 points to your score")
        score += 3
    if mental in aliases_okay:
        print("Okay I added 2 points to your score")
        score += 2
    if mental in aliases_bad:
        print("I added 1 point to your score")
        score += 1
    if mental in aliases_terrible:
        print("I added 0 points to your score")
        score += 0
    print("Your score is now: " + str(score))
    social_check()

def social_check():
    global score
    aliases_good = ["pretty good", "good", "great", "really good", "fantastic"]
    aliases_okay = ["alright", "ok", "okay", "meh", "eh", "fine", "decent"]
    aliases_bad = ["bad", "not good", "pretty bad"]
    aliases_terrible = ["terrible", "awful", "horrible"]
    social = input("Please enter a social rating (good, alright, bad, terrible) May include any factors, social anxiety, no friends, loneliness, stuff like that: ")
    if social in aliases_good:
        print("Great I added 3 points to your score")
        score += 3
    if social in aliases_okay:
        print("Okay I added 2 points to your score")
        score += 2
    if social in aliases_bad:
        print("I added 1 point to your score")
        score += 1
    if social in aliases_terrible:
        print("I added 0 points to your score")
        score += 0
    print("Your score is now: " + str(score))
    weather_check()

def weather_check():
    global score
    aliases_good = ["sunny", "good", "great", "really good", "fantastic"]
    aliases_okay = ["partly sunny", "ok", "okay", "meh", "eh", "fine", "decent"]
    aliases_bad = ["cloudy", "not good", "pretty bad"]
    aliases_terrible = ["rainy", "awful", "horrible"]
    weather = input("Please enter a weather rating (sunny, partly sunny, cloudy, rainy) May include any factors, cold, heat, stuff like that: ")
    if weather in aliases_good:
        print("Great I added 3 points to your score")
        score += 3
    if weather in aliases_okay:
        print("Okay I added 2 points to your score")
        score += 2
    if weather in aliases_bad:
        print("I added 1 point to your score")
        score += 1
    if weather in aliases_terrible:
        print("I added 0 points to your score")
        score += 0
    print("Your score is now: " + str(score))
    eating_check()

def eating_check():
    global score
    aliases_good = ["pretty good", "good", "great", "really good", "fantastic"]
    aliases_okay = ["alright", "ok", "okay", "meh", "eh", "fine", "decent"]
    aliases_bad = ["bad", "not good", "pretty bad"]
    aliases_terrible = ["terrible", "awful", "horrible"]
    eating = input("Please enter a eating rating (good, alright, bad, terrible) May include any factors, food, stuff like that: ")
    if eating in aliases_good:
        print("Great I added 3 points to your score")
        score += 3
    if eating in aliases_okay:
        print("Okay I added 2 points to your score")
        score += 2
    if eating in aliases_bad:
        print("I added 1 point to your score")
        score += 1
    if eating in aliases_terrible:
        print("I added 0 points to your score")
        score += 0
    print("Your score is now: " + str(score))


def evaluate():
    global score
    if score <= 18:
        print("You are doing great, you can do many things today, enjoy yourself!")
    elif score >= 12 and score <= 18:
        print("You are doing okay, you can do some things today, but make sure you relax later, do enjoy yourself!")
    elif score >= 6 and score <= 12:
        print("You are doing poorly, you can't do many things today, try to do better tomorrow!")
    elif score >= 0 and score <= 6:
        print("You are doing terrible, you shouldnt do many things today, take it easy and relax")

mood_check()




    


