import pandas as pd
import string

# Wczytanie wszystkich zakładek do jednego dataframe'u
dataframes = []
file_path = "gratka_kielce.xlsx"

xl = pd.read_excel(file_path, sheet_name=None)
for sheet_name, df in xl.items():
    dataframes.append(df)

result = pd.concat(dataframes)


# Usuwanie duplikatów w oparciu o kolumnę "Link do ogłoszenia"
result = result.drop_duplicates(subset='link_ogloszenia')
# Zamiana kolumny "powierzchnia" na format liczbowy
result['Cena'] = pd.to_numeric(result['Cena'], errors='coerce')

result['Powierzchnia'] = result['Powierzchnia'].str.replace(',', '.')
result['Powierzchnia'] = pd.to_numeric(result['Powierzchnia'], errors='coerce')
result['cena_za_metr'] = result['Cena'] / result['Powierzchnia']

# Zamiana polskich znaków na angielskie
translator = str.maketrans("ąćęłńóśźżŚĆŻŹ", "acelnoszzsczz")
result['tytul_ogloszenia'] = result['tytul_ogloszenia'].str.translate(translator)
result['Lokalizacja'] = result['Lokalizacja'].str.translate(translator)

# Zapisanie wyniku do nowego pliku Excel
result.to_csv("baza_danych_kielce_csv.csv", index=False)

