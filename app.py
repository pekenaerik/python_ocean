from flask import Flask , g#importa o Flask#
import sqlite3

DATABASE = "blog.bd"
SECRET_KEY = "pudim"

app = Flask(__name__) #cria variavel e atribuir a ele a aplicacao#
app.config.from_object(__name__) #diz para o flask da onde ele tem que tirar as configuracoes do objeto#

def conectar_bd():#funcao q conecta com o banco chama a bb do python e manda conectar#
    return sqlite3.connect(DATABASE)

@app.before_request#abrir a requisição antes da execução do app#
def antes_requisicao():
    g.bd = conectar_bd()

@app.teardown_request #terminar a requisicao g é um objeto(achar depois sobre) exc é excessao#
def fim_requisicao(exc):
    g.bd.close()


@app.route('/') #criando as rotas#
def exibir_entradas(): #pega os dados do banco e armazena em cur#
    sql = "SELECT titulo, texto FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []#lista de python onde ficará os dados do banco
    return str(entradas)