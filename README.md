# Project-AmstelHaege

## Introductie
Na jarenlang getouwtrek is de knoop eindelijk doorgehakt: er komt een nieuwe woonwijk in de Duivendrechtse polder, net ten noorden van Ouderkerk aan de Amstel. De huisjes zijn bedoeld voor het midden- en bovensegment van de markt, met name expats en hoogopgeleide werknemers actief op de Amsterdamse Zuidas.

Omdat de Duivenderechtse polder ooit beschermd natuurgebied was, is de compromis dat er alleen lage vrijstaande woningen komen, om zo toch het landelijk karakter te behouden. Dit, gecombineerd met een aantal strenge restricties ten aanzien van woningaanbod en het oppervlaktewater, maakt het een planologisch uitdagende klus. De gemeente overweegt drie varianten: de 20-huizenvariant, de 40-huizenvariant en de 60-huizenvariant. Er wordt aangenomen dat een huis meer waard wordt naarmate de vrijstand toeneemt, de rekenpercentages zijn per huistype vastgesteld.

Wij als **D-Place** zijn aangewezen door de gemeente om de wijk in te richten. Wij zullen voor de drie verschillende mappen een 20, 40 en 60-huizenvariant opleveren. Voor alle drie de mappen zijn er vaste restricites.

### Restricties
* De wijk bestaat voor 60% uit eengezinswoningen, 25% uit bungalows en 15% uit maisons.
* Huizen in de wijk overlappen niet met elkaar, waarbij ze wel verplichte vrijstand mogen delen.
* Huizen vallen niet buiten de map van 160x180 meter, waarbij de verplichte vrijstand van de huizen binnen de map moet vallen en de extra vrijstand wel buiten de map of in water kan vallen.

## Installatie

Dit project is geschreven in **Python 3.7**.
In *requirements.txt* staan de packages om de code te runnen.
Deze packages zijn te installeren door het runnen van het volgende commando:
```
pip3 install -r requirements.txt
```

## Versies
* Python 3.7.1 
* Matplotlib 3.0.2
* GitHub

## Gebruik

De code wordt uitgevoerd door het runnen van het volgende commando:
```
python main.py
```
Vervolgens wordt de gebruiker gevraagd of hij/zij **20/40/60** huizen wilt plaatsen. Daarna kan de gebruiker een keuze maken tussen de drie verschillende mappen en welk algoritme hij/zij wilt gebruiken.

Overzicht van de drie mappen: <br>

<img src="https://user-images.githubusercontent.com/46574470/72994312-2c706000-3df7-11ea-9711-d6041dcdca46.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/46574470/72994327-31cdaa80-3df7-11ea-838b-2d978281ee4a.png" width="30%"></img> 
<img src="https://user-images.githubusercontent.com/46574470/72994319-2ed2ba00-3df7-11ea-8e52-8acb770dd803.png" width="30%"></img>


Overzicht van de verschillende algoritmes:
- Gebruiker kan algoritme 1 selecteren voor een **random_algoritme**.
- Gebruiker kan algoritme 2 selecteren voor een **ascending_hillclimber**.
- Gebruiker kan algoritme 3 selecteren voor een **greedy_algoritme**.
- Gebruiker kan algoritme 4 selecteren voor een **swap_houses**.
- Gebruiker kan algoritme 5 selecteren voor een **random_points_ascending_hillclimber**
- Gebruiker kan optie 6 selecteren voor een combinatie van greedy, huizen swappen en huizen draaien

## Hoe het werkt

### Random
Het random algoritme selecteert een random coördinaat voor elk huis, bestaande uit een x en een y. Allereest wordt gecheckt of dit coördinaat binnen de map valt. Vervolgens checkt het algoritme of op dit coördinaat een huis geplaatst kan worden. De functie place_house wordt hiervoor gebruikt. Deze functie controleert of niet een van de vier hoeken van het huis binnen de coördinaten van het water valt en of de afstand van het dichtbijzijnde huis buiten de verplichte vrijstand van beide huizen staat.

### Ascending hillclimber
Het ascending hillclimber algoritme itereert over alle huizen die al geplaatst zijn door het greedy of random algoritme. Voor elk huis gaat het algoritme alle punten van het x en y grid af, terwijl hij checkt of de totale waarde van de map toeneemt bij het plaatsen op een nieuwe locatie. Als de totale waarde van de map toeneeemt wordt deze als nieuwe totale waarde geaccepteerd. Als de totale waarde lager wordt, plaatst het algoritme het huis terug naar de oude locatie en gaat naar het volgende punt op het x en y grid.

#### Random points ascending hillclimber
Het ascending hillclimber itereert over voor alle huizen voor alle punten op het x en y grid. Omdat het algoritme relatief gezien veel tijd gebruikt voor het vinden van een oplossing hebben we een variant gemaakt die in plaats van alle punten langs gaat op het grid, een specifiek aantal punten pakt die random worden gegenereerd.

### Greedy
Het greedy algoritme plaats eerst per keer een huis eerst op een random locatie. Vervolgens gaat het algoritme direct zoeken naar een betere locatie voor dat huis, kijkend naar de totale waarde van de map. Het algoritme gaat zo alle huizen af en plaats dus per keer het huis op de locatie die het meeste opbrengt.

### Swaphouses 
Het swaphouses algoritme vergelijkt één huis met al de andere huizen, waarbij het de coördinaten van de huizen ruilt. Het algoritme slaat eerst de locaties van beide huizen op om deze vervolgens te ruilen. Het algoritme checkt vervolgens of beide huizen geplaatst kunnen worden op de nieuwe locaties. Als dit het geval is, wordt de nieuwe totale waarde van de map berekend. Als dit meer is, wordt deze nieuwe waarde geaccepteerd en blijven de huizen op de nieuwe locatie staan. Als een van de huizen niet geplaatst kan worden op de nieuwe locatie of de waarde van de totale map wordt niet hoger, worden beide huizen weer op de oude locatie geplaatst.

## Contact

Alessandro Degenkamp - Alessandrodegenkamp@hotmail.com <br>
Kiara Evers - k.s.evers@hotmail.com <br>
Daniel Siha - daniel.siha@gmail.com <br>

Project Link: [https://github.com/alessndro/Project-AmstelHaege](https://github.com/alessndro/Project-AmstelHaege)

## Toekomstig werk

Mochten we nog meer tijd hebben om verder te gaan met dit project dan zullen wij ons richten op een simulated annealing algoritme dat ook slechtere waardes accepteerd, om vervolgens bij het plaatsen van de volgende huizen op een hogere totale waarde uit te kunnen komen.

## Licensie

Copyright 2020 alle rechten voorbehouden.

[image-1]:	doc/1.jpg
[image-2]:	doc/2.jpg
[image-3]:	doc/3.jpg