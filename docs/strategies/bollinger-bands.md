# Bandes de Bollinger

Voici la stratégie des **Bandes de Bollinger** sur quatre horizons de temps différents :

<figure style="text-align: center;">
    <a href="/TradingInPython-doc/images/strategies/bollinger-bands/interface.png" class="glightbox" data-gallery="galerie"  title="Bandes de Bollinger">
        <img src="/TradingInPython-doc/images/strategies/bollinger-bands/interface.png"/>
    </a>
    <figcaption><em>Bandes de Bollinger</em></figcaption>
</figure>

L'interface de Configuration permet de modifier horizons des Four Times Mobile Average (FTA) les moyennes mobiles des Bandes de Bollinger.

<figure style="text-align: center;">
    <a href="/TradingInPython-doc/images/strategies/bollinger-bands/config.png" class="glightbox" data-gallery="galerie"  title="Bandes de Bollinger - Configuration">
        <img src="/TradingInPython-doc/images/strategies/bollinger-bands/config.png"/>
    </a>
    <figcaption><em>Bandes de Bollinger - Configuration</em></figcaption>
</figure>

Le bouton **Double Bandes de Bollinger** permet de changer de stratégie et de passer en stratégie des Doubles Bandes de Bollinger, cette fois les horizons de temps sont identiques pour les deux bandes ce qui change c'est l'équart type StdDev (Standard Déviation) :

<figure style="text-align: center;">
    <a href="/TradingInPython-doc/images/strategies/bollinger-bands/double-bandes-bollinger.png" class="glightbox" data-gallery="galerie"  title="Doubles Bandes de Bollinger">
        <img src="/TradingInPython-doc/images/strategies/bollinger-bands/double-bandes-bollinger.png"/>
    </a>
    <figcaption><em>Doubles Bandes de Bollinger</em></figcaption>
</figure>


- **1 σ** pour la première bande **StdDev DBB1**
- **2 σ** pour la deuxièmes bande **StdDev DBB2**

L'avantage de cette stratégie c'est qu'elle donne des entrées et des sorties claires.

Exemple : Vous pouvez entrer lors que le cours sort de la bande 1 sigma (flêches vertes) et sortir (flêche rouges) lorsque le cours passe la Moyenne Mobile par le haut.

Vous pouvez également ajuster votre **StopLoss** sur la moyenne mobile.

ATTENTION : Uniquement en tendance haussière
 


