class bankAccount:
    def __init__(self, owner, number, balances):
        self._balances = 0
        self._number = number
        self._owner = owner

    @property
    def balances(self):
        return self._balances

    def get_balances(self):
        return self._balances

    @balances.setter
    def set_balances(self, balances):
        if(balances<0):
            print("The balance cannot be negative")
        else:
            self._balances = balances


    def saque(self, valor):
        if(self._balances>=valor):
            self._balances-=valor
            print("O saque foi realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposita(self, valor):
        self._balances+=valor

    def extrato(self):
        print("Cliente: ", self._owner, "Saldo atual: ", self._balances)