# UC-06 — Règles de nettoyage et de qualité

## 1. Objectif

Documenter les anomalies détectées et justifier les règles de transformation appliquées aux deux sources Retail : `store_sales` et `web_sales`.

## 2. Sources analysées

| Source          | Enregistrements | Colonnes |
| --------------- | --------------: | -------: |
| store_sales.dat |         667 579 |       23 |
| web_sales.dat   |         668 052 |       34 |

Les fichiers sources originaux sont conservés sans modification.

## 3. Règles de transformation

### R01 — Renommage des colonnes

Les colonnes génériques `_c0`, `_c1`, etc. ont été renommées avec les noms métier attendus des schémas TPC-DS.

**Justification :** améliorer la compréhension des données et faciliter les traitements.

### R02 — Conversion des types

Les identifiants et quantités ont été convertis en entiers. Les montants ont été convertis en `decimal(18,2)`.

**Résultat :** aucune erreur de conversion détectée dans les deux sources.

### R03 — Valeurs manquantes

- `store_sales` : 4 colonnes avec valeurs manquantes.
- `web_sales` : 11 colonnes avec valeurs manquantes.

**Décision :** conserver les valeurs manquantes dans les références concernées, sans les remplacer arbitrairement par zéro.

**Justification :** une référence absente n'invalide pas nécessairement une vente.

### R04 — Doublons

Aucun doublon exact n'a été détecté dans les deux sources.

Dans `store_sales`, 4 038 groupes partagent la même combinaison date, magasin, ticket et produit. Certaines lignes ont pourtant des quantités ou montants différents.

**Décision :** aucune suppression automatique.

### R05 — Quantités vendues

Les quantités sont comprises entre 1 et 100 dans les deux sources.

Aucune quantité nulle ou négative n'a été détectée.

**Décision :** conserver les enregistrements.

### R06 — Montants nets payés

| Contrôle              | Magasin |     Web |
| --------------------- | ------: | ------: |
| Montants négatifs     |       0 |       0 |
| Montants égaux à zéro |   3 954 |   3 938 |
| Bénéfices négatifs    | 495 971 | 407 163 |

**Décision :** conserver les lignes concernées.

**Justification :** les montants nuls et les bénéfices négatifs nécessitent une interprétation métier. Ils ne prouvent pas automatiquement une erreur technique.

### R07 — Cohérence financière

Les relations suivantes ont été vérifiées :

- `ss_net_paid = ss_ext_sales_price - ss_coupon_amt`
- `ws_net_paid = ws_ext_sales_price - ws_coupon_amt`

Résultats pour chaque source :

- 0 incohérence détectée.
- 0 ligne non vérifiable.

### R08 — Cohérence des dates Web

Aucune clé d'expédition inférieure à la clé de vente n'a été détectée.

Aucune clé d'expédition manquante n'a été détectée.

**Limite :** la validation chronologique définitive nécessite la correspondance des identifiants avec les dates réelles de `date_dim`.

## 4. Production Silver

Les deux sources ont été renommées et typées, puis enregistrées au format Parquet.

Les volumes après relecture sont identiques aux volumes avant écriture.

Aucune ligne n'a été supprimée.

## 5. Production Gold

Trois indicateurs ont été calculés :

- Quantité totale vendue.
- Montant net total payé.
- Bénéfice net total.

Ils ont été agrégés séparément pour les canaux Magasin et Web, puis réunis avec `unionByName()`.

Les résultats Gold ont été enregistrés et relus au format Parquet.

## 6. Limites et améliorations

- Vérifier exhaustivement les noms et types avec les schémas de référence.
- Examiner les références manquantes selon leur rôle métier.
- Valider les dates à l'aide de `date_dim`.
- Vérifier l'intégrité référentielle si les dimensions nécessaires sont disponibles.
- Documenter toute jointure ou tout enrichissement complémentaire avant son application.

## 7. Conclusion

Les traitements réalisés ont permis de structurer les deux sources et de produire des données analytiques exploitables, sans suppression arbitraire de ventes.

Les contrôles effectués sont documentés et les anomalies potentielles ont été conservées pour une analyse métier complémentaire.
