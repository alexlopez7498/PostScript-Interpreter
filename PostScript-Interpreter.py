import re

# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the stop of the list

# Now define the helper functions to push and pop values on the opstack
# (i.e, add/remove elements to/from the stop of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    if opstack: # check if the stack is not empty
        return opstack.pop() # then we pop it
    else:
        print("Stack is empty")
        return None

def opPush(value):
    opstack.append(value) # we just append item to the stop of the list




# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the stop of the list

# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name

def dictPop():
    if dictstack: # check if dictstack is not empty
        return dictstack.pop() # then pop the top of stack
    else:
        print("Dictstack is Empty")
        return None

def dictPush(d):
    if isinstance(d,dict): # check if d is a dict and if it is then we append it to list/stack
        dictstack.append(d)
    else:
        print("Not pushing a dictionary")

def define(name, value): 
    if len(dictstack):
        dictstack[-1][name] = value
    else:
        newD = {name: value} # we make a dictionary item from the name and value and then we append it to the stack
        dictstack.append(newD)

def lookup(name):
    if not name.startswith('/'):
        name = '/' + name  # we check if the name starts with a / and if it doesn't we add it 

    for dictionary in reversed(dictstack): # loop through the dictionaries to check if we found the name we looked up and return value with that name
        if name in dictionary:
            return dictionary[name]
    return None

    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.


# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.

def add():
    poppedValue1 = opPop()
    if poppedValue1 is None or not isinstance(poppedValue1, (int, float)): # pop top item from stack and check if its an int or float
        opPush(poppedValue1) # also checked if its None and if it is then we push back the item we popped
        return None
    poppedValue2 = opPop()
    if poppedValue2 is None or not isinstance(poppedValue2, (int, float)): # we do the same thing for the second item we pop
        opPush(poppedValue1) # we push both items back
        opPush(poppedValue2)
        return None

    result = poppedValue2 + poppedValue1 # add both popped items together then push it
    opPush(result)



def sub():
    poppedValue1 = opPop()
    if poppedValue1 is None or not isinstance(poppedValue1, (int, float)):  # pop top item from stack and check if its an int or float
        opPush(poppedValue1) # also checked if its None and if it is then we push back the item we popped
        return None
    poppedValue2 = opPop()
    if poppedValue2 is None or not isinstance(poppedValue2, (int, float)): # we do the same thing for the second item we pop
        opPush(poppedValue1) # we push both items back
        opPush(poppedValue2)
        return None

    result = poppedValue2 - poppedValue1 # subtract both popped items together then push it
    opPush(result)

def mul():
    poppedValue1 = opPop()
    if poppedValue1 is None or not isinstance(poppedValue1, (int, float)): # pop top item from stack and check if its an int or float
        opPush(poppedValue1) # also checked if its None and if it is then we push back the item we popped
        return None
    poppedValue2 = opPop()
    if poppedValue2 is None or not isinstance(poppedValue2, (int, float)): # we do the same thing for the second item we pop
        opPush(poppedValue1) # we push both items back
        opPush(poppedValue2)
        return None

    result = poppedValue1 * poppedValue2 # multiply both popped items together then push it
    opPush(result)

def div():
    poppedValue1 = opPop()
    if poppedValue1 is None or not isinstance(poppedValue1, (int, float)): # pop top item from stack and check if its an int or float
        opPush(poppedValue1) # also checked if its None and if it is then we push back the item we popped
        return None
    poppedValue2 = opPop()
    if poppedValue2 is None or not isinstance(poppedValue2, (int, float)): # we do the same thing for the second item we pop
        opPush(poppedValue1) # we push both items back
        opPush(poppedValue2)
        return None
    if poppedValue1 == 0: # check if the first value is 0 because we can't divide by 0
        opPush(poppedValue2)
        opPush(poppedValue1)
        return None

    result = poppedValue2 / poppedValue1 # divide both popped items together then push it
    opPush(result)

def mod():
    poppedValue1 = opPop()
    if poppedValue1 is None or not isinstance(poppedValue1, (int, float)): # pop top item from stack and check if its an int or float
        opPush(poppedValue1) # also checked if its None and if it is then we push back the item we popped
        return None
    poppedValue2 = opPop()
    if poppedValue2 is None or not isinstance(poppedValue2, (int, float)): # we do the same thing for the second item we pop
        opPush(poppedValue1) # we push both items back
        opPush(poppedValue2)
        return None

    result = poppedValue2 % poppedValue1 # mod both popped items together then push it
    opPush(result)

