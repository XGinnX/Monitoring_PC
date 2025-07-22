#importando a lib
import customtkinter as ctk

#As funções do aplicativo devem ser criadas antes da interface
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    if usuario=='teste' and senha=='123':
        print('sucesso')
        resultado_login.configure(text='Login feito com sucesso!',
                                  text_color='green')
    else:
        resultado_login.configure(text='Login incorreto',
                                  text_color='red')

#configuração de aparência
ctk.set_appearance_mode('dark')

#criação da janela principal
app = ctk.CTk()
app.title('Sistema de gerenciamento PC')
app.geometry('400x400')

#Criação dos campos
label_usuario = ctk.CTkLabel(app,text='Usuario')
label_usuario.pack(pady=5)
campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite o seu usuário...")
campo_usuario.pack(pady=5)

label_senha = ctk.CTkLabel(app,text='Senha')
label_senha.pack(pady=5)
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha...", show="*")
campo_senha.pack(pady=5)

botao = ctk.CTkButton(app, text='Login', command=validar_login)
botao.pack(pady=10)
resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)
#check_lembrar = ctk.CHECKBUTTON(app)
#Criação das funções de funcionalidades
#inicia o loop da aplicação





app.mainloop()