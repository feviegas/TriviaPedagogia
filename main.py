import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import random
import pandas as pd
import dados
# CARREGA EXCEL
df = pd.read_excel('questions.xlsx')

# IMPORTA AS PERGUNTAS ALEATORIAMENTE
questions = df.sample(n=7).values.tolist()

# VARIÁVEIS GLOBAIS
score = 0
current_question = 0

def check_answer(answer):
    global score, current_question

    if answer == correct_answer:
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        display_result()

def display_question():
    global correct_answer
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    correct_answer = answer  # Define a resposta correta para comparar
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: check_answer(4))

def display_result():
    global score
    messagebox.showinfo("Quiz Finalizado", f"Parabéns! Você Completou o Quiz:\n\nPontuação Final: {score}/{len(questions)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()  # Exibe o botão "Jogar Novamente" no final

def play_again():
    global score, current_question
    score = 0
    current_question = 0
    random.shuffle(questions)
    display_question()
    play_again_btn.pack_forget()

janela = tk.Tk()
janela.title("Quiz")
janela.geometry("400x450")
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"

janela.config(bg=background_color)
janela.option_add('*Font', 'Arial')
app_icon = PhotoImage(file="teste.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

question_label = tk.Label(janela, text="Pergunta", wraplength=380, bg=background_color, fg=text_color, font=("Arial", 25, "bold"))
question_label.pack(pady=10)

option1_btn = tk.Button(janela, text="", width=48, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 20, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text="", width=48, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 20, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text="", width=48, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 20, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela, text="", width=48, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 20, "bold"))
option4_btn.pack(pady=10)

play_again_btn = tk.Button(janela, command=play_again, text="Jogar Novamente", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))
play_again_btn.pack_forget()

display_question()

janela.mainloop()

