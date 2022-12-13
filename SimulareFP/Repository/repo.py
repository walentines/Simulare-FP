from Domain.domain import Hotel


class HotelRepo:
    def __init__(self, file):
        self.__filename = file

    def build_hotel(self, id, denumire, numar_stele, numar_camere_disponibile, piscina):
        '''
        Construieste un hotel folosind atributele specificate
        :param id:
        :param denumire:
        :param numar_stele:
        :param numar_camere_disponibile:
        :param piscina:
        :return:
        '''
        h = Hotel()
        h.set_id(id)
        h.set_denumire(denumire)
        h.set_piscina(piscina)
        h.set_numar_stele(numar_stele)
        h.set_numar_camere_disponibile(numar_camere_disponibile)

        return h

    def load_from_file(self):
        '''
        Incarca hotelurile dintr un fisier
        :return: hoteluri (list)
        '''
        try:
            f = open(self.__filename, 'r')
        except:
            raise ValueError("Fisierul nu poate fi deschis")
        hoteluri = list()
        lines = f.readlines()
        for line in lines:
            _id, denumire, numar_stele, numar_camere_disponibile, piscina = [word.strip() for word in line.split(',')]
            _id = int(_id)
            numar_stele = int(numar_stele)
            numar_camere_disponibile = int(numar_camere_disponibile)
            # piscina = int(piscina)
            if(piscina == "True"):
                piscina = 1
            elif(piscina == "False"):
                piscina = 0
            h = self.build_hotel(_id, denumire, numar_stele, numar_camere_disponibile, piscina)
            hoteluri.append(h)
        f.close()

        return hoteluri

    def save_to_file(self, hoteluri):
        '''
        Salveaza lista in fisier
        :param hoteluri:
        :return:
        '''
        try:
            f = open(self.__filename, 'w')
        except:
            raise ValueError("Fisierul nu poate fi deschis")
        for hotel in hoteluri:
            if(hotel.get_piscina() == 1):
                f.write(str(hotel.get_id()) + ", " + hotel.get_denumire() + ", " + str(hotel.get_numar_stele()) + ", " + str(hotel.get_numar_camere_disponibile()) + ", " + "True" + "\n")
            elif(hotel.get_piscina() == 0):
                f.write(str(hotel.get_id()) + ", " + hotel.get_denumire() + ", " + str(hotel.get_numar_stele()) + ", " + str(hotel.get_numar_camere_disponibile()) + ", " + "False" + "\n")
        f.close()