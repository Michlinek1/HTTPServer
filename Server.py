from http.server import HTTPServer, BaseHTTPRequestHandler

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
    portinput = int(input("Podaj port:"))
    if portinput == 0 or portinput == '':
        print("Spróbuj ponownie!")
        main()
    NazwaPliku = input("Podaj nazwę pliku html:")
    if NazwaPliku == "":
        print("Nazwa pliku nie może być pusta!")
        main()
    port = portinput #port
    plik = NazwaPliku
    serwer = HTTPServer(('', port), handler)
    print(f"Serwer działa na porcie {port}, nazwa pliku: {plik}")
    serwer.serve_forever()
    



    
    
    
if __name__ == '__main__':
    main() 