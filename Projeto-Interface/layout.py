import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.theme(new_theme="DarkGreen4")
        # Layout
        layout = [
            [sg.Text("Nome", size=(8,0)), sg.Input(size=(15, 0), key="nome")],
            [sg.Text("Sobrenome", size=(8,0)), sg.Input(size=(15,0), key="sobrenome")],
            [sg.Text("Idade", size=(8,0)), sg.Input(size=(15, 0), key="idade")],
            [sg.Text("Qual é o email que você utiliza ?")],
            [sg.Checkbox("Gmail", key="gmail"), sg.Checkbox("Outlook", key="outlook"), sg.Checkbox("Uol", key="uol")],
            [sg.Text("Aceita cartão")],
            [sg.Radio("Sim", "cartoes", key="aceitaCartao"), sg.Radio("Não", "cartoes", key="naoAceitaCartao")],
            [sg.Button("Enviar dados")],
            [sg.Output(size=(30,10))]
        ]
        # Janela
        self.janela = sg.Window("Dados do usuário").layout(layout)
        

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values["nome"]
            sobrenome = self.values["sobrenome"]
            idade = self.values["idade"]
            usuario_gmail = self.values["gmail"]
            usuario_outlook = self.values["outlook"]
            usuario_uol = self.values["uol"]
            aceita_cartao = self.values["aceitaCartao"]
            nao_aceita_cartao = self.values["naoAceitaCartao"]
            print(f"Nome: {nome}")
            print(f"Sobrenome: {sobrenome}")
            print(f"Idade: {idade}")
            print(f"Gmail usuario: {usuario_gmail}")
            print(f"Outlook usuario: {usuario_outlook}")
            print(f"Uol usuario: {usuario_uol}")
            print(f"Aceita cartão: {aceita_cartao}")
            print(f"Não aceita cartão: {nao_aceita_cartao}")


tela = TelaPython()
tela.Iniciar()
