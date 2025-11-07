import tkinter as tk
from run_tests import tes
from enviar_email import enviar_email
from enviar_email import verificar_email_e_senha
from tkinter import messagebox


def login():

    # Função de login simulada
    def fazer_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        try:
            verificar_email_e_senha(usuario, senha)
            # Ir para a segunda tela
            janela.destroy()
            tela_principal(usuario, senha)

        except:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    # Hover effects para botão
    def on_enter(_):
        botao_login['background'] = '#1a75ff'

    def on_leave(_):
        botao_login['background'] = '#0052cc'

    # Criando janela principal
    janela = tk.Tk()
    janela.title("Tela de Login")
    janela.configure(bg="#e6f2ff")
    janela.resizable(False, False)

    # 📐 Obtém o tamanho da tela e define 70% largura x 60% altura
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    width_percent = 0.4
    height_percent = 0.6
    window_width = int(screen_width * width_percent)
    window_height = int(screen_height * height_percent)
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    janela.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Top frame simula cabeçalho com cor destacada
    top_frame = tk.Frame(janela, bg="#0052cc", height=int(window_height * 0.3))
    top_frame.pack(fill="x")

    titulo = tk.Label(top_frame, text="Bem-vindo", font=("Helvetica", 28, "bold"), fg="white", bg="#0052cc")
    titulo.place(relx=0.5, rely=0.5, anchor="center")

    # Frame de login centralizado
    frame_login = tk.Frame(janela, bg="#ffffff", padx=40, pady=40)
    frame_login.place(relx=0.5, rely=0.55, anchor="center")

    # Campo de usuário
    label_usuario = tk.Label(frame_login, text="Usuário", font=("Helvetica", 13), bg="white")
    label_usuario.pack(anchor="w")
    entry_usuario = tk.Entry(frame_login, font=("Helvetica", 12), width=30, bd=2, relief="groove")
    entry_usuario.pack(pady=5)

    # Campo de senha
    label_senha = tk.Label(frame_login, text="Senha", font=("Helvetica", 13), bg="white")
    label_senha.pack(anchor="w")
    entry_senha = tk.Entry(frame_login, font=("Helvetica", 12), width=30, bd=2, relief="groove", show="*")
    entry_senha.pack(pady=5)

    # Botão de login
    botao_login = tk.Button(frame_login, text="Login", font=("Helvetica", 12, "bold"), bg="#0052cc", fg="white",
                            width=25, height=2, command=fazer_login)
    botao_login.pack(pady=20)
    botao_login.bind("<Enter>", on_enter)
    botao_login.bind("<Leave>", on_leave)

    # Rodapé
    rodape = tk.Label(janela, text="© 2025 Felipe da Silva | Portfólio", bg="#e6f2ff", font=("Helvetica", 9))
    rodape.pack(side="bottom", pady=10)

    janela.mainloop()


def tela_principal(usuario, senha):

    def testar():
        tes()
        enviar_email(usuario, senha)

    # Janela principal
    janela = tk.Tk()
    janela.title("Teste - Simples")
    janela.configure(bg="#e6f2ff")
    janela.resizable(False, False)

    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    window_width = int(screen_width * 0.4)
    window_height = int(screen_height * 0.3)
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    janela.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Topo
    top_frame = tk.Frame(janela, bg="#0052cc", height=int(window_height * 0.3))
    top_frame.pack(fill="x")

    titulo = tk.Label(top_frame, text="Teste de Função", font=("Helvetica", 20, "bold"), fg="white", bg="#0052cc")
    titulo.place(relx=0.5, rely=0.5, anchor="center")

    # Área de conteúdo
    frame_conteudo = tk.Frame(janela, bg="#ffffff", padx=20, pady=20)
    frame_conteudo.place(relx=0.5, rely=0.6, anchor="center")

    # Botão Testar
    btn_testar = tk.Button(frame_conteudo, text="Testar", bg="#0052cc", fg="white",
                           font=("Helvetica", 12, "bold"), width=15, command=testar)
    btn_testar.pack(pady=10)

    # Rodapé
    rodape = tk.Label(janela, text="© 2025 Felipe da Silva | Portfólio", bg="#e6f2ff", font=("Helvetica", 9))
    rodape.pack(side="bottom", pady=10)

    janela.mainloop()

if __name__ == '__main__':
    login()
