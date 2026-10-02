### 1. Comment les données sont structurées ? (clés - valeurs)

**Aucune table, aucune ligne, aucune colonne**, contrairement au SQL.
**Accès direct via l'adresse mémoire**, donc ultra-rapide vu qu'elle ne parcourt pas toute la base à chaque requête.

Les données sont stockées dans le format **Clés-valeurs** et sont **sensibles à la casse** :
`KEY` est différent de `Key`, qui elle-même est différente de `key` !

Une **hiérarchie** peut être faite par l'utilisateur (`user:100`, `user:100:profile`) mais la base de données ne fait pas de distinction ; pour elle ce n'est qu'une chaîne de caractères.

Elle ne **vérifie pas le format** de ce qu'on lui envoie ; ça peut être une simple donnée `str` comme `"bonjour"` ou même du JSON :
```json
{"nom": "Kevin", "role": "SWE"}
```

Les données peuvent avoir une **durée de vie configurable** ; une fois cette durée de vie passée, la clé et ses valeurs sont automatiquement supprimées (**TTL - Time To Live**).

### 2. Comment faire les opérations de base ?

Toutes les opérations de base (CRUD) reposent sur un principe fondamental : l'accès direct par une clé unique.
Contrairement au SQL, il n'existe pas de clause `WHERE` ou de filtrage sur le contenu des valeurs : il faut impérativement connaître la clé pour agir sur la donnée.

Tout d'abord, nous avons la **Création et Mise à jour (Create / Update)** :
L'écriture s'effectue avec la commande `SET`. Si la clé n'existe pas, elle est créée. Si elle existe déjà, la valeur précédente est intégralement écrasée.
Pour modifier un champ précis d'un objet sans tout remplacer, il faut utiliser un hachage avec la commande `HSET`.

Puis la **Lecture (Read)** :
La récupération est instantanée avec une complexité en $O(1)$ via la commande `GET`.

Ensuite la **Suppression (Delete)** :
La suppression de la clé et de la valeur associée en mémoire se fait avec `DEL`.

Pour finir, la **Gestion de l'expiration (TTL)** :
Une spécificité centrale du modèle clé-valeur est la destruction automatique des données temporaires.
On définit un temps de vie lors de la création grâce au paramètre `EX`.

### 3. Pourquoi ça existe, forces et limites ?

Concept de base : si l'on dispose de la clé, on peut retrouver, modifier, manipuler la valeur associée facilement
Pratique notamment dans tout ce qui est lié à Internet ==> le réseau fonctionne beaucoup sur des ID ou des clés en tous genres, il est donc plus simple de passer directement par elles pour stocker puis rechercher des données

Posinégatif :<br/>
\+ Un accès simple et direct aux données<br/>
\+ Un concept simple et clair : une clé = une donnée, on extrait ou on modifie<br/>
\+ Correspond naturellement au fonctionnement de beaucoup de concepts, qui fonctionnent eux-mêmes avec un système de clef / ID ou autre moyen d'identification simple<br/>
\+ Flexibilité dans les valeurs stockées : la BDD n'a pas besoin d'être capable de comprendre les données qu'elle stocke, simplement d'une clef et d'une valeur, cette dernière pouvant prendre des types et des structures diverses sans nécessiter de réviser la structure même de la BDD<br/>
\- Cette flexibilité peut aussi poser problème, dans la mesure où l'absence de compréhension de la base par rapport aux données qu'elle stocke l'empêche conceptuellement de savoir ce qu'elle stocke. Par exemple, il n'est pas possible de vérifier que toutes les entrées dans la BDD contiennent les mêmes champs : à l'ID d'un client peuvent très bien être associés un nom et une adresse pour un, un numéro de téléphone et un prénom pour un autre, etc.<br/>
\- En écho au point précédent, cela signifie que la responsabilité de la mise en forme des données est déplacée de la base de données (en base relationnelle classique) vers l'application elle-même, qui doit gérer la forme, l'encodage, la compatibilité entre les versions ou encore la consistance des données<br/>
\- Les jointures sont difficiles à lire ou réaliser, notamment à cause de l'inconsistance possible dans les données<br/>
\- Les requêtes sont assez limitées, notamment quand il est question de requêtes imbriquées. Le modèle permet de retrouver une valeur directement associée à une clef, mais pas de retrouver d'autres données similaires stockées derrière une autre clef<br/>
\- Les requêtes complexes doivent être gérées par l'application à laquelle la BDD est rattachée, y compris des requêtes similaires aux fonctions "COUNT", "MIN" ou "AVG" disponibles par défaut dans une base de données relationnelle

### 4. Comparaison SQL vs Clé-Valeur

**SQL (SGBDR classique)** :<br/>
\+ Recherche par défaut parfois insensible à la casse dans la plupart des SGBDR (ex: `WHERE key ILIKE 'mykey'`)<br/>
\+ Prise en charge native de requêtes complexes, filtres avancés et jointures entre tables<br/>
\- Performances plus lentes (E/S disque, indexation lourde) et coût de calcul plus élevé<br/>

**Clé-Valeur (Redis)** :<br/>
\+ Temps de réponse sub-milliseconde grâce au stockage 100% en mémoire (RAM)<br/>
\+ Modèle ultra-rapide idéal pour la gestion de cache, de sessions ou de jetons temporaires<br/>
\- Correspondance exacte obligatoire sur la clé (sensible à la casse)<br/>
\- Aucune possibilité de faire des recherches complexes ou des filtres directement sur les attributs de la valeur<br/>
