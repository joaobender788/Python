import threading
import base64
import time
from flask import Flask, request, jsonify
import requests
import rsa

app = Flask(__name__)

# --- CONFIGURAÇÃO DA APLICAÇÃO ---
# Perguntar ao usuário quem é este app para definir as portas do Webhook
print("=== CONFIGURAÇÃO DO CHAT ===")
print("1. Iniciar como Aplicação A (Porta 5000 -> Envia para 5001)")
print("2. Iniciar como Aplicação B (Porta 5001 -> Envia para 5000)")
escolha = input("Escolha a opção (1 ou 2): ").strip()

if escolha == "1":
    MINHA_PORTA = 5000
    PORTA_ALVO = 5001
    NOME = "Aplicação A"
else:
    MINHA_PORTA = 5001
    PORTA_ALVO = 5000
    NOME = "Aplicação B"

URL_ALVO = f"http://localhost:{PORTA_ALVO}"

# --- GERANDO AS CHAVES RSA DO APP ---
print(f"\n[Sistema] Gerando chaves RSA de 1024 bits para a {NOME}...")
minha_chave_publica, minha_chave_privada = rsa.newkeys(1024)
chave_publica_parceiro = None
print("[Sistema] Chaves geradas com sucesso!\n")


# --- ROTAS DO WEBHOOK (O Servidor que escuta) ---

@app.route('/receber_chave', methods=['POST'])
def receber_chave():
    """Webhook para receber a chave pública da outra aplicação."""
    global chave_publica_parceiro
    dados = request.json
    # Converte a string PEM recebida de volta para um objeto de Chave Pública RSA
    chave_pem = dados['chave_publica'].encode('utf-8')
    chave_publica_parceiro = rsa.PublicKey.load_pkcs1(chave_pem)
    print(f"\nChave pública do parceiro recebida e salva com sucesso!")
    print("Você já pode enviar mensagens criptografadas.")
    print("Você: ", end="", flush=True)
    return jsonify({"status": "Chave recebida"}), 200


@app.route('/webhook_msg', methods=['POST'])
def webhook_msg():
    """Webhook para receber as mensagens de chat criptografadas."""
    dados = request.json
    # 1. Recebe a mensagem em Base64 (texto seguro para tráfego HTTP)
    msg_criptografada_b64 = dados['mensagem'].encode('utf-8')
    # 2. Decodifica o Base64 para voltar a ser os bytes criptografados originais
    msg_criptografada_bytes = base64.b64decode(msg_criptografada_b64)
    
    # 3. Descriptografa usando a MINHA chave privada
    try:
        msg_descriptografada = rsa.decrypt(msg_criptografada_bytes, minha_chave_privada).decode('utf-8')
        print(f"\n📩 Parceiro: {msg_descriptografada}")
    except rsa.DecryptionError:
        print("\n❌ [Erro] Falha ao descriptografar a mensagem. As chaves não batem.")
        
    print("Você: ", end="", flush=True)
    return jsonify({"status": "Mensagem recebida"}), 200


# --- FUNÇÕES DE ENVIO (O Cliente que transmite) ---

def enviar_minha_chave():
    """Envia a nossa chave pública para o webhook do parceiro."""
    # Exporta a chave pública para o formato de texto PEM
    chave_pem = minha_chave_publica.save_pkcs1().decode('utf-8')
    try:
        requests.post(f"{URL_ALVO}/receber_chave", json={"chave_publica": chave_pem})
        print("Sistema. Sua chave pública foi enviada ao parceiro.")
    except requests.exceptions.ConnectionError:
        print("Erro. Não foi possível conectar ao parceiro. Ele está online?")


def enviar_mensagem(texto):
    """Criptografa a mensagem com a chave do parceiro e envia por Webhook."""
    global chave_publica_parceiro
    if not chave_publica_parceiro:
        print("Aviso. Você não tem a chave pública do parceiro. Digite '1' para negociar as chaves primeiro.")
        return

    # 1. Criptografa a string usando a chave pública do parceiro
    msg_criptografada = rsa.encrypt(texto.encode('utf-8'), chave_publica_parceiro)
    # 2. Transforma em Base64 para enviar como texto puro no JSON do HTTP POST
    msg_b64 = base64.b64encode(msg_criptografada).decode('utf-8')

    try:
        requests.post(f"{URL_ALVO}/webhook_msg", json={"mensagem": msg_b64})
    except requests.exceptions.ConnectionError:
        print("Erro. Falha ao entregar o Webhook. O parceiro desconectou.")


def interface_usuario():
    """Thread dedicada para capturar o input do terminal sem travar o Flask."""
    time.sleep(1.5) # Aguarda o Flask inicializar na tela
    print("\n" + "="*40)
    print(" COMANDOS DO CHAT:")
    print(" Digite '1' -> Para ENVIAR sua chave pública (Negociar)")
    print(" Digite qualquer outra coisa -> Envia como mensagem")
    print("="*40 + "\n")
    
    while True:
        opcao = input("Você: ").strip()
        if not opcao:
            continue
        if opcao == "1":
            enviar_minha_chave()
        else:
            enviar_mensagem(opcao)


if __name__ == '__main__':
    # Criamos uma thread de background para o usuário digitar, senão o app.run() trava o terminal
    threading.Thread(target=interface_usuario, daemon=True).start()
    
    # Desativamos o reloader e o modo debug para o Flask não duplicar a thread de input
    app.run(port=MINHA_PORTA, debug=False, use_reloader=False)
