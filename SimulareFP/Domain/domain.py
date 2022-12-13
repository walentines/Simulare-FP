class Hotel:
    def __init__(self):
        self.__id = -1
        self.__denumire = ""
        self.__numar_stele = 0
        self.__numar_camere_disponibile = -1
        self.__piscina = 0

    def __str__(self):
        '''
        Functie de printare a unui hotel
        :return:
        '''
        if(self.__piscina == 0):
            return "ID: " + str(self.__id) + "\n" + "DENUMIRE: " + self.__denumire + "\n" + "NUMAR_STELE: " + str(self.__numar_stele) + "\n" + "NUMAR CAMERE DISPONIBILE: " + str(self.__numar_camere_disponibile) + "\n" + "PISCINA: " + "False" + "\n"
        else:
            return "ID: " + str(self.__id) + "\n" + "DENUMIRE: " + self.__denumire + "\n" + "NUMAR_STELE: " + str(self.__numar_stele) + "\n" + "NUMAR CAMERE DISPONIBILE: " + str(self.__numar_camere_disponibile) + "\n" + "PISCINA: " + "True" + "\n"

    def __eq__(self, other):
        '''
        Verificare daca doua hoteluri sunt egale
        :param other:
        :return:
        '''
        if(self.__id == other.get_id() and self.__denumire == other.get_denumire() and self.__numar_stele == other.get_numar_stele() and self.__numar_camere_disponibile == other.get_numar_camere_disponibile() and self.__piscina == other.get_piscina()):
            return True
        return False

    def get_id(self):
        '''
        Returneaza id
        :return:
        '''
        return self.__id
    def get_denumire(self):
        '''
        Returneaza denumire
        :return:
        '''
        return self.__denumire
    def get_numar_stele(self):
        '''
        Returneaza numar stele
        :return:
        '''
        return self.__numar_stele
    def get_numar_camere_disponibile(self):
        '''
        Retruneaza numar camere disponibile
        :return:
        '''
        return self.__numar_camere_disponibile
    def get_piscina(self):
        '''
        Returneaza piscina
        :return:
        '''
        return self.__piscina
    def set_id(self, set):
        '''
        Schimba id
        :param set:
        :return:
        '''
        self.__id = set
    def set_denumire(self, set):
        '''
        Schimba denumire
        :param set:
        :return:
        '''
        self.__denumire = set
    def set_numar_stele(self, set):
        '''
        Schimba numar stele
        :param set:
        :return:
        '''
        self.__numar_stele = set
    def set_numar_camere_disponibile(self, set):
        '''
        Schimba numar camere disponibile
        :param set:
        :return:
        '''
        self.__numar_camere_disponibile = set
    def set_piscina(self, set):
        '''
        Schimba piscina
        :param set:
        :return:
        '''
        self.__piscina = set
