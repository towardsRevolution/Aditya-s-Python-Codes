"""
 
Author: Sean Strout @ RIT CS
Author: Aditya Pulekar

 The main program and class for a prefix expression interpreter of the
PreTee language.

Usage: python3 pretee.py source-file.pre
"""

import sys              # argv
import literal_node     # literal_node.LiteralNode
import variable_node    # variable_node.VariableNode
import assignment_node  # assignment_node.AssignmentNode
import print_node       # print_node.PrintNode
import math_node        # math_node.MathNode
import syntax_error     # syntax_error.SyntaxError
import runtime_error    # runtime_error.RuntimeError

class PreTee:
    """
    The PreTee class consists of:
    :slot srcFile: the name of the source file (string)
    :slot symTbl: the symbol table (dictionary: key=string, value=int)
    :slot parseTrees: a list of the root nodes for valid, non-commented
        line of code
    :slot lineNum:  when parsing, the current line number in the source
        file (int)
    :slot syntaxError: indicates whether a syntax error occurred during
        parsing (bool).  If there is a syntax error, the parse trees will
        not be evaluated
    """
    __slots__ = 'srcFile', 'symTbl', 'parseTrees', 'lineNum', 'syntaxError'

    # the tokens in the language
    COMMENT_TOKEN = '#'
    ASSIGNMENT_TOKEN = '='
    PRINT_TOKEN = '@'
    ADD_TOKEN = '+'
    SUBTRACT_TOKEN = '-'
    MULTIPLY_TOKEN = '*'
    DIVIDE_TOKEN = '//'
    MATH_TOKENS = ADD_TOKEN, SUBTRACT_TOKEN, MULTIPLY_TOKEN, DIVIDE_TOKEN

    def __init__(self, srcFile):
        """
        Initialize the parser.
        :param srcFile: the source file (string)
        """

        self.srcFile = srcFile
        self.symTbl = {}
        self.parseTrees=[]
        self.lineNum=1
        self.syntaxError=None

    def __parse(self, tokens):
        """
        The recursive parser that builds the parse tree from one line of
        source code.
        :param tokens: The tokens from the source line separated by whitespace
            in a list of strings.
        :exception: raises a syntax_error.SyntaxError with the message
            'Incomplete statement' if the statement is incomplete (e.g.
            there are no tokens left and this method was called).
        :exception: raises a syntax_error.SyntaxError with the message
            'Invalid token {token}' if an unrecognized token is
            encountered (e.g. not one of the tokens listed above).
        :return:
        """

        if(len(tokens)>=1):
            element = tokens.pop(0)

            if(element == self.ASSIGNMENT_TOKEN):
                if(len(tokens)!=0):
                    AssgnNodeRef = assignment_node.AssignmentNode(self.__parse(tokens),self.__parse(tokens),self.symTbl,element) #symTbl = None
                    self.parseTrees.append(AssgnNodeRef )
                    return AssgnNodeRef
                else:
                    self.syntaxError = "Incomplete Statement at Line Number: "+ str(self.lineNum)

            elif(element == self.PRINT_TOKEN):
                printNodeRef = print_node.PrintNode(self.__parse(tokens))
                self.parseTrees.append(printNodeRef)
                return printNodeRef

            elif(element.isdigit()):
                return literal_node.LiteralNode(element)

            elif (element.isidentifier()):
                return variable_node.VariableNode(element,self.symTbl)

            elif(element == self.ADD_TOKEN or element == self.MULTIPLY_TOKEN or element == self.DIVIDE_TOKEN or element == self.SUBTRACT_TOKEN):
                if(len(tokens)<=1):
                    self.syntaxError = "Incomplete Statement at Line Number: "+ str(self.lineNum)
                return math_node.MathNode(self.__parse(tokens),self.__parse(tokens),element)

            else:
                self.syntaxError= "Invalid Token '^' at Line Number: "+ str(self.lineNum)

    def parse(self):
        """
        The public parse is responsible for looping over the lines of
        source code and constructing the parseTree, as a series of
        calls to the helper function that are appended to this list.
        It needs to handle and display any syntax_error.SyntaxError
        exceptions that get raised.
        : return None
        """

        flag=0 #The program shouldn't execute if there are syntax errors in the code
        try:
            with open(self.srcFile) as file:
                for line in file:
                    line=line.strip()
                    line=line.split()
                    #print(line)
                    if(len(line) != 0):
                        if(line[0] is not "#"):
                            obj=self.__parse(line)
                            if(self.syntaxError is not None):
                                print(self.syntaxError)
                                flag=1
                                self.syntaxError=None
                    self.lineNum+=1
                if flag==1:
                    exit()
        except FileNotFoundError as e:
            print(e)

    def emit(self):
        """
        Prints an infiex string representation of the source code that
        is contained as root nodes in parseTree.
        :return None
        """
        for itr in self.parseTrees:
            toPrint=itr.emit()
            if not isinstance(itr,assignment_node.AssignmentNode):
                if(toPrint==None):
                    print("print: ")
                else:
                    print("print: ",toPrint)
            else:
                if(toPrint==None):
                    print("  ")
                else:
                    print(toPrint)

    def evaluate(self):
        """
        Prints the results of evaluating the root notes in parseTree.
        This can be viewed as executing the compiled code.  If a
        runtime error happens, execution halts.
        :exception: runtime_error.RunTimeError may be raised if a
            parse tree encounters a runtime error
        :return None
        """
        for itr in self.parseTrees:
            if not isinstance(itr,assignment_node.AssignmentNode):
                eval = itr.evaluate()
                print(eval)
            else:
                itr.evaluate()


def main():
    """
    The main function prompts for the source file, and then does:
        1. Compiles the prefix source code into parse trees
        2. Prints the source code as infix
        3. Executes the compiled code
    :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3 pretee.py source-file.pre')
        return

    pretee = PreTee(sys.argv[1])
    print('PRETEE: Compiling', sys.argv[1] + '...')
    pretee.parse()
    print('\nPRETEE: Infix source...')
    pretee.emit()
    print('\nPRETEE: Executing...')
    try:
        pretee.evaluate()
    except runtime_error.RuntimeError as e:
        # on first runtime error, the supplied program will halt execution
        print('*** Runtime error:', e)

if __name__ == '__main__':
    main()
