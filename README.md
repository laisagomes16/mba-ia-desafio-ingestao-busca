# Desafio MBA Engenharia de Software com IA - Full Cycle

Descreva abaixo como executar a sua solução.
Passo a passo para executar:

1) Criar seu ambiente virtual e ative no terminal:
-Windows:
comando: python -m venv venv
comando: .\venv\Scripts\Activate.ps1

2) Instalar as dependencias do requirements.txt no terminal
-Windows:
comando: pip install -r requirements.txt

3) Copiar o .env.example e renomear para .env e colocar o valor das variaveis

4) Subir o docker com o banco de dados no terminal
-Windows:
Ter o docker desktop instalado e iniciado
comando: docker composer up -d

5) Executar o script de ingestao de pdf
comando: python src/ingest.py

6) Executar o script do chat
comando: python src/chat.py

7) Esclher a opcao desejada (1 - enviar uma pergunta / 2 - Sair)

8) Digitar a pergunta