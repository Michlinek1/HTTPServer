from http.server import HTTPServer, BaseHTTPRequestHandler
import glob

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            index = open(plik).read()
            self.send_response(200)
        except:
            index = "blad!"
            self.send_response(404)
        self.send_header('Content-type', 'text/html; charset=UTF-8')
        self.end_headers()
        self.wfile.write(index.encode()) #Encode - zamienia string na bity
        
def main():
    global plik
    htmllista = [f for f in glob.glob("*.html")] #sprawdza plikiw danym folderze o rozszerzeniu .html
    portinput = int(input("Podaj port:"))
    if portinput == 0:
        print("Spróbuj ponownie!")
        main()
    while True:
        print(f"Lista plików: {' '.join(htmllista)}") # .join konwertuje listę do stringa
        NazwaPliku = input("Podaj nazwę pliku html:")
        if NazwaPliku == "":
            print("Nazwa pliku nie może być pusta!")
        elif ".html" not in NazwaPliku:
            print("Nazwa pliku nie ma końcowki .html!")
        elif NazwaPliku not in htmllista:
            pytanie = str(input("Nie istnieje taki plik! Chcesz go stworzyć?"))
            if pytanie == "tak" or pytanie == "Tak":
                f = open(NazwaPliku, "w")
                f.close()
                print("Plik został stworzony!")
                break
        else:
            break
            
    port = portinput #port
    plik = NazwaPliku
    serwer = HTTPServer(('', portinput), handler)
    print(f"Serwer działa na porcie {port}, nazwa pliku: {NazwaPliku}")
    serwer.serve_forever()
    



    
    
    
if __name__ == '__main__':
    main() 
