**E-Com Shop**

Konsolowa aplikacja e-commerce napisana w Pythonie, pozwalająca na zarządzanie produktami w magazynie, kontami klientów i składanie prostych zamówień.

Funkcje:

Zarządzanie produktami

Ładowanie i zapisywanie produktów do pliku products.json

Dodawanie nowych produktów (tylko po zalogowaniu jako administrator)

Grupowanie i scalanie duplikatów (sumowanie ilości)

Wyświetlanie listy dostępnych produktów

Rejestracja i logowanie klientów

Tworzenie konta klienta

Logowanie istniejących klientów

Przeglądanie produktów i składanie zamówień

Panel administratora

Logowanie jako administrator

Dodawanie, edytowanie i usuwanie produktów

Przeglądanie zamówień klientów

Struktura **projektu**
📦e_com_shop
 ┣ 📂e-shop
 ┃ ┣ body.py        # Definicja klas: Product, Order, Customer, Admin i globalne listy
 ┃ ┣ functions.py   # Logika menu, logowanie, obsługa interakcji
 ┃ ┣ storage.py     # Funkcje zapisu/odczytu JSON
 ┃ ┗ main.py        # Punkt wejścia aplikacji, inicjalizacja i główna pętla
 ┣ products.json    # Dane produktów (plik JSON generowany przez aplikację)
 ┗ README.md        # Ten plik

 Wymagania

Python 3.7 lub nowszy

Standardowa biblioteka Pythona (brak zewnętrznych zależności)


**Użycie**

Brak produktów

Przy pierwszym uruchomieniu plik products.json może być pusty.

Aplikacja poprosi o zalogowanie jako administrator i dodanie pierwszego produktu.

Menu główne

1. Zaloguj się jako klient

2. Utwórz konto klienta

3. Zaloguj się jako administrator

4. Wyjście

**Panel administratora**

1. Dodaj produkt

2. Pokaż produkty

3. Scal duplikaty w pliku JSON (sumowanie ilości)

4. Wyloguj się

Panel klienta

Przeglądaj dostępne produkty, dodawaj do koszyka, finalizuj zamówienia.