from search import search_prompt

# Mesmo ID em todas as perguntas desta execução do programa = um único histórico.
CHAT_SESSION_ID = "cli"


def main():
    print(
        "Olá, eu sou seu agente de faturamento. Você pode perguntar qual o faturamento "
        "de determinada empresa e eu te respondo. Você também pode perguntar qual a "
        "data de fundação da empresa. Vamos lá.\n"
    )

    while True:
        print("Escolha uma opção:")
        print("  1 - Fazer uma pergunta")
        print("  2 - Sair")
        opcao = input("Opção: ").strip()

        if opcao == "2":
            print("Até logo!")
            break

        if opcao != "1":
            print("Opção inválida. Digite 1 ou 2.\n")
            continue

        pergunta = input("Digite sua pergunta: ").strip()
        if not pergunta:
            print("Você precisa digitar uma pergunta.\n")
            continue

        try:
            resposta = search_prompt(pergunta, session_id=CHAT_SESSION_ID)
            print(f"\n{resposta}\n")
        except Exception as e:
            print(f"Erro: {e}\n")


if __name__ == "__main__":
    main()
