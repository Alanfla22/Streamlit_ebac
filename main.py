import time
import flet as ft
import spacy
import random
import os

nlp = spacy.load('es_core_news_sm')
app_data_path = os.getenv("FLET_APP_STORAGE_DATA")
my_file_path = os.path.join(app_data_path, "data.txt")

# função de atualização da lista
def atualizar_lista():
  
  arquivo = open(my_file_path, 'r')
  lista_frase = arquivo.readlines()
  frase = lista_frase[0]
  lista_frase.remove(frase)
  lista_frase.append(frase)
  with open(my_file_path, 'w') as novo_arquivo:
    for i in lista_frase:
      novo_arquivo.writelines(i)

# função tokenização
def tokenizacao(frase):
  doc = nlp(frase)
  tokens = [token.text.casefold() for token in doc]
  random.shuffle(tokens)
  for i in (['.', '\n', '?', '¿', ',', '¡', '!']):
    if i in tokens:
      tokens.remove(i)
  vocabulos = ''
  for token in tokens:
    vocabulos += token + ' '
  return vocabulos        

# PÁGINA PRINCIPAL
def main(page: ft.Page):

  page.adaptive = True
  page.platform = ft.PagePlatform.ANDROID
  page.update()
  frase = open(my_file_path, 'r').readlines()[0]
  vocabulos = tokenizacao(frase)

  a = ft.Container(
      content=ft.Text(value=vocabulos, color="red"),
      width=150,
      height=50,
      bgcolor="yellow",
      border_radius=10,
      )  

  def revel(e):
    frase = open(my_file_path, 'r').readlines()[0]
    c.content = ft.Text(value=frase, color="green")
    c.update()

  c = ft.Container(
      content=ft.Text(value='frase', color="green"),
      width=150,
      height=150,
      bgcolor="blue",
      border_radius=10,
      on_click=revel
      )
  
  def atualizar(e):
    atualizar_lista()
    frase = open(my_file_path, 'r').readlines()[0]
    vocabulos = tokenizacao(frase)
    a.content = ft.Text(value=vocabulos, color="red")
    c.content=ft.Text(value='frase', color="red")
    page.update()        

  b = ft.TextButton("Próxima", on_click=atualizar)
  page.add(a, c, b)

ft.app(main)
