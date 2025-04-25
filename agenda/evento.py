from contato import Contato
import datetime

class Evento:
    '''
    Classe que cria eventos da agenda telefonica
    '''
    def __init__(self, descricao, data_inicio, data_fim, contato):
        self._descricao = descricao
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._contato = contato
        Evento._total_eventos+=1
    
    def get_informacoes(self):
        return (f"Descrição: {self._descricao}\n"
                f"Período: {self._data_inicio.strftime('%d-%m-%Y')} - "
                f"{self._data_fim.strftime('%d-%m-%Y')}\n"
                f"Contato: {self._contato.nome}")