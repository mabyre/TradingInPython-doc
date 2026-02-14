# Tour rapide

Découvrez rapidement les grands modules que vous pourrez utiliser avec {{ "TradingInPython" | keyword }}, la plateforme dédiée au trading technique.

La plateforme {{ "TradingInPython" | keyword }} est un ensemble complet de trading avec :

- des analyses techniques,
- des cartes chaleurs et de performance pour surveiller des marchés,
- des alertes techniques pour mettre les marchés sous surveillance,
- le gestionnaire de portefeuille vous donne en temps réel la performance de votre trading.

## Présentation des stratégies de trading technique

Ce tour rapide vous présente rapidement les stratégies automatiques de trading technique et les grands modules de la plateforme.

### Ichimoku Kinko Hyo

Dans cet exemple, on récupère les données du cours de TRIGANO pour la période des six derniers mois `6mo` par intervalle de 1 jour `1d`.

La stratégie de trading technique choisie est {{ "Ichimoku Kynko Hyo" | keyword }} :

<figure style="text-align: center;">
  <a href="/images/tour-rapide/ichimoku.png" class="glightbox" data-gallery="galerie" title="Interface de l'Ichimoku-Kinko-Hyo">
    <img src="/images/tour-rapide/ichimoku.png"/>
  </a>
  <figcaption><em>Plateforme de trading technique gratuite - TradingInPython</em></figcaption>
</figure>

Un fois ces éléments renseignés, vous cliquez sur le bouton {{ "Graphique" | keyword }} pour afficher l'analyse technique de l'action ({{ "stock" | g_tooltip }}).

Pour ce tour rapide de la Plateforme de Trading Technique, voici une analyse avec {{ "Ichimoku Kynko Hyo" | keyword }}, pour l'action TRIGANO :

<figure style="text-align: center;">
  <a href="/images/tour-rapide/ichimoku-2.png" class="glightbox" data-gallery="galerie" title="Interface de l'Ichimoku-Kinko-Hyo">
    <img src="/images/tour-rapide/ichimoku-2.png"/>
  </a>
  <figcaption><em>Plateforme de Trading and Data Analyse</em></figcaption>
</figure>

- **(1)** Vous reconnaissez l'Interface de [récupération des données](recuperation-des-data.md).
- **(2)** C'est l'interface de configuration spécifique de la Stratégie choisie par l'utilisateur
- **(3)** C'est la possibilité d'afficher un graphe secondaire avec l'indicateur de votre choix :

<figure style="text-align: center;">
  <a href="/images/tour-rapide/ichimoku-3.png" class="glightbox" data-gallery="galerie" title="Interface de l'Ichimoku-Kinko-Hyo">
    <img src="/images/tour-rapide/ichimoku-3.png"/>
  </a>
  <figcaption><em>Afficher un graphique secondaire</em></figcaption>
</figure>

Ici j'ai cliqué sur l'indicateur {{ "MACD" | i_link }}, il apparaît dans un graphe secondaire sous le graphe de la Stratégie pour venir la confirmer. Vous pouvez afficher sous le graphe de stratégie un second, un troisième, indicateur et ainsi de suite.

- **(4)** C'est le Graphique Ichimoku pour l'action TRIGANO

Vous remarquerez une série de cases à cocher également spécifique à la Stratégie Ichimoku. Pour chacune des stratégies, il y a des éléments spécifiques qui viendront s'afficher à cet endroit, des paramètres que vous pourrez manipuler.

Vous pourrez cliquer sur la case {{ "Forcast" | keyword }} (prédiction) pour faire une prédiction du signal d'achat/vente calculée par le réseau de neurones {{ "Keras et Jax" | keyword }} (équivalent de Tensorflow) entraîné sur les données.

Vous venez de découvrir l'une des nombreuses stratégies de trading technique de la plateforme.

### Les stratégies de trading technique

