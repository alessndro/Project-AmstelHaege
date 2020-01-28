# Process van D-place

### Maandag 6 januari 2019
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
    
### Dinsdag 7 januari 2020
Technische aspecten besproken, objecten aangemaakt, begonnen met schrijven van het benodigde algoritme.
Random function afgemaakt, we hebben gekozen voor een soort grid systeem op basis van x,y coordinaten afgerond op hele getallen.
Omdat de hoeken van een vrijstand eigenlijk afgerond zijn (pythagoras) bepalen wij nu dat het mogelijk is een huis te plaatsen op
datzelfde exacte punt omdat hier in de werkelijkheid geen verplichte vrijstand meer is (afstand is groter) maar we dit nog niet
visualiseren omdat dit momenteel makkelijker te programmeren moet zijn.

### Woensdag 8 januari 2020
Voortgangs gesprek en presentaties gehad, we wilde het probleem ook wiskundig oplossen ons werd aangeraden om dit (nog) niet te doen en het probleem eerst echt random aan te pakken. Ons idee was om eerst te beginnen met de grote huizen, maar dit is een geinformeerde random. Eén van de TA's was het hier niet mee eens en vind dat dit ook echt random zou moeten zijn. Begonnen met het verdiepen in matplotlib om data te kunnen visualiseren, functies geschreven voor het maken van de objecten op basis van de gegeven input. Daarnaast extra functies geschreven voor de house class om de waarde van de woning te kunnen bepalen, en de locaties die bij de woning horen. Naam attribuut toegevoegd omdat we de berekende afstand tot andere huizen al willen kunnen vastleggen bij het plaatsen van de woning zodat er uiteindelijk minder berekeningen dubbel uitgevoerd hoeven te worden. Daarnaast zijn we begonnen met de functie om te bepalen of een huis geplaatst mag worden.

### Donderdag 9 januari
Begonnen met het schrijven voor het algoritme voor de kortste afstand. Daarnaast hebben we uitgezocht hoe wij onze oplossing kunnen visualiseren en hoe de beste oplossing vervolgens naar een apart file geschreven kan worden. De afstand tot andere huizen kunnen we eerst het beste berekenen met if-statements die gebasseerd zijn op de locatie van het ene huis ten opzichte van het andere huis Als bijvoorbeeld een ander huis rechtsboven zit van het huis je vergelijkt, gebruik dan de rechter boven hoek van het huis dat je vergelijkt en de linker onder hoek van het andere huis. Vervolgens kan je de abc-formule gebruiken om de afstand te berekenen.

### Vrijdag 10 januari
Bugs gefixed in het huidige programma en de basis voor de visualisatie gemaakt zonder koppeling naar ons algoritme. We zijn nu in staat zelf huizen te maken op een map door coördinaten in te vullen. Ook is het visualiseren van de vrije ruimte tersprake gekomen omdat dit snel zichtbaar moest worden. Hier zijn de restricties van de vrije ruimte van huizen als linewidth gevisualiseerd die voor elk soort huis size een andere dikte heeft. Als toevoeging hierop is er ook besloten om verschillende kleuren te vormen voor de verschillende formaat huizen. Helaas is het displayen van de namen van de huizen op de map nog niet mogelijk wat wel van pas zou kunnen komen voor latere debug fixes. 

### Maandag 13 januari
Het random algoritme dat we hebben geschreven werkt nog niet helemaal volledig. Vandaag hebben we vooral gebrainstormt over hoe we het random algoritme kunnen verbeteren, zodat we op een betere oplossing uitkomen. Als we onze random runnen waarbij we tevens random kiezen met welk soort huis we beginnen met plaatsen, is er een hogere kans dat het random algoritme geen oplossing kan vinden waarbij alle huizen zijn geplaatst. Als we beginnen met het plaatsen van kleine huizen vind ons random algoritme heel vaak geen oplossing. Als we uiteindelijk het random algoritme starten met het plaatsen van grote huizen komen we altijd op een oplossing waarin alle huize geplaatst zijn.

### Dinsdag 14 januari
Vandaag hebben we een functie gemaakt die water voor de drie verschillende mappen aanmaakt. We hebben uiteindelijke gekozen om voor verschillende mappen waterobjecten aan te maken, die bestaat uit de coördinaten van de vier hoeken van het water. Zo kunnen we vervolgens makkelijk checken of een huis binnen de coördinaten van water valt. Verder is het gelukt om de map en de huizen te visualiseren. Ook is er een scatterplot die de waarde van de totale map inclusief alle huizen toont na elk random plaatsing van huizen.

### Woensdag 15 januari
De random kunnen we nu gemakkelijk testen, omdat onze visualtie nu goed werkt. Na testen zijn we erachter gekomen dat een huis soms voor een gedeelte in water wordt geplaatst. Dit was vooral het geval bij map 2. We kunenn niet precies erachter komen welk medium huis er steeds im het water valt en of dit het zelfde huis steeds is. Na testen lijk het erop dat het niet steeds het zelfde huis is wat in het water ligt, want ook een small of large huis valt soms gedeeltelijk in het water.

### Donderdag 16 januari
Nagedacht over ons volgende algoritme, waarbij we op het idee zijn gekomen om na het random algoritme per huis te kijken voor elke locatie op ons grid of de totale waarde van de map groter is. Als dit het geval is wordt het huis op de locatie geplaats met een grotere totale waarde. Zo gaat dit algoritme elke huis langs, zodat de totale waarde van de map na de random hoger wordt. Dit algoritme is gebasseerd op een ascending hill climber. Vandaag nog niet volledig gelukt om dit algoritme te runnen.

