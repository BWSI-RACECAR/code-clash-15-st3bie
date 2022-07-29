"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #15 - Name Decoder (namedecoder.py)


Author: Carter Berlind

Difficulty Level: 5/10

Prompt: Gregory asks you to help him write a program to decode some users of a program he built. 
You need to write a function that accepts an encoded string as a parameter. This string will contain 
a first name, last name, and an id.

Values in the string can be separated by any number of zeros. The id is a numeric value but will 
contain no zeros. The function should parse the string and return a string that contains the first 
name, last name, and id values. (Note that the shown examples are all people who have had major 
influences on the field of robotics, if there is someone you do not know please look them up to 
learn some of the history and figures of this amazing field!)

Constraints: Strings have no spaces in them and only contain first names, last names, and numeric 
values with zeros to separate them. There does not need to be a zero separating the last name from the id. 

Test Cases:
Input: “Isaac00Asimov0001”          ; Output: “First name = Isaac, Last name = Asimov, id = 1”
Input: “Joeseph0000Engleberger215”  ; Output: “First name = Joseph, Last name = Engleberger, id = 215”
Input: “Raffaello0DAndea00003178”   ; Output: “First name = Raffaello, Last name = DAndea, id = 3178”
Input: “Marc00000000Raibert0023”    ; Output: “First name = Marc, Last name = Raibert, id = 23”
Input: “Daniela00000Rus0132”        ; Output: “First name = Daniela, Last name = Rus, id = 132”
"""

class Solution:
    def decoder(self, id):
        # type id: string
        # return: string

        # TODO: Write code below to return a string with the solution to the prompt
        arr = list(id)
        zero = 0
        fn = ""
        ln = ""
        prev = ""
        character = ""
        num = ""

        for character in arr:
            if (character != "0" and zero == 0):
                fn += character
            
            elif (character != "0" and character.isdigit() == True):
                zero += 1
                num += character
                
            elif (character != "0" and zero == 1):
                ln += character
                
            elif (character != "0" and zero == 2):
                num += character
            else:
                if (prev != "0"):
                    zero += 1
                
            prev = character
            
        return "First name = " + fn + ", Last name = " + ln + ", id = " + num






def main():
    string1 = input()

    tc1 = Solution()
    ans = tc1.decoder(string1)
    print(ans)

if __name__ == "__main__":
    main()