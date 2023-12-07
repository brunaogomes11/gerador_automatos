# No código do Estado, ajuste o nome da variável 'transiction' para 'transition'
class Estado:
    def __init__(self, name, state, alphabet, transition):
        self.name = name
        self.isEndState = state
        self.alphabet = alphabet
        self.transition = transition

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def move(self, letter):
        return self.transition[letter]
