from tkinter import *
import pyodbc

#pip install pyodbc

windows = Tk()

class aplicacao():
	def __init__(self):
		self.windows = windows
		windows.iconphoto(False, PhotoImage(file='icon.png'))
		self.configuraTela(windows)
		self.criaElementosTelaInicial()
		self.posicionaElementosTelaInicial()
		
		#------------------------------
		windows.mainloop()
		


	def retornar_conexao_sql(self):
		server = "localhost\KAPTUREALL"
		database = "cadastro"
		username = "sa"
		password = "K4ptur34ll"
		#string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
		string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
		self.conexao = pyodbc.connect(string_conexao)
		return self.conexao.cursor()


	def configuraTela(self,tk):
		tk.title("Cadastro")
		tk.geometry('500x300')
		tk.configure(background='#84b4c2')
		#tk.iconphoto(False, PhotoImage(file='icon.png'))
		tk.resizable(width=False, height=False)


# ------------------------------------
  #Tela Inicial

	def criaElementosTelaInicial(self):
		self.frameS = Frame(self.windows, bd=4, bg='#BEBEBE', highlightbackground='black', highlightthickness=3)
		self.botaoArmazenar = Button(self.frameS, width=12, height=3, text="Armazenar",  fg='white', bd=2, bg='#66aabd', relief=FLAT, font = ('Segoe UI', 12, 'bold'), command=self.TelaCadastrar)
		self.botaoRecuperar = Button(self.frameS, width=12, height=3, text="Recuperar",  fg='white', bg='#66aabd', relief=FLAT, font = ('Segoe UI', 12, 'bold'), command=self.TelaRecuperar)
		#self.labelTitulo = Label(self.frameS, text = "Cadastro", fg='white', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))

	def posicionaElementosTelaInicial(self):
		self.frameS.place(x= 10, y=10, width= 475, height= 135)
		self.botaoArmazenar.place(x=40, y=30)
		self.botaoRecuperar.place(x=210, y=30)
		#self.labelTitulo.place(x=150, y=3)


#-------------------------------------------------
  #Telas Auxiliares

	def TelaCadastrar(self):
		telaCadastro = Tk()
		self.telaCadastro = telaCadastro   
		self.configuraTela(telaCadastro)
		self.frameCad = Frame(self.telaCadastro,  bd=4, bg='#BEBEBE', highlightbackground='black', highlightthickness=3)
		self.frameCad.place(x= 10, y=10, width= 475, height= 280)

		self.labelEndereco = Label(self.frameCad, text="Endereço", fg='white', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))
		self.labelEndereco.place(x=10, y=10)

		self.EnderecoCad = Entry(self.frameCad)
		self.EnderecoCad.place(x= 10, y=40, width= 120, height= 20)

		self.labelInformacoes = Label(self.frameCad, text="informações", fg='white', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))
		self.labelInformacoes.place(x=10, y=70)

		self.InformacoesCad = Entry(self.frameCad)
		self.InformacoesCad.place(x= 10, y=100, width= 150, height= 30)

		self.botaoSalvar = Button(self.frameCad, width=7, height=1, text="Salvar",  fg='white', bd=2, bg='#66aabd', relief=FLAT,command=self.InserirDados, font = ('Segoe UI', 12, 'bold'))
		self.botaoSalvar.place(x=30, y=150)

		self.botaoLimpa = Button(self.frameCad, width=7, height=1, text="Limpa",  fg='white', bd=2, bg='#66aabd', relief=FLAT, command=self.LimpaTela, font = ('Segoe UI', 12, 'bold'))
		self.botaoLimpa.place(x=150, y=150)

		self.botaoVoltar = Button(self.frameCad, width=7, height=1, text="Voltar",  fg='white', bd=2, bg='#66aabd',command=telaCadastro.destroy, relief=FLAT, font = ('Segoe UI', 12, 'bold'))
		self.botaoVoltar.place(x=270, y=150)

		telaCadastro.mainloop()



	def LimpaTela(self):
		self.EnderecoCad.delete(0, END)
		self.InformacoesCad.delete(0, END)



	def InserirDados(self):
		self.cursor = self.retornar_conexao_sql()
		Endereco = self.EnderecoCad.get()
		Informacoes = self.InformacoesCad.get()
		
		#insert into tbl_dados(id_numero, informacao) values(CONVERT (int,'50'),'teste50')
		camposConcatenados = str('CONVERT (int,'+"'"+Endereco+"'),'"+Informacoes+"'")

		#camposConcatenados = str(Endereco+','+"'"+Informacoes+"'")

		#cursor.execute('insert into tbl_dados(id_numero, informacao) values('+Endereco+','+Informacoes+')')
		
		try:
			rows = self.cursor.execute(str('insert into tbl_dados(id_numero, informacao) values('+camposConcatenados+')')).rowcount
			self.conexao.commit()
			self.Retorno = Label(self.frameCad, text='dados inseridos com sucesso !', fg='green', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))
			self.Retorno.place(x=110, y=200)
		except:
			self.Retorno = Label(self.frameCad, text='Erro ao inserir os dados!', fg='red', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))
			self.Retorno.place(x=110, y=200)