def eq():
    poppedValue1 = opPop()
    poppedValue2 = opPop()
    if poppedValue1 == poppedValue2: # pop top 2 items and compare if theyre equal to each other 
        opPush(True) # push true if yes
    else:
        opPush(False) # push false if no

def lt():
    poppedValue1 = opPop()
    poppedValue2 = opPop()
    if poppedValue2 < poppedValue1: # pop top 2 items and compare if poppedValue2 less than poppedValue1 to each other 
        opPush(True) # push true if yes
    else:
        opPush(False) # push false if no

def gt():
    poppedValue1 = opPop()
    poppedValue2 = opPop()
    if poppedValue2 > poppedValue1: # pop top 2 items and compare if poppedValue2 greater than poppedValue1 to each other 
        opPush(True) # push true if yes
    else:
        opPush(False) # push false if no

# String operators: define the string operators length, get, getinterval, put
def length():
    poppedValue1 = opPop()
    resultLength = 0
    for char in poppedValue1: # loop through each character in poppedvalue
        if char != '(' and char != ')': # if the char is from the alphabet then we add 1 to the length
            resultLength = resultLength + 1
    
    opPush(resultLength) # push the length to the stack


def get():
    index = opPop() # top item is the index
    poppedValue = opPop() # second top item is the string
    counter = 0
    for char in poppedValue: # loop through the string
        if counter == index and char != '(' and char != ')': # if the char is from the alphabet and the counter is equal to the index then we get that chracter
            value = ord(char)
            opPush(value)
            return 
        elif counter != index and char != '(' and char != ')': # if the counter is not equal to the index then we increment it
            counter = counter + 1

def getinterval():
    count = opPop()
    index = opPop()
    string = opPop()
    counter = 0
    newString = ""
    length = 0
    if isinstance(count, int) and isinstance(index, int) and isinstance(string, str): # check if each variable is the correct data type
        for char in string:  #loop through the string
            if length != index and char != '(' and char != ')':
                length = length + 1
            elif char != '(' and char != ')' and index == length and counter != count: # if the char is in the alphabet and the index is less than or equal to the count
                newString = newString + char # we add the char to the newString and increment the index
                index = index + 1
                length = length + 1
                counter = counter + 1
        newString = '(' + newString  + ')' # at the stop we readd the () to the interval and push the newString
        opPush(newString)
    else:
        print("One of the variables is not the correct type")


def put():
    poppedValue = opPop()
    index = opPop()
    string = opPop()
    newString = ""
    counter = 0
    for char in string: # loop through the string
        if char != '(' and char != ')' and counter == index: # if the char is in the alphabet and the counter is equal to the index 
            newString = newString + chr(poppedValue) # add the number for that charcter
            counter = counter + 1 # so that counter is not equal to index
        elif not char != '(' and char != ')': # then we add that character to the new string
            newString = newString + char
        else: # then we add that character to the new string and we increment counter
            newString = newString + char
            counter = counter + 1
    # opPush(newString) # push the new string that was made
    for i, item in enumerate(opstack):
        if item == string:
            opstack[i] = newString
            break



# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
def dup():
    poppedValue = opPop() # pop top value and push it twice
    opPush(poppedValue)
    opPush(poppedValue)

def copy(): 
    stack2 = [] # make a new stack
    for item in opstack: # loop through each item from the stack and append it to the new one
        stack2.append(item)
    while len(stack2) > 0: # while the len of the new stack is greater than 0 then we pop from it and push it to the original stack
        poppedValue = stack2.pop()
        opPush(poppedValue)

def pop():
    opPop() # we just call the opPop function

def clear():
    opstack.clear() # we clear the whole stack

def exch():
    poppedValue1 = opPop() # pop top 2 items from the stack and push them back in swapped
    poppedValue2 = opPop()
    opPush(poppedValue1)
    opPush(poppedValue2)

