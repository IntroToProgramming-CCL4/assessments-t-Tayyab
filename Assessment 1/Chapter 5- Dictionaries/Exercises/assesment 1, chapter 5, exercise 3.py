# these are 5 programming words and there meaning stored in a dictonary 
glossary ={'Variables':'these are containers for storing data values',
'input()':'it is used for taking user input from the keyboard',
'strip()':'is used to remove both leading and trailing whitespace',
'Keywords':'these are reserved words in python',
'Operators':'these are special symbols in Python that perform arithmetic or logical computation'}

# Using for loop to retrive the key/value pair and printing them
for key,value in glossary.items():
    print(key,":\n",value)

#adding 5 more programming words and there meaning
glossary['Data type'] = 'it define the type of data a variable can hold, such as integers, floating-point numbers, strings, lists, and more.'    
glossary['Comments'] = 'These describe what is going on inside a program'
glossary['Lists'] = 'A list is an ordered set of values, where each value is identified by an index.'
glossary['Control structures'] = 'it determine the flow of a program, including conditional statements'
glossary['Loops'] = 'it allow you to repeatedly execute a block of code, either a fixed number of times or as long as a certain condition is met.'

# Using for loop to retrive the key/value pair and printing them
for key,value in glossary.items():
    print(key,":\n",value)
