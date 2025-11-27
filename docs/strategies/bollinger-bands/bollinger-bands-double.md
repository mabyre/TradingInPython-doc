# Double Bandes de Bollinger

Dans l'[interface](bollinger-bands-ftma.md#interface) de la stratégie des Bandes de Bollinger, le bouton {{ "Double Bandes de Bollinger" | keywordi }} permet de changer de stratégie et de passer en stratégie des Doubles Bandes de Bollinger.

Cette fois les horizons de temps sont identiques pour les deux bandes ce qui change c'est l'équart type StdDev (Standard Déviation) :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/double-bandes-bollinger.png" class="glightbox" data-gallery="galerie"  title="Doubles Bandes de Bollinger">
        <img src="/images/strategies/bollinger-bands/double-bandes-bollinger.png"/>
    </a>
    <figcaption><em>Doubles Bandes de Bollinger</em></figcaption>
</figure>


- **1 σ** pour la première bande {{ "StdDev DBB1" | keyword }}
- **2 σ** pour la deuxièmes bande {{ "StdDev DBB2" | keyword }}

L'avantage de cette stratégie c'est qu'elle donne des entrées et des sorties claires facilement exploitables.

Exemple : Vous pouvez entrer lors que le cours sort de la bande 1 sigma (flêches vertes) et sortir (flêche rouges) lorsque le cours passe la Moyenne Mobile par le haut.

Vous pouvez également ajuster votre {{ "StopLoss" | g_tooltip }} sur la moyenne mobile.

!!! warning

    {{ "A utiliser uniquement en tendance haussière." | red }}

## Formation

Retrouvez les formation sur le Blog Trading et Data Analyses :

- <a href="https://www.trading-et-data-analyses.com/2025/10/strategie-de-trading-des-doubles-bandes-de-bollinger.html" target="_blank">Stratégie de trading des Doubles Bandes de Bollinger</a>