def roll():
    newStack = [] # make a new stack
    rolls = opPop()
    indexes = opPop()
    check = indexes
    length = len(opstack) # get length of the opstack

    while rolls > 0: # loop till rolls hits 0
        while indexes != 0:  # loop till indexes hits 0
            if length / 2 <= indexes: # if length /2 is less than or equal to indexes 
                if len(opstack) >= 2: # and if len of opstack is greater than or equal to 2 then we call exch function
                    exch()
                    poppedValue = opPop()
                    newStack.insert(0,poppedValue) # pop from the original stack and insert it to the new stack
                    indexes = indexes - 1 # decrement indexes
            else:
                poppedValue = opPop() # we pop it and we dont use exch on it 
                newStack.insert(0,poppedValue)
                indexes = indexes - 1
        opstack.extend(newStack) # add both stacks together into one
        newStack.clear() # clear the new stack we created 
        indexes = check 
        rolls = rolls - 1 # decrement rolls

    while rolls < 0: # loop till rolls hits 0
        while indexes != 0:  # loop till indexes hits 0
            if length / 2 <= indexes: # if length /2 is less than or equal to indexes 
                if len(opstack) >= 2: # and if len of opstack is greater than or equal to 2 then we call exch function
                    exch()
                    poppedValue = opPop()
                    newStack.insert(0,poppedValue) # pop from the original stack and insert it to the new stack
                    indexes = indexes - 1 # decrement indexes
            else:
                poppedValue = opPop() # we pop it and we dont use exch on it 
                newStack.insert(len(newStack),poppedValue)
                indexes = indexes - 1
        opstack.extend(newStack) # add both stacks together into one
        newStack.clear() # clear the new stack we created 
        indexes = check 
        rolls = rolls + 1 # decrement rolls

def stack():
    for value in reversed(opstack): # print every item in the stack starting from the top
        print(value)

# Define the dictionary manipulation operators: psDict, begin, stop, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict(): 
    poppedValue = opPop() # we pop the top item and push an empty dictionary
    opPush({})

def begin(): 
    dic = opPop() # pop from the dict from opstack 
    if(isinstance(dic,dict)): # if it is an dict instance then we push it to the dict stack
        dictPush(dic)
    else: # we push it back into the opstack if its not a dict
        opPush(dic)

def stop(): # pop top item from the dict stack
    dictPop()

def psDef(): # we pop a value and a name from the opstack
    value = opPop()
    name = opPop()
    if isinstance(name, str): # then we make define them 
        define(name, value)

def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

def psFor():
    poppedValue1 = opPop()
    stop = opPop()
    steps = opPop()
    start = opPop()
    if isinstance(poppedValue1,list) and isinstance(stop, int) and isinstance(steps, int) and isinstance(start, int): # check if each is the right data type
        if start <= stop:
            stop = stop + 1
        else:
            stop = stop - 1
            for value in range(start, stop, steps): 
                opPush(value) # push each step into stack
                interpretSPS(poppedValue1) # then use interpretSPS
    else:
        opPush(start) # push everything back in if the data types arent right
        opPush(steps)
        opPush(stop)
        opPush(poppedValue1)
        print("psFor didn't work")

def psIf():

    poppedValue1 = opPop()
    poppedValue2 = opPop()
    if isinstance(poppedValue1,list) and isinstance(poppedValue2,bool): # check if both values are the right data types
        if poppedValue2 == True: # if true then use interpretSPS
            interpretSPS(poppedValue1)
        else: # if its false
            opPush(poppedValue2)
            opPush(poppedValue1)  
            print("psIf did not work") 
    else:# if the data types are wrong
        opPush(poppedValue2)
        opPush(poppedValue1)
        print("psIf did not work")

def psIfelse():
    poppedValue1 = opPop()
    poppedValue2 = opPop()
    poppedValue3 = opPop()
    if isinstance(poppedValue1,list) and isinstance(poppedValue2,list) and isinstance(poppedValue3,bool): # check if values are the right data type
        if poppedValue3 == True: # if true then we use interpretSPS are the poppedValue2
            interpretSPS(poppedValue2)
        elif poppedValue3 == False: # if false then we use interpretSPS are the poppedValue1
            interpretSPS(poppedValue1)
    else: # if wrong data types
        opPush(poppedValue3)
        opPush(poppedValue2)
        opPush(poppedValue1)
        print("psIfelse did not work")

# The it argument is an iterator.
# The sequence of return characters should represent a list of properly nested
# tokens, where the tokens between '{' and '}' is included as a sublist. If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code array for the inner
            # paranthesis, it will be appended to the list we are constructing
            # as a whole.
            res.append(groupMatching2(it))
        elif c.lower() == 'true': # we check to see if c is the word true is that we just append True
            res.append(True)
        elif c.lower() == 'false': # we check to see if c is the word false is that we just append False
            res.append(False)
        elif c.isdigit() or (c.startswith('-') and c[1:].isdigit()): # check to see if c is an int
            res.append(int(c))
        else:
            res.append(c)
    return False

# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested lists.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c == '}':  #non matching closing paranthesis; return false since there is
                    # a syntax error in the Postscript code.
            return False
        elif c == '{':
            res.append(groupMatching2(it))
        elif c.lower() == 'true': # we check to see if c is the word true is that we just append True
            res.append(True)
        elif c.lower() == 'false': # we check to see if c is the word false is that we just append False
            res.append(False)
        elif c.isdigit() or (c.startswith('-') and c[1:].isdigit()): # check to see if c is an int
            res.append(int(c))
        else:
            res.append(c)
    return res


# auxiliary functions if you need them. This will probably be the largest
# function of the whole project, but it will have a very regular and obvious
# structure if you've followed the plan of the assignment.

def interpretSPS(code): # code is a code array
    def processCode(item):
        if isinstance(i, (list,int,bool)): # check to see if c is a list, int or bool
            opPush(i)
        elif i in operators:# if c in an operation from above then we use it
            operators[i]()
        elif isinstance(i, str): # if its a string and it starts with a / then we just push it
            if i.startswith('/'):
                opPush(i)
            elif not i.startswith('/'): # if it doesn't start with a / then we use lookup on it
                item = lookup(i)
                if isinstance(item, list) and item != None: # if the item is a list then use interpretSPS
                    interpretSPS(item)
                elif not isinstance(item, list) and item != None: # if the item is not a list then opPush item
                    opPush(item)
                else: # otherwise push c
                    opPush(i)
    operators = { # we make a hash table of all the operators we've made 
        "add": add,
        "sub": sub,
        "mul": mul,
        "div": div,
        "mod": mod,
        "eq": eq,
        "lt": lt,
        "gt": gt,
        "length": length,
        "get": get,
        "getinterval": getinterval,
        "put": put,
        "dup": dup,
        "copy": copy,
        "pop": pop,
        "clear": clear,
        "exch": exch,
        "roll": roll,
        "stack": stack,
        "dict": psDict,
        "begin": begin,
        "stop": stop,
        "def": psDef,
        "for": psFor,
        "if": psIf,
        "ifelse": psIfelse
        }
    for i in code:
        processCode(i)
                    

def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))


#clear opstack and dictstack
def clear():
    del opstack[:]
    del dictstack[:]


#testing

input1 = """
        /square {
               dup mul
        } def
        (square)
        4 square
        dup 16 eq
        {(pass)} {(fail)} ifelse
        stack
        """

input2 ="""
    (facto) dup length /n exch def
    /fact {
        0 dict begin
           /n exch def
           n 2 lt
           { 1}
           {n 1 sub fact n mul }
           ifelse
        stop
    } def
    n fact stack
    """

input3 = """
        /fact{
        0 dict
                begin
                        /n exch def
                        1
                        n -1 1 {mul} for
                stop
        } def
        6
        fact
        stack
    """

input4 = """
        /lt6 { 6 lt } def
        1 2 3 4 5 6 4 -3 roll
        dup dup lt6 {mul mul mul} if
        stack
        clear
    """
# 1 2 4 5 6 3
# 1 2 5 6 3 4 
# 1 2 6 3 4 5 
input5 = """
        (CptS355_HW5) 4 3 getinterval
        (355) eq
        {(You_are_in_CptS355)} if
         stack
        """

input6 = """
        /pow2 {/n exch def
               (pow2_of_n_is) dup 8 n 48 add put
                1 n -1 1 {pop 2 mul} for
              } def
        (Calculating_pow2_of_9) dup 20 get 48 sub pow2
        stack
        """

print(tokenize(input1))
print("-------------------------------\n")
print(parse(tokenize(input1)))
print("-------------------------------\n")
print(tokenize(input2))
print("-------------------------------\n")
print(parse(tokenize(input2)))
print("-------------------------------\n")
print(tokenize(input3))
print("-------------------------------\n")
print(parse(tokenize(input3)))
print("-------------------------------\n")
print(tokenize(input4))
print("-------------------------------\n")
print(parse(tokenize(input4)))
print("-------------------------------\n")
print(tokenize(input5))
print("-------------------------------\n")
print(parse(tokenize(input5)))
print("-------------------------------\n")
print(tokenize(input6))
print("-------------------------------\n")
print(parse(tokenize(input6)))
print("-------------------------------\n")
interpreter(input1)
clear()
print("-------------------------------\n")
interpreter(input2)
clear()
print("-------------------------------\n")
interpreter(input3)
clear()
print("-------------------------------\n")
interpreter(input4) # roll function
clear()
print("-------------------------------\n")
interpreter(input5) # getinterval
clear()
print("-------------------------------\n")
interpreter(input6) # put function
print("-------------------------------\n")