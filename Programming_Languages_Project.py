from lark import Lark
from functools import reduce

my_grammar = """
?start: token+

?token: operation | word


word: /[^AaSsDdMm][a-z]*/ punctuation

punctuation: ["," | "." | "!" | "?"]

// Allow optional punctuation after each word
?operation: add_operation punctuation | subtract_operation punctuation | divide_operation punctuation | multiply_operation punctuation

add_operation: /[Aa][a-z]*/
subtract_operation: /[Ss][a-z]*/
divide_operation: /[Dd][a-z]*/
multiply_operation: /[Mm][a-z]*/

// imports WORD, WS, CNAME from library
%import common.WORD
%import common.NUMBER
%import common.WS
%import common.CNAME-> NAME
%ignore WS     
"""

def eval_tree(t):
    stack = []
    
    if t.data == 'start':
        for child in t.children:#for children in t.data?
            eval_tree(child)

    elif t.data == 'word':# t.data->child
        stack.append(len(t.children[0]))
        print("word")
        #eval_tree(child)

    elif t.data == 'add_operation':
        x = stack.top()
        stack.pop()
        newX = x+stack.top()
        stack.pop()
        stack.append(newX)
        print("add")
        #eval_tree(child)

    elif t.data == 'divide_operation':
        x = stack.top()
        stack.pop()
        newX = x/stack.top()
        stack.pop()
        stack.append(newX)
        print("divide")
        #eval_tree(child)

    elif t.data == 'subtract_operation':
        x = stack.top()
        stack.pop()
        newX = x-stack.top()
        stack.pop()
        stack.append(newX)
        print("subtract")
        #eval_tree(child)
        
    elif t.data == 'multiply_operation':
        x = stack.top()
        stack.pop()
        newX = x*stack.top()
        stack.pop()
        stack.append(newX)
        print("multiply")
        #eval_tree(child)

    else:
        raise SyntaxError("Unrecognized Tree")
    return stack


parser = Lark(my_grammar)
program = "Were you alright last month?"
parse_tree = parser.parse(program)
#print(parse_tree.pretty())
print(eval_tree(parse_tree))
#print(solve(parse_tree))

   
