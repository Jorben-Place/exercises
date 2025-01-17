import sys
# reading the file
with open(sys.argv[1]) as fp:
    contents=fp.readlines()

# initialize two counter to check mismatch between "(" and ")"
open_bracket_counter=0
close_bracket_counter=0 

# whenever an element deleted from the list length of the list will be decreased
decreasing_counter=0   

for number in range(len(contents)):

    # checking if the line contains "#" or not
    if "#" in contents[number-decreasing_counter]:

        # delete the line if startswith "#"
        if contents[number-decreasing_counter].startswith("#"):
            contents.remove(contents[number-decreasing_counter])
            decreasing_counter+=1

        # delete the character after the "#"    
        else:  
            newline=""  
            for character in contents[number-decreasing_counter]:
                if character=="(":
                    open_bracket_counter+=1
                    newline+=character
                elif character==")":
                    close_bracket_counter+=1
                    newline+=character
                elif character=="#" and open_bracket_counter==close_bracket_counter:
                    break
                else:
                    newline+=character
            contents.remove(contents[number-decreasing_counter])     
            contents.insert(number-decreasing_counter,newline)   


# writing into a new file
with open(sys.argv[2],"w") as fp:
    fp.writelines(contents)