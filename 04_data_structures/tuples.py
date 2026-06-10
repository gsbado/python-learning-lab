dataset = [("Alice", 22, 8.5), ("Bruno", 19, 7.0), ("Carla", 
22, 9.2), ("Diego", 25, 6.5), ("Elena", 19, 8.0), ("Fábio", 
25, 7.8)]

#nomes com nota acima da média geral

soma_notas = 0

print("\n====== LISTA DE ALUNOS ======\n")

for nome, idade, nota in dataset:
    print(f"- Nome {nome} | Idade: {idade} | Nota: {nota}")
    soma_notas += nota

media_turma = soma_notas / len(dataset)
print(f"\n A média geral da turma nesse semestre é {media_turma:.1f} \n")
print("====== ALUNOS ACIMA DA MÉDIA ======\n")

for nome, idade, nota in dataset:
    if nota > media_turma:
        print(f"{nome} teve nota acima da média, com {nota}")

#use set para verificar se há idades duplicadas e liste quais são as 
#duplicadas (dica: você pode usar “in” no set para verificar se um 
#dado já está nele ou não)

idades_visitadas = set()
idades_duplicadas = set()
nomes_por_idade = {}

for nome, idade, nota in dataset:

    if idade in idades_visitadas:
        idades_duplicadas.add(idade)
    else:
        idades_visitadas.add(idade)

    if idade not in nomes_por_idade:
        nomes_por_idade[idade] = []

    nomes_por_idade[idade].append(nome)

print("\n====== IDADES DUPLICADAS ======\n")
print("Os seguintes alunos têm idades duplicadas:")

for idade in idades_duplicadas:
    print(f"{' e '.join(nomes_por_idade[idade])} ({idade} anos)")
