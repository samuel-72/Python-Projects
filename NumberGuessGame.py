# Program to guess what number the user has thought of

print "Please think of a number between 0 and 100!"

low = 0
high = 100
user_response = ''

while user_response != 'c':

    answer = (low+high)/2
    print "Is your secret number " + str(answer) + "?"
    user_response = raw_input("Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.").lower()
    
    if ( user_response not in ('h','l','c') ):
        print "Sorry, I did not understand your input."  
        continue
                    
    if ( user_response == 'c' ):
        print "Game over. Your secret number was: " + str(answer)
        break      
    
    elif ( user_response == 'h' ):
        high = answer
            
    elif ( user_response == 'l' ):
        low = answer
