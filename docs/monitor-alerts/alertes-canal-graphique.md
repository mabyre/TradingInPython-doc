---
description: "Tracez un canal sur le graphique pour être alerté quand le cours sort de ce canal le retest ou le break"
keywords: "stock, alertes, trading, technique, monitor, market, canal"
---

En trading technique, le résultat de vos analyse techniques, c'est le positionnement d'alertes. Avec le canal d'alertes vous allez pouvoir tracer un canal qui va devenir une alerte.

Un canal c'est simplement deux lignes entre lesquels le cours du titre va être observé (monitoré) pour savoir s'il le dépasse {{ "TOUCH" | keywordi }} ou le franchit {{ "BREAK" | keywordi }}.

## Tracez un canal d'alertes

Sur la stratégie de trading technique [Bollinger Bands FTMA](../strategies/bollinger-bands/bollinger-bands-ftma.md) vous allez tracer un canal d'alertes.

Vous tracez la ligne {{ "UPPER" | green }} en maintenant la touche : <kbd>U</kbd> (U comme Upper) enfoncée et en déplaçant la souris pour tracer votre ligne.

Vous tracez ensuite la ligne {{ "LOWER" | red }} en maintenant la touche <kbd>L</kbd> (L comme Lower) enfoncée et en déplaçant la souris.

Vous devez obtenir le graphique suivant :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/canal-graphique-alertes.png" class="glightbox" data-gallery="galerie" title="Positionnez graphiquement un canal d'alertes">
        <img src="/images/monitor-stock-market/canal-graphique-alertes.png" alt="Positionnez graphiquement un canal d'alertes"/>
    </a>
    <figcaption><em>Positionnez graphiquement un canal d'alertes</em></figcaption>
</figure>

Cela ne vous convient pas, vous souhaitez recommencer à tracer votre canal, cliquez sur : <kbd>Echap</kbd> pour effacer le canal en cours de tracé.

Vous souhaitez supprimer ce canal, tapez sur la touche : <kbd>X</kbd> pour tout supprimer.

Une fois le canal tracé, vous pouvez retourner en mode édition par la touche : <kbd>S</kbd> pour retoucher, déplacer les extrémités des lignes du canal.

Le canal est {{ "sauver automatiquement" | keyword }} quand vous avez terminé de le tracer.

## Monitorez votre canal d'alertes

Le {{ "Monitor Stock Market" | keyword }} recalcule, à chaque tour, les projections des droites du canal pour alerter si le cours s'approche, {{ "touche" | keyword }} le canal en Haut ou en Bas ou si le cours le cours {{ "casse" | keyword }} le canal en Haut ou en Bas.

Tout se passe comme si à chaque tour vous réajustiez le seuil limite qui se déplacerait le long de la droite {{ "UPPER" | green }} et {{ "LOWER" | red }}.

Plus besoin de d'ajuster un seuil de prix, si le cours sort du canal, une alerte est déclenchée.

Retrouvez votre alerte canal dans le [Moniteur des marchés financiers](../monitor-alerts/monitor-stock-market.md).

### Interface de configuration

Dans le [Monitor Stock Market](./monitor-stock-market.md), le bouton {{ "Alertes canal" | keywordi }} vous permet d'afficher la fenêtre d'édition de l'Alerte canal.

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/interface-canal-graphique.png" class="glightbox" data-gallery="galerie" title="Interface de configuration du canal d'alertes">
        <img src="/images/monitor-stock-market/interface-canal-graphique.png" alt="Interface de configuration du canal d'alertes"/>
    </a>
    <figcaption><em>Interface de configuration du canal d'alertes</em></figcaption>
</figure>

Vous avez la possiblité de ne plus utiliser cette alerte en décochant la case {{ "Activer l'alerte" | keywordi }}.

Vous configurer la {{ "Tolérance du canal" | keywordi }} pour distinguer deux types d'alertes, une alerte {{ "Touche" | keyword }} quand le prix touche le canal ou s'en approche et une alerte lorsque le cours {{ "Casse" | keyword }} le canal.

Vous pouvez ainsi avec le même canal configurer un Retest suivi d'un Pullback du cours de l'action.

Le {{ "Temps de rémarment (min)" | keywordi }} est là pour éviter que ces alarmes ne se déclencent trop souvent.

### Résultat du monitoring de votre canal d'alertes

Maintenant regardons le résultat produit par le tracé graphique de votre canal d'alertes dans le Monitor Stock Market.

Imaginez que vous ayez tracé le canal d'alerte suivant :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/canal-alertes-intel.png" class="glightbox" data-gallery="galerie" title="canal d'alertes sur le cours de INTEL">
        <img src="/images/monitor-stock-market/canal-alertes-intel.png" alt="Positionnez graphiquement un canal d'alertes"/>
    </a>
    <figcaption><em>canal d'alertes sur le cours de INTEL</em></figcaption>
</figure>

Vous obtenez dans le Monitor Stock Market, les alertes suivantes :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/alertes-canal-intel.png" class="glightbox" data-gallery="galerie" title="Monitorer le canal d'alertes sur le cours de INTEL">
        <img src="/images/monitor-stock-market/alertes-canal-intel.png" alt="Positionnez graphiquement un canal d'alertes"/>
    </a>
    <figcaption><em>Monitorer le canal d'alertes sur le cours de INTEL</em></figcaption>
</figure>

Vous retrouvez les messages d'alertes correspondants aux flèches en rouge sur le graphique.

Le Canal d'alertes travaille sur les prix de clôture des bougies (-1) à (-5) mais si le besoin se fait sentir, on ajoutera d'autres signaux d'alertes.
