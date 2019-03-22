##### System do zapisywania treści stron internetowych w bazie danych:

Program napisany w języku python ver 3.7 z wykorzystaniem frameworku django-rest framework
z zaimplementowanym REST API.

Na dzień dzisiejszy system ma następujące funkcjonalności:

- pobiera treść strony internetowej z podanego adresu url, czyści tekst z tagów i zapisuje czysty tekst w bazie danych

- aktualizuje treści stron całej bazy danych na żądanie, po czym podaje ilość rekordów zaktualizowanych i niezauktualizowanych

- pozwala wyszukiwać treści według adresów stron

- pozwala na usuwanie poszczególnych rekordów


System zostanie rozbudowany o możliwość pobierania plików graficznych.

Chwilowo system działa na sqlite3, ale docelowo zostanie postawiony na postgreSQL