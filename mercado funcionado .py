from cgitb import text
from datetime import date
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont

data = date.today()
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']
ano, mes, dia = str(data).split("-")
mes = meses[int(mes) - 1]

for i in meses:
    exec(f"estoque{i}=open(f\"estoque de {i}.txt\",\"a\")")
    exec(f"vendas{i}=open(f\"vendas de {i}.txt\",\"a\")")

janela = Tk()
janela.configure(bg='green yellow')

janela.title("mercado")

janela.geometry('350x200')

data2 = Label(janela, text=f" {dia} {mes} {ano}",bg='green yellow')
data2.grid(column=0, row=0,)
data2.configure(font=tkFont.Font(family='Consolas',size=9))

lbl = Label(janela, text="-MERCADO-",bg='green yellow')
lbl.grid(column=0, row=1,)
lbl.configure(font=tkFont.Font(family='Consolas'))

#estoque = {}
fim = False
produtos = []

nomes = []
precos = []
estoques = []
for i in meses:
    produtos_atual = open(rf'estoque de {i}.txt', 'r').readlines()
    if not not produtos_atual:  # verificar se não está vazia
        for produto in produtos_atual:
            separado = produto.strip().split(':')
            
            if 'produto' in separado:
                nome_produto = separado[1]
                nomes.append(nome_produto)
                
            if 'preço' in separado:
                preco_produto = float(separado[1].replace('R$', ''))
                precos.append(preco_produto)
                
            if 'estoque' in separado:
                estoque_produto = int(separado[1])
                estoques.append(estoque_produto)
                
            estoque = {key: [value1, value2] for key, value1, value2 in zip(nomes, estoques, precos)}


def defestoque():
    global produtos,nomes,precos,estoques,estoque,janela
    
    estoque1 = Tk()
    estoque1.configure(bg='green yellow')

    estoque1.title(" ADD estoque")

    estoque1.geometry('350x200')

    data2 = Label(estoque1, text=f"{dia} {mes} {ano}", bg='green yellow')
    data2.grid(column=0, row=1)

    addestoquejanela = Label(estoque1, text="ADD Estoque",bg='green yellow')
    addestoquejanela.grid(column=1, row=1)

    produto = Label(estoque1, text="PRODUTO",bg='green yellow')
    produto.grid(column=0, row=3, sticky=W, padx=5, pady=5)

    produtoentry = Entry(estoque1)
    produtoentry.grid(column=1, row=3, sticky=E, padx=5, pady=5)

    produtos.append(produtoentry.get())

    quantidade = Label(estoque1, text="QUANTIDADE",bg='green yellow')
    quantidade.grid(column=0, row=4, sticky=E, padx=5, pady=5)
    quantidadeentry = Entry(estoque1)
    quantidadeentry.grid(column=1, row=4, sticky=E, padx=5, pady=5)

    preco = Label(estoque1, text="PREÇO",bg='green yellow')
    preco.grid(column=0, row=5, sticky=E, padx=5, pady=5)
    precoentry = Entry(estoque1)
    precoentry.grid(column=1, row=5, sticky=E, padx=5, pady=5)

    blank1 = Label(estoque1, text="",bg='green yellow')
    blank1.grid(column=0, row=6)
    
    salvarmessage=Label(estoque1, text="")

    def salvarestoque(nome, preco, qtde):
        global estoque,janela,nomes,precos,estoques
               
        estoque[nome.get()] = [qtde.get(), preco.get()]
        for i in meses:
            if i == mes:
                return exec(rf'estoque{i}.write(f"produto:{nome.get()}\npreço: R${preco.get()}\nestoque:{qtde.get()}\n\n")')
            
            salvarmessage.config(text="SALVO !!",bg='green yellow')
            salvarmessage.configure(font=tkFont.Font(family='Consolas'))
            salvarmessage.grid(column=1, row=7)
            
    

    salvar = Button(estoque1, text="Salvar", bg='DarkSeaGreen1',
                    command=lambda: salvarestoque(produtoentry, precoentry, quantidadeentry))

    salvar.grid(column=0, row=7)

    estoque1.mainloop()

