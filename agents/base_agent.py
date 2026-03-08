class BaseGRAAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def act(self, state):
        raise NotImplementedError("Subclasses must implement act()")