numero = 123
titular = "Gabriel"
saldo = 550.0
limite = 100000.0
conta = {"numero": 123, "titular": "Gabriel", "saldo": 550.0, "limite": 100000.0}
conta["numero"]
conta["saldo"]

conta2 = {"numero": 321, "titular": "Marco", "saldo": 100.0, "limite": 1000.0}

def cria_conta():
    conta2 = {"numero": 321, "titular": "Marco", "saldo": 100.0, "limite": 1000.0}

def cria_conta(numero, titular, saldo, limite):
   conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
   return conta