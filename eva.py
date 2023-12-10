import re

'''Environment: Names storage'''
class Environment:
    def __init__(self, record = None):
        self.record = record or dict() 
    
    '''Creates variable with the give name and value'''
    def define(self,name, value):
        self.record[name] = value
        return self.record[name]
    
    def lookup(self, name):
        if name in self.record:
            return self.record[name]
        raise Exception("Variable " + str(name) + " is not defined")
            
#Eva interpreter
class Eva:
    def __init__(self,globalEnv = Environment()):
        self.globalEnv = globalEnv
    
    def eval(self,exp, env = None):
        '''
        Returns the evaluation of a given expression in a specific environment
        Examples of expressions can be simple arithmetic operations, variable assignments and scope evaluation
            Parameters:
                    exp - expression to be evaluated
                    env (optional) - a specific environment to be used in the evaluation of the expression
            
            Returns an exception if the expression cannot be evaluated else returns the result of the given expression
        '''
        if env == None:
            env = self.globalEnv

        # Self evaluation expressions
        if self.isInteger(exp):
            return exp
        if self.isString(exp):
            return exp[1:-1]
        
        # Math Operations
        if (exp[0] == '+'):
            return self.eval(exp[1]) +  self.eval(exp[2])
        if (exp[0] == '-'):
            return self.eval(exp[1]) -  self.eval(exp[2])
        if (exp[0] == '*'):
            return self.eval(exp[1]) *  self.eval(exp[2])
        if (exp[0] == '/'):
            return self.eval(exp[1]) /  self.eval(exp[2])
        
        #Block sequence of expressions
        if(exp[0] == 'begin'):
            pass
        #Environment logic
        if (exp[0] == 'var'):
            name = exp[1]
            value = self.eval(exp[2])
            return env.define(name, value)
        if(self.isVariableName(exp)):
            return env.lookup(exp)

        raise Exception("Unimplemented --> " + str(exp))
    
    def isInteger(self,var):
        return type(var) == int
    
    def isString(self,var):
        # check that it is a string and that the first and last characters are double quotes
        return type(var) == str and var[0] == '''"'''  and var[-1] == '''"'''
    
    def isVariableName(self,var):
        return type(var) == str and re.search('^[a-zA-Z][a-zA-Z_0-9]*$', var)
    
    def evalBlock(self, block, env):
        '''
        Function to sequentially evaluate  expressions in a block
            Parameaters:
                block - block keyword
                env -
        '''
    


defaulRecord = {
    'null': 'NULL',
    'true' : True
    }
env = Environment(defaulRecord)
eva = Eva( env )

assert eva.eval(1) == 1
assert eva.eval('''"Hello"''') == "Hello"
assert eva.eval(['+', 1, 5]) == 6
testList = ['+',['+', 3, 2],5 ]
assert eva.eval(['+',['+', 3, 2],5 ]) == 10
assert eva.eval(['*',['*', 3, 2],5 ]) == 30
assert eva.eval(['+',['*', 3, 2],5 ]) == 11
assert eva.eval(['/',['*', 3, 5],3 ]) == 5

'''Environment tests'''
assert eva.eval(['var', 'x', 10]) == 10 # definning variable
assert eva.eval('x') == 10 # accessing variable name
assert eva.eval(['var', 'number_1', 5]) == 5
assert eva.eval('number_1') == 5
assert eva.eval(['var', 'isUser', 'true']) == True  
assert eva.eval(['var', 'z', ['*',2,2]]) == 4

'''Block Tests'''
assert eva.eval(
    ['begin',
     ['var', 'x', 10],
     ['var', 'y', 20],
     ['+',['*', 'x' , 'y '],30]
     ]) == 230

print("All assertions passed")


