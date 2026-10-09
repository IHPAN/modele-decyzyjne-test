# modele-decyzyjne-test
Repozytorium na dane i skrypty do testowania modeli decyzyjnych

W folderze Data: próbka 250 fragmentów haseł SGKP (Słownik Geograficzny Królestwa Polskiego) z przypisaną tematyką, treścią zapytania oraz oceną człowieka, czy treść pasuje do tematyki. Fragmenty zwrócone przez wyszukiwanie semantyczne (model jina-embeddings-3). Dodatkowa warstwa weryfikacyjna w postacji modelu decyzyjnego typu JEV powinna eliminować niepasujące ze znalezionych fragmentów w stopniu zbliżonym do oceny człowieka. 

Wyniki testu dla 3 modeli decyzyjnych:

**TEV1:4b**: zgodność z oceną człowieka: 223/250 (**89.2%**)
**BASAL-1.5-4.5b**: zgodność z oceną człowieka: 197/250 (**78.8%**)
**JEV**: zgodność z oceną człowieka: 244/250 (**97.6%**)

Dane i testy przygotowane w ramach projektu „Geografia kulturowo-intelektualna dawnych ziem polskich pod zaborami 1865–1918 – cyfrowe vademecum” prowadzonego w Instytucie Historii Polskiej Akademii Nauk. 

Licencja: Apache-2.0
