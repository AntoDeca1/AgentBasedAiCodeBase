class Constraint:
    def __init__(self, variables):
        self.variables = variables

    def check(self, state):
        return True


class UnaryConstraint(Constraint):
    def __init__(self, variable):
        self.variable = variable
        super(UnaryConstraint, self).__init__(variables=variable)

    def check(self, state):
        return True


class ValueConstraint(UnaryConstraint):
    def __init__(self, variable, allowed_values):
        super(ValueConstraint, self).__init__(variable)
        self.allowed_values = allowed_values

    def check(self, state):
        if self.variable in state:
            return state[self.variable] in self.allowed_values
        return True


class DifferentValues(Constraint):

    def check(self, state):
        values = [state[var] for var in self.variables if var in state]
        return len(values) == len(set(values))
