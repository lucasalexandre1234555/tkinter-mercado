from datetime import date
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

data = date.today()
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']
ano, mes, dia = str(data).split("-")
mes = meses[int(mes) - 1]

for i in meses:
    exec(f"estoque{i}=open(f\"estoque de {i}.txt\",\"a\")")
    exec(f"vendas{i}=open(f\"vendas de {i}.txt\",\"a\")")

janela = Tk()

janela.title("mercado")

janela.geometry('350x200')

data2 = Label(janela, text=f"{dia} {mes} {ano}")
data2.grid(column=0, row=0)

lbl = Label(janela, text="-MERCADO-")
lbl.grid(column=0, row=1)

estoque = {}
fim = False
produtos = []

def salvarestoque(nome, qtde, preco):
    global estoque
    global janela
    estoque[nome.get()] = [qtde.get(), preco.get()]
    for i in meses:
        if i == mes:
            return exec(rf'estoque{i}.write(f"produto:{nome.get()}\npreço: R${preco.get()}\nestoque:{qtde.get()}\n\n")')



def defestoque():
    global produtos
    global estoque
    global janela
    estoque1 = Tk()

    estoque1.title(" ADD estoque")

    estoque1.geometry('350x200')

    data2 = Label(estoque1, text=f"{dia} {mes} {ano}", )
    data2.grid(column=0, row=1)

    addestoquejanela = Label(estoque1, text="ADD Estoque")
    addestoquejanela.grid(column=1, row=1)

    produto = Label(estoque1, text="PRODUTO")
    produto.grid(column=0, row=3, sticky=W, padx=5, pady=5)

    produtoentry = Entry(estoque1)
    produtoentry.grid(column=1, row=3, sticky=E, padx=5, pady=5)

    produtos.append(produtoentry.get())

    quantidade = Label(estoque1, text="QUANTIDADE")
    quantidade.grid(column=0, row=4, sticky=E, padx=5, pady=5)
    quantidadeentry = Entry(estoque1)
    quantidadeentry.grid(column=1, row=4, sticky=E, padx=5, pady=5)

    preco = Label(estoque1, text="PREÇO")
    preco.grid(column=0, row=5, sticky=E, padx=5, pady=5)
    precoentry = Entry(estoque1)
    precoentry.grid(column=1, row=5, sticky=E, padx=5, pady=5)

    blank1 = Label(estoque1, text="")
    blank1.grid(column=0, row=6)

    salvar = Button(estoque1, text="Salvar",
                    command=lambda: salvarestoque(produtoentry, precoentry, quantidadeentry))

    salvar.grid(column=0, row=7)

    estoque1.mainloop()


btn_estoque = Button(janela, text="ADD Estoque",command=defestoque)
btn_estoque.grid(column=0, row=2)



def defvender():
    global produtos
    global estoque
    global janela
    vender = Tk()

    vender.title("Vender")
    vender.geometry('350x200')

    vendertitle=Label(vender, text="  Vender")
    vendertitle.grid(column=1, row=0)

    data2 = Label(vender, text=f"{dia} {mes} {ano}", )
    data2.grid(column=0, row=0)

    produto= Label(vender, text=" PRODUTO")
    produto.grid(column=0, row=1,sticky=W, padx=5, pady=5)
    produtoentry= Entry(vender)
    produtoentry.grid(column=1, row=1,sticky=E, padx=5, pady=5)

    quantidade=Label(vender, text=" QUANTIDADE")
    quantidade.grid(column=0, row=2,sticky=W, padx=5, pady=5)
    quantidadeentry = Entry(vender)
    quantidadeentry.grid(column=1, row=2,sticky=E, padx=5, pady=5)

    blank1 = Label(vender, text="")
    blank1.grid(column=0, row=3)

    def salvarvenda(nome, quantidade):
        global quantidadeentry

        #quantidade <= estoque[produto][0]:  # qtde < estoque
        preco = quantidade * estoque[produto][1]  # preco
        estoque[produto][0] = estoque[produto][0] - quantidade
        for i in meses:
            if i == mes:
                return exec(
                    rf'vendas{i}.write(f"produto:{nome.get()}\nvalor: R${preco.get()}\nestoque:{quantidade.get()}\n\n")')

    salvar = Button(vender, text="Salvar",
                    command=lambda: salvarvenda(produtoentry, quantidadeentry))

    salvar.grid(column=0, row=4)

    vender.mainloop()

btn_vender = Button(janela, text="Vender", width=10, height=1, command=defvender)
btn_vender.grid(column=0, row=3)

btn_verestoque = Button(janela, text="Ver estoque", width=10, height=1)
btn_verestoque.grid(column=0, row=4)

btn_vervendas = Button(janela, text="Ver vendas", width=10, height=1)
btn_vervendas.grid(column=0, row=5)

btn_fechar = Button(janela, text="fechar", width=10, height=1, command=lambda: janela.quit())
btn_fechar.grid(column=0, row=6)

janela.mainloop()