Voici maintenant toutes les stratégies intégrées dans la plateforme mais vous pouvez également [développer d'autres stratégies](open-software.md) d'analyse technique que vous pourrez intégrer dans le menu des stratégies d'analyse.

Vous avez actuellement le choix entre les stratégies suivantes pour analyser vos données :

<ul>
    <li>{{ "Ichimoku Kinko Hyo Modernised" | green }} + prédiction grâce à keras et tensorflow</li>
    <li>{{ "Moyennes mobiles et Exponetielle"  | green }} - Simple Mobile Average 1 et 2 and Exponential</li>
    <li>{{ "Volume Buy/Sell" | keyword }} - Analyse de la pression volumique des flux d'achats et de ventes</li>
    <li>{{ "Bollinger bands" | keyword }} - Les bandes de Bollinger, appliquées à plusieurs horizons temporels différents.</li>
    <li>{{ "Double Bandes de Bollinger" | keyword }} - Une stratégie puissante pour trader les momentums haussiers.</li>
    <li>{{ "Bollinger bands multiframes + histogrammes" | keyword }} - Détecteur de changement de tendance</li>
    <li>{{ "VWAP + STOCH - Volume Weighted Average Price" | keyword }} - Intraday follows thanks to VWAP</li>
    <li>{{ "Fractales Bill Williams" | keyword }} - Le fameux Bill Williams pour des signaux automatiques de Trading</li>
    <li>{{ "Gator Alligator S from Bill Williams" | keyword }}</li>
    <li>{{ "Filtre de Kalman" | keyword }} - Le fameux filtre pour la détection des tendances et de la volatilité</li>
    <li>{{ "Prédiction Keras" | keyword }} - Utilisation du réseau de neurones keras deeplearning avec Jax</li>
    <li>{{ "Smart Money Concept ICT" | keyword }} - Décoder le trading des grands acteurs du marché</li>
</ul>

Quand vous installez la plateforme **les stratégies en {{ "vert" | green }} sont gratuites**.

### Votre routine de trading

Pour trader correctement et avoir une chance de gagner en bourse, vous devez avoir une démarche proactive et régulière vis à vis des marchés et mettre en place votre routine de trading.

- Exemple de routine, vous démarrez la découverte d'une nouvelle {{ "stock" | g_tooltip }} par une analyse Ichimoku à l'échelle weekly/max.

- Ensuite vous affinez avec les Bandes Bollinger puis vous utilisez les Moyennes Mobiles pour découvrir son {{ "Spread" | g_tooltip }}.

- Vous déterminez les points d'entrée et de sortie ainsi que le {{ "Stoploss" | g_tooltip }} pour enfin placer des alertes.

L'ensemble de ces stratégies de trading technique vous permet d'élaborer votre propre routine de trading :

- [Découvrir : Votre routine de trading avec TradingInPython](trading-routine.md)

## Mode Screener

Pour vous montrer la facilité avec laquelle vous aurez le loisir de parcourir vos actions ({{ "stock" | g_tooltip }}) et de réaliser des analyses techniques.

En mode screener, vous pouvez parcourir toutes vos actions, avec par exemple la stratégie des [Fractales de Bill Williams](strategies/fractales-bill-williams.md), pour découvrir les signaux d'achat ou de vente de cette stratégie automatique de trading :

<figure style="text-align: center;">
  <a href="/images/tour-rapide/mode-screener.png" class="glightbox" data-gallery="galerie" title="TradingInPython - Mode Screener">
    <img src="/images/tour-rapide/mode-screener.png"/>
  </a>
  <figcaption><em>TradingInPython - Mode Screener</em></figcaption>
</figure>

## Cartes de chaleur (heatmap) & Performance

Découvrez le moyen de surveiller des dizaines d'actions d'un seul coup d'œil avec la Heatmap Performance ou "Carte de chaleur" et ses couleurs pour vous permettre de détecter, les actions qui croissent et sont à la hausse ou qui décroissent et sont à la baisse, par leurs performances :

<figure style="text-align: center;">
  <a href="/images/tour-rapide/carte-chaleur.png" class="glightbox" data-gallery="galerie" title="TradingInPython - Heatmap Performance surveiller des dizaines d'actions">
    <img src="/images/tour-rapide/carte-chaleur.png"/>
  </a>
  <figcaption><em>TradingInPython - Heatmap Performance surveiller des dizaines d'actions</em></figcaption>
</figure>

Pour chaque action tous les indicateurs techniques sont calculés et présentés dans une fenêtre de détails pour vous permettre de prendre les bonnes décisions de trading.

- [Découvrir : Les Cartes de chaleur (heatmap)](heatmap-screener/heatmaps.md)

## Monitoring Stock Market Alertes

Mettez le marché sous surveillance grâce au Monitoring Stock qui vous permet de placer des alertes sur le cours des actions et d'être prévenu par email :

<figure style="text-align: center;">
  <a href="/images/tour-rapide/monitor-stock-market.png" class="glightbox" data-gallery="galerie" title="TradingInPython - Monitoring stock market alertes">
    <img src="/images/tour-rapide/monitor-stock-market.png"/>
  </a>
  <figcaption><em>TradingInPython - Monitoring stock market alertes</em></figcaption>
</figure>

Un système d'alertes efficace pour être prévenu lorsqu'un cours franchit une résistance ou un support, ou encore, que le marché dépasse un certain volume de transactions et pouvoir ainsi agir et maîtriser totalement votre trading.

Les alertes avancées vous permettent de mettre des alertes sur les indicateurs techniques RSI, MACD, STOCH, Bollinger bands, etc

Par exemple, vous réalisez vos analyses techniques le matin vous positionnez vos alertes et vous être prévenu dans la journée lorsque quelque chose se passe ...

- [Découvrir : La Mise sous surveillance du Marché](monitor-alerts/monitor-stock-market.md)

## Votre Gestionnaire de Portefeuilles

Le portfolio ou gestionnaire de portefeuilles est l'outil indispensable du trader efficace. Il vous permet de centraliser tous vos achats/ventes et de les consolider dans un tableau de bord afin de connaitre le rendement réel de vos trades sur les Cryptos, Actions, <a href="https://www.trading-et-data-analyses.com/2024/01/termes-boursiers.html#ETF"  target="_blank">ETF</a>, <a href="https://www.trading-et-data-analyses.com/2024/01/termes-boursiers.html#Futures" target="_blank">Futures</a>, <a href="https://www.trading-et-data-analyses.com/2024/01/termes-boursiers.html#FOREX" target="_blank">Forex</a>, etc.

<figure style="text-align: center;">
  <a href="/images/tour-rapide/portefolio.png" class="glightbox" data-gallery="galerie" title="TradingInPython - Le portfolio ou Gestionnaire de Portefeuilles">
    <img src="/images/tour-rapide/portefolio.png"/>
  </a>
  <figcaption><em>TradingInPython - Le portfolio ou Gestionnaire de Portefeuilles</em></figcaption>
</figure>

La plateforme TradingInPython vous permet de gérer autant de portefeuilles que vous le souhaitez et de calculer ainsi l'efficacité réelle de vos trades.

- [Découvrir : Le Gestionnaire de portefeuilles](portfolio-manager.md)

## Téléchargement et abonnement

Vous venez de faire un {{ "Tour rapide" | keyword }} des fonctionnalités de la plateforme {{ "TradingInPython" | keyword }}.

Vous pensez que ce logiciel est fait pour vous et que vous allez pouvoir utiliser ces stratégies afin d'élaborer votre {{ "routine de trading" | keyword }} :

- <a href="https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html"  target="_blank">Téléchargez et abonnez-vous au logiciel TradingInPython</a>

Vous souhaitez nous laisser un message, une remarque, une question :

- <a href="https://www.trading-et-data-analyses.com/p/formulaire-de-contact.html"  target="_blank">Contactez-nous</a>
