import hashlib
import os

def gerar_hash_arquivo(caminho_arquivo):
    """Lê o arquivo .txt e gera o hash SHA-256."""
    sha256_hash = hashlib.sha256()
    try:
        with open(caminho_arquivo, "rb") as f:
            # Lemos em blocos para suportar arquivos de qualquer tamanho
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def main():
    print("=== Validador de Autenticidade SHA-256 ===")
    
    # --- PRIMEIRO ENVIO ---
    caminho1 = input("\nDigite o caminho do PRIMEIRO arquivo (.txt): ").strip()
    # Remove aspas caso o usuário tenha arrastado o arquivo para o terminal
    caminho1 = caminho1.replace('"', '').replace("'", "")
    
    hash1 = gerar_hash_arquivo(caminho1)
    
    if hash1 is None:
        print("Erro: Primeiro arquivo não encontrado.")
        return

    print(f"Hash gerado com sucesso: {hash1}")
    print("-" * 40)

    # --- SEGUNDO ENVIO ---
    print("Agora você pode alterar o arquivo ou selecionar outro para comparar.")
    caminho2 = input("Digite o caminho do SEGUNDO arquivo (ou o mesmo para retestar): ").strip()
    caminho2 = caminho2.replace('"', '').replace("'", "")
    
    hash2 = gerar_hash_arquivo(caminho2)
    
    if hash2 is None:
        print("Erro: Segundo arquivo não encontrado.")
        return

    # --- COMPARAÇÃO ---
    print("\n" + "="*30)
    print(f"Hash 1: {hash1}")
    print(f"Hash 2: {hash2}")
    print("="*30)

    if hash1 == hash2:
        print("✅ RESULTADO: Os arquivos são IDÊNTICOS. Autenticidade confirmada.")
    else:
        print("❌ RESULTADO: Os arquivos são DIFERENTES. O conteúdo foi alterado.")

if __name__ == "__main__":
    main()
