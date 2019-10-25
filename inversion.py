# Dependency inversion
class Google:
    def component(self):
        pass

class GoogleMaps(Google):
    def component(self):
        return "GoogleMaps"

class GoogleDrive(Google):
    def component(self):
        return "GoogleDrive"

def google_server(element):
    print(element.component())

def main():
    g1 = GoogleMaps()
    g2 = GoogleDrive()
    google_server(g1)
    google_server(g2)

if __name__ == '__main__':
    main()