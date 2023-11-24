import pandas as pd

# LISTA DE PERGUNTAS
questions = [
    ["Qual é o principal objetivo da pedagogia na educação infantil?", "Transmitir conhecimentos avançados", "Desenvolver habilidades de trabalho em equipe", "Promover o desenvolvimento integral da criança", "Preparar as crianças para o mercado de trabalho", 3],
    ["Quais são os pilares da pedagogia na educação infantil?", "Matemática e Ciências", "Leitura e Escrita", "Conhecimento histórico e geográfico", "Desenvolvimento físico, cognitivo, social e emocional", 4],
    ["Qual é o papel do pedagogo na educação infantil?", "Administrar a escola", "Orientar e apoiar o desenvolvimento das crianças", "Ensinar disciplinas específicas", "Cuidar da infraestrutura da escola", 2],
    ["Qual dos seguintes teóricos é frequentemente associado na educação infantil?", "Albert Einstein", "Sigmund Freud", "Maria Montessori", "Isaac Newton", 3],
    ["Por que é importante promover a socialização na educação infantil?", "Para evitar o contato com outras crianças", "Para desenvolver habilidades de comunicação", "Para aumentar o tempo de estudo", "Para afastar as crianças dos pais", 2],
    ["O que significa aprendizado lúdico na educação infantil?", "Aprendizado exclusivamente teórico", "Aprendizado através de jogos e brincadeiras", "Aprendizado baseado apenas em leitura", "Aprendizado físico intensivo", 2],
    ["Qual é o foco principal da avaliação na educação infantil?", "Classificar as crianças em relação às outras", "Identificar erros dos professores", "Avaliar o desenvolvimento individual da criança", "Preparar relatórios para os pais", 3]
]

# Criar Banco de Perguntas
df= pd.DataFrame(questions, columns=["Perguntas", "Opção 1", "Opção 2", "Opção 3", "Opção 4", "Respostas"])

# Salvar no Excel
df.to_excel("questions.xlsx", index=False)

print("Perguntas Salvas Com Sucesso :)")

