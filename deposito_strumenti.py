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
                anno = int(campi[3])
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
            ultimo_codice = self.strumenti[-1].codice
            ultimo_numero = int(ultimo_codice[1:])

        nuovo_codice = f"S{ultimo_numero + 1}"
        nuovo_strumento = Strumento(nuovo_codice, tipo, marca, int(anno_acquisto), float(valore))
        self.strumenti.append(nuovo_strumento)
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti, key=attrgetter("marca"))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # Controlla se lo strumento esiste nel deposito
        esiste = False
        for s in self.strumenti:
            if s.codice == id_strumento:
                esiste = True
                break
        if not esiste:
            raise Exception(f"Errore: Strumento {id_strumento} non presente nel deposito")

        # Controlla se lo strumento è già in prestito
        for p in self.prestiti:
            if p.id_strumento == id_strumento:
                raise Exception(f"Errore: Lo strumento {id_strumento} è gia in prestito")

        # Calcola il nuovo codice (es. P1,P2 ecc...)
        ultimo_numero = 0
        if len(self.prestiti) > 0:
            ultimo_codice = self.prestiti[-1].codice
            ultimo_numero = int(ultimo_codice[1:])

        nuovo_codice = f"P{ultimo_numero + 1}"
        prestito = Prestito(
            nuovo_codice,
            data,
            id_strumento,
            cognome_allievo
            )
        self.prestiti.append(prestito)
        return prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""

        for prestito in self.prestiti:
            if prestito.codice == id_prestito:
                self.prestiti.remove(prestito)
                return True

        # Se il ciclo finisce senza trovare prestito, lancia l'eccezione
        raise Exception(f"Errore: Prestito {id_prestito} non trovato")
