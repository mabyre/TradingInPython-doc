# Bandes de Bollinger

Sur le Net, la documentation sur les {{ "Bandes de Bollinger" | keyword }} est plétorique, voici la mise en oeuvre des {{ "Bolls" | i_link }} dans la plateforme.

## Interface FTMA Bollinger Bands

Voici la stratégie des {{ "Bandes de Bollinger" | keyword }} sur quatre horizons de temps différents : Four Times frame Mobile Average Bollinger Bandes :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/interface.png" class="glightbox" data-gallery="galerie"  title="Bandes de Bollinger">
        <img src="/images/strategies/bollinger-bands/interface.png"/>
    </a>
    <figcaption><em>Bandes de Bollinger</em></figcaption>
</figure>

Quand elles s'alignent, cela indique généralement une tendance claire. Quand elles se contractent c'est souvent avant un mouvement fort.

## Configuration

L'interface de Configuration vous permet de modifier les horizons des Four Times Mobile Average (FTMA), les moyennes mobiles des Bandes de Bollinger.

Le Slider vous permet de les déplacer toutes les quatre.

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/config.png" class="glightbox" data-gallery="galerie"  title="Bandes de Bollinger - Configuration">
        <img src="/images/strategies/bollinger-bands/config.png"/>
    </a>
    <figcaption><em>Bandes de Bollinger - Configuration</em></figcaption>
</figure>

Vous choisissez les valeurs des FTA 1, 2, 3, 4 et le bouton {{ "Save" | keywordi }} vous permet de sauver ces valeurs pour l'action en cours.

- {{ "Read" | keywordi }} pour relire les valeurs sauvegardées.
- {{ "Default" | keywordi }} pour remettre les valeurs par défaut.

## Double Bandes de Bollinger

Le bouton {{ "Double Bandes de Bollinger" | keywordi }} permet de changer de stratégie et de passer en stratégie des Doubles Bandes de Bollinger, cette fois les horizons de temps sont identiques pour les deux bandes ce qui change c'est l'équart type StdDev (Standard Déviation) :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/double-bandes-bollinger.png" class="glightbox" data-gallery="galerie"  title="Doubles Bandes de Bollinger">
        <img src="/images/strategies/bollinger-bands/double-bandes-bollinger.png"/>
    </a>
    <figcaption><em>Doubles Bandes de Bollinger</em></figcaption>
</figure>


- **1 σ** pour la première bande {{ "StdDev DBB1" | keyword }}
- **2 σ** pour la deuxièmes bande {{ "StdDev DBB2" | keyword }}

L'avantage de cette stratégie c'est qu'elle donne des entrées et des sorties claires.

Exemple : Vous pouvez entrer lors que le cours sort de la bande 1 sigma (flêches vertes) et sortir (flêche rouges) lorsque le cours passe la Moyenne Mobile par le haut.

Vous pouvez également ajuster votre {{ "StopLoss" | g_tooltip }} sur la moyenne mobile.

ATTENTION : A utiliser uniquement en tendance haussière.

## Bollinger Bandes Multiframes + histogramme

Stratégie FTMA Bolls Multiframes (For Timeframes Mobile Average), les FTMA Bolls sont un puissant moyen d'analyse mais des plus complexe à manœuvrer, cette stratégie permet de dégager les grandes tendances mais également d'affiner pour des entrées et des sorties propres.

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/multiframes.png" class="glightbox" data-gallery="galerie"  title="Doubles Bandes de Bollinger">
        <img src="/images/strategies/bollinger-bands/multiframes.png"/>
    </a>
    <figcaption><em>Bandes de Bollinger Multiframes + Histogramme</em></figcaption>
</figure>

Les histogrammes vous permettent de visualiser très finement les resserrements des FTMA Bolls qui sont les prémices d'un changement tendance.

## Formation

- [Formation - FTMA Bollinger bands +  histogrammes](https://www.trading-et-data-analyses.com/2025/03/formation-ftma-bolls-histogrammes.html)

## Vidéo sur YouTube

Vous avez raté quelque chose :

<div align="center" class="md-video">
<iframe width="560" height="315" src="https://www.youtube.com/embed/vyCHZOKIokg?si=73ddSsx-bJKCydbc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Voilà vous savez tout sur les stratégies à base de Bandes de Bollinger.



