Maandag 6 januari 2019
Start van het groepsproject
Case: AmstelHaege

optimalisastieprobleem:
Stuk grond 160x180
20,40 of 60 huizen
3 soorten huizen met eigen afmetingen en vereisten met eigen waardevermeerdering
vraagstuk: Wat is de maximale waarde die je kunt bereiken met een zelfgekozen verdeling en plaatsing van het water?
Belangrijke aandachtspunten:
- Ratio huizen staat vast
- 6 verschillende plattegronden -> 3 met voorbepaalde locatie water -> 3 met zelf in te delen water plekken
- Voor extra waardevermeerdering moet de oppervlakte rondom een meter extra zijn
- Tuinen mogen overlappen het huis met de grootste vereisten is dan de beperkende factor
- Huizen mogen gedraaid worden
- Volgens pythogoras zijn het geen rechthoeken maar rechthoeken met afgeronde hoeken (straal^2 x pi)
- Water telt mee als vrijstand
- Grootste huizen hebben de meeste waarde, en leveren het meest op per meter extra de kleinste huizen het minst, daarom afstand van de kleinste huizen minimaliseren
- afweging maken tussen de extra meters benodigd voor de grote woning
- grote huizen hebben de meeste prioriteit daardoor

Datastructuren:
- List
    - Beschikbare meters
    - Onbeschikbare meters
    - Water meters
    - Grond meters
- Objecten
    - Huis object
        - Locatie woning
        - Locatie tuin
        - Type woning
        - Vereiste ruimte om het huis
        - Waarde woning
        - Waardevermeerdering
        - rentepercentage enkel
        - extra meters

        functie totalprice
            * extra meters x rentepercentage -> rentepercentage x waarde woning = totalprice
        functie extra meters
            * 
    - Waterobject
        - bezet (bool)
        - Locatie beschikbaar
        - Locatie onbeschikbaar

Beschikbare ruimte:
grond 180x160 = 28.800
20% water = 5.760
ruimte over voor huizen = 23.040

situatie 20 huizen:
    small = 0.6 x 20 = 12
    medium = 0.25 x 20 = 5
    large = 0.15 x 20 = 3

    oppervlakte:
    small = 12 x 8 x 8 = 768
    medium = 5 x 11 x 7 = 385
    large = 3 x 12 x 10 = 360
    totaal = 1.513

situatie 40 huizen:
    small = 0.6 x 40 = 24
    medium = 0.25 x 40 = 10
    large = 0.15 x 40 = 6

    oppervlakte:
    small = 24 x 8 x 8 = 1536
    medium = 10 x 11 x 7 = 770
    large = 6 x 12 x 10 = 720
    totaal = 3.026

situatie 60 huizen:
    small = 0.6 x 60 = 36
    medium = 0.25 x 60 = 15
    large = 0.15 x 60 = 9

    oppervlakte:
    small = 36 x 8 x 8 = 2.304
    medium = 15 x 11 x 7 = 1.155
    large = 9 x 12 x 10 = 1.080
    totaal = 4.539
    
Dinsdag 7 januari 2020
Technische aspecten besproken, objecten aangemaakt, begonnen met schrijven van het benodigde algoritme
Random function afgemaakt, we hebben gekozen voor een soort grid systeem op basis van x,y coordinaten afgerond op hele getallen.
Omdat de hoeken van een vrijstand eigenlijk afgerond zijn (pythagoras) bepalen wij nu dat het mogelijk is een huis te plaatsen op
datzelfde exacte punt omdat hier in de werkelijkheid geen verplichte vrijstand meer is (afstand is groter) maar we dit nog niet
visualiseren omdat dit momenteel makkelijker te programmeren moet zijn

Woensdag 8 januari 2020
Voortgangs gesprek en presentaties gehad, we wilde het probleem ook wiskundig oplossen ons werd aangeraden om dit (nog) niet te doen en het probleem eerst echt random aan te pakken. Ons idee was om eerst te beginnen met de grote huizen, maar dit is een geinformeerde random. één van de TA's was het hier niet mee eens en vind dat dit ook echt random zou moeten zijn.
Begonnen met het verdiepen in matplotlib om data te kunnen visualiseren, functies geschreven voor het maken van de objecten op basis van de gegeven input. Daarnaast extra functies geschreven voor de house class om de waarde van de woning te kunnen bepalen, en de locaties die bij de woning horen. Naam attribuut toegevoegd omdat we de berekende afstand tot andere huizen al willen kunnen vastleggen bij het plaatsen van de woning zodat er uiteindelijk minder berekeningen dubbel uitgevoerd hoeven te worden. Daarnaast zijn we begonnen met de functie om te bepalen of een huis geplaatst mag worden

Donderdag 9 januari
Begonnen met het schrijven voor het algoritme voor de kortste afstand. Daarnaast hebben we uitgezocht hoe wij onze oplossing kunnen visualiseren en hoe de beste oplossing vervolgens naar een apart file geschreven kan worden.