# Double Bandes de Bollinger

Dans l'[interface](bollinger-bands-ftma.md#interface) de la stratégie des Bandes de Bollinger, le bouton {{ "Double Bandes de Bollinger" | keywordi }} permet de configurer la stratégie et de passer en Doubles Bandes de Bollinger.

Cette fois les horizons de temps sont identiques pour les deux bandes, ce qui change c'est l'équart type StdDev (Standard Déviation) :

- **1 σ** pour la première bande {{ "StdDev DBB1" | keyword }}
- **2 σ** pour la deuxièmes bande {{ "StdDev DBB2" | keyword }}

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/double-bandes-bollinger.png" class="glightbox" data-gallery="galerie"  title="Doubles Bandes de Bollinger">
        <img src="/images/strategies/bollinger-bands/double-bandes-bollinger.png" alt="Doubles Bandes de Bollinger"/>
    </a>
    <figcaption><em>Doubles Bandes de Bollinger</em></figcaption>
</figure>

L'avantage de cette stratégie c'est qu'elle donne des entrées et des sorties claires et facilement exploitables.

## Singaux d'entrée et de sortie

Vous pouvez entrer lors que le cours sort de la bande 1 sigma {{ "flêches vertes" | green }} et sortir {{ "flêche rouges" | red }} lorsque le cours passe la Moyenne Mobile par le haut. La moyenne mobile étant le signal {{ "bleu" | blue }} au milieu des deux bandes de Bollinger.

Vous pouvez également ajuster votre {{ "StopLoss" | g_tooltip }} sur le niveau de la moyenne mobile.

!!! warning

    <b>Les signaux sont clairs uniquement en tendance haussière.</b>

## Formation

Retrouvez les formation sur le Blog Trading et Data Analyses :

- <a href="https://www.trading-et-data-analyses.com/2025/10/strategie-de-trading-des-doubles-bandes-de-bollinger.html" target="_blank">Stratégie de trading des Doubles Bandes de Bollinger</a>

## Détection des Squeeze

Un Squeeze se forme lorsque le marché est en {{ "forte compression" | keyword }} juste avant un mouvement brusque et une tendance forte.

Réglage de la stratégie :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/ftma-bolls-keltner.png" class="glightbox" data-gallery="galerie"  title="Détecter les Squeeze">
        <img src="/images/strategies/bollinger-bands/ftma-bolls-keltner.png" alt="Détecter les Squeeze"/>
    </a>
    <figcaption><em>Bandes de Bollinger pour détecter les Squeeze</em></figcaption>
</figure>

N'afficher que la FTA 2 avec une standard déviation de **2 σ** et le Canal de Keltner (période 20 et {{ "ATR" | i_tooltip }} x 1,5)

En {{ "(3)" | red }} vous avez un Squeeze juste avant une très forte tendance haussière.

## Pas de Repainting

D'une façon générale les Bandes de Bollinger sont peu affactées par le {{ "Repainting" | g_tooltip }}, en effet ce sont des moyennes assez longues qui sont peu modifiées par les valeurs futures du cours de l'action.

Pour voir ce qu'il se passe exactement lors de cette séquence et grâce au fonctions de {{ "Backtesing" | keyword }} vous pouvez regarder cette annimation :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/ftma-bolls-keltner-squeeze.gif" class="glightbox" data-gallery="galerie" title="Détection des Squeeze">
        <img src="/images/strategies/bollinger-bands//ftma-bolls-keltner-squeeze.gif" alt=""/>
    </a>
    <figcaption><em>Détection des Squeeze</em></figcaption>
</figure>

On voit la Bande 2 σ rentrer dans le Canal de Keltner formant un Squeeez juste avant la poussée haussière.

Il faut avouer que sans cette stratégie de Bandes et Bollinger et de la détection de Squeeze, il était difficile de prévoir le cours avec une si forte hausse.
