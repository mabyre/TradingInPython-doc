# Smart Money Concept et Trading ICT

Richard D. Wyckoff (années 1900–1930) a posé les base du trading de la Smart Money, elles ont été reprises par Michael J. Huddleston dont il n’existe pas d’information publique fiable sur la date de naissance précise, il serait probablement né dans les années 1960–1970.

Michael J. Huddleston reprend les bases pour les struturer en Smart Money Concept (SMC) :

- {{ "Structure" | keyword }} : Dow's waves - bearish: LH, LL, LH - bullish: HH, HL, HH
- {{ "BOS" | keyword }} : Break Of Structure
- {{ "CHoCH" | keyword }} : Change Of Character
- {{ "Order Blocks" | keyword }} :  Zones où de grands ordres ont été exécutés
- {{ "Liquidity grabs" | keyword }} : Prises de liquidités par la Smart Money
- {{ "FVG" | keyword }} : Fair Value Gap
- {{ "OTE" | keyword }} : Optimal Trade Entry / Premium-Discount

Michael J. Huddleston est l'Inner Circle Trader, ICT est devenu son pseudo.

Le trading de la Smart Money s'attache à repérer dans le cours des actions, les grands cycles de la smart money.

Les acteurs de la {{ "Smart Money" | keyword }} sont :

- Banques d’investissement (J.P. Morgan, Goldman Sachs, Morgan Stanley…)
- Market Makers (Citadel Securities, Virtu Financial…)
- Hedge Funds (Bridgewater, Renaissance Technologies, Two Sigma…)
- Institutions financières (fonds de pension, assurances, fonds souverains)
- Grosses prop firms (Jane Street, Jump Trading, DRW…)

Ce sont eux qui génèrent la majorité du volume et de la liquidité. Alors leurs actions laissent des traces dans les cours et le trading {{ "ICT" | g_tooltip }} consiste à détecter ces traces pour faire un trading astucieux et finalement suivre la smart money.

## Stratégie du trading de la Smart Money

Voici comment se présente l'interface de cette stratégie :

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/interface.png" class="glightbox" data-gallery="galerie" title="Interface - Smart Money Concept - Trading ICT">
        <img src="/images/strategies/smart-money-concept/interface.png" alt="" />
    </a>
    <figcaption><em>Smart Money Concept - Trading ICT</em></figcaption>
</figure>

## Concepts ICT de la Smart Money

Voici trois formations essentielles à la compréhension du trading de la Smart Money :

- <a href="https://www.trading-et-data-analyses.com/2026/01/trading-de-la-smart-money-structure-du-marche.html" target="_blank">Structure du marché en vagues de Dow</a>

- <a href="https://www.trading-et-data-analyses.com/2026/01/trading-de-la-smart-money-cassure-de-structure.html" target="_blank">Cassure de structure CHoCH - BoS</a>

- <a href="https://www.trading-et-data-analyses.com/2026/01/trading-de-la-smart-money-concept-de-liquidity.html" target="_blank">La prise de liquidité</a>

Une fois que vous avez en tête ces différents concepts de l'ICT, voici comment les enchaîner pour faire une lecture efficace du trading de la Smart Money :

- <a href="https://www.trading-et-data-analyses.com/2026/01/comment-enchainer-les-concepts-du-trading-smart-money.html" target="_blank">Structure du marché en vagues de Dow</a>

## Paramètrage des concepts ICT

### Configuration

Voici les paramètres de la Smart Money, ils permettent d'ajuster la finesse des concepts de l'{{ "ICT" | g_tooltip }} :

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/configuration.png" class="glightbox" data-gallery="galerie" title="Configuration - Smart Money Concept - Trading ICT">
        <img src="/images/strategies/smart-money-concept/configuration.png" alt="" />
    </a>
    <figcaption><em>Configuration Smart Money Concept - Trading ICT</em></figcaption>
</figure>

Vous pourrez configurer ces paramètres graphiquement, nous allons détailler les effets de chacun d'entre eux sur les concepts de l'{{ "ICT" | g_tooltip }}.

### Swing with

Régler la largeur des swings, les swings ce sont les hauts et les bas qui permettent de déterminer les vagues de Dow.

Un swing haut est déterminé par un plus haut au milieu de plus bas autour de lui, un swing de 3 signifie que le plus haut est entouré de 3 plus bas à droite et trois plus bas à gauche.

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/swing-3.png" class="glightbox" data-gallery="galerie" title="Swing de 3">
        <img src="/images/strategies/smart-money-concept/swing-3.png" alt="" />
    </a>
    <figcaption><em>Swing de 3</em></figcaption>
</figure>

Si maintenant je clique pour augmenter le Swing with à 4 :

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/swing-4.png" class="glightbox" data-gallery="galerie" title="Swing de 4">
        <img src="/images/strategies/smart-money-concept/swing-4.png" alt="" />
    </a>
    <figcaption><em>Swing de 4</em></figcaption>
</figure>

Au moins 4 bougies autour de ce plus haut HH sont plus basses que lui.

Vous pouvez constater que le réglage du swing modifie notablement la structure.

Vous allez pouvoir régler le swing graphiquement en voyant les vagues de Dow se former ou non.

### Liquidity threshold

Le Liquidity threshold ou {{ "Seuil de liquidité" | keyword }}, cette fois le graphe n'est pas redessiné lorsque vous modifiez le Liquidity threshold, pour redessiner le graphe avec un nouveau seuil cliquez sur le bouton {{ "Apply" | keywordi }}.

