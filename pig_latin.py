#userin = input("Enter word(s) to convert to Pig Latin: ")




#Takes user input
userStr = input("Enter word(s) to convert to Pig Latin: ")


#Converts the sentance to a list of words
piecesStr = userStr.split(" ")


pigLatin = ''

#Keeps running the loop until all the words in the list are converted
for i in range(len(piecesStr)):
    
    #takes one word at a time from the list
    word1 = piecesStr[i]

#Checking to see if the first letter in the word is a vowel
    if word1[0] == "a" or word1[0] == "e" or word1[0] == "i" or word1[0] == "o" or word1[0] == "u" or word1[0] == "y":

       piecesStr[i] += "yay "
       pigLatin += piecesStr[i]
        
    else:
        #Runs the loop until it finds the next vowel
        for j in range(len(word1)):
            if word1[j] in "aeiouy":
                #When it finds the vowel, it moves the consonats to the back, adds an "ay" at the end and adds this new word to pigLatin variable
                pigLatin += word1[j:] + word1[:j] + "ay "
                break;

#Prints the final output            
print(f'In Pig Latin, \"{userStr}\" is: {pigLatin}')        
        
