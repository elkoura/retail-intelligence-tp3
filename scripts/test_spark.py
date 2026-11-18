from pyspark.sql import SparkSession

# Créer une session Spark locale
spark = (
    SparkSession.builder
    .appName("Test-Retail-Intelligence")
    .master("local[*]")
    .getOrCreate()
)

print("Version Spark :", spark.version)

# Petit jeu de données de test
donnees = [
    ("Magasin A", 1200.0),
    ("Magasin B", 850.0),
    ("Magasin C", 1600.0)
]

colonnes = ["magasin", "chiffre_affaires"]

df = spark.createDataFrame(donnees, colonnes)

# Afficher les données
df.show()

# Arrêter proprement Spark
spark.stop()
