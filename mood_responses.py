# Module for modules and data handling

def mood_response(mood):
    if mood == 'happy':
        print("I'm glad you are having a good day! Soak up the good energy!")
    elif mood == 'sad':
        print("I'm sorry that you are having a bad day! Better days are coming!")
    elif mood == 'excited':
        print("I hope that the excitement continues!")
    elif mood == 'tired':
        print("Oh no, you are tired! Try to get some extra sleep tonight!")
    elif mood == 'bad':
        print("I'm sorry you are having a bad day! Tomorrow is a new day!")
    else:
        print("Mood response not in system, sorry.")