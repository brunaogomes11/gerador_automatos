import json
from automato import Automato


def criarAutomato():

    alphabet = input("Digite o alfabeto separado por espaços: ").split()
    stateInitial = input("Digite o estado inicial: ")
    stateEnd = input("Digite o estado final (se mais de um, utilize espaço para separar): ").split()
    transictions = criarTransicoes(alphabet)
    newAutomato = Automato(alphabet, stateInitial, stateEnd, transictions)
    newAutomato.populateTransictions()

    return newAutomato

def criarTransicoes(alfabeto):
    transicoes = {}
    while True:
        estadoAtual = input("Informe o estado atual (ou 'exit' para encerrar): ")
        dictEstado = {estadoAtual:{}}
        if (estadoAtual.lower() != 'exit'):
            for simbolo in alfabeto:
                if simbolo != '':
                    dictEstado[estadoAtual][simbolo] = input(f"Para o símbolo '{simbolo}', informe o próximo estado: ")

        else:
            break
        transicoes.update(dictEstado) 
    return transicoes
def main():
    while True:
        print("\n1- Criar Automato\n2- Testar Automato\n2- Finalizar")

        optionInput = int(input("\nEscolha uma opção acima: "))

        if optionInput == 1:
            
            automato = criarAutomato()
        elif optionInput == 2:
            optionWordTest = input(
                "\nInforme uma palavra para testar o autômato: ")
            automato.testAutomato(optionWordTest)
        else:
            print("Opção inválida, tente novamente!")
            break

if __name__ == "__main__":
    main()