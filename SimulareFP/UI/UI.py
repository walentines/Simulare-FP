from Service.service import HotelS
from Service.service import sortare_hoteluri

def print_hoteluri(hoteluri):
    '''
    Functie pentru afisarea hotelurilor
    :param hoteluri:
    :return:
    '''
    for hotel in hoteluri:
        print(hotel)

def print_menu():
    '''
    Functie pentru printarea meniului
    :return:
    '''
    print("Afisare hoteluri care au camere disponibile si piscina - afisare")
    print("Inchiriere camera hotel - inchiriere [id]")
    print("Iesire din aplicatie - exit")

class UI:
    def __init__(self):
        self.__hotelS = HotelS("/Users/valentinserban/PycharmProjects/SimulareFP/Data/hotel.txt")

    def afisare_hoteluri_disponibile(self):
        '''
        Afiseaza hotelurile disponibile sortate dupa numarul de stele
        :return:
        '''
        hoteluri = self.__hotelS.afisare_hoteluri_disponibile()
        hoteluri_sortate = sortare_hoteluri(hoteluri)
        print_hoteluri(hoteluri_sortate)

    def inchiriere_hotel(self):
        '''
        Inchiriaza hotelul cu id-ul specificat, iar daca acesta nu exista se printeaza mesajul corespunzator
        Daca nu mai are camere disponibile, se afiseaza hotelurile cu camere disponibile care au acelasi numar de stele ca si cel cu id-ul introdus
        :return:
        '''
        id = input("Introdu ID: ")
        hoteluri = self.__hotelS.inchiriere_hoteluri(id)
        print_hoteluri(hoteluri)
    def run(self):
        '''
        Functie de rulare a UI-ului
        :return:
        '''
        print_menu()
        while True:
            command = input("Introduceti comanda dorita: ")
            if(command == "afisare"):
                self.afisare_hoteluri_disponibile()
            elif(command == "inchiriere"):
                self.inchiriere_hotel()
            elif(command == "exit"):
                break