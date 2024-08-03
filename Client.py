class Client:
    def __init__(self, n, phone):
        self._name = n
        self._cellphone = phone

    #get
    def get_name(self):
        return self._name

    #set
    def set_name(self, _name):
        self._name = _name
