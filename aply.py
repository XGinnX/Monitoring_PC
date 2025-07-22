import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Tema opcional
ctk.set_default_color_theme("blue")  # Tema opcional


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("Sensei Hiro App")

        # Criando as páginas (frames)
        self.page1 = Page1(self)
        self.page2 = Page2(self)

        # Mostrando a primeira página
        self.show_page(self.page1)

    def show_page(self, page):
        # Esconde todas as páginas
        self.page1.pack_forget()
        self.page2.pack_forget()

        # Mostra apenas a página solicitada
        page.pack(fill="both", expand=True)


class Page1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = ctk.CTkLabel(self, text="Página 1")
        label.pack(pady=20)

        botao_ir = ctk.CTkButton(self, text="Ir para Página 2",
                                 command=lambda: master.show_page(master.page2))
        botao_ir.pack()


class Page2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = ctk.CTkLabel(self, text="Página 2")
        label.pack(pady=20)

        botao_voltar = ctk.CTkButton(self, text="Voltar para Página 1",
                                     command=lambda: master.show_page(master.page1))
        botao_voltar.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
