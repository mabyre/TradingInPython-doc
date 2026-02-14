# Votre routine de trading au quotidien

Nous allons aborder rapidement chacune des stratégies de la plateforme et leur mise en oeuvre dans l'ensemble global qu'est la {{ "routine de trading" | keyword }}.

Avoir une routine bien rodée, c'est la clef d'un bon trader. Pour trader correctement et avoir une {{ "chance de gagner" | keyword }}, vous devez avoir une démarche proactive et régulière vis à vis des marchés.

Voici une routine de trading que vous pouvez suivre en <a href="https://www.trading-et-data-analyses.com/p/abonnement.html" target="_blank">vous abonnant à la plateforme TradingInPython</a>.

Vous allez chercher les informations sur les actions que vous souhaitez analyser sur les grandes plateformes d'informations boursières comme Boursorama, Yahoo, Investing.com, etc.

Vous avez choisi l'intervalle et la période de temps de votre analyse, pour une première analyse choisissez une échelle grande de temps Interval: `1d` un jour et analysez sur les 6 dernier mois Period: `6mo`. Encore mieux avec une échelle de temps `1w` et la période à `max`.

Vous avez maintenant le choix entre toutes les stratégies proposées par la Plateforme :

<figure style="text-align: center;">
    <a href="/images/strategies/strategies.png" class="glightbox" data-gallery="galerie" title="Choix de la Stratégie pour l'analyse des données">
        <img src="/images/strategies/strategies.png" alt="Choix de la Stratégie pour l'analyse des données"/>
    </a>
    <figcaption><em>Choix de la Stratégie pour l'analyse des données</em></figcaption>
</figure>

Les stratégies de trading technique de la plateforme sont là pour déterminer la tendance, faire des entrées et des sorties propres et placer vos {{ "Stoploss" | g_tooltip }}.

## Première analyse avec Ichimoku Kinko Hyo

Disons que si vous souhaitez {{ "faire une première analyse" | keyword }} de l'action que vous venez de trouver, pour dégager des tendances globales, l' {{ "Ichimoku Kinko Hyo" | keyword }} est une stratégie idéale pour dégager de grandes tendances fortes :

<figure style="text-align: center;">
    <a href="/images/strategies/ichimoku/routine.png" class="glightbox" data-gallery="galerie"  title="Stratégie de l'Ichoku Kinko Hyo">
        <img src="/images/strategies/ichimoku/routine.png" alt="Stratégie de l'Ichoku Kinko Hyo"/>
    </a>
    <figcaption><em>Stratégie de l'Ichoku Kinko Hyo</em></figcaption>
</figure>

Cette stratégie est à utiliser sur de grandes échelles de temps comme weekly max.

Vous trouverez de la formation et des exemples sur cette stratégie sur ce site :

- [Découvrir : Ichimoku-Kinko-Hyo](./strategies/ichimoku-kinko-hyo.md)

## Double Bandes de Bollinger

C'est une stratégie également comme l'Ichimoku extrêmement graphique pour vous permettre d'affiner votre sentiment de trading et commencer à envisager une entrée (achat).

Les Doubles Bandes de Bollinger sont un moyen puissant d'obtenir des entrées et des sorties claires :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/double-bandes-bollinger.png" class="glightbox" data-gallery="galerie"  title="Doubles Bandes de Bollinger">
        <img src="/images/strategies/bollinger-bands/double-bandes-bollinger.png" alt="Doubles Bandes de Bollinger"/>
    </a>
    <figcaption><em>Doubles Bandes de Bollinger</em></figcaption>
</figure>

Exemple :

- Signaux d'entrée (achat) lorsque le prix sort de la bande de Bollinger 1 σ et 2 σ
- Signaux de sortie (vente) lorsque le prix touche la Moyenne Mobile

Ces signaux sont clairs en tendance haussière uniquement.

- [Découvrir : Double Bandes de Bollinger](./strategies/bollinger-bands/bollinger-bands-double.md)

## Analyse de la pression du flux volumique

Après une analyse globale et rapide du titre grâce à l'[Ichimoku Kinko Hyo](./strategies/ichimoku-kinko-hyo.md), vous souhaitez peaufiner votre analyse par exemple en découvrant si en ce moment les {{ "acheteurs sont à la manœuvre" | keyword }} ou si ce sont plutôt les {{ "vendeurs qui manœuvrent" | keyword }}.

L'analyse des flux volumiques par la stratégie {{ "Volume Buy/Sell" | keyword }} est idéale pour ce genre d'analyse.

C'est une stratégie exclusive sur la plateforme {{ "TradingInPython" | keyword }} et que vous ne trouverez pas sur d'autres plateformes.

