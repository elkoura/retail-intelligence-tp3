## UC-06 — Jointure métier et enrichissement des ventes

### Objectif

Enrichir les ventes magasin avec les catégories de produits afin d'analyser les performances commerciales par catégorie.

### Source de référence

La dimension `item.dat` contient 17 820 produits et 22 colonnes.

La clé `i_item_sk` a été contrôlée :

- 17 820 clés distinctes.
- 0 clé nulle.
- Aucun doublon de clé.

### Jointure réalisée

Une jointure gauche (`LEFT JOIN`) a été effectuée entre `store_sales.ss_item_sk` et `item.i_item_sk`.

La jointure permet d'ajouter la catégorie métier `i_category` à chaque ligne de vente.

### Contrôle d'intégrité référentielle

- Ventes sans correspondance produit : 0.
- Lignes avant jointure : 667 579.
- Lignes après jointure : 667 579.

La jointure n'a entraîné aucune perte ni multiplication d'enregistrements.

### Production Gold

Les ventes enrichies ont été regroupées par catégorie afin de calculer :

- Le nombre de lignes de vente.
- La quantité totale vendue.
- Le montant net payé.
- Le bénéfice net.

Neuf catégories ont été obtenues.

### Réconciliation

Les totaux après agrégation correspondent aux résultats initiaux :

| Indicateur       |            Total |
| ---------------- | ---------------: |
| Lignes de vente  |          667 579 |
| Quantité vendue  |       33 755 474 |
| Montant net payé | 1 150 529 586,37 |
| Bénéfice net     |  -552 553 374,82 |

### Stockage

Le nouveau jeu Gold a été enregistré dans `data/gold/ventes_par_categorie/` au format Parquet.

Sa relecture a confirmé la présence des neuf catégories et la conservation des types numériques.

**Conclusion :** cette transformation démontre une jointure vérifiée, un enrichissement métier et une agrégation analytique sans modification des totaux de référence.
