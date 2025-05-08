def linguagem_an_bn(w):
    """
    L = { a^n b^n | n ≥ 0 }
    """
    a_count = 0
    b_count = 0
    state = "a"

    for c in w:
        if c == 'a':
            if state != "a":
                return False
            a_count += 1
        elif c == 'b':
            state = "b"
            b_count += 1
        else:
            return False
    return a_count == b_count

def linguagem_b_a_n(w):
    """
    L = { b a^n | n ≥ 1 }
    """
    if not w or w[0] != 'b':
        return False
    # depois do 'b' deve vir pelo menos um 'a' e só 'a'
    rest = w[1:]
    return len(rest) >= 1 and all(c == 'a' for c in rest)

def testar_lema_bombeamento(linguagem, w, p):
    """
    Aplica o lema do bombeamento à cadeia w com valor p, testando se L é regular.
    Retorna lista de quebras (x, y, z, resultados).
    """
    n = len(w)
    quebras = []

    for i in range(1, p+1):       # |xy| ≤ p
        for j in range(1, p+1):   # |y| > 0
            if i + j > n:
                continue
            x = w[:i]
            y = w[i:i+j]
            z = w[i+j:]

            resultados = []
            for k in range(3):    # testar i = 0, 1, 2
                nova_cadeia = x + y * k + z
                pertence = linguagem(nova_cadeia)
                resultados.append((k, nova_cadeia, pertence))

            if not all(r[2] for r in resultados):
                quebras.append((x, y, z, resultados))

    return quebras

def main():
    print("Escolha a linguagem para testar:")
    print("1) L = { a^n b^n | n ≥ 0 }")
    print("2) L = { b a^n | n ≥ 1 }")
    opc = input("Opção (1 ou 2): ").strip()

    if opc == '1':
        linguagem = linguagem_an_bn
        desc = "L = { a^n b^n | n ≥ 0 }"
    elif opc == '2':
        linguagem = linguagem_b_a_n
        desc = "L = { b a^n | n ≥ 1 }"
    else:
        print("Opção inválida. Encerrando.")
        return

    w = input(f"Digite a cadeia w (símbolos válidos para {desc}): ").strip()
    p = int(input("Digite o valor de bombeamento p (inteiro ≥ 1): ").strip())

    print(f"\nTestando linguagem {desc} com w = '{w}' e p = {p}\n")
    quebras = testar_lema_bombeamento(linguagem, w, p)

    if not quebras:
        print("Nenhuma quebra do lema encontrada para as divisões testadas.")
    else:
        for x, y, z, resultados in quebras:
            print(f"Divisão: x='{x}', y='{y}', z='{z}'")
            for i, nova_cadeia, pertence in resultados:
                status = "Pertence" if pertence else "Fora da linguagem"
                print(f"  i={i}: {nova_cadeia} → {status}")
            print("→ QUEBRA DO LEMA!\n")

if __name__ == "__main__":
    main()
