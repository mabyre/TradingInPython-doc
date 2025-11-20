# Gator Alligator de Bill Williams

L'indicateur technique {{ "Alligator" | keyword }} et son histogramme le Gator est inventé par Bill Williams en 1995.

C'est la fameuse {{ "parabole du marché" | keyword }} par Bill Williams, le marché se comporte comme un Alligator :

- Il {{ "dort" | keyword }} : Les trois lignes sont entrelacées ou proches, le marché est en phase de consolidation, sans tendance claire. Il vaut mieux éviter de trader.
- Il {{ "se réveille" | keyword }} : Les lignes commencent à s'écarter, une nouvelle tendance potentielle émerge.
- Il {{ "mange" | keyword }} : Les trois lignes sont bien séparées et alignées dans le même sens, forte tendance en cours. C'est le moment idéal pour suivre la tendance.
- Il {{ "est repu" | keyword }} : Les lignes se rapprochent après s'être écartées, la tendance faiblit, il est temps de sécuriser ses gains.

Le {{ "Gator" | keyword }} est l'histogramme qui mesure la distance entre les lignes de l'{{ "Alligator" | keyword }} avec deux parties l'une au-dessus et en dessous de zéro. 

Il permettet de visualiser rapidement les phases d'expansion et de contraction de la tendance.

Cet indicateur est particulièrement apprécié pour sa {{ "simplicité visuelle" | keyword }} et son efficacité à identifier les périodes de trading favorables.

## Interface

Voici l'interface de cet indicateur. Ici on a affiché les Fractales de Bill Williams pour une stratégie complète de trading sur les {{ "pullback" | g_link }} et les {{ "breakout" | g_link }}.

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/gator-alligator/interface.png" class="glightbox" data-gallery="galerie" title="Stratégie du Gator Alligator de Bill Williams">
    <img src="{{ base_url }}/images/strategies/gator-alligator/interface.png" alt="Capture d'écran" class="centered"/>
  </a>
  <figcaption><em>Stratégie du Gator Alligator de Bill Williams</em></figcaption>
</figure>

## Configuration

Vous configurer la {{ "PERIOD" | keywordi }} des fractales, et les trois Moyennes Mobiles de l'Alligator :

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/gator-alligator/configuration.png" class="glightbox" data-gallery="galerie" title="Configuration du Gator Alligator de Bill Williams">
    <img src="{{ base_url }}/images/strategies/gator-alligator/configuration.png" alt="Capture d'écran" class="centered"/>
  </a>
  <figcaption><em>Configuration du Gator Alligator de Bill Williams</em></figcaption>
</figure>

Les lignes de l’Alligator :

- {{ "Jaw" | keywordi }} (mâchoire) : Moyenne mobile bleue 13 périodes, lissée, décalée de 8 vers l’avant

- {{ "Teeth" | keywordi }} (dents) : Moyenne mobile rouge 8 périodes, lissée, décalée de 5 vers l’avant

- {{ "Lips" | keywordi }} (lèvres) : Moyenne mobile verte 5 périodes, lissée, décalée de 3 vers l’avant

La mâchoire (Jaw) est la plus lente, elle représente la tendance principale.

## Principe fondamental

Bill Williams dit :

- On ne doit acheter que si la fractale haussière est au-dessus de la Jaw.
- On ne doit vendre que si la fractale baissière est en dessous de la Jaw.

Pourquoi ?

Parce que la Jaw représente l’axe de la tendance.
Si un breakout se produit du bon côté de cette ligne, il est dans le sens de la dynamique dominante.

## Signaux d'achat

"Acheter une fractale haussière au-dessus de la mâchoire (Jaw)".

Une fractale haussière (sommet local) représente une résistance locale.

Si cette fractale est au-dessus de la Jaw, cela signifie que :

- La tendance est haussière (prix au-dessus de la ligne lente).
- La fractale identifie une résistance en zone de tendance.

Si un breakout casse cette fractale, le marché accélère dans le sens du mouvement dominant.

On place un ordre {{ "Buy Stop" | g_link }} juste au-dessus du plus haut de la fractale.

L’entrée n’est déclenchée que si la tendance continue réellement.

Cela évite les achats quand le prix est dans un range ou sous l’Alligator.

### Exemple graphique

Voici un magnifique breakout suivi d'un pullback haussier sur Air Liquide le 07/01/2025 :

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/gator-alligator/signal-achat.png" class="glightbox" data-gallery="galerie" title="Signal d'achat selon le Gator Alligator de Bill Williams">
    <img src="{{ base_url }}/images/strategies/gator-alligator/signal-achat.png" alt="Capture d'écran" class="centered"/>
  </a>
  <figcaption><em>Signal d'achat selon le Gator Alligator de Bill Williams</em></figcaption>
</figure>

La Fractale Up est au dessus de la machoire.

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/gator-alligator/signal-achat2.png" class="glightbox" data-gallery="galerie" title="Signal d'achat selon le Gator Alligator de Bill Williams">
    <img src="{{ base_url }}/images/strategies/gator-alligator/signal-achat2.png" alt="Capture d'écran" class="centered"/>
  </a>
  <figcaption><em>Signal d'achat confirmation selon le Gator Alligator de Bill Williams</em></figcaption>
</figure>

L'ordre de Buy Stop placé à 160 le 17/01/2025 lors le Gator Alligator ouvre la machoire avec les deux barres vertes de l'histogramme lors qu'il se réveille.

## Signaux de vente

"Vendre une fractale baissière en dessous de la mâchoire".

Même logique en miroir : Si une fractale baissière (creux local) est en dessous de la Jaw, alors :

- Le marché est baissier.
- La fractale marque un support dans la zone de tendance.

Si la cassure se produit, la dynamique baissière continue.

On place un ordr {{ "Sell Stop" | g_tooltip }} sous le plus bas de la fractale.

L’ordre n'est exécuté que si la tendance se prolonge vraiment.

### Exemple graphique vente

Voici un magnifique breakdown suivi d'un pullback baissier sur Air Liquide :

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/gator-alligator/signal-vente.png" class="glightbox" data-gallery="galerie" title="Signal de vente selon le Gator Alligator de Bill Williams">
    <img src="{{ base_url }}/images/strategies/gator-alligator/signal-vente.png" alt="Capture d'écran" class="centered"/>
  </a>
  <figcaption><em>Signal de vente confirmation selon le Gator Alligator de Bill Williams</em></figcaption>
</figure>

- **(1)** La fractale est dessous de la Jaw
- **(2)** Confirmation par les deux barres rouge du Gator

L'ordre de Sell Stop placé en dessous de la valeur la plus basse de la fractale.

## Résumé

| Situation                                   | Autoriser un trade ? |
| ------------------------------------------- | -------------------- |
| Fractale haussière **au-dessus** de la Jaw  | Oui (trade haussier) |
| Fractale haussière **en dessous** de la Jaw | Non                  |
| Fractale baissière **sous** la Jaw          | Oui (trade baissier) |
| Fractale baissière **au-dessus** de la Jaw  | Non                  |