btn_estoque = Button(janela, text="ADD Estoque", bg='DarkSeaGreen1', command=defestoque)
btn_estoque.grid(column=0, row=2)


def defvender():
    global produtos,estoque, janela, nomes,precos,estoques
    vender = Tk()
    vender.configure(bg='green yellow')

    vender.title("Vender")
    vender.geometry('350x200')

    vendertitle=Label(vender, text="  Vender", bg='green yellow')
    vendertitle.grid(column=1, row=0)

    data2 = Label(vender, text=f"{dia} {mes} {ano}", bg='green yellow')
    data2.grid(column=0, row=0)

    produto= Label(vender, text=" PRODUTO",bg='green yellow')
    produto.grid(column=0, row=1,sticky=W, padx=5, pady=5)
    produtoentry= Entry(vender)
    produtoentry.grid(column=1, row=1,sticky=E, padx=5, pady=5)

    quantidade=Label(vender, text=" QUANTIDADE",bg='green yellow')
    quantidade.grid(column=0, row=2,sticky=W, padx=5, pady=5)
    quantidadeentry = Entry(vender)
    quantidadeentry.grid(column=1, row=2,sticky=E, padx=5, pady=5)
    
    salvarmessage=Label(vender, text="",bg='green yellow')
                                
    def calcular():
        global precos,estoque,estoques,preco
        print(estoque)
        if not not quantidadeentry.get():
            qtde2 = int(quantidadeentry.get())
            pass
        else:
            return messagebox.showinfo("Mensagem", f'Quantidade/Produto não podem estar vazios!')
      
        for i, j in enumerate(nomes):
            print (precos)
            
            if not not j == produtoentry.get():
                pass
            else:
                messagebox.showinfo("Mensagem", f'{produtoentry.get()}\nnão está no estoque',)
                
                                   
            if qtde2 <= estoques[i]:  # qtde < estoque          
                preco = qtde2 * precos[i]  # preco    
                estoque[j] = [(estoques[i] - qtde2),precos[i]]  
                 
                showpreco=Entry(vender)
                showpreco.grid(column=1,row=4,)
                showpreco.insert(0, str(preco))
                print(estoque)  
                    
                
    blank1 = Label(vender, text="",bg='green yellow')
    blank1.grid(column=0, row=3)
    
    calcularpreco= Button(vender, text="calcular preço",bg='DarkSeaGreen1',command=calcular)
    calcularpreco.grid(column=0,row=4)
    
    blank2 = Label(vender, text="",bg='green yellow')
    blank2.grid(column=0, row=5)
    
    blank3 = Label(vender, text="",bg='green yellow')
    blank3.grid(column=0, row=6)
    
   
    
    salvarmessage=Label(vender, text="",bg='green yellow')
    def salvarvenda(nome,quantidade):
        global quantidadeentry,vender,estoque,preco,qtde,mese,nomes,precos,estoques
            
        for i in meses:
            if i == mes:
                return exec(
                    rf'vendas{i}.write(f"produto:{nome.get()}\nqtde:{quantidade.get()}\n")')
            
            salvarmessage.config(text=f'SALVO!', bg="green yellow")
            salvarmessage.configure(font=tkFont.Font(family='Consolas'))
            salvarmessage.grid(column=1, row=7)
            
    salvar = Button(vender, text="Salvar",bg='DarkSeaGreen1',
                    command=lambda:salvarvenda(produtoentry, quantidadeentry))
    
    salvar.grid(column=0, row=7)

    vender.mainloop()

btn_vender = Button(janela, text="Vender", width=10, height=1, bg='DarkSeaGreen1', command=defvender)
btn_vender.grid(column=0, row=3)

# ============================================================================================================

