# -*- coding: utf-8 -*-


# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split



# Daten einlesen
df_quality = pd.read_csv("Schnittflaechendaten.csv")

# Überflüssige Spalten entfernen und verbleibende Informationen in einem neuen Dataframe speichern
df_neu = df_quality.drop(columns=["file_name", "WS", "MR"])
print(df_neu.head(10))

# Korrelationsanalyse zur Verbesserung des Datenverständnisses durchführen
correlation_matrix = df_neu.corr(method = "pearson").round(1)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='viridis')
plt.savefig('Korrelationsmatrix.png', dpi=1200)
plt.show()

# Beachte Multikollinearität. Ansatz: Rm behalten und Rp0,2, Ag sowie A80 entfernen
df_neu = df_neu.drop(columns=["Ag", "A80", "Rp0.2"])
print(df_neu.head(10))

# Datenvorbereitung für das Modelltraining
# Inputs normalisieren. Die Inputs sind: Rm, s, u, SB, SW, SR
df_neu["Rm_normalized"] = df_neu["Rm"] / df_neu["Rm"].max()
df_neu["s_normalized"] = df_neu["s"] / df_neu["s"].max()
df_neu["u_normalized"] = df_neu["u"] / df_neu["u"].max()
df_neu["SB_normalized"] = df_neu["SB"] / df_neu["SB"].max()
df_neu["SW_normalized"] = df_neu["SW"] / df_neu["SW"].max()
df_neu["SR_normalized"] = df_neu["SR"] / df_neu["SR"].max()

# Ouputs normalisieren. Die Outputs sind: KEA, GSA, BFA, Grat
df_neu["KEA_normalized"] = df_neu["KEA"]
df_neu["GSA_normalized"] = df_neu["GSA"]
df_neu["BFA_normalized"] = df_neu["BFA"]
df_neu["Grat_normalized"] = df_neu["Grat"]

# Tensoren für Inputs und Outputs zusammenfassen
# Input Tensor x
x1 = np.column_stack((df_neu["Rm_normalized"],df_neu["s_normalized"],df_neu["u_normalized"],df_neu["SB_normalized"],df_neu["SW_normalized"],df_neu["SR_normalized"]))

# Output Tensor y
y1 = np.column_stack((df_neu["KEA_normalized"],df_neu["GSA_normalized"],df_neu["BFA_normalized"],df_neu["Grat_normalized"]))


# Aufteilung der Tensoren in Trainings-, Validierungs- und Testdatensatz nach den Zufallsprinzip (Holdout Methode)

x1_train_1 , x1_test , y1_train_1 , y1_test = train_test_split(x1 , y1 , test_size = 0.2 , random_state = 42, shuffle=True)
x1_train , x1_val , y1_train , y1_val =train_test_split(x1_train_1 , y1_train_1, test_size = 0.1 , random_state = 42, shuffle=True)





