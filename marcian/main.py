from ui.airportUI import AirportUI
from application.airportCtrl import AirportController
from infrastructure.airport import Airport



airport = Airport()
ctrl = AirportController(airport)
ui = AirportUI(ctrl)

ui.start()