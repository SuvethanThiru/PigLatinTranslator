def PigLatin():
    vowels = ("A","a","E","e","I","i","O","o","U","u","Y","y")
    x=0
    output=""
    phrase = input("Enter a sentence that you want to translate into English. Type in all the words in lowercase.")
    word=phrase.split()
    while True:
        if phrase=="quit":
            break
        else:
            while x!=len(word):
                word2=word[x]
                word2=word2.replace("-","")
                if word2.isnumeric():
                    print("That is not a word, please enter a word.")
                    x=x+1
                elif word2[len(word2)-3]=="u" and word2[len(word2)-4]=="q":
                    output=output+" "+word2[len(word2)-4].lower()+word2[len(word2)-3].lower()+word2[0:len(word2)-4].lower()
                    x=x+1
                elif (not word2[len(word2)-3] in vowels) and (not word2[len(word2)-4] in vowels):
                    output=output+" "+word2[len(word2)-4].lower()+word2[len(word2)-3].lower()+word2[0:len(word2)-4].lower()
                    x=x+1
                elif (not (word2[len(word2)-3] in vowels)) and (word2[0] in vowels):
                    output=output+" "+word2[len(word2)-3].lower()+word2[0:len(word2)-3].lower()
                    x=x+1
                elif word2[len(word2)-3] in vowels:
                    output=output+" "+word2[0:len(word2)-3].lower()
                    x=x+1
            print(output)
            x=0
            output=""
            phrase=""
            phrase = input("Enter a sentence that you want to translate into English. Type in all the words in lowercase.")
            word=phrase.split()
    print("Thanks for playing.")
    return
def English():
    vowels = ("A","a","E","e","I","i","O","o","U","u","Y","y")
    x=0
    output=""
    phrase = input("Enter a sentence that you want to translate into Pig Latin. Type in all the words in lowercase.")
    word=phrase.split()
    while True:
        if phrase=="quit":
            break
        else:
            while x!=len(word):
                word2=word[x]
                if word2.isnumeric():
                    print("That is not a word, please enter a word.")
                    x=x+1
                elif phrase=="quit":
                    break
                elif word2[0] in vowels:
                    output=output+" "+word2.lower()+"way"
                    x=x+1
                elif word2[0]=="q" and word2[1]=="u":
                    output=output+" "+word2[2:len(word2)].lower()+"-quay"
                    x=x+1
                elif (not(word2[0] in vowels)) and (word2[1] in vowels):
                    output=output+" "+word2[1:len(word2)].lower()+"-"+word2[0].lower()+"ay"
                    x=x+1
                elif not word2[0] in vowels and not word2[1] in vowels:
                    output=output+" "+word2[2:len(word2)].lower()+"-"+word2[0].lower()+word2[1].lower()+"ay"
                    x=x+1
            print(output)
            x=0
            output=""
            phrase=""
            phrase = input("Enter a sentence that you want to translate into Pig Latin. Type in all the words in lowercase.")
            word=phrase.split()
    print("Thanks for playing.")
    return
print("Welcome to the Pig Latin Translator!")
print("1. Pig Latin to English")
print("2. English to Pig Latin")
choice = input("Pick one of the choices above. Enter \"quit\" to leave the translator.")
while choice.isalnum():
    if choice=="1": 
        PigLatin()
        break
    if choice=="2":
        English()
        break
    while choice=="quit":
        print("You are now leaving the translator.")
        break
    else:
        print("Please enter a valid word or phrase.")
        choice = input("Pick one of the choices above. Enter \"quit\" to leave the translator.")
