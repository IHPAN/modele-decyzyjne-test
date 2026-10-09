# modele-decyzyjne-test
Repozytorium na dane i skrypty do testowania modeli decyzyjnych

W folderze `data`: próbka 250 fragmentów haseł SGKP (Słownik Geograficzny Królestwa Polskiego) z przypisaną tematyką, treścią zapytania oraz oceną człowieka, czy treść pasuje do tematyki. Fragmenty zwrócone przez wyszukiwanie semantyczne (model jina-embeddings-3). Dodatkowa warstwa weryfikacyjna w postacji modelu decyzyjnego typu JEV powinna eliminować niepasujące ze znalezionych fragmentów w stopniu zbliżonym do oceny człowieka. 

Wyniki testu (2026-10-09) dla 3 modeli decyzyjnych:

**TEV1:4b**: zgodność z oceną człowieka: 223/250 (**89.2%**)

**BASAL-1.5-4.5b**: zgodność z oceną człowieka: 197/250 (**78.8%**)

**JEV**: zgodność z oceną człowieka: 244/250 (**97.6%**)



Dane i testy przygotowane w ramach projektu „Geografia kulturowo-intelektualna dawnych ziem polskich pod zaborami 1865–1918 – cyfrowe vademecum” prowadzonego w Instytucie Historii Polskiej Akademii Nauk. 

Licencja: Apache-2.0

## Uruchamianie testów

Model otrzymuje wyłącznie zapytanie, nazwę hasła oraz pełny fragment hasła z arkusza. Ocena człowieka
jest zapisywana w raporcie, lecz nie jest przekazywane modelowi.

Dane: `data/modele_decyzyjne_test.xlsx`. 

### Środowisko

Z głównego katalogu tego projektu:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### TEV1 — lokalna Ollama

```bash
python src/evaluate_tev1.py
```

Domyślnie: `tev1:4b`, `http://localhost:11434`.
Usługa Ollama musi działać i mieć zainstalowany model.

### BASAL — basal-serve

```bash
python src/evaluate_basal.py
```

Domyślnie: `http://localhost:8000`. Model jest wybierany przez
`basal-serve`; argument `--model` jest nazwą zapisywaną w raporcie. W teście użyty został basal-1.5-4.5b-GGUF

### JEV — OpenRouter

W pliku `.env` w głównym katalogu tego projektu ustaw
`OPEN_ROUTER_KEY` (wzór w `.env.example`).

```bash
python src/evaluate_jev.py
```

Domyślnie: `typesafe/jev-1.13`. Można jawnie wskazać istniejący plik env w innej lokalizacji:

```bash
python src/evaluate_jev.py --env-file ../sgkp_search/.env
```

### Opcje i kontrola wyników

Każdy skrypt obsługuje `--input` (XLSX lub CSV), `--output` (CSV),
`--limit`, `--threshold`, `--timeout`, `--model`, `--url`,
`--env-file` oraz `--sheet` (tylko XLSX).

```bash
python src/evaluate_tev1.py --limit 5
python src/evaluate_jev.py --input data/modele_decyzyjne_test.csv --threshold 0.5
```

Raport jest zapisywany po każdym przykładzie. Błąd wywołania ma osobny status
i nie jest traktowany jako decyzja „NIE”. Zgodność z człowiekiem dotyczy
poprawnie ocenionych przykładów z etykietą TAK/NIE.
