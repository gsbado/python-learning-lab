print("\n====== CALCULADORA DE PREÇOS ======\n")

def calcular_preco_final(preco_original, *descontos, **alternativas):
    preco_final = preco_original
    valor_frete = alternativas.get("frete", 0)

    for desconto in descontos:
        preco_final -= preco_final * (desconto / 100)
        print(f"Desconto de {desconto}%: R$ {preco_final:.2f}")

    preco_final += valor_frete
    
    print(f"Frete adicionado: R$ {preco_final:.2f}")

    return preco_final

resultado = calcular_preco_final(100, 10, 5, frete=15)

print(f"\nPreço final: {resultado}\n")