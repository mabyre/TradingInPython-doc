# Tour rapide

Découvrez rapidement les grands modules que vous trouverez dans {{ "TradingInPython" | keyword }}, la plateforme dédiée au trading technique.

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

Vous remarquerez une série de case à cocher également spécifique à la Stratégie Ichimoku. Pour chacune des stratégies, il y a des éléments spécifiques qui viendront s'afficher à cet endroit, des paramètres que vous pourrez manipuler.

Vous pourrez cliquer sur la case {{ "Forcast" | keyword }} (prédiction) pour faire une prédiction du signal d'achat/vente calculée par le réseau de neurones {{ "Keras et Jax" | keyword }} (équivalent de Tensorflow) entraîné sur les données.

Retrouvez les analyses faites de l'action <a href="https://www.trading-et-data-analyses.com/2024/10/trigano.html#Ichikomu_Kinko_Hyo" target="_blank">TRIGANO</a>.

### Les stratégies de trading technique

Vous venez de découvrir l'une des nombreuses stratégies de trading technique de la plateforme.

Voici toutes les stratégies que vous pouvez utiliser et qui sont intégrées dans la plateforme mais vous pouvez également facilement de développer d'autres stratégies d'analyse technique que vous pourrez intégrer dans le menu des stratégies d'analyse.

Vous avez actuellement le choix entre les stratégies suivantes pour analyser vos données :

<ul>
    <li><span style="color: #38761d;">Ichimoku Kinko Hyo Modernised</span> + prédiction grâce à keras et tensorflow</li>
    <li><span style="color: #38761d;">Moyennes mobiles et Exponetielle</span> - Simple Mobile Average 1 et 2 and Exponential</li>
    <li>Volume Buy/Sell - Analyse de la pression volumique des flux d'achats et de ventes</li>
    <li>Bollinger bands - Les bandes de Bollinger, appliquées à plusieurs horizons temporels différents.</li>
    <li>Double Bandes de Bollinger - Une stratégie puissante pour trader les momentums haussiers.</li>
    <li>Bollinger bands multiframes + histogrammes - détecteur de changement de tendance</li>
    <li>VWAP + STOCH - Volume Weighted Average Price - Intraday follows thanks to VWAP</li>
    <li>Fractales Bill Williams - Le fameux Bill Williams pour des signaux automatiques de Trading</li>
    <li>Gator Alligator S from Bill Williams</li>
    <li>Filtre de Kalman - Le fameux filtre pour la détection des tendance et de la volatilité</li>
    <li>Prédiction Keras - utilisation du réseau de neurones keras deeplearning avec Jax</li>
</ul>

Quand vous installez la plateforme **les stratégies en <span style="color: #38761d;">vert</span> sont gratuites**.

Pour découvrir comment utiliser ces stratégies pour élaborer votre **routine de trading** :

- [Abonnez-vous](https://www.trading-et-data-analyses.com/p/abonnement.html)

### Votre routine de trading

Pour découvrir la routine de trading que vous pouvez réaliser avec la plateforme :

- [Routine de trading](trading-routine.md)

## Mode Screener

En mode screen, vous pouvez parcourir toutes vos actions, avec par exemple la stratégie des <a href="https://www.trading-et-data-analyses.com/2024/11/formation-indicateur-fractales-bill-williams.html" target="_blank">Fractales de Bill Williams</a>, pour découvrir les signaux d'achat ou de vente de cette stratégie automatique de trading :

<figure style="text-align: center;">
  <a href="/images/tour-rapide/mode-screener.png" class="glightbox" data-gallery="galerie" title="TradingInPython - Mode Screener">
    <img src="/images/tour-rapide/mode-screener.png"/>
  </a>
  <figcaption><em>TradingInPython - Mode Screener</em></figcaption>
</figure>

Ce chapître pour montrer la facilité avec laquelle vous aurez le loisir de parcourir vos actions (stocks) et de réaliser des analyses techniques.

## Cartes de chaleur (heatmap) & Performance

Découvrez le moyen de surveiller des dizaines d'actions d'un seul coup d'œil avec la Heatmap Performance ou "Carte de chaleur" et ses couleurs pour vous permettre de détecter, les actions qui croissent et sont à la hausse ou qui décroissent et sont à la baisse, par leurs performances :

<figure style="text-align: center;">
  <a href="/images/tour-rapide/carte-chaleur.png" class="glightbox" data-gallery="galerie" title="TradingInPython - Heatmap Performance surveiller des dizaines d'actions">
    <img src="/images/tour-rapide/carte-chaleur.png"/>
  </a>
  <figcaption><em>TradingInPython - Heatmap Performance surveiller des dizaines d'actions</em></figcaption>
</figure>

Pour chaque actions tous les indicateurs techniques sont calculés et présentés dans une fenêtre de détails pour vous permettre de prendre les bonnes décisions de trading.

- [Heatmap cartes de chaleur - Découvrir](./heatmap-screener/heatmaps.md)

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

- [Mise sous surveillance du Marché - Découvrir](./monitor-alerts/monitor-stock-market.md)

## Votre Gestionnaire de Portefeuilles

Le portfolio ou gestionnaire de portefeuille est l'outil indispensable du trader efficace. Il vous permet de centraliser tous vos achats/ventes et de les consolider dans un tableau de bord afin de connaitre le rendement réel de vos trades sur les Cryptos, Actions, <a href="https://www.trading-et-data-analyses.com/2024/01/termes-boursiers.html#ETF"  target="_blank">ETF</a>, <a href="https://www.trading-et-data-analyses.com/2024/01/termes-boursiers.html#Futures" target="_blank">Futures</a>, <a href="https://www.trading-et-data-analyses.com/2024/01/termes-boursiers.html#FOREX" target="_blank">Forex</a>, etc.

<figure style="text-align: center;">
  <a href="/images/tour-rapide/portefolio.png" class="glightbox" data-gallery="galerie" title="TradingInPython - Le portfolio ou Gestionnaire de Portefeuilles">
    <img src="/images/tour-rapide/portefolio.png"/>
  </a>
  <figcaption><em>TradingInPython - Le portfolio ou Gestionnaire de Portefeuilles</em></figcaption>
</figure>

La plateforme TradingInPython vous permet de gérer autant de portefeuilles que vous le souhaitez et de calculer ainsi l'efficacité réelle de vos trades.

- [Gestionnaire de portefeuilles - Découvrir](./portfolio-manager.md)

## Conclusion

Vous venez de faire un Tour rapide des fonctionnalités de la plateforme {{ "TradingInPython" | keyword }}.

Téléchargez le logiciel, abonnez vous :

- <a href="https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html"  target="_blank">TradingInPython</a>
