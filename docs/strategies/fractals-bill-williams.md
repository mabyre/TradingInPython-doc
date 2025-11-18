# Fractales de Bill Williams

L'indicateur technique des Fractales de Bill Williams est utilisé pour identifier des points potentiels de {{ "retournement du marché" | keyword }}.
Une fractale up marque une résistance locale. Une fractale down marque un support local.

## Alorithme de démonstration

- {{ "Fractale Up" | keyword }} Sommet local PERIOD = 2 -> Retournement Baissier

La bougie centrale (n) possède un plus haut supérieur aux deux bougies qui la précèdent et aux deux bougies qui la suivent :

```Python
High[n] > High[n-1]
High[n] > High[n-2]
High[n] > High[n+1]
High[n] > High[n+2]
```

- {{ "Fractale Down" | keyword }} Creux local PERIOD = 2 -> Retournement Haussier

La bougie centrale (n) possède un plus bas inférieur aux deux bougies qui la précèdent et aux deux bougies qui la suivent :

```Python
Low[n] < Low[n-1]
Low[n] < Low[n-2]
Low[n] < Low[n+1]
Low[n] < Low[n+2]
```

## Ojectifs

Identifier des points de retournement possibles de la tendance.

Mettre en évidence la structure du marché.

Fournir des niveaux d'entrée potentiels pour des stratégies de {{ "Breakout" | g_tooltip }} ou de {{ "Pullback" | g_tooltip }}.

## Implémentation

Un paramètre dans la fenêtre de configuration : PERIOD

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/fractale-bill-williams/graphe1.png" class="glightbox" data-gallery="galerie" title="Fractales de Bill Williams">
        <img src="{{ base_url }}/images/strategies/fractale-bill-williams/graphe1.png" alt="Fractales de Bill Williams"/>
    </a>
    <figcaption><em>Implémentation</em></figcaption>
</figure>

- **(1)** L'algorithme travaille sur les prix Haut (High) et Bas (Low) qui sont affichés
- **(2)** Choix de la PERIOD des fractales = 2
- **(3)** {{ "Fractale Down" | keyword }} les croix montrent des prix plus haut à deux de distance -> retournement haussier
- **(4)** {{ "Fractale Up" | keyword }} les croix montrent des prix plus bas à deux de distance -> retournement baissier

## Fractale Down

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/fractale-bill-williams/graphe2.png" class="glightbox" data-gallery="galerie" title="Fractale Down">
        <img src="{{ base_url }}/images/strategies/fractale-bill-williams/graphe2.png" alt="Fractale Down"/>
    </a>
    <figcaption><em>Fractale Down</em></figcaption>
</figure>

La Fractale Down nous indique un retournement du marché à la Hausse

## Fractale Up

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/fractale-bill-williams/graphe3.png" class="glightbox" data-gallery="galerie" title="Fractale Up">
        <img src="{{ base_url }}/images/strategies/fractale-bill-williams/graphe3.png" alt="Fractale Up"/>
    </a>
    <figcaption><em>Fractale Up</em></figcaption>
</figure>

La Fractale Up nous indique un retournement du marché à la Baisse

Fractale Down PERIODE: 3

## Fractale PERIOD 5

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/fractale-bill-williams/graphe4.png" class="glightbox" data-gallery="galerie" title="Fractale PERIOD 5">
        <img src="{{ base_url }}/images/strategies/fractale-bill-williams/graphe4.png"/>
    </a>
    <figcaption><em>Fractale PERIOD 5</em></figcaption>
</figure>

Avec une période égale à 5 vous voyez les fractales consolider les supports et les résitances du cours. 

## Combinaison avec l'Alligator

- Filtre directionnel avec l'Alligator

Stratégie originale de Bill Williams :

- **acheter** uniquement au-dessus des fractales up situées au-dessus de la mâchoire de l’Alligator,

- **vendre** uniquement sous les fractales down situées sous la mâchoire.

Cela évite les faux signaux dans les phases de range.

## Fractales pour valider un breakout

Un {{ "Breakout" | g_link }} valide signifie :

- "Le marché a finalement assez de force pour casser une zone où il avait échoué."

Une fractale up montre un sommet où la hausse a buté.

Si plus tard, le prix casse ce sommet, cela montre une accélération haussière.

La cassure de cette fractale sert d’ordre d’achat logique.

C’est exactement ce que proposait Bill Williams :

Placer des ordres "buy stop" au-dessus des fractales up, et des "sell stop" en dessous des fractales down.

Cela revient à dire :

"J’entre seulement si le marché prouve qu’il dépasse un obstacle important."

Donc :

Les fractales donnent des niveaux objectifs pour des breakouts validés.

## Fractales pour valider un pullback

Lorsqu’un prix casse une fractale, il revient très souvent la retester, c'est un {{ "Pullback" | g_link }}

Ce phénomène est classique en analyse technique :

- une résistance cassée devient support,
- un support cassé devient résistance.

Les fractales fonctionnent très bien dans ce rôle parce qu’elles représentent déjà :

- un point extrême local,
- fortement défendu précédemment.

Donc, si le prix casse une fractale puis revient dessus, ce niveau devient :

- un point bas pour acheter (pullback haussier),
- un point haut pour vendre (pullback baissier).

## Résumé

| Type de fractale   | Rôle              | Utilisation                                      |
| ------------------ | ----------------- | ------------------------------------------------ |
| Fractale Up        | Résistance locale | Achat sur breakout au-dessus / achat sur retest  |
| Fractale Down      | Support local     | Vente sur breakout en dessous / vente sur retest |
