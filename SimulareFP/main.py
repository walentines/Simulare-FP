from UI.UI import UI
from Tests.testsDomain import run_tests_domain
from Tests.testsRepo import run_tests_repo
from Tests.testsService import run_tests_service

def start():
    ui = UI()
    ui.run()

run_tests_domain()
run_tests_repo()
run_tests_service()
start()