#--------------------------------------
# Tela Recuperar

	def TelaRecuperar(self):
		telaRecuperar = Tk()
		self.telaRecuperar = telaRecuperar
		self.configuraTela(telaRecuperar)

		self.frameRec = Frame(self.telaRecuperar,  bd=4, bg='#BEBEBE', highlightbackground='black', highlightthickness=3)
		self.frameRec.place(x= 10, y=10, width= 475, height= 280)

		self.labelEndereco = Label(self.frameRec, text="Endereço", fg='white', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))
		self.labelEndereco.place(x=10, y=10)

		self.EnderecoRec = Entry(self.frameRec)
		self.EnderecoRec.place(x= 10, y=40, width= 160, height= 35)

		self.botaoRec = Button(self.frameRec, width=7, height=1, text="Recuperar",  fg='white', bd=2, bg='#66aabd', relief=FLAT, command=self.ConsultarBancoDeDados, font = ('Segoe UI', 12, 'bold'))
		self.botaoRec.place(x= 180, y=40,)

		self.botaoVoltar = Button(self.frameRec, width=7, height=1, text="Voltar",  fg='white', bd=2, bg='#66aabd', relief=FLAT,command=telaRecuperar.destroy, font = ('Segoe UI', 12, 'bold'))
		self.botaoVoltar.place(x=280, y=40,)

		self.Resultado = Label(self.frameRec, text='Resultado:', fg='black', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))
		self.Resultado.place(x=9, y=100)

		telaRecuperar.mainloop()

	def ConsultarBancoDeDados(self):
		cursor = self.retornar_conexao_sql()
		numero = self.EnderecoRec.get()
		cursor.execute('select informacao from tbl_dados where id_numero = ' + numero)
		rows = cursor.fetchall()
		retorno = rows


		if (retorno):
			self.Retorno = Label(self.frameRec, text=retorno, fg='green', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))
			self.Retorno.place(x=100, y=100)
		else:
			self.Retorno = Label(self.frameRec, text='Erro', fg='red', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))
			self.Retorno.place(x=100, y=100)



aplicacao()























#self.Botao2 = Button(self.frame3, text='Clique nesse botão para voltar.', command=self.reverter, bg='darkgray')













	#	self.labelTeste = Label(self.frameRec, text=str(self.EnderecoRec.get()), fg='white', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))
	#	self.labelTeste.place(x=100, y=10)












				# fg = color da letra, bd = tamanho dorda, relief = estilo, bg = cor de fundo
		#self.frameS.place(relx= 0.02 , rely=0.02, relwidth= 0.96,relheight= 0.45)










	#	valor = self.EnderecoRec.get()
		#self.labelErro = Label(self.frameRec, text=valor, fg='white', bg='#BEBEBE', font = ('Segoe UI', 12, 'bold'))
	#	self.labelErro.place(x=200, y=200)












	#	botaoArmazenar = Button(windows, width=12, height=3, text="Armazenar",  fg='#403e47', bg='#66aabd', relief=FLAT)
		#botaoArmazenar.place(x=40, y=20)

	#	botaoRecuperar = Button(windows, width=12, height=3, text="Recuperar",  fg='#403e47', bg='#66aabd', relief=FLAT)
	#	botaoRecuperar.place(x=210, y=20)