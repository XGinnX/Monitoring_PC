#importando a lib
import customtkinter as ctk

#configuração de aparência
ctk.set_appearance_mode('dark')

#criação da janela principal
app = ctk.CTk()
app.title('Sistema de gerenciamento PC')
app.geometry('400x400')

#Criação dos campos
campo_usuario = ctk.CTkLabel(app,text='Usuario')
campo_senha = ctk.CTkLabel(app,text='Senha')
campo_usuario.pack(pady=5)
#check_lembrar = ctk.CHECKBUTTON(app)
#Criação das funções de funcionalidades
#inicia o loop da aplicação





app.mainloop()