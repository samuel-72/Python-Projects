# Program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

s = 'zyxwvutsrqponmlkjihgfedcba'

alphabets = 'abcdefghijklmnopqrstuvwxyz'

intial_substring = ''
intial_substring_length = 0

comparison_substring = ''
comparison_substring_length = 0

main_string_index = 0

for current_character in s:
    
    intial_substring_length = 1    
    intial_substring = current_character
    running_index_of_main_string = main_string_index-1
    counter = 0
    length_of_remaining_string = len(s[main_string_index+1:]) 
    
    for letter in s[main_string_index+1:]:

        counter += 1
        #print "The subset of letters is : " + s[main_string_index+1:]
        running_index_of_main_string += 1
        #print "Running Index is : " + str(running_index_of_main_string)

#This block of code below was written to capture the longest substring if it happens to include the last charater as well.

        if (counter == length_of_remaining_string):

            if ( str.find(alphabets,letter) >= str.find(alphabets,s[running_index_of_main_string]) ):
                intial_substring_length += 1
                intial_substring += letter
            
            if ( intial_substring_length > comparison_substring_length ):
                comparison_substring_length = intial_substring_length
                comparison_substring = intial_substring
                #print "Comparison Substring is : " + comparison_substring
            elif  ( intial_substring_length == comparison_substring_length and comparison_substring_length == 2 ):
                #In case of ties, the first substring is to be left as it is. So do Nothing and leave the existing Substring as it is.
                #print "In case of ties, the first substring is to be left as it is. So do Nothing and leave the existing Substring as it is." 
                comparison_substring = intial_substring
                break

#This block of code above was written to capture the longest substring if it happens to include the last charater as well.


#This block of code below was written to capture the longest substring when the index is not at the last character.

        if ( str.find(alphabets,letter) >= str.find(alphabets,s[running_index_of_main_string]) ):
            #print "Current letter is : " + s[main_string_index] + " ||||      Next letter is : " + letter + " |||| Previous letter is : " + s[running_index_of_main_string]
            intial_substring_length += 1
            intial_substring += letter
            #print "Initial Substring is : " + intial_substring
        
                
        else:
            
            if ( intial_substring_length > comparison_substring_length ):
                comparison_substring_length = intial_substring_length
                comparison_substring = intial_substring
                #print "Comparison Substring is : " + comparison_substring
            elif  ( intial_substring_length == comparison_substring_length and comparison_substring_length == 2 ):
                #In case of ties, the first substring is to be left as it is. So do Nothing and leave the existing Substring as it is.
                #print "In case of ties, the first substring is to be left as it is. So do Nothing and leave the existing Substring as it is." 
                comparison_substring = intial_substring
                
            break                
#This block of code below was written to capture the longest substring when the index is not at the last character.
                      
    main_string_index += 1
        
print "Longest substring in alphabetical order is: " + comparison_substring
