# Sentence-Calculator

This project is a sentence calculator that interprets an english language sentence. It takes the length of each word in the sentence (not starting with m, d, s, or a) 
and applies it to one of four operations. The last word of the sentence is an word that represents the operation. The operation that is used in the calculation will be determined based on the first
letter of the "operation" word. 

The length of the "operation" word is not significant. Each word length is added into a stack based on their position in the sentence. For example "This works fine." is order with "This" at the bottom, followed by "works", then "fine". Notice that the punctuation is not included in the length of the word.

The code can be run with the command "python Programming_Languages_Project.py" from the command line. Examples can be changed between the different example sentences (program1-13).
