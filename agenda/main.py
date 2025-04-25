from contato import Contato
from evento import Evento
import datetime

# Mensagem de boas-vindas
print("Bem vindo a agenda telefonica")

# Criando contatos
contato1 = Contato(
    nome="Adam Smith",
    telefone="61 999999999",
    datanasc=datetime.date(2000, 9, 12),
    email="joao@gmail.com"
)

contato2 = Contato()
contato2.nome = "Maria Rocha"
contato2.telefone = "61 988888888"
contato2.datanasc = datetime.date(2002, 8, 12)
contato2.email = "maria@gmail.com"

# Criando um evento
evento1 = Evento(
    descricao="Avaliação n1",
    data_inicio=datetime.date(2025, 5, 9),
    data_fim=datetime.date(2025, 5, 9),
    contato=contato1
)

# Exibindo informações
print("\nInformações do Evento:")
print(evento1.get_informacoes())