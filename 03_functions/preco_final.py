#Crie uma função calcular_preco_final que receba o preço original como
#parâmetro posicional obrigatório, aceite múltiplos descontos em
#porcentagem via *args (cada desconto é aplicado em sequência sobre o valor
#já descontado), e opções extras via **kwargs com as chaves frete (valor
#numérico a somar) e mensagem (bool que, se True, imprime uma frase
#explicando o cálculo). A função deve retornar o preço final.

def calcular_preco_final(preco_original, *descontos, **alternativas):

    preco_final = preco_original
    valor_frete = alternativas.get("frete", 0)
    mostrar_mensagem = alternativas.get("mensagem", False)

    if mostrar_mensagem:
        print(f"Preço inicial: R$ {preco_original:.2f}")

    for desconto in descontos:
        preco_final -= preco_final * (desconto / 100)

        if mostrar_mensagem:
            print(
                f"Aplicando desconto de {desconto}% → "
                f"novo valor: R$ {preco_final:.2f}"
            )

    preco_final += valor_frete

    if mostrar_mensagem and valor_frete > 0:
        print(
            f"Adicionando frete de R$ {valor_frete:.2f} → "
            f"novo valor: R$ {preco_final:.2f}"
        )

    return preco_final

print("\n====== CALCULADORA DE PREÇOS ======")
print("\n- Resultado com mensagem explicando o cálculo")

resultado = calcular_preco_final(100, 10, 5, frete=15, mensagem=True)
print(f"Preço final: R$ {resultado:.2f}")

resultado = calcular_preco_final(100, 10, 5, frete=15, mensagem=False)
print("\n- Resultado sem mensagem explicando o cálculo")
print(f"Preço final: R$ {resultado:.2f}\n")