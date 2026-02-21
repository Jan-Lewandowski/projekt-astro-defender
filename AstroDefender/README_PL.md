# AstroDefender

AstroDefender to gra jednoosobowa stworzona w Pygame, w której gracz wciela się w obrońcę kosmicznej bazy przed nadciągającymi falami 
wrogich statków.

## Jak uruchomić?

Aby uruchomić grę, wykonaj poniższe kroki:

1. **Zainstaluj Python** (wymagana wersja 3.8 lub nowsza). Możesz sprawdzić wersję Pythona, wpisując w terminalu:
   ```sh
   python --version
   ```

2. **Zainstaluj Pygame**, jeśli jeszcze go nie masz:
   ```sh
   pip install pygame
   ```

3. **Sklonuj repozytorium**:
   ```sh
   git clone https://gitlab.com/ug_jn/wst-p-do-programowania-2024/grupa-3-lg/jan-lewandowski.git
   ```

4. **Uruchom grę**:
   ```sh
   python main.py
   ```

## Zasady gry

- Celem gry jest obrona bazy przed atakującymi falami wrogów, których po czasie jest coraz więcej. Gracz ma zadanie uzyskać jak największą liczbę punktów.
- Za każde trafenie gracza przez przeciwnika, gracz traci jedno życie. Każde trafienie meteorytu zabiera trzy życia, a każde trafienie bombą kończy rozgrywkę. Gra kończy się, gdy życia gracza spadną do zera.
- Od poziomu trzeciego zaczynają pojawiać się bonusy, za które możemy zgarnąć trzy punkty. Od poziomu piątego zaczynają pojawiać się serduszka dodające graczowi jeden punkt zdrowia.
- Za każde trafienie przeciwnika gracz otrzymuje jeden punkt.

## Dodatkowo

- Każdy wynik gry zapisuje się w tabeli wyników.
- Gracz ma możliwość wyciszenia/odciszenia muzyki/efektów dźwiękowych w opcjach.

## Sterowanie

- **W/S/A/D (góra/dół/lewo/prawo)** – ruch statku.
- **Spacja** – strzał.
- **P/O** - pauza oraz wznowienie rozgrywki
- **M** - wyciszenie/odciszenie muzyki
- **N** - wyciszenie/odciszenie efektów dźwiękowych