[a4paper, 10pt]{article}
[utf8]{inputenc}
[T1]{fontenc}
[scale=0.9]{geometry}
[boxed, vlined, french]{algorithm2e}

{0cm}
{1ex plus 0.5ex minus 0.2ex}
{}
{{0.5mm}}
{rgb}{0.99,0.69,0.07}

    [scale=0.2]{images/amu2.png}

    Master 2 Intelligence Artificielle \& Apprentissage Automatique \\
    Aix-Marseille Université \\

  ## Problèmes d'optimisation sous contraintes (COP)

    ### Modélisation du problème

      Pour chaque instance du problème, nous disposons de diverses informations que nous regroupons par les notations suivantes.
      On note `n` le nombre de stations et `k` le nombre de régions de l'instance du problème. De plus, on note `L` l'ensemble des couples de stations qui souhaitent être en liaisons
      Soit `i  \{1,2,...,n \}`, on note :

        - Pour ` j  \{1,2,...,n \}, i<j`, `_{i,j}` qui correspond à l'écart minimum entre les fréquences des stations `i` et `j`. Cette valeur est nulle par défaut, et est non nulle lorsqu'elle est renseignée dans les données.
        - `n_{i}` le nombre maximum de fréquences différentes utilisées pour la région `i`
        - `_{i}` l'écart entre les deux fréquences de la station `i`
        - `r_{i}` le numéro de région de la station `i`

      Ainsi, nous pouvons définir l'instance ` = (X, D, C, f)` avec :

        - `X = \{ fe_i, fr_i |  i  \{1,2,...,n\}` tel que ` i  \{1,2,...,n\}`:

                - `fe_{i}` correspond à la fréquence pour l'émetteur de la station `i`.
                - `fr_{i}` correspond à la fréquence pour le récepteur de la station `i`.

        - `D = \{d_{fe_i}, d_{fr_i} |  i  \{1,2,...,n\} \}` où, ` i  \{1,2,...,n\}`

                - `d_{fe_i}` correspond à l'ensemble des valeurs de fréquences possibles pour la fréquence émetrice de la station `i`. Cet ensemble de valeur se retrouve dans le fichier de données.
                - `d_{fr_i}` correspond à l'ensemble des valeurs de fréquences possibles pour la fréquence réceptrice de la station `i`. Cet ensemble de valeurs se retrouve dans le fichier de données.

        - `C = C_1  C_2  C_3  C_4 ` où :

                - `C_1` modélise la contrainte que l'écart entre les deux fréquences d'une même station `i` doit être `_{i}`.\\
                 On note `C_{1,i} := \{ (d_{fe_i},d_{fr_i})~ tels~que~ | fe_{i} - fr_{i} | =  \}`. \\
                 Ainsi, `^{n} C_{1,i}}`
                - `C_2` modélise l'écart minimum à garantir entre les fréquences de deux stations `i` et `j`, on note :

                        - `C_{2A,i,j} := \{(d_{fe_i},d_{fe_j},d_{fr_i},d_{fr_j}) ~tels~que~ | d_{fe_i} - d_{fe_j} |  _{i,j} \}`
                        - `C_{2B,i,j} := \{(d_{fe_i},d_{fe_j},d_{fr_i},d_{fr_j}) ~tels~que~ | d_{fe_i} - d_{fr_j} |  _{i,j} \}`
                        - `C_{2C,i,j} := \{(d_{fe_i},d_{fe_j},d_{fr_i},d_{fr_j}) ~tels~que~| d_{fr_i} - d_{fe_j} |  _{i,j} \}`
                        - `C_{2D,i,j} := \{(d_{fe_i},d_{fe_j},d_{fr_i},d_{fr_j}) ~tels~que~ | d_{fr_i} - d_{fr_j} |  _{i,j} \}`

                      Ainsi, `^{n} C_{2A,i,j}  C_{2B,i,j}  C_{2C,i,j}   C_{2D,i,j}}`
                - `C_3` modélise que le nombre de fréquences différentes pour la région `t` est au maximum `n_t`. \\
                      On note, `C_{3,t} = nValues(\{fr_{i}, fe_{i} |  i  \{1,2,...,n \}, r_{i} = t \}, , n_{t})`. \\
                      Ainsi, `^{k} C_{3,t}}`
                - `C_4` modélise que si les stations `i` et `j` doivent pouvoir communiquer, alors la fréquence émétrice de l'une correspond à la fréquence réceptice de l'autre, et inversement. \\
                On note, ` := \{ (d_{fe_i},d_{fe_j},d_{fr_i},d_{fr_j})~tels~que~d_{fr_i} = d_{fe_j}~et~d_{fe_i} = d_{fr_j} \} }` \\
                Ainsi, `^{|L|} C_{4,r}}`

          - `f` est la fonction objectif qui va dépendre du cas dans lequel on se trouve. Nous allons donner sa définition dans chaque cas dans les sous-parties suivantes.

        Dans le premier cas, nous souhaitons minimiser le nombre de fréquences utilisées. Pour ce faire, nous avons choisi de définir la fonction objectif comme suit :
        `$ }  nValue(\{ e_{i}, r_{i} |  i  \{1,2,...,n \}, =, m) }`$

        Intuitivement, la contrainte globale `nValue` permet de fixer le nombre de valeurs de fréquences différentes, émétrice et réceptrice mélangées, à `m`. Ainsi, on souhaite minimiser la valeur de `m`, ce qui correspond à notre problème.

        Dans ce deuxième cas, l'objectif est d'utiliser les valeurs de fréquences les plus basses possibles. Pour ce cas, nous avons eu deux points de vue différent. Ainsi, nous avons défini deux fonctions objectif différentes. Les voici :

          - On parlera ici du `CAS 2`. On défini la fonction objectif suivante :
                `$ } _{i=1}^{n} fe_i + fr_i } `$

                Intuitivement, cette fonction cherche à minimiser la somme totale des fréquences, en encourageant l'utilisation des fréquences les plus basses pour chaque station.

           - On parlera dans ce cas du `CAS 2BIS`. On défini la fonction objectif par :
                 `$  fe_i , _{i} fr_i \} \}} `$
                 Intuitivement, on prend la plus grande valeur des fréquences émétrice, de même pour les fréquences réceptrice, on prend la plus grande des deux et on tente de la rendre la plus petite possible. Ainsi, on prend la valeur de fréquence la plus grande et on tente de la minimiser, ce qui va forcer toutes les autres à être minimisées.

        Dans ce troisième et dernier cas, on souhaite minimiser la largeur de la bande de fréquences utilisées, c'est-à-dire, l'écart entre la plus basse et la plus haute fréquence. Intuitivement cela se traduit par la fonction objectif suivante :
        `$  | _{} \{_{j} fe_j, _{j} fr_j\}  - _{} \{_{j} fe_j, _{j} fr_j\}  |} `$

    ### Résultats d'expériences

      Pour ces expériences, nous avons utilisées un ordinateur avec la configuration matériel suivante :

        - CPU : i5-12450H  (jusqu'à 4.4GHz)
        - Taille de la RAM (mémoire) : 16 GB

      Nous avons choisi d'utiliser le langage python, en utilisant la bibliothèque PyCSP3 permettant la modélisation et la résolution des COP. Concernant la résolution, nous avons décidé d'utiliser deux solveurs différents. Le premier étant le solveur choco, le deuxième étant le solveur ace. Ce sont deux solveurs disponibles dans la bibliothèque PyCSP3. Pour des questions pratiques, nous avons limité les temps d'exécution à 10 minutes par instance et par solveur.

        Nous avons réuni les valeurs des fonctions objectifs dans le tableau qui suit, en fonction des cas. Ces valeurs sont identiques quel que soit le solveur utilisé puisque nous utilisons des solutions complètes qui ne dépendent uniquement des données, et non de la méthode de résolution. \\
        Le tableau est découpé en quatres paquets de lignes. Le premier paquet de lignes correspond à des intances avec 150 stations et 15 régions. Le deuxième à des instances avec 250 stations et 25 régions. Le troisième à des instances avec 500 stations et 30 régions. Et pour finir, le dernier paquet correspond à des instances avec 50 stations et 7 régions. \\
        De plus, les [gray]{0.6}{T.O} *(Time Out)* dans le tableau signifie que les solveurs ont été arrêtés avant la fin de l'éxecution.
        [!h]

          { |c|c|c|c|c| }

          **Nom du fichier** & **CAS 1** & [gray]{0.6}{**CAS 2**}   & **CAS 2 BIS** & **CAS 3** \\

           & 8 & [gray]{0.6}{ T.O} & 364 & 350\\

           & 8 & [gray]{0.6}{ T.O} & 462  &  448\\

           & 8 & [gray]{0.6}{ T.O} & 406 &  378\\

           & 8 & [gray]{0.6}{ T.O} & 462 & 448\\

           & 8 & [gray]{0.6}{ T.O} & 378 & 364 \\

           & 6 & [gray]{0.6}{ T.O} &  308 & 294 \\

           & 8 & [gray]{0.6}{ T.O} & 476 & 462\\

           & 6 & [gray]{0.6}{ T.O} & 308 &  294\\

           & 8 & [gray]{0.6}{ T.O} &406  &378  \\

           & 6 & [gray]{0.6}{ T.O} & 308 & 294 \\

           & 6 & [gray]{0.6}{ T.O} & 364&  350\\

           & 8 & [gray]{0.6}{ T.O} & 308  &  294\\

           & 8 & [gray]{0.6}{ T.O} & 406  & 392\\

           & [gray]{0.6}{ T.O} & [gray]{0.6}{ T.O} & 308 &  294\\

           & 6 & [gray]{0.6}{ T.O} &350  & 336 \\

           & 6 & [gray]{0.6}{ T.O} & 378 & 364 \\

           & 6 & [gray]{0.6}{ T.O} & 378 & 364 \\

           & 6 & [gray]{0.6}{ T.O} & 280 &  238\\

           & 6 & [gray]{0.6}{ T.O }&280 & 252 \\

        Raisonnons cas par cas.

          - **CAS1**. On remarque que seulement deux valeurs différentes apparaissent : `6` et `8`. Pour rappel, dans ce cas nous souhaitions minimiser le nombre de fréquences utilisées. Ainsi, ces valeurs correspondent au nombre de fréquences utilisées pour l'instance concernée.
          Il est étonnant de voir que celà ne semble pas dépendre du nombre de stations. En effet, même avec 500 stations on arrive à utiliser seulement `6` fréquences différentes. Nous avions imaginé que plus on a de stations, plus on aurait besoin d'utiliser un nombre de fréquences grand au vue des possibles conflits. Mais finalement, ce sont les conflits qui vont définir le nombre de fréquences nécessaire, et le nombre de conflit n'est pas en lien direct avec le nombre de stations, ce qui explique pourquoi, avec le recul, les résultats ne sont pas si étonnant.
          - **CAS2**. Dans ce cas là, malheureusement, aucune exécution n'a abouti.
          - **CAS2BIS**. Ici, nous souhaitions utiliser les valeurs de fréquences les plus basses possible. Les valeurs du tableau indique quelle est la plus grande valeur de fréquence utilisée pour l'instance correspondante. Encore une fois, on retrouve parfois des valeurs similaires, indépendemment du nombre de stations et/ou du nombre de régions. Celà est beaucoup moins étonnant puisque les domaines de fréquences ne dépendent pas du nombre de stations ou de régions.
          - **CAS3**. L'objectif de ce dernier cas était de minimiser la largeur de la bande de fréquences utilisées. Ainsi, les valeurs du tableau représente l'écart entre la plus basse et la plus haute fréquence utilisées. Encore une fois, on ne retrouve pas un *pattern* particulier en fonction des instances.

        Nous avons réuni dans les tableaux suivant les temps d'exécution pour les 4 cas différentes. Le tableau de gauche correspond aux temps d'execution lorsqu'on utilise le solveur choco, tandis que le tableau de droite correspond au solveur ace. Il est important de préciser que nous avons limité le temps d'exécuton à 10 minutes.

        [t]{0.5}

          { |c|c|c|c|c| }

            **Nom du fichier** & **CAS 1** & [gray]{0.6}{**CAS 2**}   & **CAS 2 BIS** & **CAS 3** \\

             & {9,114s} & [gray]{0.6}{ 10m0,003s} & 1,875s& {1,775s}\\

             & {8,746s} & [gray]{0.6}{ 10m0,003s} & {1,768s} & 2,177s \\

             &{ 23,106s} & [gray]{0.6}{ 10m0,003s} & {2,432s} & 9,770s \\

             & {9,103s} & [gray]{0.6}{ 10m0,003s} & 3,863s & {4,869s} \\

             & 14,385s & [gray]{0.6}{ 10m0,006s} & {8,735s} & {14,841s}\\

             & {20,851s} & [gray]{0.6}{ 10m0,003s} & {12,317s} & 15,637s \\

             &{ 21,368s} & [gray]{0.6}{ 10m0,014s} & {10,138s} & 15,675s \\

             & {24,417s} & [gray]{0.6}{ 10m0,004s} & {13,985s} & 18,861s \\

             & {1m25,918s} & [gray]{0.6}{ 10m0,009s} & {17,085s} & 23,151s \\

             & {30,516s} & [gray]{0.6}{ 10m0,004s} & {12,427s} & 16,081s\\

             & {1m5,376s} & [gray]{0.6}{ 10m0,008s} & {22,674s} & 32,296s \\

             & {1m48,111s} & [gray]{0.6}{ 10m0,009s} & {23,076s} & 1m4,631s \\

             & {1m37,911s} & [gray]{0.6}{ 10m0,008s} & {18,963s} & 44,055s \\

             & [gray]{0.6}{10m0,016s} & [gray]{0.6}{ 10m0,017s} & {21,797s} & {50,926s} \\

             &{ 15,259s} & [gray]{0.6}{ 10m0,003s} & {7,826s} & 10,754s \\

             & 14,113s & [gray]{0.6}{ 10m0,067s} & {8,736s} & {21,748s} \\

             & {12,067s} & [gray]{0.6}{ 10m0,071s} & {6,799s} & 7,601s \\

             & {28,409s} & [gray]{0.6}{ 10m0,006s} & {7,375s} & 8,325s \\

             & {13,511s} & [gray]{0.6}{ 10m0,003s }& 8,190s & {7,660s} \\

          ~\\

          ** Tableau des résultats avec le solveur Choco** % C'est le titre de la minipage

       [t]{0.6}

           { |c|c|c|c|c| }

             **Nom du fichier** & **CAS 1** &[gray]{0.6}{ **CAS 2**} & **CAS 2 BIS** & **CAS 3** \\

              & {9,148s} & [gray]{0.6}{10m0,003s} & {1,934s} & 2,080s\\

              & **} & [gray]{0.6}{10m0,003 }& {2,045s} & 2,819s \\

              & {38,114s} & [gray]{0.6}{10m0,003s} & {3,033s} & **8,701s** \\

              & {11,311s} & [gray]{0.6}{10m0,003s} & {6,704s} & 8,018s \\

              & {19,314s} & [gray]{0.6}{10m0,003s} & {9,039s} & 16,969s \\

              & {22,871s} & [gray]{0.6}{10m0,003s} & {12,827s} & 15,720s \\

              & **} & [gray]{0.6}{10m0,040s} & {13,023s} & 17,823s \\

              & **} & [gray]{0.6}{10m0,003 }& **} & **15,649s** \\

              & **}& [gray]{0.6}{10m0,004s} &** } & **21,511s** \\

              & **} & [gray]{0.6}{10m0,017s} & {14,780s} & 20,984s \\

              & {1m17,392s} & [gray]{0.6}{10m0,069s} & {23,233s} & 36,927s \\

              & {1m37,635s} & [gray]{0.6}{10m0,008s} & {18,379s} & 49,842s \\

              & {1m42,731s} & [gray]{0.6}{10m0,018s} & 1m2,116s & {51,214s} \\

              & [gray]{0.6}{10m0,011s} & [gray]{0.6}{10m0,009s} &  {22,408s} & **} \\

              &** } & [gray]{0.6}{10m0,003s} & {8,766s} & **10,333s** \\

              & **13,005s** & [gray]{0.6}{10m0,003s} & {8,972s} & **} \\

              & {37,418s} & [gray]{0.6}{10m0,073s} & **} & **7,170s** \\

              & **} & [gray]{0.6}{10m0,007s} & {8,416s} & **10,006s** \\

              & **} & [gray]{0.6}{10m0,068s} & **7,770s** & {7,660s} \\

         ~\\\\

         ** Tableau des résultats avec le solveur Ace** % C'est le titre de la minipage

       Nous avons mis en gris les temps correspondant à des non-aboutissements, c'est-à-dire que le processus a été arrêté en cours d'exécution, au bout de 10 minutes.

         - Concernant le *CAS 2*, nous observons une absence totale de résultats aboutis. Cette situation contraste fortement avec le *CAS 2 BIS*, qui a systématiquement abouti à des résultats. Cette différence pourrait suggérer que la fonction objectif définie dans le *CAS 2* est soit mal adaptée, soit trop complexe pour être traitée efficacement par le solveur utilisé. Cette distinction entre les deux cas souligne l'importance d'une formulation adéquate de la fonction objectif dans la résolution de problèmes de programmation sous contrainte.
         - Généralement, on remarque que le solveur Choco est plus efficace en terme de temps que le solveur Ace. Les valeurs dans le tableau de droite sont en gras lorsque le temps d'exécution est plus faible en utilisant le solveur Ace qu'en utilisant le solveur choco.
         - On peut voir que dans la plus part des instances, le *CAS 2 BIS* à le plus faible temps d'exécution.

  ## Problèmes de satisfaction de contraintes valués

    ### Modélisation du problème

      Pour chaque instance du problème, nous disposons de diverses informations que nous regroupons par les notations suivantes.
      On note `n` le nombre de stations et `k` le nombre de régions de l'instance du problème. De plus, on note `L` l'ensemble des couples de stations qui souhaitent être en liaison.
      Soit `i  \{1,2,...,n \}`, on note :

        - Pour ` j  \{1,2,...,n \}, i<j`, `_{i,j}` qui correspond à l'écart minimum entre les fréquences des stations `i` et `j`. Cette valeur est nulle par défaut, et est non nulle si elle est renseignée dans les données.
        - `n_{i}` le nombre maximum de fréquences différentes utilisées pour la région `i`
        - `_{i}` l'écart entre les deux fréquences de la sation `i`
        - `r_{i}` le numéro de région de la station `i`

      Ainsi, nous pouvons définir l'instance ` = (X, D, W, SV)` avec :

        - `X = \{ fe_i, fr_i |  i  \{1,2,...,n\}` tel que ` i  \{1,2,...,n\}`:

                - `fe_{i}` correspond à la fréquence pour l'émetteur de la station `i`.
                - `fr_{i}` correspond à la fréquence pour le récepteur de la station `i`.

        - `D = \{d_{fe_i}, d_{fr_i} |  i  \{1,2,...,n\} \}` où, ` i  \{1,2,...,n\}`

                - `d_{fe_i}` correspond à l'ensemble des valeurs de fréquences possible pour la fréquence émetrice de la station `i`. Cet ensemble de valeurs se retrouve dans le fichier de données.
                - `d_{fr_i}` correspond à l'ensemble des valeurs de fréquences possible pour la fréquence réceptrice de la station `i`. Cet ensemble de valeurs se retrouve dans le fichier de données.

        - `W` :

                - L'écart entre les deux fréquences d'une même station doit être `_{i}` pour toute sation `i`. Cette contrainte est matérielle, on la met donc en contrainte dure. Ainsi, on la définie par :
                 `| fe_{i} - fr_{i} | = ` `$  0  + `$ 

                 - L'écart minimum à garantir entre les fréquences des stations `i` et `j`. Pour cette contrainte, on a décidé de la catégoriser en tant que contrainte douce. La raison est que l'on estime que les interférences ont un impacte moindre puisque les stations ne rentrent pas forcément en communication. Le poids d'une contrainte violée est `_{i,j}` car on souhaite que plus l'écart demandé est grand, plus la contrante doit être satisfaite.

                          - `| fe_i - fe_j |  _{i,j}  {0}, {_{i,j}}`
                          - `| fe_i - fr_j |  _{i,j}  {0}, {_{i,j}}`
                          - `| fr_i - fe_j |  _{i,j}  {0}, {_{i,j}}`
                          - `| fr_i - fr_j |  _{i,j}  {0}, {_{i,j}}`

                 - Pour que les stations `i` et `j` puissent communiquer, on doit avoir que la fréquence réceptrice de l'une soit la fréquence émetrice de l'autre, et inversement. Cependant, nous passons cette contrante en contrainte douce puisqu'avoir toutes les stations concernées en communications implique que le problème n'a pas de solution. L'objectif est donc d'avoir tout de même certaines liaisons possible. On écrit donc la contrainte :
                 `$( fr_i = fe_j~et~fe_i = fr_j ) {0}, {max_{Delta}}`` où `max_{Delta} = _{i,j} Delta_{i,j}$ Nous avons décidé de prendre le même poids pour chaque contrainte de liaisons car nous n'avons pas d'informations sur quelles pourraient être les liaisons les plus importantes, nous mettons donc toutes les liaisons au même niveau. De plus, nous avons trouver cela logique de prendre la valeur maximale des poids des contraintes douces qui concernent les interférences puisque les liaisons sont des contraintes plus importantes à nos yeux. De plus, si nous n'établissons pas de liaisons entre les stations, gérer les interférences n'est plus aussi important.

          - `SV = (  \{ +  \}, , +, 0, +)`

    ### Résultats d'expériences
      Pour ces expériences, nous avons utilisées un ordinateur avec la configuration matériel suivante :

        - CPU : 11th Gen Intel(R) Core(TM) i9-11950H @ 2.60GHz
        - Taille de la RAM (mémoire) : 117 Gi de disponible

      Nous avons décidé d'implémenter un programme en langage Python afin qu'à partir d'une fichier de donnée type JSON, nous en déduisons le fichier au format WCSP correspondant. Ainsi, nous donnons le fichier WCSP au solveur Toulbar2 utilisé pour résoudre les différentes instances. Pour des questions pratiques, nous avons limité le temps d'exécution à 10 minutes via l'option proposé par le solveur. De plus, nous avons uniquement utilisé ce solveur, cependant nous avons décidé de regarder différentes options qu'il propose. Nous avons donc établi 4 types de test :

        - **TEST 1**. Pour ce test, nous avons ni activé, ni modifié les options du solveur. Ce test nous permet d'avoir une base de comparaisons pour les autres.
        - **TEST 2**. Pour ce test, nous avons décidé de limiter le nombre de *backtack* (**-bt**) à `10000`. Par défault, cette valeur est `9223372036854775807`, cela équivaut à dire qu'il n'existe pas réellement de limite de *backtracking*. Limiter cette valeur peut permettre de forcer le solveur à changer de stratégie de résolution. En effet, par défault il optera pour une stratégie de *backtracking* chronologique, c'est-à-dire qu'il revient à la dernière décision non explorée dans l'ordre chronologique dans lequel les décisions ont été prises. En limitant cette valeur, il peut arriver qu'il ne puisse pas utiliser cette stratégie.
        - **TEST 3**. Pour ce troisième test, on a modifié l'option **-p**. Cette option permet d'activer un prétraitement des WCSP, toujours en limitant le nombre de *backtrack*. En effet, par défault la valeur est à `-1` ce qui implique qu'il n'y a pas ce prétraitement. Nous avons fixé sa valeur à `3`. Cette option indique que le solveur va se concentrer sur la simplification et la réduction du problème mais ne cherchera pas à trouver une solution complète. L'option activé implique une élimination des variables de degrès inferieur à la valeur de *p*. Ainsi, dans notre cas, nous avons décidé que toutes les variables de degrès inférieur ou égal à `3` seraient supprimé du problème. Pour rappel, le degré d'une variable correspond au nombre de contraintes dans lesquels la variable apparait.
        - **TEST 4**. Pour ce dernier type de test, nous avons décidé de modifier l'option **-e** qui par défault vaut `3`., toujours en limitant le nombre de *backtrack*. Cette option implique que la recherche par *boosting* avec élimination de variable de degré inférieur ou égale à la valeur de *e*. Nous avons décidé de mettre cette valeur à `2` pour voir si celà changeait quelque chose lors de la résolution. Cette option concerne l'utilisation de l'élimination de variables pour accélerer la recherche dans la résolution de WCSP. Le solveur va retirer certaines variables du problème pour réduire sa complexité. Nous avons choisi une valeur inférieure à la valeur par défaut pour voir la différence notamment en terme de temps de calcul qui devrait être plus élevé dans ce cas là, car on obtient un problème plus complexe car moins réduit. A la différence du **TEST 3**, cette élimination n'est pas fait en prétraitement.

      Nous avons regroupé nos résultats dans les tableaux qui suivent. D'une part, nous avons sauvegardé les résultats *(primal bound)* donnés en fin d'exécution de Toulbar2. D'autre part, nous avons retenu les temps d'exécutions.

        [t]{0.5}

            {| c | c | c| c| c |}

              **Nom du fichier** & **TEST 1** & **TEST 2** & **TEST 3** & **TEST 4** \\

              celar\_50\_7\_10\_5\_0.800000\_0 & [gray]{0.6}{T.O}  & {1000} & 1050 & {1000}  \\

              celar\_50\_7\_10\_5\_0.800000\_1 &  [gray]{0.6}{T.O} & 800 & {750} & 800 \\

              celar\_50\_7\_10\_5\_0.800000\_4 & [gray]{0.6}{T.O}  & 350 & 350 & 350 \\

              celar\_50\_7\_10\_5\_0.800000\_9 & [gray]{0.6}{T.O}  & {350} & 400  & {350}  \\

              celar\_50\_8\_10\_5\_0.800000\_8 & [gray]{0.6}{T.O} & 550 & {450} & 550 \\

              celar\_150\_13\_15\_5\_0.800000\_2 & [gray]{0.6}{T.O} & 890 & {850} & 890\\

              celar\_150\_13\_15\_5\_0.800000\_9 & [gray]{0.6}{T.O} & 1420 & {1250} & 1420 \\

              celar\_150\_13\_15\_5\_0.800000\_18 & [gray]{0.6}{T.O} & 1580 & {1540} & 1580 \\

              celar\_150\_13\_15\_5\_0.800000\_20 & [gray]{0.6}{T.O} & 1250 & 1250 & 1250\\

              celar\_150\_13\_15\_5\_0.800000\_25 & [gray]{0.6}{T.O} & 1180 & {1140} & 1180 \\

              celar\_250\_25\_15\_5\_0.820000\_0 & [gray]{0.6}{T.O} & 1800 & {1630} & 1800\\

              celar\_250\_25\_15\_5\_0.820000\_6 & [gray]{0.6}{T.O} & 1640 & {1440} & 1640  \\

              celar\_250\_25\_15\_5\_0.820000\_8 &[gray]{0.6}{T.O}  & 1440 & {1350} & 1440\\

              celar\_250\_25\_15\_5\_0.820000\_17 & [gray]{0.6}{T.O} & 1700 & {1500} & 1700 \\

              celar\_250\_25\_15\_5\_0.820000\_29 & [gray]{0.6}{T.O}  &  1550 & {1450} & 1550 \\

              celar\_500\_30\_20\_5\_0.870000\_0 & [gray]{0.6}{T.O} & 2750 & {2650} & 2750 \\

              celar\_500\_30\_20\_5\_0.870000\_8 & [gray]{0.6}{T.O} & 3350 & {3250} & 3350  \\

              celar\_500\_30\_20\_5\_0.870000\_25 & [gray]{0.6}{T.O} & 3800 & {3570} & 3800  \\

              celar\_500\_30\_20\_5\_0.870000\_30 &  [gray]{0.6}{T.O} & 3050 & {2950} & 3050 \\

              celar\_500\_30\_20\_5\_0.870000\_49 &[gray]{0.6}{T.O}  & 3140 & {3090} & 3140  \\

          ~\\

          ** Tableau des bornes maximale des fonctions de coût** % C'est le titre de la minipage

       [t]{0.6}

         {| c | c | c| c| c |}

           **Nom du fichier** & **TEST 1** & **TEST 2** & **TEST 3** & **TEST 4** \\

           celar\_50\_7\_10\_5\_0.800000\_0 & [gray]{0.6}{T.O} & {0.869s} & 5.757s & 0.919s  \\

           celar\_50\_7\_10\_5\_0.800000\_1 & [gray]{0.6}{T.O}  & 0.745s & 9.205s & {0.706s} \\

           celar\_50\_7\_10\_5\_0.800000\_4 & [gray]{0.6}{T.O}&{0.034s} & 3.031s & {0.034s} \\

           celar\_50\_7\_10\_5\_0.800000\_9 &  [gray]{0.6}{T.O} &{ 1.675s} & 4.25144s & 1.684s \\

           celar\_50\_8\_10\_5\_0.800000\_8 & [gray]{0.6}{T.O} & {1.055s} & 9.333s & 1.060s  \\

           celar\_150\_13\_15\_5\_0.800000\_2 & [gray]{0.6}{T.O} & 0.726s & 8.037s & {0.723s} \\

           celar\_150\_13\_15\_5\_0.800000\_9 & [gray]{0.6}{T.O} & {1.121s} & 10.644s & 1.162s  \\

           celar\_150\_13\_15\_5\_0.800000\_18 & [gray]{0.6}{T.O} &{ 0.877s }&  20.548s & 0.965s \\

           celar\_150\_13\_15\_5\_0.800000\_20 & [gray]{0.6}{T.O} & {1.062s} & 4.927s & 1.065s \\

           celar\_150\_13\_15\_5\_0.800000\_25 &  [gray]{0.6}{T.O}& 0.948s & 5.837s & {0.895s } \\

           celar\_250\_25\_15\_5\_0.820000\_0 &  [gray]{0.6}{T.O} & 0.819s & 30.339s & {0.810s} \\

           celar\_250\_25\_15\_5\_0.820000\_6 & [gray]{0.6}{T.O} &{ 0.694s} & 34.476s & 0.696s  \\

           celar\_250\_25\_15\_5\_0.820000\_8 & [gray]{0.6}{T.O} & 0.690s & 26.214s & {0.687s} \\

           celar\_250\_25\_15\_5\_0.820000\_17 & [gray]{0.6}{T.O} &{0.778s} & 27.572s & {0.778s} \\

           celar\_250\_25\_15\_5\_0.820000\_29 & [gray]{0.6}{T.O}  &  0.817s & 25.092s & {0.809s} \\

           celar\_500\_30\_20\_5\_0.870000\_0 & [gray]{0.6}{T.O} & {0.914s} & 52.039s & 0.927s  \\

           celar\_500\_30\_20\_5\_0.870000\_8 & [gray]{0.6}{T.O} & 0.887s & 45.885s & {0.872s} \\

           celar\_500\_30\_20\_5\_0.870000\_25 & [gray]{0.6}{T.O} & 0.995s & 52.014s & {0.989s} \\

           celar\_500\_30\_20\_5\_0.870000\_30 & [gray]{0.6}{T.O} &  {1.016s} & 36.721s & 1.022s \\

           celar\_500\_30\_20\_5\_0.870000\_49 &[gray]{0.6}{T.O}  &  {0.951s} & 34.141s & 0.982s \\

         ~\\\\

         ** Tableau des temps d'execution** % C'est le titre de la minipage

       Dans le tableau de droite, les valeurs en {vertes} sont les temps d'exécution les plus bas, tant dis que dans le tableau de gauche ce sont les bornes les plus basses. \\

       La première remarque est que le **TEST 1** n'a jamais aboutie. Ainsi, pour éviter ceci dans les autres cas, nous avons dû limiter le nombre de *backtracking*. \\

       On remarque que la plus part des bornes minimales se trouvent dans la colonne de **TEST 2**, alors que les temps d'execution de celui-ci est en général bien plus grand que celui des autres tests. \\

       Bien que **TEST 2** présente les meilleures bornes minimales, son temps d'exécution global est plus élevé. Cela suggère une efficacité variable, où le test peut rapidement identifier une borne minimale mais prend plus de temps pour compléter l'ensemble du processus. Cela peut être dû à une complexité algorithmique plus élevée ou à un besoin accru de ressources computationnelles. \\

       La différence entre les temps d'exécution les plus bas et les temps d'exécution plus élevés dans les autres tests indique un équilibre nécessaire entre la rapidité de trouver une solution et l'efficacité globale du processus. Optimiser pour l'un peut entraîner des compromis dans l'autre, soulignant l'importance de choisir la bonne stratégie en fonction des exigences spécifiques de chaque situation.

