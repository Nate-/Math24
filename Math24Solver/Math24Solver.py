"""
Python3 implementation for a solver for Math 24 cards
"""

import itertools

class Math24Solver():
    def _calculateEquation(self, lhs, operation, rhs):
        """
        Calculates and returns the mathematical solution to the 
        equation depending on the operation

        :type lhs: int
        :type operation: str
        :type rhs: int
        :rtype: int
        """
        if operation is "+":
            return lhs + rhs
        elif operation is "-":
            return lhs - rhs
        elif operation is "*":
            return lhs * rhs
        else:
            if rhs is not 0:
                return lhs / rhs

    def _is24(self, values, op1, op2, op3):
        """
        Checks whether the complete equation equates to 24.

        :type values: List[int]
        :type op1: str
        :type op2: str
        :type op3: str
        :rtype: bool
        """
        solution = values[0]
        solution = self._calculateEquation(solution, op1, values[1])
        solution = self._calculateEquation(solution, op2, values[2])
        solution = self._calculateEquation(solution, op3, values[3])

        if solution is 24:
            return True
        else:
            return False

    def _isPlusOrMinus(self, op):
        """
        Checks whether operation is addition or subtraction
        
        :type op: str
        :rtype: bool
        """

        if op is "+" or op is "-":
            return True
        else:
            return False

    def _formatSolution(self, values, op1, op2, op3):

        """
        Formats the solution by adding parentheses to show proper
        order of operations to create 24

        Possible combinations of operations 
        (where + represents addition and subtraction tier of operations
        and * represents multiplication and division tier of operations)

        +++ -> No change
        ++* -> (++)*
        +*+ -> (+)*+
        *++ -> No change
        **+ -> No change
        *+* -> (*+)*
        +** -> (+)**
        *** -> No change
        
        :type values: List[int]
        :type op1: str
        :type op2: str
        :type op3: str
        :rtype: str
        """
        #Default solution is no change
        solution = "{}{}{}{}{}{}{}".format( \
                    values[0], op1, values[1], op2, values[2], op3, values[3])

        #Adding parenthesis where first operation is + or -
        if self._isPlusOrMinus(op1):
            if self._isPlusOrMinus(op2) and not self._isPlusOrMinus(op3): #Case: ++* -> (++)*
                solution = "({}{}{}{}{}){}{}".format( \
                    values[0], op1, values[1], op2, values[2], op3, values[3])
            elif not self._isPlusOrMinus(op2): #Cases: +*+ -> (+)*+  and +** -> (+)**
                solution = "({}{}{}){}{}{}{}".format( \
                    values[0], op1, values[1], op2, values[2], op3, values[3])

        #Adding parenthesis where the operation is *+* -> (*+)*
        else:
            if self._isPlusOrMinus(op2) and not self._isPlusOrMinus(op3): #Case: *+* ->(*+)*
                solution = "({}{}{}{}{}){}{}".format( \
                    values[0], op1, values[1], op2, values[2], op3, values[3])

        return solution

    def solve(self, inputValues):
        """
        Given four numbers, solves whether there is a solution that creates 24. Returns the
        solution if it exists, and returns "No Solutions" otherwise

        :type inputValues: List[int]
        :rtype: str
        """

        #List the valid operations of addition, subtraction, multiplication and division
        validOps = ["+", "-", "*", "/"]

        #Get user input for the four values from Math 24 card
        length = len(inputValues)
        if length is not 4:
            raise ValueError("Invaid number of inputs.")

        #Get permutations of the four numbers
        inputValues = itertools.permutations(inputValues)

        #Search for a solution that equal 24

        for i in inputValues:   #Go through permutations list

            for op1 in validOps:    #Go through valid operations

                for op2 in validOps:

                    for op3 in validOps:
                        if self._is24(i, op1, op2, op3):
                            return self._formatSolution(i, op1, op2, op3)

        return "No Solutions"

if __name__ == "__main__":
    userInput = list(map(int, input("Enter four numbers:  ").split()))
    solver = Math24Solver()
    print(solver.solve(userInput))
