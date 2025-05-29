** **E-Com Shop** **

Konsolowa aplikacja e-commerce napisana w Pythonie, pozwalająca na zarządzanie produktami w magazynie, kontami klientów i składanie prostych zamówień.

**Funkcje:**

1. Zarządzanie produktami
2. Ładowanie i zapisywanie produktów do pliku products.json
3. Dodawanie nowych produktów (tylko po zalogowaniu jako administrator)
4. Grupowanie i scalanie duplikatów (sumowanie ilości)
5. Wyświetlanie listy dostępnych produktów
6. Rejestracja i logowanie klientów
7. Tworzenie konta klienta
8. Logowanie istniejących klientów
9. Przeglądanie produktów i składanie zamówień

**Panel administratora**

1. Logowanie jako administrator
2. Dodawanie, edytowanie i usuwanie produktów
3. Przeglądanie zamówień klientów

**Struktura projektu**

e_com_shop

 ┣ e-shop

 ┣ body.py  
 ┃ ┣ functions.py  
 ┃ ┣ storage.py  
 ┃ ┗ main.py  
 ┣ products.json  
 ┗ README.md

**Wymagania**

- Python 3.7 lub nowszy
- Standardowa biblioteka Pythona (brak zewnętrznych zależności)


**Użycie**

- Brak produktów
    - Przy pierwszym uruchomieniu plik products.json może być pusty.
    - Aplikacja poprosi o zalogowanie jako administrator i dodanie pierwszego produktu.

**Menu główne**

1. Zaloguj się jako klient

2. Utwórz konto klienta

3. Zaloguj się jako administrator

4. Wyjście

**Panel administratora**

1. Dodaj produkt

2. Pokaż produkty

3. Scal duplikaty w pliku JSON (sumowanie ilości)

4. Wyloguj się

**Panel klienta**

Przeglądaj dostępne produkty, dodawaj do koszyka, finalizuj zamówienia.