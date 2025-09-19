# **Flask ISBN Boekenzoeker**

Dit is een simpele Flask webapplicatie waarmee gebruikers de titel van een boek kunnen vinden door het 13-cijferige ISBN in te voeren.

## **Kenmerken**

* Eenvoudige, strakke gebruikersinterface met styling via Tailwind CSS.
* ISBN-validatie (moet 13 karakters lang zijn).
* Zoekt boekgegevens op uit een lokaal books.csv-bestand.
* Gebruikt een flexibel Book-model dat extra eigenschappen uit de CSV kan verwerken.
* Toont gebruiksvriendelijke foutmeldingen.
* Bevat een minimale test-suite die Pytest gebruikt.

## **Projectstructuur**

```
|-- app.py              \# Hoofdapplicatie (Flask)
|-- books.csv           \# Voorbeeld boekendata
|-- test\_app.py         \# Tests voor de applicatie
|-- requirements.txt    \# Python-afhankelijkheden
|-- README.md           \# Dit bestand
|-- templates/
|   |-- index.html      \# Hoofdpagina (zoekformulier)
|   |-- resultaat.html  \# Pagina om resultaat te tonen
```

## **Setup en de Applicatie Draaien**

1. **Kloon de repository of download de bestanden.**
2. **Maak een virtual environment aan (aanbevolen):**
```
   python \-m venv venv
   source venv/bin/activate  \# Gebruik \`venv\\Scripts\\activate\` op Windows
```
3. **Installeer de afhankelijkheden:**
   `pip install \-r requirements.txt`

4. **Draai de Flask-applicatie:**
   `python app.py`

5. Open je webbrowser en ga naar http://127.0.0.1:5000.

## **De Tests Draaien**

Om de tests te draaien, voer je het volgende commando uit in je terminal:
pytest

## **Werken met GitHub (voor beginners)**

Als je niet bekend bent met Git en GitHub, is hier een basisworkflow om wijzigingen aan te brengen in dit project.

### **1\. Het project klonen**

Kloon de repository naar je lokale machine. Hiermee download je alle projectbestanden. Gebruik de URL van de GitHub-pagina.
`git clone \<URL\_VAN\_DE\_REPOSITORY\>`
`cd \<NAAM\_VAN\_DE\_MAP\>`

### **2\. Een nieuwe branch aanmaken**

Werk nooit rechtstreeks op de master- of main-branch. Maak een nieuwe branch aan voor jouw wijzigingen. Geef het een logische naam.
\# Ga eerst zeker naar de hoofdbranch en haal laatste wijzigingen op
`git checkout main`
`git pull`

\# Maak nu je nieuwe branch
`git checkout \-b mijn-nieuwe-feature`

### **3\. Lokaal ontwikkelen**

Nu kun je de code aanpassen. Open het project in je favoriete editor en voer de wijzigingen door die je wilt maken. Draai de applicatie lokaal om je wijzigingen te testen.

### **4\. Wijzigingen opslaan en pushen**

Als je tevreden bent met je wijzigingen, sla je ze op in Git (een "commit") en stuur je ze naar GitHub ("pushen").
\# Voeg alle gewijzigde bestanden toe
`git add .`

\# Maak een commit met een duidelijke boodschap
`git commit \-m "Beschrijving van wat ik heb aangepast"`

\# Push je branch naar GitHub
`git push origin mijn-nieuwe-feature`

### **5\. Een Pull Request (PR) aanmaken**

Ga naar de GitHub-pagina van de repository. Je zult een melding zien om een Pull Request aan te maken voor je zojuist gepushte branch. Klik hierop, geef een duidelijke titel en beschrijving, en maak de Pull Request aan.

### **6\. De Pull Request mergen**

Een Pull Request is een verzoek om jouw wijzigingen samen te voegen (te "mergen") met de hoofdbranch (main). Meestal zal iemand anders je code reviewen. Als alles in orde is, kan de Pull Request gemerged worden. Zodra dit gebeurd is, zijn jouw wijzigingen onderdeel van het hoofdproject.
