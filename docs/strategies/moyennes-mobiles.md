# Moyennes Mobiles

C'est une stratégie des plus {{ "simples mais pas simpliste" | keyword }} car elle permet d'appréhender ce que sont les stratégies automatiques de trading, des algorithmes qui délivrent des signaux d'achats et de ventes sur les cours de bourse. La stratégie des moyennes mobiles calcule le {{ "Spread" | g_tooltip }}

Nous allons détailler la stratégie des moyennes mobiles à l'aide de deux SMA (Simple Mobile Average) et d'une EMA (Esponential Moving Average).

La stratégie automatique de trading avec 2 SMA et 1 EMA repose sur la détection des croisements des moyennes pour générer des signaux d’achat ou de vente. Elle est simple à implémenter et efficace pour capter les tendances.

## Principes

Deux SMA de longueur différentes vont se croiser et sont lentes à réagir aux changements rapides.

La EMA donne plus de poids aux prix récents, elle est donc plus réactive aux retournements de tendance.

### Signaux achats/vente

- {{ "Achat" | keyword }} : la SMA courte passe au-dessus de la SMA longue **ET** que le prix est au-dessus de l’EMA.
- {{ "Vente" | keyword }}: la SMA courte passe en dessous de la SMA longue **ET** que le prix est en dessous de l’EMA.

### Avantages

- C'est une stratégie Facile à comprendre et à implémenter
- Elle fonctionne bien en tendance marquée
- Paramétrable selon l’actif et l’horizon de temps

### Limites

- Moins efficace en marché sans tendance (en range)
- Sensible aux faux signaux en période de forte volatilité

## Interface

Une fois implémentée et tracer dans le plateforme nous obtenons le graphique suivant :

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/moyennes-mobiles/interface.png" class="glightbox" data-gallery="galerie" title="Stratégie automatique de trading des Moyennes Mobiles">
    <img src="{{ base_url }}/images/strategies/moyennes-mobiles/interface.png" alt="Capture d'écran" class="centered"/>
  </a>
  <figcaption><em>Stratégie automatique de trading des Moyennes Mobiles</em></figcaption>
</figure>

Nous sommes avec l'action Air Liquide à l'échelle de temps 1 jour sur une période de 6 mois. On à le cours de l'action sous forme de bougies (candle). Les moyennes mobiles sont tracées et les surfaces entre, sont matérialisées par des couleurs verte et rouge.

### Configuration

Des Sliders vous permettent de configurer les moyennes mobiles :

- SMA 1 = 10
- SMA 2 = 15
- EMA = 15

Grâce à l'[algorithme en Python](#algorithme), la détection des croisements est marquée par les signaux d'achat {{ "triangles verts" | green }} et les signaux de ventes {{ "triangles rouges" | red }}.

Et là où vous pouvez aller plus loin avec TradingInPython, c'est que l'algorithme calcul les spreads, c'est à dire toutes les différences entre les signaux d'achat et les signaux de vente puis en fait le cumul :

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/moyennes-mobiles/console.png" class="glightbox" data-gallery="galerie" title="Les spread de l'algorithme des moyennes mobiles">
    <img src="{{ base_url }}/images/strategies/moyennes-mobiles/console.png" alt="Capture d'écran" class="centered"/>
  </a>
  <figcaption><em>Les spread de l'algorithme des moyennes mobiles</em></figcaption>
</figure>

On obtient ainsi pour l'action Air Liquide un {{ "Spread" | g_link }} affiché dans le Titre de : **5,180**.

Cela signifie que si vous aviez suivi tous ces signaux d'achat et de ventre vous auriez gagné : 5,18.

Dans le Graph de la stratégie des moyennes mobiles, vous allez pouvoir ajuster SMA 1, SMA 2, et EMA pour optimiser ce spread.

Par exemple avec les réglages suivants :

- SMA 1 = 10
- SMA 2 = 18
- EMA = 18

Vous obtenez un {{ Spread | g_tooltip }} de : 9,50

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/moyennes-mobiles/spread.png" class="glightbox" data-gallery="galerie" title="Optimisation du Spread par les Moyennes Mobiles">
    <img src="{{ base_url }}/images/strategies/moyennes-mobiles/spread.png" alt="Capture d'écran" class="centered"/>
  </a>
  <figcaption><em>Optimisation du Spread par les Moyennes Mobiles</em></figcaption>
</figure>

Vous avez à votre disposition un outil d'optimisation de votre stratégie automatique par les moyennes mobiles qui vous permet de choisir les meilleures valeurs pour les moyennes mobiles SMA1 et 2 et EMA afin d'obtenir le meilleur {{ "Spread" | g_tooltip }} (le meilleur gain).

## Stratégie en action

Voici la Stratégie des moyennes mobiles en action pour optimiser votre Spread :

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/moyennes-mobiles/annimation-moyennes-mobiles.gif" class="glightbox" data-gallery="galerie" title="Optimisation du Spread par les Moyennes Mobiles">
    <img src="{{ base_url }}/images/strategies/moyennes-mobiles/annimation-moyennes-mobiles.gif" alt="Capture d'écran" class="centered"/>
  </a>
  <figcaption><em>Stratégie automatique des Moyennes Mobiles</em></figcaption>
</figure>

## Algorithme

Open Software, d'écouvrez l'implémentation de la stratégie des moyennes mobiles au sein de la plateforme :

- <a href="https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/strategy_sma12e.py" target="_blank">Stratégie automatique des Moyennes Mobiles</a>

## Conclusion

Cette stratégie est primodiale pour caractériser une action (stock) afin de déterminer s'il est intéressant de la trader. 

Elle vous donne une indication sur combien vous pourriez gagner, si vous effectuez tous les trades indiqués par la stratégie sur cette action.

N'hésitez plus venez faire vos analyses techniques avec la plateforme [TradingInPython](https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html).
