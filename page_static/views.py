from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Essa é view de teste</h1>')

def contatos(request):
    return HttpResponse('<h1>Faça contato:<h1> <p>Telefone: 21 978583459</p> <p>Email: teste@gmail.com</p>')