- Seuil de liquidité à 0.005 :

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/liquidity-005.png" class="glightbox" data-gallery="galerie" title="Seuil de liquidité à 0.005">
        <img src="/images/strategies/smart-money-concept/liquidity-005.png" alt="" />
    </a>
    <figcaption><em>Seuil de liquidité à 0.005</em></figcaption>
</figure>

- Seuil de liquidité à 0.015 :

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/liquidity-015.png" class="glightbox" data-gallery="galerie" title="Seuil de liquidité à 0.015">
        <img src="/images/strategies/smart-money-concept/liquidity-015.png" alt="" />
    </a>
    <figcaption><em>Seuil de liquidité à 0.015</em></figcaption>
</figure>

Les prises de liquidité de la Smart Money se font en général sur des bougies proches les unes des autres. Là encore vous pouvez régler graphiquement ce paramètre.

### ATR period

l'ATR c'est l'indicateur technique {{ "ATR" | g_link }} qui permet de valider le BoS (Break Of Structure) c'est-à-dire l'engouement du marché pour un mouvement puissant du prix d'où la rupture de la tendance en cours. 14 est la valeur de réglage qui convient mais certains traders préféreront une autre valeur.

### Displacement ratio

Ou ratio de déplacement, sous entendu de déplacement du prix, ce paramètre est un élément clef du trading de la Smart Money, il détermine la force du mouvement du prix en mesurant la force de la bougie. Cette force se trouve en calculant un ratio entre son corps (Open - Close) et la longueur des mèches.

Avec un {{ "Displacement ratio" | keyword }} de 0.70 vous ne voyez que les bougies très fortes :

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/displacement-070.png" class="glightbox" data-gallery="galerie" title="Seuil de déplacement à 0.7">
        <img src="/images/strategies/smart-money-concept/displacement-070.png" alt="" />
    </a>
    <figcaption><em>Seuil de déplacement à 0.7</em></figcaption>
</figure>

Notez au-dessus des bougies un triangle rouge avec la valeur du displacement (déplacement). Vous pouvez ainsi juger des bougies les plus fortes.

En passant ce seuil à 0.35 et en cliquant sur {{ "Apply" | keywordi }} pour redessiner le graphe, vous voyez beaucoup plus de bougies.

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/displacement-035.png" class="glightbox" data-gallery="galerie" title="Seuil de déplacement à 0.35">
        <img src="/images/strategies/smart-money-concept/displacement-035.png" alt="" />
    </a>
    <figcaption><em>Seuil de déplacement à 0.35</em></figcaption>
</figure>

Les {{ "CHoCH" | keyword }} et les {{ "BoS" | keyword }} sont validés et sont de vrais signaux s'ils se produisent sur de forts déplacements. Vous comprenez que pour casser une structure baissière, il va falloir une hausse conséquente surtout si c'est la Smart Money qui est à la manoeuvre.

### FVG displacement ATR

Fair Value Gap, appelé également "inbalance" car il reflète un déséquilibre, voici ce qu'est un FVG :

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/fvg.png" class="glightbox" data-gallery="galerie" title="Fair Value Gap">
        <img src="/images/strategies/smart-money-concept/fvg.png" alt="" />
    </a>
    <figcaption><em>Fair Value Gap</em></figcaption>
</figure>

C'est quand les mèches de deux bougies, séparées par une troisième, ne se recouvrent pas. On dit qu'il y a un déséquilibre du cours.

Le paramètre {{ "FVG displacement ATR" | keyword }} permet de mesurer la force des FVG et de ne tenir compte que des FVG puissants.

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/fvg-30.png" class="glightbox" data-gallery="galerie" title="Seuil de FVG 0.30">
        <img src="/images/strategies/smart-money-concept/fvg-30.png" alt="" />
    </a>
    <figcaption><em>Seuil de FVG 0.30</em></figcaption>
</figure>

Vous voyez plein de FVG, ils n'ont pas tous la même importance.

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/fvg-70.png" class="glightbox" data-gallery="galerie" title="Seuil de déplacement à 0.70">
        <img src="/images/strategies/smart-money-concept/fvg-70.png" alt="" />
    </a>
    <figcaption><em>Seuil de FVG à 0.70</em></figcaption>
</figure>

Avec un seuil de 0.70 vous ne voyez plus que les Fair Value Gap puissants, il y a un fort mouvement du prix dans cette zone. Les FVG permettent de valider la force du BoS de la cassure de la structure avec force.

## Trading de la Smart Money

Vous avez maintenant entre les mains une stratégie qui vous permet de lire les graphes du trading de la Smart Money.

Vous voyez également sur ce graphe affichés les OTE (Optimal Trade Entry) les points d'entrée optimum :

<figure style="text-align: center;">
    <a href="/images/strategies/smart-money-concept/smart-money.png" class="glightbox" data-gallery="galerie" title="Lecture du trading de la Smart Money">
        <img src="/images/strategies/smart-money-concept/smart-money.png" alt="" />
    </a>
    <figcaption><em>Lecture du trading de la Smart Money</em></figcaption>
</figure>

Vous avez la possibilité de placer sur le graphe vos des Order Blocks {{ "à la main" | keywordi }} pour venir affiner votre stratégie et votre lecture de la Smart Money.

## Code en Python

Pour les développeurs en langage {{ "Python" | g_tooltip }} sur le GitHub de PyTrading :

- <a href="https://github.com/SoDevLog/PyTrading/tree/main/TradingInPython/Z-Integration/indicator/smart_money_concept" target="_blank">Smart Money Concept et Trading ICT</a>

Utilisez dès maintenant cette stratégie de trading technique disponible dans la plateforme [TradingInPython](https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html)
