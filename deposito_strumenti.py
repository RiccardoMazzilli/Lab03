from operator import attrgetter
from strumento import Strumento
from prestito import Prestito



class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []
        self.prestiti = []


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # Apre il file
        with open(file_path, "r", encoding = "utf-8") as file:
            for riga in file:
                campi = riga.strip().split(",")

                # Estrae i campi
                codice = campi[0]
                tipo = campi[1]
                marca = campi[2]
                anno = campi[3]
                valore = float(campi[4])

                # Crea il nuovo strumento
                strumento = Strumento(
                    codice,
                    tipo,
                    marca,
                    anno,
                    valore
                )
                # Lo inserisce nel deposito
                self.strumenti.append(strumento)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        ultimo_numero = 0
        if len(self.strumenti) > 0:
            pass

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
