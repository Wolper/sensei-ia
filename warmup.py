# Warm-up: mini sistema de perguntas e respostas

qa = {
    "O que é IA?": "É o campo que estuda sistemas capazes de aprender e tomar decisões.",
    "O que é aprendizado de máquina?": "É o uso de algoritmos que aprendem padrões a partir de dados.",
    "Quem criou o Sensei-IA?": "Foi o Dikson, para conduzir um plano de 6 meses de domínio em IA."
}

pergunta = input("Pergunte algo sobre IA: ")
print(qa.get(pergunta, "Ainda não aprendi essa resposta."))
