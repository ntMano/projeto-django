from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Solicitacao
from django.urls import reverse_lazy
# Create your views here.


class SolicitacaoCreateView(CreateView):
    model = Solicitacao
    fields = ['name', 'cpf', 'coren_number',
              'email', 'cel', 'workplace', 'city', 'file']
    template_name = 'Solicitacao/solicitacao_form.html'
    success_url = reverse_lazy('solicitacao_list')


class SolicitacaoListView(ListView):
    model = Solicitacao
    template_name = 'Solicitacao/solicitacao_list.html'

class SolicitacaoUpdateView(UpdateView):
    model = Solicitacao
    fields = ['name', 'cpf', 'coren_number',
              'email', 'cel', 'workplace', 'city', 'file']
    template_name = 'Solicitacao/solicitacao_form.html'
    success_url = reverse_lazy('solicitacao_list')