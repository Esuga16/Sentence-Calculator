from lark import Lark
from functools import reduce

my_grammar = """
?start: token+

?token: operation | word


word: /[^AaSsDdMm?,.!][a-z]*/ | /[^AaSsDdMm][a-z]*/ punctuation 


punctuation: "," | "." | "!" | "?"

// Allow optional punctuation after each word
?operation: add_operation | subtract_operation | divide_operation | multiply_operation 

add_operation: /[Aa][a-z]*/ | /[Aa][a-z]*/ punctuation


subtract_operation:  /[Ss][a-z]*/ | /[Ss][a-z]*/ punctuation


divide_operation: /[Dd][a-z]*/ | /[Dd][a-z]*/ punctuation


multiply_operation: /[Mm][a-z]*/  | /[Mm][a-z]*/ punctuation


// imports WORD, WS, CNAME from library
%import common.WORD
%import common.NUMBER
%import common.WS
%import common.CNAME-> NAME
%ignore WS     
"""

stack = []
reverse = []
def eval_tree(t):
    
    if t.data == 'start':
        
        for child in t.children:
            eval_tree(child)

    elif t.data == 'word':

        if (t.children[0].__contains__(" ")):

            stack.append(len(t.children[0])-1)
            
        else:
            stack.append(len(t.children[0]))
        

    elif t.data == 'add_operation':
        
        stackLength = len(stack)
        
        for i in range(stackLength-1):
            x1 = stack.pop()
            newX1 = x1+stack.pop()
            stack.append(newX1)

    elif t.data == 'divide_operation':
        stackLength = len(stack)

        for i in range(stackLength-1):
            x1 = stack.pop()
            newX1 = stack.pop()/x1
            stack.append(newX1)

    elif t.data == 'subtract_operation':
        stackLength = len(stack)
        for i in range(stackLength-1):
            x = stack.pop()
            newX = stack.pop()-x
            stack.append(newX)
        
    elif t.data == 'multiply_operation':
        stackLength = len(stack)
        for i in range(stackLength-1):
            x2 = stack.pop()
            newX2 = x2*stack.pop()
            stack.append(newX2)
    
    else:
        raise SyntaxError("Unrecognized Tree")
    
    return stack[0]

stack.clear()
parser = Lark(my_grammar)
program = "Were you alright last month?" # add then multiply
program2 = "Were you alright?" #add
program3 = "Were you mad?" #multiply
program4 = "It is Sunday!" #subtract
program5 = "It took days." #divide
program6 = "This is a complex example sentence!"
program7 = "badd grammar is cool sometimes"
program8 = "Were you really alright?" #add extended
program9 = "This is the even longer extended adder!" #more extended add
program10 = "This implements extended multiply." #extended multiply
program11 = "This will review divide" #divide extend
program12 = "This will work divide" # 4/(4/4) = 1 
parse_tree = parser.parse(program12)
#print(parse_tree.pretty())
print(eval_tree(parse_tree))
#print(solve(parse_tree))

   
