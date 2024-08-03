class Main:
    pass

from Client import Client
from bankAccount import bankAccount

c1 = Client("João", "999999999")
account = bankAccount(c1._name(), 6565)


account.deposita(1000)
account.saque(50)
account.extrato()