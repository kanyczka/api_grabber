##### System do zapisywania treści stron internetowych w bazie danych:

Program napisany w języku python ver 3.7 z wykorzystaniem frameworku django-rest framework
z zaimplementowanym REST API.

Na dzień dzisiejszy system ma następujące funkcjonalności:

- tworzy tabelę, w której rekordami są teksty ściągnięte z podanych stron internetowych (id, adres strony, czysty tekst, 
data ściągnięcia)

- po podaniu adresu strony wwww, system pobiera treść strony internetowej z podanego url, czyści tekst z tagów i 
zapisuje czysty tekst w bazie danych

- wyświetla wszystkie zapisane rekordy: api/url_texts/
- wyświetla konkretny podany rekord: api/url_txts/id/

- aktualizuje treści stron całej bazy danych na żądanie, po czym podaje ilość rekordów zaktualizowanych i 
niezauktualizowanych: api/url_texts/update_all/
- aktualizuje tekst z konkretnej strony (po podaniu id): api/url_texts/id/update_one/

- pozwala filtrowac rekordy po adresach stron (np rekordy zawierające "onet"): api/url_texts/?url_path=onet

- pozwala wyszukiwać treści po adresach stron: api/url_texts?search=url

- pozwala na usuwanie wybranych rekordów
- 


System zostanie rozbudowany o możliwość pobierania plików graficznych.

Chwilowo system działa na sqlite3, ale docelowo zostanie postawiony na postgreSQL