En vous abonnant vous aurez accès à la formation complète sur cette stratégie.

<figure style="text-align: center;">
    <a href="/images/strategies/volume-pression/nvidia.png" class="glightbox" data-gallery="galerie" title="Analyse des flux volumiques d'achats et de vente">
        <img src="/images/strategies/volume-pression/nvidia.png" alt="alt" />
    </a>
    <figcaption><em>Analyse des flux volumiques d'achats et de vente</em></figcaption>
</figure>

Ici la pression de vente qui s'exerce sur LEGRAND est de 0.53 %. La pression du flux volumique est à la vente mais le prix monte c'est probablement le moment d'entrer en position.

- <a href="https://www.trading-et-data-analyses.com/2025/02/formation-analyse-pression-volumiques-des-flux.html" target="_blank">Formation - Analyse de la pression volumique</a>
- <a href="https://www.trading-et-data-analyses.com/2025/04/analyse-de-pression-volumique.html" target="_blank">Vidéo de démo - Analyse de la pression volumique</a>

Maintenant si vous décidez d'entrer ou de sortir de position, les deux stratégies {{ "Moyennes Mobiles 1/2/E" | keyword }} et les {{ "Fractales Bill Williams" | keyword }} sont indiquées pour lire dans les signaux automatiques d'achat et de vente. Là encore vous trouverez de la formation et des exemples sur ce site et ailleurs.

## Moyennes Mobiles 1/2/E

C'est la fameuse stratégie automatique par les deux moyennes mobiles et la moyenne exponentielle. Cette stratégie est certainement à utiliser au début de la découverte d'une nouvelle action pour calculer son {{ "Spread" | g_tooltip }}.

<figure style="text-align: center;">
    <a href="/images/strategies/moyennes-mobiles/interface.png" class="glightbox" data-gallery="galerie" title="Analyse des flux volumiques d'achats et de vente">
        <img src="/images/strategies/moyennes-mobiles/interface.png" alt="alt" />
    </a>
    <figcaption><em>Analyse des flux volumiques d'achats et de vente</em></figcaption>
</figure>

Lorsque la moyenne mobile {{ "Moyenne Mobile courte" | keyword }} passe au dessous de {{ "Moyenne Mobile longue" | keyword }} et que l'exponentielle est au dessus des deux moyennes mobiles c'est un signal d'achat {{ "(triangle vert)" | green }} une tendance haussière débute.

Inversement, lorsque  {{ "Moyenne Mobile courte" | keyword }} passe en dessous {{ "Moyenne Mobile longue" | keyword }} et que l'exponentielle est en dessous de ma1 et ma2 c'est un signal de vente {{ "(triangle rouge)" | red }} une tendance baissière débute.

L'intérêt de cette stratégie c'est qu'elle permet de calculer la rentabilité d'une action, le {{ "Spread" | keyword }} qui est ici pour DASSAULT AVIATION est de 126,50. Cela signifie que si vous aviez suivi tous les signaux d'achat et de vente de cette stratégie, vous auriez gagné le Spread.

Le {{ "Spread" | keyword }} est un indicateur intéressant car il permet de se rendre compte du rendement de l'action, il est en général, peu intéressant de trader des actions avec peu de Spread.

- [Découvrir : Stratégie des Moyennes Mobiles](./strategies/moyennes-mobiles.md)

## Fractales de Bill Williams + SAR

C'est une stratégie simple parce qu'elle regarde les plus hauts et les plus bas mais sont interprétation est complexe et passe par la compréhension des {{ "breakout" | g_tooltip }} et des {{ "pullback" | g_tooltip }}

Les sommets indiqués en rouge indiquent un possible retournement baissier. Les ceux indiqués en vert indiquent un possible retournement haussier.

<figure style="text-align: center;">
    <a href="/images/strategies/fractale-bill-williams/routine.png" class="glightbox" data-gallery="galerie" title="Stratégie des Fractales de Bill Williams">
        <img src="/images/strategies/fractale-bill-williams/routine.png" alt="Copie d'écran" />
    </a>
    <figcaption><em>Stratégie des Fractales de Bill Williams</em></figcaption>
</figure>

Utilisé avec la {{ "Gator Alligator" | keyword }} cette routine peut devenir un système de trading complet.

- [Découvrir : Fractales de Bill Williams](./strategies/fractales-bill-williams.md)

## Stop And Reverse parabolic

Le SAR (Stop And Reverse parabolic) est un indicateur de tendance que j'ai intégré dans cette stratégie pour confirmer les signaux donnés par les Fractales de Bill Williams et ainsi pouvoir comparer les deux.

