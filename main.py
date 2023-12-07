from automato import Automato
import networkx as nx
import matplotlib.pyplot as plt

def criarAutomato():

    alphabet = input("Digite o alfabeto separado por espaços: ").split()
    stateInitial = input("Digite o estado inicial: ")
    stateEnd = input("Digite o estado final (se mais de um, utilize espaço para separar): ").split()
    transictions = criarTransicoes(alphabet)
    newAutomato = Automato(alphabet, stateInitial, stateEnd, transictions)
    newAutomato.populateTransictions()
    
    return newAutomato

def visualizar_automato(automato):
    G = nx.DiGraph()

    for state in automato.states:
        G.add_node(state.name, isEndState=state.isEndState)

    for state in automato.states:
        for symbol, next_state_name in state.transiction.items():
            G.add_edge(state.name, next_state_name, label=symbol)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'label')

    node_colors = ['red' if G.nodes[node]['isEndState'] else 'skyblue' for node in G.nodes]

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=node_colors)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()


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
    automato = None  # Initialize automato outside the loop
    while True:
        print("\n1- Criar Automato\n2- Testar Automato\n3- Finalizar")

        optionInput = input("\nEscolha uma opção acima: ")

        if optionInput == '1':
            automato = criarAutomato()
            visualizar_automato(automato)
        elif optionInput == '2':
            if automato is not None:
                optionWordTest = input("\nInforme uma palavra para testar o autômato: ")
                automato.testAutomato(optionWordTest)
            else:
                print("Você não criou o automato")
        elif optionInput == '3':
            print("Finalizando...")
            break
        else:
            print("Opção inválida, tente novamente!")

if __name__ == "__main__":
    main()