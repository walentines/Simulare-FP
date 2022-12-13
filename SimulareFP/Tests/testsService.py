from Service.service import HotelS
from Repository.repo import HotelRepo
from Service.service import sortare_hoteluri
from Domain.domain import Hotel

def generare_input():
    h = HotelS("/Users/valentinserban/PycharmProjects/SimulareFP/Data/hotel.txt")

    return h

def test_afisare_hoteluri_disponibile():
    h = generare_input()
    h_correct = HotelRepo("/Users/valentinserban/PycharmProjects/SimulareFP/Data/fisier_test.txt")
    hoteluri = h.afisare_hoteluri_disponibile()
    hoteluri = sortare_hoteluri(hoteluri)
    hoteluri_corecte = h_correct.load_from_file()
    assert hoteluri == hoteluri_corecte

def test_inchiriere_hotel():
    h = generare_input()
    hotels = HotelRepo("/Users/valentinserban/PycharmProjects/SimulareFP/Data/hotel.txt")
    hotel_prev = hotels.load_from_file()
    hoteluri = h.inchiriere_hoteluri(2)
    hotel_correct = Hotel()
    hotel_correct.set_id(2)
    hotel_correct.set_denumire("Hotel Pascalopol")
    hotel_correct.set_piscina(1)
    hotel_correct.set_numar_stele(4)
    hotel_correct.set_numar_camere_disponibile(19)
    hoteluri_correcte = [hotel_correct]
    hotels.save_to_file(hotel_prev)
    assert hoteluri == hoteluri_correcte
    hoteluri = h.inchiriere_hoteluri(11)
    assert hoteluri == []
    hoteluri = h.inchiriere_hoteluri(4)
    assert hoteluri == []

def run_tests_service():
    test_afisare_hoteluri_disponibile()
    test_inchiriere_hotel()