<figure style="text-align: center;">
    <a href="/images/strategies/fractale-bill-williams/routine-sar.png" class="glightbox" data-gallery="galerie" title="SAR Parabolic (Stop And Reverse) Parabolic indicator">
        <img src="/images/strategies/fractale-bill-williams/routine-sar.png" alt="Copie d'écran" />
    </a>
    <figcaption><em>SAR Parabolic (Stop And Reverse) Parabolic indicator</em></figcaption>
</figure>

Ici le dernier point est en dessous du cours le plus bas signifiant que la tendance pourrait bien se retourner.

- {{ "SAR Parabolic" | i_link }}
- <a href="https://www.trading-et-data-analyses.com/2025/05/reglages-de-lindicateur-technique-sar.html" target="_blank">Réglage de l'indicateur SAR</a>

## Stratégie Intraday VWAP + STOCH

Maintenant passons à l'Intraday, au sein de la journée.

Vous souhaitez suivre le cours de votre action durant la journée pour savoir quels sont les meilleurs moments d'entrée et de sortie, la stratégie {{ "VWAP" | i_tooltip }} + {{ "STOCH" | i_tooltip }} Intraday, est adaptée à cette analyse du cours dans la journée :

<figure style="text-align: center;">
    <a href="/images/strategies/intraday-vwap-stoch/routine.png" class="glightbox" data-gallery="galerie" title="Stratégie VWAP + STOCH Intraday">
        <img src="/images/strategies/intraday-vwap-stoch/routine.png" alt="alt" />
    </a>
    <figcaption><em>Stratégie VWAP + STOCH Intraday</em></figcaption>
</figure>

Si le prix est au dessus du {{ "VWAP" | i_tooltip }} (Volume Weighted Average Price) alors il est surestimé et une correction vers le bas pourrait se produire si au contraire le prix est en dessous, une correction à la hausse pourrait se produire.

Notez également la présence de deux indicateurs techniques {{ "ATR" | i_tooltip }} et l'{{ "OBV" | i_tooltip }} qui sont pratiques pour les entrées ou les sorties dans la journée.

## Gator Alligator de Bill Williams

Voici maintenant le Gator Alligator de Bill Williams et ses histogrammes :

<figure style="text-align: center;">
    <a href="/images/strategies/gator-alligator/routine.png" class="glightbox" data-gallery="galerie" title="Stratégie Gator Alligator de Bill Williams">
        <img src="/images/strategies/gator-alligator/routine.png" alt="alt" />
    </a>
    <figcaption><em>Stratégie Gator Alligator de Bill Williams</em></figcaption>
</figure>

Selon la métaphore de l'alligator de Bill Williams le marché évolue en quatre phases :

<ul style="text-align: left;">
 <li>Gator dort : Les barres des deux côtés sont rouges → pas de tendance.</li>
 <li>Gator se réveille : Une barre rouge et une barre verte → début de tendance.</li>
 <li>Gator en chasse : Deux barres vertes → tendance forte.</li><li>Gator rassasié : Une barre devient rouge → ralentissement de la tendance.</li>
</ul>

- [Découvrir : Alligator Gator de Bill Williams](./strategies/gator-alligator.md)
- <a href="https://www.trading-et-data-analyses.com/2024/10/formation-bill-williams-alligator-gator.html" target="_blank">Gator Alligator - Généralités</a>

## Trading de la Smart Money Concept ICT

La stratégie de trading de la Smart Money, ou comment remarquer les traces du trading de la Smart Money (les grands acteurs du marché). 

Si vous familier des concept {{ "ICT" | g_link }}, vous pouvez utiliser cette stratégie seule dans une routine complète.

Sinon il est bon de temps en temps de tester sur une action si la Smart Money n'est pas en train d'effectuer une manipulation du cours de l'action car il ne faut pas aller contre la Smart Money mais s'en servir pour suivre la tendance.

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/smart-money.png" class="glightbox" data-gallery="galerie" title="Lecture du trading de la Smart Money">
        <img src="/images/strategies/smart-money-concept/smart-money.png" alt="" />
    </a>
    <figcaption><em>Lecture du trading de la Smart Money</em></figcaption>
</figure>

- [Découvrir : Le trading de la Smart Money](./strategies/smart-money-concept.md)

## Conclusion

Vous venez de parcourir les stratégies de trading de la plateforme. Vous pouvez découvrir l'utilisation de ces stratégies afin de peaufiner votre propre routine de trading suivant que vous souhaitez faire de l'intraday, du scalping, du swing trading ou de l'investissement.

Abonnez-vous à TradingInPython :

- <a href="https://www.trading-et-data-analyses.com/p/abonnement.html" target="_blank">TradingInPython</a>
