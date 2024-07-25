# Schadow-Security-Scanner
 


## Überblick

Der Schadow-Security-Scanner bietet eine umfassende Lösung zur Identifizierung und Verwaltung von Code-Schwachstellen in Ihren Projekten. Dieses Tool besteht aus zwei Hauptkomponenten:

1. CLI-Tool: Ein plattformunabhängiges Befehlszeilen-Tool, das manuell auf dem Client verwendet werden kann.
2. GitHub Action: Eine GitHub Action, die in GitHub Actions Workflows integriert werden kann, um automatisierte Schwachstellenscans durchzuführen.

## Installation und Build

### Vorraussetzungen

1. Python 3.11.1
2. pip 22.3.1
3. (optional) passende IDE z.B. VSCode (bitte beachte, dass cmd.exe als default Terminal eingestellt ist)

### Clone

Klonen Sie das Repository und navigieren Sie zum Projektverzeichnis:

```bash
git clone https://github.com/schadow98/Schadow-Security-Scanner.git
cd Schadow-Security-Scanner
pip install -r requirements.txt
```

### Development 

Um das Skript zu erweitern und für Entwicklungszwecke zu nutzen, führen Sie folgenden Befehl aus:

```bash
python src/SecurityScanner.py
```

Um mehr über die Übergabeparameter zu erfahren, führen Sie folgenden Befehl aus:

```bash
python src/SecurityScanner.py --help
```

### Build  CLI Tool

Um das CLI-Tool zu bauen, führen Sie folgenden Befehl aus:

```bash
pyinstaller --onefile --add-data "src;." --distpath ./dist --name SecurityScannerSchadow ./src/SecurityScanner.py
```

Im dist-Verzeichnis wird eine ausführbare Datei erstellt:
- Unter Windows: ./dist/SecurityScannerSchadow.exe
- Unter Linux: ./dist/SecurityScannerSchadow

### Build  Github Action und Container

Nach einem Push ins Repository und erfolgreichen Unittests wird ein Image automatisch in der Pipeline gebaut. Das Docker-Image befindet sich unter: https://ghcr.io/schadow98/schadow-security-scanner:latest.


## Tests

Um sicherzustellen, dass alles korrekt funktioniert, führen Sie die Tests wie folgt aus:

### Unittest

Um die Unittests auszuführen, führen Sie folgenden Befehl aus:

```bash
python tests/unittest
```

Das Logging für die Unittests wurde deaktiviert. 
Es werden nur Testnachrichten ausgegeben.

### EndToEnd-Test

Bitte beachten Sie, dass ggf. die Pakete/Module in requirements.txt angepasst werden müssen. 
Um erfolgreiche Tests durchzuführen, müssen sichere Pakete in den Testfällen benutzt werden. 
Im End-to-End-Test wird die REST-API von Sonatype aufgerufen. 
Um den End-to-End-Test auszuführen, führen Sie den folgenden Befehl aus:

```bash
runEnd2EndTest.bat
```

Dieser Befehl funktioniert nur unter Windows. 
Auf anderen Betriebssystemen führen Sie den folgenden Befehl aus:

```bash
robot --outputdir ./logs ./tests/end2end/
```

Der End-to-End-Test benötigt Zugriff auf das Test-Repository. 
Legen Sie dazu eine Umgebungsvariable namens GITHUB_TOKEN an. 
Unter Windows kann diese auch mit dem dotenv-Modul gesetzt werden:

```python
#.env
GITHUB_TOKEN=<Secret_Token>
```


## Nutzung

Die Anwendung kann auf unterschiedliche Weise je nach Ihren Bedürfnissen genutzt werden.

### CLI-Nutzung

Die ausführbare Datei können Sie über ein beliebiges Terminal ausführen:

```bash
./dist/SecurityScannerSchadow.exe
```

Für mehr Informationen führen Sie folgenden Befehl aus:

```bash
./dist/SecurityScannerSchadow.exe --help
```

### Github Action Nutzung-Nutzung

Um die ScanDependencies GitHub Action in Ihre CI/CD-Pipeline zu integrieren, fügen Sie einfach den Job SecurityScanner hinzu. 
Die folgende YAML-Datei zeigt eine mögliche Integration:

```yaml
#.github/workflows/SecurityScan.yml
name: SecurityScanner
run-name: SecurityScanner
        
jobs:
  ScannerSuccess:
    runs-on: ubuntu-latest
    steps:
      - name: ${{github.event.inputs.distinct_id}}
        run: echo run identifier ${{ inputs.distinct_id }}

      - name: Checkout
        uses: actions/checkout@v4

      - name: SecurityScanner
        uses: schadow98/Schadow-Security-Scanner@main  
        with:
          path: ./sucess
          configFile: ./securityScannerConfig.json
          logDir: ./logs_success
          requirementsFile: ./sucess/requirements.txt

      - name: Upload logs
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: SecurityScanner
          path: logs_success
```


Die Parameter unter dem Job SecurityScanner können beliebig angepasst werden. 
Dabei werden die gleichen Parameter wie für das CLI-Tool verwendet.