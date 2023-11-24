
#Eva interpreter
class Eva:
    def __init__(self) -> None:
        pass
    
    def eval(self,exp):
        if self.isInteger(exp):
            return exp
        if self.isString(exp):
            return exp[1:-1]
        if (exp[0] == '+'):
            if (isinstance(exp[1],list)):
                exp[1] = self.eval(exp[1])
            return exp[1] + exp[2]
        
        raise Exception("Unimplemented")
    
    def isInteger(self,var):
        return type(var) == int
    
    def isString(self,var):
        # check that it is a string and that the first and last characters are double quotes
        return type(var) == str and var[0] == '''"'''  and var[-1] == '''"'''
    
    #def sum(self,exp):
     #   start = 1
      #  if (exp[start] == '+'):



    
eva = Eva()

assert eva.eval(1) == 1
assert eva.eval('''"Hello"''') == "Hello"
assert eva.eval(['+', 1, 5]) == 6
testList = ['+',['+', 3, 2],5 ]
assert eva.eval(['+',['+', 3, 2],5 ]) == 10

