# Dependency injection example
from dependency_injector import providers, containers
import company
import google_servers

class GoogleServer(containers.DeclarativeContainer):
    calendar = providers.Factory(google_servers.GoogleCalendar)
    drive = providers.Factory(google_servers.GoogleDrive)
    sheet = providers.Factory(google_servers.GoogleSheet)
    maps = providers.Factory(google_servers.GoogleMaps)

class GoogleCompany(containers.DeclarativeContainer):
    calendar = providers.Factory(company.GoogleServers, server=GoogleServer.calendar)
    drive = providers.Factory(company.GoogleServers, server=GoogleServer.drive)
    sheet = providers.Factory(company.GoogleServers, server=GoogleServer.sheet)
    maps = providers.Factory(company.GoogleServers, server=GoogleServer.maps)

if __name__ == '__main__':
    calendar = GoogleCompany.calendar()
    drive = GoogleCompany.drive()
    sheet = GoogleCompany.sheet()
    maps = GoogleCompany.maps()