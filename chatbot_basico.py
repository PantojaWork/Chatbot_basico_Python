import random

def generate_response(user_input):
    # Lista de respostas possíveis
    responses = [
        "Eu estou bem, obrigado.",
        "O que posso fazer por você?",
        "O tempo está bom hoje."
    ]

    # Gera uma resposta aleatória
    return random.choice(responses)

def main():
    # Inicia o chatbot
    print("Bem-vindo ao chatbot!")

    # Loop principal
    while True:
        # Obtém a entrada do usuário
        user_input = input("O que posso fazer por você? ")

        # Gera uma resposta
        response = generate_response(user_input)

        # Imprime a resposta
        print(response)

if __name__ == "__main__":
    main()
