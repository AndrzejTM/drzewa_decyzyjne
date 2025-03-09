import numpy as np

def wczytaj_dane(plik: str):
    # Wczytanie danych z pliku
    # Zakładamy, że dane są oddzielone spacjami lub tabulatorami, a kolumny są rozdzielone wierszami
    dane = np.loadtxt(plik, dtype=str)
    return dane

def liczba_unikalnych_wartosci(dane):
    # Obliczamy liczbę unikalnych wartości dla każdego atrybutu (kolumny)
    unikalne_wartosci = []
    for i in range(dane.shape[1] - 1):  # Ostatnia kolumna to atrybut decyzyjny, więc pomijamy ją
        unikalne_wartosci.append(np.unique(dane[:, i]))
    return unikalne_wartosci

def wystapienia_wartosci(dane):
    # Obliczamy wystąpienia każdej wartości dla każdego atrybutu
    wystapienia = []
    for i in range(dane.shape[1] - 1):  # Ostatnia kolumna to atrybut decyzyjny
        wartosci, liczba = np.unique(dane[:, i], return_counts=True)
        wystapienia.append(dict(zip(wartosci, liczba)))  # Mapowanie wartości do liczby wystąpień
    return wystapienia

# Testowanie funkcji
plik = "tabela_decyzyjna.txt"  # Przykład nazwy pliku
dane = wczytaj_dane(plik)

# Obliczanie liczby unikalnych wartości
unikalne_wartosci = liczba_unikalnych_wartosci(dane)
print("Liczba unikalnych wartości dla każdego atrybutu:")
for idx, unikalne in enumerate(unikalne_wartosci):
    print(f"Atrybut {idx + 1}: {unikalne}")

# Obliczanie wystąpień wartości
wystapienia = wystapienia_wartosci(dane)
print("\nWystąpienia wartości dla każdego atrybutu:")
for idx, wystapienie in enumerate(wystapienia):
    print(f"Atrybut {idx + 1}: {wystapienie}")
