# Trader avec les Bandes de Bollinger FTMA

Comment utiliser les Bandes de Bollinger FTMA en situation de trading pour trouver les points d'entrée et les sorties ainsi que le {{ "StopLoss" | g_tooltip }}.

Comme John Bollinger lui même dit qu'il ne faut pas utiliser les Bandes seule nous allons confirmer la tendance par le volume.

J'ai cliqué que le bouton {{ "Default Short" | keywordi }} pour avoir les valeurs suivantes des FTA 9 26 52 96.

## Point d'entrée

On se sert du fait que les BB se resserrent avant d'initier un nouveau mouvement puissant.

Les prix dérivent latéralement, cela signifie qu'il n'y a pas de tendance claire on est en {{ "range" | g_tooltip }}.  

Le range est important car c'est la période pendant laquelle des {{ "tensions se forment" | keyword }} et la libération de ces tensions peut engendrer des mouvements importants donc des opportunités de trading.

Voici le point de départ : les BB sont resserées, on est en observation d'une future tendance, une bougie {{ "rouge" | red }} vient de franchir la BB9.

Le volume est très légèrement en baisse. On n'entre pas encore on est en observation sur un possible rebond et un retournement à la hausse :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/ftma-entry-point-0.png" class="glightbox" data-gallery="galerie" title="Trading Haussier sur les Bandes Bollinger FTMA">
        <img src="/images/strategies/bollinger-bands/ftma-entry-point-0.png"/>
    </a>
    <figcaption><em>Trading Haussier sur les Bandes Bollinger FTMA</em></figcaption>
</figure>

Deux jours plus tard, c'est parti, déclenchement la BB9 s'ouvre vers le haut suivie par la BB26 :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/ftma-entry-point-1.png" class="glightbox" data-gallery="galerie" title="Trading Haussier sur les Bandes Bollinger FTMA">
        <img src="/images/strategies/bollinger-bands/ftma-entry-point-1.png"/>
    </a>
    <figcaption><em>Trading Haussier sur les Bandes Bollinger FTMA</em></figcaption>
</figure>

Une bougie {{ "verte" | green }} franchie par le haut la BB9, on entre car l'augmentation du volume est là pour confirmer la tendance à la hausse (trading agressif) ou on attend confirmation je jour d'après.

Deux jours plus tard, bougie rouge mais elle a franchit la BB26 et la BB52 donc une cassure ({{ "breakout" | g_tooltip }}) puissante s'est formée.

Le {{ "StopLoss" | g_tooltip }} peut-être positionné au niveau de la Moyenne Mobile 52 :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/stoploss-ftma.png" class="glightbox" data-gallery="galerie" title="StopLoss positionné sur la MM52">
        <img src="/images/strategies/bollinger-bands/stoploss-ftma.png" width="350"/>
    </a>
    <figcaption><em>StopLoss positionné sur la MM52</em></figcaption>
</figure>

## Point de sortie

On voit que certaines mèches viennent titiller la MM52, c'est chaud mais votre StopLoss sur la MM52 tient bon.

On sort lorque le prix de clôture est inférieur à la MM9 :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/ftma-out-point.png" class="glightbox" data-gallery="galerie" title="Sortie sur franchissement de la MM9">
        <img src="/images/strategies/bollinger-bands/ftma-out-point.png"/>
    </a>
    <figcaption><em>Sortie sur franchissement de la MM9</em></figcaption>
</figure>

Trois jours avant c'est très chaud avec une <a href="https://www.trading-et-data-analyses.com/2024/01/analyse-technique-des-marches.html" target="_blank">étoile du matin</a>. Mais le prix de clôture restera au dessus de la MM9 avec le petit redonf attendu.

## Animation

Voici l'animation complète de ce trade en tendance haussière grâce au Bandes de Bollinger FTMA :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/animation-bollinger-bands-ftma.gif" class="glightbox" data-gallery="galerie" title="Trading Haussier sur les Bandes Bollinger FTMA">
        <img src="/images/strategies/bollinger-bands/animation-bollinger-bands-ftma.gif"/>
    </a>
    <figcaption><em>Trading Haussier sur les Bandes Bollinger FTMA</em></figcaption>
</figure>