def defverestoque():
    global meses
    for i in meses:
        with open(rf'C:\Users\User\Desktop\lucas python\LUCAS PYTHON\estoque de {i}.txt', 'r') as f:
            print(str(f.read()).strip())
            
    verestoque=Tk()
    verestoque.configure(bg='green yellow')
    verestoque.title("VER ESTOQUE")
    tamanho = '300x370'
    verestoque.geometry(tamanho)
    verestoquetitle=Label(verestoque, text="VER ESTOQUE", bg='green yellow', fg='black')
    verestoquetitle.grid(column=0, row=1)
    data2 = Label(verestoque, text=f"{dia} {mes} {ano}", bg='green yellow', fg='black')
    data2.grid(column=0, row=0)

    mes_selecionado = StringVar()
    month_cb = ttk.Combobox(verestoque, textvariable=mes_selecionado)
    month_cb['values'] = [mes for mes in meses]
    month_cb.current(meses.index(mes))
    month_cb.grid(row=2, column=0)

    scrollbar = Scrollbar(verestoque)
    scrollbar.grid(row=3, column=1, rowspan=2,  sticky=N+S+W,)
    ver_text = Text(verestoque, height=20, width=35, yscrollcommand=scrollbar.set, bg='DarkSeaGreen1')
    ver_text.grid(row=3, column=0)
    scrollbar.config( command = ver_text.yview )

    
    def mudou(event):
        texto = month_cb.get()
        for i in open(rf'C:\Users\User\Desktop\lucas python\LUCAS PYTHON\estoque de {month_cb.get()}.txt', 'r').readlines():
            ver_text.insert(END, i)
    
    
    month_cb.bind('<<ComboboxSelected>>', mudou)
    verestoque.mainloop()

btn_verestoque = Button(janela, text="Ver estoque", width=10, height=1, bg='DarkSeaGreen1' ,command=defverestoque)
btn_verestoque.grid(column=0, row=4)


# ============================================================================================================


def defvervendas():
    global meses
    for i in meses:
        with open(rf'C:\Users\User\Desktop\lucas python\LUCAS PYTHON\vendas de {i}.txt', 'r') as f:
            print(str(f.read()).strip())
            
    vervendas=Tk()
    vervendas.configure(bg='green yellow')
    vervendas.title("VER VENDAS")
    vervendas.geometry('300x370')
    vervendastitle=Label(vervendas, text="   VER VENDAS",bg='green yellow')
    vervendastitle.grid(column=0, row=1)
    data2 = Label(vervendas, text=f"{dia} {mes} {ano}", bg='green yellow' )
    data2.grid(column=0, row=0)
    
    mes_selecionado = StringVar()
    month_cb = ttk.Combobox(vervendas, textvariable=mes_selecionado)
    month_cb['values'] = [mes for mes in meses]
    month_cb.current(meses.index(mes))
    month_cb.grid(row=2, column=0)
    
    scrollbar = Scrollbar(vervendas)
    scrollbar.grid(row=3, column=1, rowspan=2,  sticky=N+S+W)
    ver_text = Text(vervendas, height=20, width=35, yscrollcommand=scrollbar.set,bg='DarkSeaGreen1')
    ver_text.grid(row=3, column=0)
    scrollbar.config( command = ver_text.yview )
    
    #ver_text = Text(vervendas,height=20, width=43)
    #ver_text.grid(row=3, column=0)
    
    def mudou(event):
        texto = month_cb.get()
        for i in open(rf'C:\Users\User\Desktop\lucas python\LUCAS PYTHON\estoque de {month_cb.get()}.txt', 'r').readlines():
            ver_text.insert(END, i)
    
    
    month_cb.bind('<<ComboboxSelected>>', mudou)

    vervendas.mainloop()

btn_vervendas = Button(janela, text="Ver vendas", width=10, height=1, bg='DarkSeaGreen1', command=defvervendas)
btn_vervendas.grid(column=0, row=5)

def fechar():
    global janela
    messagebox.showinfo("showinfo", "fechando...." )
    janela.quit()
    #lambda:

btn_fechar = Button(janela, text="fechar", width=10, height=1, bg='DarkSeaGreen1' , command=fechar )
btn_fechar.grid(column=0, row=6)

janela.mainloop()
