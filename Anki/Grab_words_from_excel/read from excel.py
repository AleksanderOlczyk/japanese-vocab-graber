import pandas as pd
pd.set_option('display.max_rows', None)


def wczytaj_komorki_z_excel(plik, arkusz, poczatkowy_wiersz, pierwsza_komorka, druga_komorka):
    try:
        df = pd.read_excel(plik, sheet_name=arkusz, skiprows=poczatkowy_wiersz - 1)
        komorki_B_C = df[[pierwsza_komorka, druga_komorka]]
        komorki_B_C = komorki_B_C.dropna()
        komorki_B_C[druga_komorka] = komorki_B_C[druga_komorka].str.strip()
        komorki_B_C[pierwsza_komorka] = komorki_B_C[pierwsza_komorka].str.strip()
        return komorki_B_C
    except Exception as e:
        print("Wystąpił błąd podczas wczytywania danych z pliku Excel:", e)
        print("Dostępne kolumny w arkuszu:", df.columns)
        return None


plik_excel = 'Słówka　Genki.xlsx'
nazwa_arkusza = '3課'
poczatkowy_wiersz = 3
pierwsza_komorka = 'film'
druga_komorka = 'えいが'
page = 3

komorki_B_C = wczytaj_komorki_z_excel(plik_excel, nazwa_arkusza, poczatkowy_wiersz, pierwsza_komorka, druga_komorka)

if komorki_B_C is not None:
    print("Wczytane komórki z kolumn B i C:")
    print(komorki_B_C.to_string(index=False, justify='left'))
    nazwa_pliku_txt = f'Genki_{page}.txt'
    komorki_B_C.to_csv(nazwa_pliku_txt, index=False, header=None, sep='\t', encoding='utf-8')

    print("Dane zostały zapisane do pliku:", nazwa_pliku_txt)
