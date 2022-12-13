from Repository.repo import HotelRepo
from Validators.validator import validate_id

def sortare_hoteluri(hoteluri):
    '''
    Functie pentru sortarea hotelurilor dupa numarul de stele
    :param hoteluri:
    :return: hoteluri_sortate (list)
    '''
    return sorted(hoteluri, key = lambda x: x.get_numar_stele(), reverse = True)

class HotelS:
    def __init__(self, file):
        self.__hotelS = HotelRepo(file)

    def afisare_hoteluri_disponibile(self):
        '''
        Afiseaza hotelurile disponibile care au si piscina
        :return: hoteluri_gasite (list)
        '''
        hoteluri_gasite = list()
        hoteluri = self.__hotelS.load_from_file()
        for hotel in hoteluri:
            if(hotel.get_numar_camere_disponibile() > 0 and hotel.get_piscina() == 1):
                hoteluri_gasite.append(hotel)

        return hoteluri_gasite

    def util_inchiriere_hoteluri(self, hoteluri, id):
        '''
        Functie utila pentru inchiriere (scade numarul de camere disponibile)
        :param hoteluri:
        :param id:
        :return:
        '''
        for hotel in hoteluri:
            if(hotel.get_id() == id):
                hotel.set_numar_camere_disponibile(hotel.get_numar_camere_disponibile() - 1)
        self.__hotelS.save_to_file(hoteluri)

    def inchiriere_hoteluri(self, id):
        '''
        Inchiriaza hotelul cu id-ul specificat, daca acesta nu exista sau nu este disponibil se afiseaza mesajele
        corespunzatoare
        :param id:
        :return: hoteluri_gasite (list)
        '''
        if(not validate_id(id)):
            raise ValueError("Id ul introdus trebuie sa fie un numar natural pozitiv!")
        id = int(id)
        hoteluri = self.__hotelS.load_from_file()
        ok = 0
        hoteluri_gasite = list()
        numar_stele = 0
        for hotel in hoteluri:
            if(hotel.get_id() == id):
                ok = 1
                numar_stele = hotel.get_numar_stele()
                if(hotel.get_numar_camere_disponibile() > 0):
                    hoteluri_gasite.append(hotel)
                    self.util_inchiriere_hoteluri(hoteluri, id)
                    return hoteluri_gasite
        if(not ok):
            print("Hotelul cu id-ul " + str(id) + " nu exista")
            return list()
        print("Ne pare rau. Hotelul nu mai are camere disponibile")
        for hotel in hoteluri:
            if(hotel.get_numar_stele() == numar_stele and hotel.get_numar_camere_disponibile() > 1):
                hoteluri_gasite.append(hotel)

        return hoteluri_gasite