### Vrijdag 17 januari
Na het testen van ons hill climber algoritme kwamen we erachter dat ons random algoritme een enkele keer een medium huis in het water plaats. Na testen van de code en debuggen, kwamen we erachter dat we een kleine fout hadden gemaakt in de hoogte en breedte, omdat we die hadden omgedraaid. Nadat we dit hadden aangepast, werkte ons random volledig en konden we door met het volgende algoritme. In eerste istantie plaatste ons volgende algoritme alle huizen helemaal links onder. Het algoritme itereerde dus over de punten van de grid en begon bij (0,0). Het probleem was echter dat het algoritme gelijk alle huizen hier plaatsten zonder te kijken of er huizen overlappen.

### Maandag 20 januari
In het hill climber algoritme hadden we een if statement te ver naar rechts staan, waardoor hij deze oversloeg en dus alle huizen links onder plaatste op het eerste coördinaat. Na dit if statement goed te plaatsen, werkt ons hill climber algoritme goed. Na testen komt dit algoritme steeds op de zelfde uitkomst, waarbij de verschillende grote huizen zo ver mogelijk uit elkaar staan. De medium huizen en kleine huizen plaatst het algoritme dichtbij elkaar.

### Dinsdag 21 januari
Vandaag hebben we gewerkt aan een nieuw algoritme, namelijk een greedy algoritme. Het greedy algoritme plaats eerst per keer een huis eerst op een random locatie. Vervolgens gaat het algoritme direct zoeken naar een betere locatie voor dat huis, kijkend naar de totale waarde van de map. Het algoritme gaat zo alle huizen af en plaats dus per keer het huis op de locatie die het meeste opbrengt. Het algoritme werkt nog niet volledig, dus morgen gaan we hier verder aan werken.

### Woensdag 22 januri
Na brainstormen zijn we op een nieuw idee gekomen. We hebben bedacht dat nadat een algoritme de huizen heeft geplaatst, zou je deze huizen ook nog kunnen ruilen met elkaar terwijl je kijkt of de totale waarde van de map toeneemt. Als de totale waarde van de map toeneemt en je kan de huizen op de locatie van het ander huis plaatsen, plaats het huis dan op die locatie. Zo kan de waarde van de geplaatste huizen na een greedy of hill climber nog hoger worden.

### Donderdag 23 januari
We hebben een optie toegevoegd voor de gebruiker om meerdere algoritmes na elkaar te gebruiken. Als de gebruiker kiest voor optie 6, wordt allereest het greedy algoritme gebruikt om deze huizen te plaatsen en vervolgens worden de huizen geswapt als dit zorgt voor een waarde stijging van de map. Naast dat de huizen kunnen swappen, is het ook mogelijk dat ze 90 graden draaien. In de visualisatie hebben we elk huis een nummer kunnen geven, zoals S1 voor een small house, of L1 voor een large huis. Dit was vooral handig met bugs fixing, waarbij we dus precies wisten welk huis niet goed geplaastst was.

### Vrijdag 24 januari
Readme hebben we vandaag gemaakt, waarbij we duidelijk uitleggen waar het project over gaat, hoe je de code kan runnen en welke algoritmes gebruikt worden. Na technische assistentie aangevraagd te hebben, kregen we de tip om onze main kleiner te maken. Main wordt nu alleen gebruikt om de verschillende algoritmes aan te roepen, ipv verschillende loops in main. We hebben alle algoritmes geplaatst in een python file genaamd algoritmes.py en andere hulp functies die we gebruiken voor de algoritmes hebben we geplaatst in helper_functions.py.

### Maandag 27 januari
Aan het begin van de dag is er een korte script scan gedaan. Hier is gekenen of spaceblanks en comments allemaal voldoen aan de regels. Vervolgens om 11 uur waren we bezig met een voortgangsgesprek waarin we hebben gediscussieerd over onze stappen en technieken die we hebben gebruikt. Hierop is een theoretisch eindcijfer gebaseerd. Later op de dag hebben we de oefen presentaties gehad. Hier hebben we gekeken wat de presentatie technieken zijn en waar het aan moet voldaan. Zo is besproken welke project stappen wel uitbundig behandeld/besproken moeten worden tijdens de presentatie en welke niet. Ook is er kort besproken wat voor veranderingen het vak nodig heeft voor volgend jaar die wij persoonlijk dit jaar niet zo goed vonden. Hierna is de MAIN aangepast. Deze is nog een stuk kleiner en simpeler geworden en ziet er voor de gebruiken dus makkelijker uit. Helaas hadden wel een systematisch probleem, namelijk dat de functies niet goed worden geïmport. Dit hebben we voor de vragen ronde van morgen bewaard.  

### Dinsdag 28 janauri
Ons project hebben we verdeelt in folders, waarbij algoritmes en de hulp functies zijn gesplitst in aparte files. We krijgen echter een error als we nu de code willen runnen, waarbij het algoritme de functies uit het andere file niet herkent. We hebben een TA om hulp gevraagd bij deze import fout, maar hij wist het ook niet. Op dit moment hebben we ervoor gekozen de hulp functies in het zelfde file te zetten als het algoritmes, totdat we technische assistentie krijgen. Technische assistentie is gekomen en heeft ons vertelt dat het niet mogelijk is om in twee verschillende bestanden allebei functies van elkaar te importeren. Ook zei hij dat het beter is om de algoritmes in verschillende python bestanden te stoppen. 


