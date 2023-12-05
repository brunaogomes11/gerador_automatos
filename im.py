import networkx as nx
import matplotlib.pyplot as plt

def gerar_automato(alfabeto, regras):
    automato = nx.DiGraph()

    for estado, transicoes in regras.items():
        automato.add_node(estado)
        for simbolo, proximo_estado in transicoes.items():
            automato.add_edge(estado, proximo_estado, label=simbolo)

    return automato

def visualizar_automato(automato):
    pos = nx.spring_layout(automato)
    labels = nx.get_edge_attributes(automato, 'label')

    nx.draw(automato, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
    nx.draw_networkx_edge_labels(automato, pos, edge_labels=labels)

    plt.show()

def verificar_palavra(automato, palavra):
    estado_atual = list(automato.nodes)[0]

    for simbolo in palavra:
        proximos_estados = automato.successors(estado_atual)

        simbolo_presente = False
        for proximo_estado in proximos_estados:
            # Verifica se há uma aresta entre estado_atual e proximo_estado com o rótulo correto
            arestas = automato[estado_atual][proximo_estado]

            for aresta in arestas.values():
                if aresta == simbolo :
                    simbolo_presente = True
                    estado_atual = proximo_estado  # Atualiza o estado_atual apenas se encontrar o símbolo na aresta
                    break

        if not simbolo_presente:
            return False

    return estado_atual in automato.nodes

def main():
    alfabeto = input("Informe o alfabeto (separado por vírgulas): ").split(",")
    regras = {}

    while True:
        estado = input("Informe um estado ou regra de produção (ou 'exit' para encerrar): ")
        if estado.lower() == 'exit':
            break

        transicoes = {}
        for simbolo in alfabeto:
            proximo_estado = input(f"Para o símbolo '{simbolo}', informe o próximo estado: ")
            transicoes[simbolo] = proximo_estado

        regras[estado] = transicoes

    automato = gerar_automato(alfabeto, regras)
    visualizar_automato(automato)

    while True:
        palavra = input("Informe uma palavra para verificar (ou 'exit' para encerrar): ")
        if palavra.lower() == 'exit':
            break

        if verificar_palavra(automato, palavra):
            print("Palavra reconhecida pelo autômato.")
        else:
            print("Erro: Palavra não reconhecida pelo autômato.")

if __name__ == "__main__":
    main()
