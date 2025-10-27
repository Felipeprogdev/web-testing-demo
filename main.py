import tkinter as tk
from run_tests import tes
from enviar_email import enviar_email

def tela_teste():

    def testar():
        tes()
        enviar_email()

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
    tela_teste()
