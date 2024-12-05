# Daten_Hohlschneiden


Die in der Datei "Schnittflaechendaten.csv" aufgeführten Header haben folgende Bedeutung:
- file_name = Dateibezeichung der durchgeführten Simulation. Ist für Korrelationsanalyse zu entfernen
- WS = Bezeichnung des schergeschnittenen Blechwerkstoffs (hier: DC03, DP600, DP800). Ist für Korrelationsanalyse zu entfernen 
- Ag = Gleichmaßdehnung des Blechwerkstoffs in %
- A80 = Bruchdechnunh des Blechwerkstoffs in %
- Rp0,2 = Streckgrenze des Blechwerkstoffs in MPa
- Rm = Zugfestugkeit des Blechwerkstoffs in MPa
- s = Blechdicke des Blechwerkstoffs in mm 
- u = Relativer Schneidspalt in %
- SB = Stegbreite des Hohlstempels in mm 
- SW = Stegwinkel des Hohlstempels in %
- SR = Stempelschneidkantenradius in mm 
- MR = Matrizenkantenradius in mm
- KEA = Kanteneinzugsanteil in % 
- GSA = Glattschnittanteil in %
- BFA = Bruchflächenanteil in %
- Grat = Gratanteil in %

Das Python Skript "Schnittflächendaten_auswerten" zeigt auf, wie die Daten in einem Pandas DataFrame eingelesen werden können 
Das Python Skript "Schnittflächendaten_auswerten" zeigt weiterhin auf, wie die Daten einer Pearson-Korrelationsanalyse unterzogen werden können
Das Python Skript "Schnittflächendaten_auswerten" zeigt Datenvorverarbeitungsschritte für das Training maschineller Lernalgorithmen auf.
Beim Schritt der Datenvorverarbeitung kann der gesamte Datensatz durch die in meiner Dissertationsschrift spezifizierten Maxima (Rm_max, s_max, u_max,...) geteilt werden. Data Leakage tritt nicht auf, da es sich hierbei um physikalische Randbedingungen des Hohlschneidens handelt. 

Folgende Python Bibliotheken wurden in das Python Skript importiert:
- pandas (Version 1.5.2)
- numpy (Version 1.23.5)
- matplotlib (Version 3.6.2)
- seaborn (Version 0.12.2)
- scikit-learn (Version 1.2.0)
 
Informationen zum Autor und Kontakt: 
- Herr Adrian Schenek
- Institut für Umformtechnik (IFU)
- Holzgartenstr, 17
- 70174 Stuttgart 
- adrian.schenek@ifu.uni-stuttgart.de

Datum: 25.03.2024  
