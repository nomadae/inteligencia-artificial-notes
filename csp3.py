from abc import ABC, abstractmethod


class Constraint(ABC):
    def __init__(self, variables=[]):
        # las variables sobre las que la restricción opera
        self.variables = variables

    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignment={}):
        ...


class CSP():
    def __init__(self, variables=[], domains={}):
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Cada variable debe tener un dominio asignado.")

    def add_constraint(self, constraint):
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("La variable no está en el problema")
            else:
                self.constraints[variable].append(constraint)

    # checar si la asignación es consistente evaluando las restricciones con la variable
    def consistent(self, variable, assignment = {}):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
            return True

    def backtracking_search(self, assignment = {}, ):
        # la asignación se considera completa si cada variable es asignada
        if len(assignment) == len(self.variables):
            return assignment

        # obtener las variables sin asignar
        unassigned = [v for v in self.variables if v not in assignment]

        # obtener todos los valores posibles para las variables sin asignar
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # si es consistente, entra a la recursión
            if self.consistent(first, local_assignment):
                result = self.backtracking_search(local_assignment)
                # si no se encuentra un resultado, paramos el backtracking
                if result is not None:
                    return result
        return None
