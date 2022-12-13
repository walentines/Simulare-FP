from Repository.repo import HotelRepo

def generare_input():
    h = HotelRepo("/Users/valentinserban/PycharmProjects/SimulareFP/Data/hotel.txt")

    return h

def test_build_hotel():
    h = generare_input()
    id = 1
    denumire = "salut"
    numar_stele = 0
    numar_camere_disponibile = 0
    piscina = 1
    hotel = h.build_hotel(id, denumire, numar_stele, numar_camere_disponibile, piscina)
    assert hotel.get_id() == id
    assert hotel.get_piscina() == piscina
    assert hotel.get_denumire() == denumire
    assert hotel.get_numar_stele() == numar_stele
    assert hotel.get_numar_camere_disponibile() == numar_camere_disponibile

def test_load_from_file():
    h = HotelRepo("/Users/valentinserban/PycharmProjects/SimulareFP/Data/fisier_test1.txt")
    id = 1
    denumire = "salut"
    numar_stele = 0
    numar_camere_disponibile = 0
    piscina = 1
    hotel = h.build_hotel(id, denumire, numar_stele, numar_camere_disponibile, piscina)
    hoteluri = h.load_from_file()
    hoteluri_correcte = [hotel]
    assert hoteluri == hoteluri_correcte

def run_tests_repo():
    test_load_from_file()
    test_build_hotel()