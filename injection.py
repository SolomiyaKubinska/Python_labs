# Dependency injection example
from dependency_injector import providers, containers
from company import GoogleCompany
from google_servers import GoogleMaps

class Servers(containers.DeclarativeContainer):
    server = providers.Configuration('server')

class Company(containers.DeclarativeContainer):
    google = providers.Singleton(GoogleCompany, Servers.server)

class Data(containers.DeclarativeContainer):
    client_data = providers.Factory(GoogleMaps, data=Company.google)

def main():
    Servers.server.override({
        "name": "GoogleMaps",
        "location": "client_location",
    })
    client_data = Data.client_data()
    print(client_data.get())

if __name__ == '__main__':
    main()