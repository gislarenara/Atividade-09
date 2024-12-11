import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para a janela de IMC (Índice de Massa Corporal)
def janela_imc():
    def calcular_imc():
        try:
            peso = float(entry_peso.get())
            altura = float(entry_altura.get())
            imc = peso / (altura ** 2)
            messagebox.showinfo("Resultado", f"Seu IMC é: {imc:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

    # Criar a janela do IMC
    imc_window = tk.Toplevel(root)
    imc_window.title("Cálculo do IMC")
    
    tk.Label(imc_window, text="Peso (kg):").pack(pady=5)
    entry_peso = tk.Entry(imc_window)
    entry_peso.pack(pady=5)

    tk.Label(imc_window, text="Altura (m):").pack(pady=5)
    entry_altura = tk.Entry(imc_window)
    entry_altura.pack(pady=5)
    
    btn_calcular = ttk.Button(imc_window, text="Calcular IMC", command=calcular_imc)
    btn_calcular.pack(pady=10)

# Função para a janela de Calculadora
def janela_calculadora():
    def calcular():
        try:
            expression = entry_calculadora.get()
            result = eval(expression)  # Avalia a expressão matemática
            label_resultado.config(text=f"Resultado: {result}")
        except Exception as e:
            label_resultado.config(text="Erro na expressão")

    # Criar a janela da Calculadora
    calc_window = tk.Toplevel(root)
    calc_window.title("Calculadora")
    
    tk.Label(calc_window, text="Digite a expressão:").pack(pady=5)
    entry_calculadora = tk.Entry(calc_window, width=30)
    entry_calculadora.pack(pady=5)

    btn_calcular = ttk.Button(calc_window, text="Calcular", command=calcular)
    btn_calcular.pack(pady=10)
    
    label_resultado = tk.Label(calc_window, text="Resultado: ")
    label_resultado.pack(pady=10)

# Função para a janela de Regra de 3
def janela_regra_3():
    def calcular_regra_3():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            d = (b * c) / a
            messagebox.showinfo("Resultado", f"O valor de d é: {d:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para os números.")

    # Criar a janela da Regra de 3
    regra_window = tk.Toplevel(root)
    regra_window.title("Regra de 3")
    
    tk.Label(regra_window, text="a:").pack(pady=5)
    entry_a = tk.Entry(regra_window)
    entry_a.pack(pady=5)

    tk.Label(regra_window, text="b:").pack(pady=5)
    entry_b = tk.Entry(regra_window)
    entry_b.pack(pady=5)

    tk.Label(regra_window, text="c:").pack(pady=5)
    entry_c = tk.Entry(regra_window)
    entry_c.pack(pady=5)
    
    btn_calcular = ttk.Button(regra_window, text="Calcular", command=calcular_regra_3)
    btn_calcular.pack(pady=10)

# Janela principal
root = tk.Tk()
root.title("Sistema de Cálculos")

# Configurar a janela principal
btn_imc = ttk.Button(root, text="Cálculo do IMC", command=janela_imc)
btn_imc.pack(pady=10)

btn_calculadora = ttk.Button(root, text="Calculadora", command=janela_calculadora)
btn_calculadora.pack(pady=10)

btn_regra_3 = ttk.Button(root, text="Regra de 3", command=janela_regra_3)
btn_regra_3.pack(pady=10)

# Iniciar o loop principal
root.mainloop()
