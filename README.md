## ▶️ Execução do Código

Para executar o programa que aplica o Lema do Bombeamento:

1. Certifique-se de que o Python 3 está instalado no sistema.
2. Salve o código no arquivo `lema_bombeamento.py`.
3. No terminal, execute o seguinte comando:

```bash
python lema_bombeamento.py
```

Durante a execução, o programa irá:

- Solicitar ao usuário que escolha entre duas linguagens formais:
  - L1: L = { a^n b^n | n ≥ 0 }
  - L2: L = { b a^n | n ≥ 1 }
- Receber a cadeia de entrada `w` e o valor de bombeamento `p`.
- Testar todas as possíveis divisões x, y, z da cadeia, com |xy| ≤ p e |y| > 0.
- Gerar as cadeias x y^i z para i = 0, 1, 2 e verificar se pertencem à linguagem.
- Identificar e exibir quebras do lema, caso existam.

### 🔍 Pontos importantes

- O Lema do Bombeamento é uma ferramenta teórica utilizada para provar que uma linguagem **não é regular**.
- A função `testar_lema_bombeamento` automatiza a aplicação do lema e facilita a análise de linguagens formais.
- A ausência de quebras **não comprova** que a linguagem seja regular — apenas que não foi possível provar sua irregularidade com os dados fornecidos.
