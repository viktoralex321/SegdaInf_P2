import os
import sys
import math

def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ler_inteiro(mensagem):
    """Lê um número inteiro, repetindo até a entrada ser válida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def eh_primo(n):
    """Verifica se n é um número primo."""
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    limite = math.isqrt(n)

    for divisor in range(3, limite + 1, 2):
        if n % divisor == 0:
            return False

    return True

def ler_primo(mensagem):
    """Lê e valida um número primo."""
    while True:
        numero = ler_inteiro(mensagem)

        if eh_primo(numero):
            return numero

        print(f"Erro: {numero} não é um número primo. Tente novamente.")

def criptografar(texto, e, n):
    """
    Criptografa cada caractere separadamente.
    Retorna uma lista de blocos numéricos.
    """
    blocos = []

    for caractere in texto:
        codigo = ord(caractere)

        if codigo >= n:
            raise ValueError(
                f"O caractere '{caractere}' (código {codigo}) não pode ser "
                f"criptografado porque é maior ou igual a N = {n}."
            )

        blocos.append(pow(codigo, e, n))

    return blocos

def descriptografar(blocos, d, n):
    """Descriptografa uma lista de blocos numéricos."""
    caracteres = []

    for bloco in blocos:
        if not 0 <= bloco < n:
            raise ValueError(
                f"O bloco {bloco} é inválido: deve estar entre 0 e {n - 1}."
            )

        caracteres.append(chr(pow(bloco, d, n)))

    return "".join(caracteres)

def main():
    limpar_tela()

    print("=== Criptografia RSA simplificada ===\n")

    p = ler_primo("Digite o número primo P: ")
    q = ler_primo("Digite o número primo Q: ")

    if p == q:
        print("\nErro: P e Q devem ser números primos diferentes.")
        return

    n = p * q
    z = (p - 1) * (q - 1)

    # Escolhe um expoente privado d coprimo com z.
    d = 3

    while math.gcd(d, z) != 1:
        d += 2

    # e é o inverso modular de d em relação a z.
    e = pow(d, -1, z)

    print("\nChaves geradas com sucesso!")
    print(f"P = {p}")
    print(f"Q = {q}")
    print(f"N = P * Q = {n}")
    print(f"Z = (P - 1) * (Q - 1) = {z}")
    print(f"Chave pública (E, N) = ({e}, {n})")
    print(f"Chave privada (D, N) = ({d}, {n})")

    while True:
        print("\n=========================")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("0 - Sair")
        print("=========================")

        try:
            opcao = input("Digite a opção desejada: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nEncerrando o programa...")
            break

        if opcao == "1":
            texto = input("Digite o texto a ser criptografado: ")

            try:
                blocos = criptografar(texto, e, n)
                print("Texto criptografado:")
                print(" ".join(str(bloco) for bloco in blocos))
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            entrada = input(
                "Digite os números a serem descriptografados "
                "(separados por espaço): "
            )

            try:
                blocos = [int(valor) for valor in entrada.split()]
                texto = descriptografar(blocos, d, n)
                print(f'Texto descriptografado: "{texto}"')
            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Digite 1, 2 ou 0.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma encerrado.")
        sys.exit(0)
