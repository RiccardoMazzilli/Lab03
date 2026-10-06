

# Definisco la classe Strumento
class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        # Definisco gli attributi
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

        # Per la stampa dell'oggetto
        def __str__(self):
            return (f"{self.codice} - {self.tipo} - {self.marca} - {self.valore:.2f}€")      # Valore con due cifre decimali