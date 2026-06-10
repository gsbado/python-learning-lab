#Gabriela Spanemberg Bado

#Parte 1: Lista e tupla:
#Crie uma lista com 4 livros, onde cada livro é uma tupla com título e ano de publicação
#Imprima todos os livros
#Imprima apenas o livro mais antigo (sem usar min())

livros = [("Harry Potter e a Pedra Filosofal", 1997), ("O Iluminado", 1977), ("O Senhor dos Anéis: A Sociedade do Anel", 1954), ("O Pequeno Príncipe", 1943), ("A Biblioteca da Meia-Noite", 2020)]

print("\n*** INÍCIO DOS ATENDIMENTOS DA BIBLIOTECA ***\n")
print("====== LISTA DE LIVROS ====== \n")
for titulo, ano in livros:
    print(f"- Título do livro: {titulo} | Ano de publicação: {ano}")

livro_mais_antigo = livros[0]

for livro in livros:
    if livro[1] < livro_mais_antigo[1]:
        livro_mais_antigo = livro

print(f"\nO livro mais antigo da lista é: {livro_mais_antigo[0]} publicado em {livro_mais_antigo[1]}\n")

#Parte 2: Pilha de devoluções:
#Simule uma pilha de devoluções: adicione 3 livros devolvidos um por um
#Processe as devoluções retirando sempre o último devolvido primeiro
#Imprima qual livro está sendo processado a cada retirada

pilha_livros = []

for livro in livros:
    pilha_livros.append(livro)

print("====== PILHA DE DEVOLUÇÕES ====== \n")
for _ in range(3):
    livro_processado = pilha_livros.pop()
    print(f"- O livro {livro_processado[0]} foi devolvido à bibilioteca")

contagem_livros_restantes = len(pilha_livros)

print(f"\n Ainda existem {contagem_livros_restantes} livros na pilha de livros que devem ser devolvidos.\n")

#Parte 3: Fila de atendimento:
#Simule uma fila de atendimento com 3 clientes
#Atenda os clientes na ordem de chegada
#Após atender o primeiro cliente, adicione um novo cliente à fila
#Imprima a fila após cada atendimento

from collections import deque

fila_atendimento = deque()
fila_atendimento.append("Gabriela")
fila_atendimento.append("Jean")
fila_atendimento.append("Maria Joana")

print("====== FILA DE ATENDIMENTO ====== \n")
cliente = fila_atendimento.popleft()
print(f"O cliente que está sendo atendido no momento se chama {cliente}. Esse cliente é o primeiro da fila pois chegou primeiro.")
fila_atendimento.append("Ronaldinho Gaúcho")
print(f"Um novo cliente entrou na fila! Olhe, é o {fila_atendimento[-1]}!")
print("Fila de atendimento atual:", " -> ".join(fila_atendimento))

while fila_atendimento:
    cliente = fila_atendimento.popleft()
    print(f"\nO novo cliente em atendimento é {cliente}")
    if fila_atendimento:
        print("Fila de atendimento atual:", " -> ".join(fila_atendimento))
    else:
        print("Não há mais leitores na fila de atendimento. Vamos aguardar o próximo cliente chegar!")
        break

print("\n *** FIM DO ATENDIMENTO DA BIBLIOTECA *** \n")
