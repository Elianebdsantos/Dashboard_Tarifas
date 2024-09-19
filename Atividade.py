
#pip install dash
#pip install pandas
#pip install openpyxl


#Estrutura dentro de um dashboard
#Layout -> tudo que vi ser visualizado
#Callbacks -> Funcionalidades que voce tera no dash

from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel("Tarifas.xlsx")
#Esta linha lê o arquivo Excel e armazena os dados em uma variavel chamada df

fig = px.bar(df, x="Tipo de Serviço", y="Valor", color="ID Canal", barmode="group")
#Esta linha cria uma linha contendo os valores unicos da coluna
opcoes = list(df['ID Canal'].unique())
# esta linha adiciona a string "Todas as logjas ao final da lista de opções"
opcoes.append("Todos os Canais")

app.layout = html.Div(children=[
    html.H1(children='Valores Cestas'),
    html.H2(children='Gráfico com os valores dos serviços envolvendo Cesta de Serviços'),
    dcc.Dropdown(opcoes, value='Todos os Canais', id='lista_canais'),

    dcc.Graph(
        id='grafico_quantidade_Tipo_de_serviço',
        figure=fig
    )

])
# utilizado para mudar a interface cada vez que o usuário selecionar algo diferente
@app.callback(
    Output('grafico_quantidade_Tipo_de_serviço','figure'), #é uma função para atualização do gráfico
    Input('lista_canais','value')
)

def update_output(value):
    if value == "Todos os Canais":
        fig = px.bar(df, x="Tipo de Serviço",y="Valor", color= "ID Canal", barmode="group")
    else: 
        tabela_filtrada= df.loc[df['ID Canal'] == value, :]
        fig = px.bar(tabela_filtrada, x="Tipo de Serviço",y="Valor", color= "ID Canal", barmode="group")

    return fig

if __name__ == '__main__':
    app.run(debug=True)
