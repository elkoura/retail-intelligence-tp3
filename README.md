# Retail Intelligence Platform — TP Jour 3

**Mastère Développement, Data & IA — IPSSI**

**UC-06 : Traitement et transformation des données avec Python/PySpark**

## Objectif

Construire un pipeline de traitement de données Retail permettant d'explorer deux sources, de contrôler leur qualité, de préparer des données Silver et de produire des indicateurs métier Gold.

## Technologies

- Python 3.11
- Apache Spark / PySpark 3.5.6
- JupyterLab
- Parquet
- Git / GitHub
- macOS, exécution Spark en mode local

## Sources utilisées

| Source            |  Lignes | Colonnes |
| ----------------- | ------: | -------: |
| `store_sales.dat` | 667 579 |       23 |
| `web_sales.dat`   | 668 052 |       34 |

Les sources proviennent du jeu de données Retail utilisé dans le cadre du TP.

## Architecture des données

- **Raw / Bronze** : fichiers `.dat` d'origine.
- **Silver** : données renommées, typées et contrôlées, stockées en Parquet.
- **Gold** : indicateurs métier agrégés par canal de vente.

## Traitements réalisés

1. Chargement et exploration des deux sources avec PySpark.
2. Vérification des volumes, schémas et valeurs manquantes.
3. Renommage des colonnes selon les schémas métier attendus.
4. Conversion des identifiants et quantités en entiers, et des montants en décimaux.
5. Contrôles des conversions et des doublons exacts.
6. Conservation des valeurs manquantes et des lignes répétées non prouvées incorrectes.
7. Écriture et relecture des données Silver au format Parquet.
8. Agrégation des quantités, montants nets payés et bénéfices nets.
9. Production et relecture d'un tableau Gold multicanal au format Parquet.

## Principaux résultats

| Indicateur         |          Magasin |              Web |
| ------------------ | ---------------: | ---------------: |
| Quantité totale    |       33 755 474 |       33 724 378 |
| Montant net total  | 1 150 529 586,37 | 1 535 374 825,67 |
| Bénéfice net total |  -552 553 374,82 |  -168 576 494,45 |

Les montants correspondent aux valeurs monétaires du jeu de données.

## Contrôles qualité

- Aucune erreur de conversion détectée sur les deux sources.
- Aucun doublon exact détecté.
- Valeurs manquantes dans 4 colonnes magasin et 11 colonnes web.
- Quantités comprises entre 1 et 100.
- Aucun montant net payé négatif.
- Relations entre les montants de vente, coupons et montants nets payés vérifiées.
- Dates d'expédition web contrôlées par comparaison des clés, sous réserve de validation via la dimension calendrier.

Les montants nets nuls et bénéfices négatifs ont été conservés et documentés.

## Organisation du dépôt

- `notebooks/` : notebook PySpark et résultats.
- `scripts/` : script de vérification de Spark.
- `reports/` : résultats des contrôles qualité.
- `docs/preuves/` : PDF de preuves d'exécution.

Les données sources et les fichiers Parquet volumineux ne sont pas suivis par Git.

## Reproduction

Prérequis : Python 3.11, Java 17, PySpark 3.5.6 et JupyterLab.

Installer les dépendances dans un environnement virtuel, placer les deux fichiers `.dat` aux emplacements attendus par le notebook, démarrer JupyterLab puis exécuter les cellules dans l'ordre.

Les chemins locaux utilisés doivent être adaptés à l'environnement d'exécution.

## Limites

Les correspondances avec les schémas métier, la cohérence chronologique via `date_dim` et l'intégrité référentielle nécessitent une validation complémentaire. Aucune jointure de dimension n'a été réalisée dans cette version.

Les KPI sont calculés sur les lots initiaux analysés.