## Conclusion

Ce projet a été une exploration approfondie des techniques de résolution de problèmes de programmation par contrainte et de recherche opérationnelle. Nous avons mis en œuvre plusieurs tests algorithmiques, chacun conçu pour évaluer différentes stratégies dans la résolution de différent problèmes. Notre objectif était de comprendre comment différentes approches affectent la performance, notamment en termes de temps d'exécution et d'efficacité dans la recherche de solutions ou bornes optimale.

Nous avons également rencontré des défis, notamment avec le Test 1 (WCSP), qui n'a pas abouti dans de nombreux cas. Cette difficulté a été surmontée en limitant le nombre de backtracking, ce qui a permis d'éviter les échecs d'exécution tout en obtenant des résultats significatifs. Cette adaptation a souligné l'importance de la flexibilité et de l'ajustement des approches en fonction des limites et des exigences de l'environnement d'exécution.

Pour l'avenir, il y a plusieurs domaines d'amélioration possibles. Premièrement, une exploration plus approfondie des algorithmes de backtracking et de leur optimisation pourrait améliorer l'efficacité des tests. Enfin, une analyse plus détaillée des caractéristiques spécifiques des différents problèmes pourrait nous permettre de personnaliser davantage les stratégies algorithmiques pour chaque cas.

En conclusion, ce projet a non seulement renforcé notre compréhension des techniques de programmation par contrainte et de recherche opérationnelle, mais a également mis en lumière l'importance de la flexibilité et de l'adaptation dans le choix des stratégies algorithmiques. Les leçons apprises ici sont précieuses pour de futures recherches et applications dans ce domaine.









# Projet de Recherche Opérationnelle et Programmation par Contrainte

## Description du Projet
Ce projet a pour objectif d'explorer et de comparer différentes techniques de résolution de problèmes en recherche opérationnelle et programmation par contrainte dans le contexte de l'UE MRO du Master 2 Intelligence Artificielle et Apprentissage Automatique de d'Aix-Marseille Université. 
Nous avons mis en œuvre et évalué diverses stratégies algorithmiques pour comprendre leur impact sur les performances, notamment en termes de temps d'exécution et d'efficacité dans la recherche de solutions optimales.

Réalisé par Manon Girard, Victor Tancrez, Paul Peyssard.

Encadré par Cyril Terrioux.
