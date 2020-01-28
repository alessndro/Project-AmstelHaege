## Resultaten
Onze resultaten worden opgeslagen in een csv file (document dat gescheiden wordt door middel van komma's).
Er zijn meerdere csv files te vinden, in progress_run worden de resultanten gevonden van de huidige run. Wanneer het programma beeindigt wordt word dit document automatisch geleegd. In solutions.csv worden alle behaalde resultaten opgeslagen van elke run die gedaan is, deze file wordt dus nooit geleegd en wordt bij elke run steeds groter.

De resulaten in progress_run worden als volgt opgeslagen:<br>
argument 1: aantal gekozen huizen<br>
argument 2: gekozen map nummer<br>
argument 3: totale waarde die behaalt is met het algoritme<br>
argument 4: het algoritme dat gebruikt is om het resultaat te behalen<br>

De resultaten in solutions worden als volgt opgeslagen:<br>
Het begint met een begin regel waarbij;<br>
argument 1: aantal gekozen huizen<br>
argument 2: gekozen map nummer<br>
argument 3: totale waarde die behaalt is met het algoritme<br>
argument 4: het algoritme dat gebruikt is om het resultaat te behalen<br>

vervolgens komen er het gekozen aantal huizen aan regels onder, <br>
Deze huizen worden per regel beschreven.<br>
argument 1: naam van de woning<br>
argument 2: grootte van de woning<br>
argument 3: x en y coordinaat van de linker onderhoek<br>
argument 4: x en y coordinaat van de rechter bovenhoek<br>
