import contato

class ContatoEmergencia(contato.Contato):
    
    '''
    Classe que cria contatos de emergencia
    '''
    
    def __init__(self,nome,telefone, datanasc, email, prioridade=True):
        super().__init__(nome,telefone,datanasc,email)
        self._prior = prioridade