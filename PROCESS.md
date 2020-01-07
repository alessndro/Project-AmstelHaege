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
    




