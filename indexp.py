from flask import Flask, render_template, request, flash
import pandas as pd



app = Flask(__name__)
app.secret_key = "907894907894"

produtos = pd.read_csv("ofertar.csv")
produtos['valor'] = produtos['valor'].astype('float')


@app.route('/')
def Home():
    flash("Digite o nome")
    return render_template("index.html")

@app.route('/pedido')  
def Pedido():
    global listas, seucep
    seucep = int(input('digite localidade'))
    listando = ()
    listas = []
    while listando!='':
        listando= input('digite o produto')
        listas.append(listando)
    
    return render_template ('pedido.html', listas=listas)

  


@app.route ("/greet", methods=["POST", "GET"])
def greet():
    totaldiferenca = []
    lista = []
    for merca in listas:
        lista1 = produtos.loc[(produtos.produto == merca)]
        lista2 = produtos.loc[(produtos.cep == seucep)]
        resultado1 = pd.merge(lista1, lista2)
        menor = resultado1.nsmallest(n=1, columns='valor', keep='all')
        maior = resultado1.nlargest(n=1, columns='valor', keep='all')
        print(menor)
        print(maior)
        precomenor1= menor['valor'].min()
        print(precomenor1)
        precomaior1 = maior['valor'].max()
        print(precomaior1)
        diferenca = float(precomaior1 - precomenor1)
        print(diferenca)
        lista.append(menor)
        print(lista[0:-1])
        totaldiferenca.append(diferenca)
        print(totaldiferenca[0:-1])
        totaldif= sum(totaldiferenca[0:-1])
        print(totaldif)
        

    return render_template("lista.html", totaldif=totaldif, lista=lista)
    




if __name__ == "__main__":
    app.run(debug=True) 



