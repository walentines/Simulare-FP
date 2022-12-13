from Repository.repo import HotelRepo

def generare_input():
    h = HotelRepo("/Users/valentinserban/PycharmProjects/SimulareFP/Data/hotel.txt")
    hoteluri = h.load_from_file()

    return hoteluri

def test_getters():
    hoteluri = generare_input()
    correct_id = 1
    assert hoteluri[0].get_id() == correct_id

    correct_denumire = "Hotel Riviera"
    assert hoteluri[0].get_denumire() == correct_denumire

    correct_numar_stele = 5
    assert hoteluri[0].get_numar_stele() == correct_numar_stele

    correct_numar_camere_disponibile = 0
    assert hoteluri[0].get_numar_camere_disponibile() == correct_numar_camere_disponibile

    correct_piscina = 0
    assert hoteluri[0].get_piscina() == correct_piscina

def test_setters():
    hoteluri = generare_input()
    correct_id = 2
    hoteluri[0].set_id(correct_id)
    assert hoteluri[0].get_id() == correct_id

    correct_denumire = "x"
    hoteluri[0].set_denumire(correct_denumire)
    assert hoteluri[0].get_denumire() == correct_denumire

    correct_numar_stele = 0
    hoteluri[0].set_numar_stele(correct_numar_stele)
    assert hoteluri[0].get_numar_stele() == correct_numar_stele

    correct_numar_camere_disponibile = 100
    hoteluri[0].set_numar_camere_disponibile(correct_numar_camere_disponibile)
    assert hoteluri[0].get_numar_camere_disponibile() == correct_numar_camere_disponibile

    correct_piscina = 1
    hoteluri[0].set_piscina(correct_piscina)
    assert hoteluri[0].get_piscina() == correct_piscina

def run_tests_domain():
    test_getters()
    test_setters()