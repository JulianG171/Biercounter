# KG Silschede Bierzähler

## Funktion

Nach Druck auf einen Pilzknopp wird der Zähler um eine Fassgröße (aktuell 50L) erhöht. Zudem kann man die Eingabe über
ein webinterface steuern.

## Installation

```bash
sudo apt install php8.1-cli
```

## Starten des Webservers
```bash
php -S 127.0.0.1:9099 index.php
```

Nachdem der Webserver gestartet wurde, kann das webinterface über <ip-adresse-des-pis>:9099 im Browser aufgerufen werden.