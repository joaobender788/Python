def sha256_custom(data: bytes) -> str:
    """Implementação pura do algoritmo SHA-256 em Python (Sem hashlib)."""
    
    # 1. Constantes K (Primeiros 32 bits das partes fracionárias das raízes cúbicas dos primeiros 64 primos)
    K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    # 2. Valores iniciais de hash H (Primeiros 32 bits das partes fracionárias das raízes quadradas dos primeiros 8 primos)
    H = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]

    # 3. Funções auxiliares de rotação de bits (Garantindo sempre 32-bits usando o mask & 0xFFFFFFFF)
    def rotr(x, n):
        return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

    # --- ETAPA DE PADDING (PREENCHIMENTO) ---
    orig_len_bits = len(data) * 8
    
    # Adiciona o bit '1' (em formato de byte: 0x80 = 10000000)
    data += b'\x80'
    
    # Adiciona bits '0' até que o tamanho do bloco seja congruente a 448 mod 512
    while (len(data) * 8) % 512 != 448:
        data += b'\x00'
    
    # Adiciona o tamanho original do arquivo como um inteiro de 64 bits (8 bytes) no final
    data += orig_len_bits.to_bytes(8, byteorder='big')

    # --- PROCESSAMENTO DOS BLOCOS DE 512 BITS ---
    for i in range(0, len(data), 64):
        block = data[i:i+64]
        W = [0] * 64
        
        # Divide o bloco de 64 bytes em 16 palavras de 32 bits (4 bytes cada)
        for t in range(16):
            W[t] = int.from_bytes(block[t*4:(t+1)*4], byteorder='big')
            
        # Expande as 16 palavras para 64 palavras (Message Schedule)
        for t in range(16, 64):
            s0 = rotr(W[t-15], 7) ^ rotr(W[t-15], 18) ^ (W[t-15] >> 3)
            s1 = rotr(W[t-2], 17) ^ rotr(W[t-2], 19) ^ (W[t-2] >> 10)
            W[t] = (W[t-16] + s0 + W[t-7] + s1) & 0xFFFFFFFF

        # Inicializa as variáveis de trabalho com os valores do hash anterior
        a, b, c, d, e, f, g, h = H

        # Loop principal de compressão (64 rodadas)
        for t in range(64):
            S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h + S1 + ch + K[t] + W[t]) & 0xFFFFFFFF
            
            S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            # Rotaciona os valores das variáveis
            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        # Adiciona os valores mastigados ao estado atual do Hash H
        H[0] = (H[0] + a) & 0xFFFFFFFF
        H[1] = (H[1] + b) & 0xFFFFFFFF
        H[2] = (H[2] + c) & 0xFFFFFFFF
        H[3] = (H[3] + d) & 0xFFFFFFFF
        H[4] = (H[4] + e) & 0xFFFFFFFF
        H[5] = (H[5] + f) & 0xFFFFFFFF
        H[6] = (H[6] + g) & 0xFFFFFFFF
        H[7] = (H[7] + h) & 0xFFFFFFFF

    # Converte os 8 inteiros de 32 bits finalizados para uma string hexadecimal de 64 caracteres
    return ''.join(f'{x:08x}' for x in H)


def ler_arquivo_completo(caminho_arquivo):
    """Lê o arquivo inteiro em modo binário."""
    try:
        with open(caminho_arquivo, "rb") as f:
            return f.read()
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o caminho.")
        return None
    except PermissionError:
        print("Erro: Sem permissão para acessar o arquivo.")
        return None


def main():
    while True:
        print("\n=== Autenticador SHA-256 ===")
        print("1. Gerar hash de um arquivo")
        print("2. Validar autenticidade de um arquivo (Arquivo + Hash)")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção (1, 2 ou 3): ").strip()

        if opcao == "1":
            caminho = input("Digite o caminho do arquivo (qualquer formato): ").strip()
            caminho = caminho.replace('"', '').replace("'", "")
            
            conteudo = ler_arquivo_completo(caminho)
            if conteudo is not None:
                hash_gerado = sha256_custom(conteudo)
                print("-" * 40)
                print(f"Hash SHA-256 gerado com sucesso:\n{hash_gerado}")
                print("-" * 40)
                
        elif opcao == "2":
            caminho = input("Digite o caminho do arquivo para validação: ").strip()
            caminho = caminho.replace('"', '').replace("'", "")
            
            hash_esperado = input("Digite a chave (hash) SHA-256 original: ").strip().lower()
            
            conteudo = ler_arquivo_completo(caminho)
            if conteudo is not None:
                hash_calculado = sha256_custom(conteudo)
                
                print("\n" + "="*40)
                print(f"Hash Original : {hash_esperado}")
                print(f"Hash Calculado: {hash_calculado}")
                print("="*40)
                
                if hash_calculado == hash_esperado:
                    print("O arquivo é autêntico e não sofreu alterações.")
                else:
                    print("O arquivo é inválido. O conteúdo foi alterado.")
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
