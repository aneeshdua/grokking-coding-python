"""
Parse Strings that form a simple language as follows:

input: “add(1,3)”
output: 4

input: “sub(1,3)”
output: -2

operations take only 2 params, commands may be nested
ie. "add(sub(3,4), 1)" "sub(add(238943, 2343), add(1, sub(323, 43)))"

Limitations:
string length: 1024 chars

For invalid strings throw syntax error. Error message must include the position in the string where the error is i.e. “add(bad, 2342)”, returns “syntax error at position 5 “”bad” in the string. Looking for testing numbers are INTEGERS

Constraints:
Can't use built in "eval" type functionality in a language ie. python , JS.

"""

"""
1. operation(x,y). All integers. Max Length of string is 1024
2. Parts of the problem:
    - parse the string into operation and x and y. Handle whitespaces. Handle cases?
    
    - identify the operation. Only first three characters? Extendible approach for more than or less than 3chars - handle incorrect scenario 1
    - convert the x and the y to integers - handle scenario 2
    - apply the operation to x and y - 
3. Looks like recursive is the solution.
4. Scenarios where string is invalid:
 - unknown/incorrect operation string is supplied
 - x and y are not integers
 - incorrect structure (parenthesis/comma)
 
Approach Steps in detail:
1. Parsing of the string:
    Generic pattern: operation(Int,Int)


Possible Test Cases:
1. Happy Cases:
    - basic command
    - nested command
    - Whitespaces in between of the command string
2. Exception cases:
    - having incorrect operation name
    - having either float or alphanumeric characters in places of operands
    - Incorrect parenthesis (correct open and close and its position)
    - Input string of length more than 1024 characters
    
    
"""
# import requests
# import mysql.connector
# import pandas as pd
import re

def extractOp(subInput):
    pattern1 = "^[a-z]+\([0-9]+\,[0-9]+\)$"
    pattern2 = "[0-9]+"
    re.compile(pattern1)
    match1 = re.match(pattern1, subInput)
    match2 = re.match(pattern2,subInput)
    value=0
    if len(match1)>0:
        value = processCommand(match1)
        return True,value
    elif len(match2)>0:
        value = int(x)
        return True,value
    else:
        return False,None
        
    # returns the value of the operand
    
    
def extractEntity(input):
    pattern1 = "$[a-z]+([0-9]+,[0-9]+)^" #single command
    pattern2 = "[0-9]+" #just integer
    subString1 = input[:index]
    #extractOp()
    # # do a regex match
    # regex.compile(pattern)
    # if regex.match(pattern, input):

    # magic regex
    # returns the x and y
    # Checks if x and y are actually integers, handles issue2. Returns the integer values
    # returns -1 and the x and y in a tuple
    # return index of error and an empty tuple incase of any exception occured
    
    # regex.compile(pattern1)
    # match1 = regex.match(pattern1, input)
    # match2 = regex.match(pattern2,input)
    # x=y=0
    # if len(match1)>0:
    #     x = processCommand(match1)
    # elif len(match2)>0:
    #     x = Int(x)
    # else:
    #     #raise exception
    #     print("Error parsing operand1")
        
        
   
    

    
def processCommand(input:str):
    #parse
    #start from the beginning
    # we iterate till we see an open parenthesis
    parenthesisOpenIdx = operand1Idx = operand2Idx = 0
    for chrIndex1 in range(0,len(input)):
        if input[chrIndex1] =='(':
            parenthesisOpenIdx = chrIndex1
            break

    operationString = input[:parenthesisOpenIdx]

    # validate the operation string
    #add1,3) - need to handle the position for this
    if operationString not in operationLookup or parenthesisOpenIdx==len(input):
        print("syntax error at position ", parenthesisOpenIdx, operationString,"in the string") # handles issue1 
    
    for chrIndex1 in range(parenthesisOpenIdx+1,len(input)):
        if input[chrIndex1] ==',':
            operand1Idx = chrIndex1
            break
    operand1 = input[chrIndex1+1,operand1Idx-1]
    #parse operand1

    for chrIndex1 in range(operand1Idx+1,len(input)):
        if input[chrIndex1] ==',':
            operand2Idx = chrIndex1
            break
    operand2 = input[chrIndex1+1,operand2Idx-1]
    #parsedSuccess, x,y = extractEntity(input[:chrIndex])
    # if parsedSuccess == -1:
    #     return operationLookup[operationString](x,y)
    # else:
    #     print("Error parsing Integers", parsedSuccess, ) #handles issue2
    #     return None

    
    
def addTwoNums(x,y):
    return x+y

def subTwoNums(x,y):
    return x-y

operationLookup = {
    'add': addTwoNums,
    'sub': subTwoNums
}
inputCommand = "add(1,3)"

processCommand(inputCommand)

