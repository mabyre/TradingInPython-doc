---
description: "Tracez un canal sur le graphique pour être alerté quand le cours sort de ce canal"
keywords: "stock, alertes, trading, technique, monitor, market, canal"
---

En trading technique le résultat de vos analyse techniques c'est le positionnement d'alertes avec l'alerte canal vous allez pouvoir tracer un canal qui va devenir une alerte.

Sur la stratégie de trading technique [Bollinger Bands FTMA](../strategies/bollinger-bands/bollinger-bands-ftma.md) vous allez tracer un canal d'alertes.

D'abord la ligne {{ "UPPER" | green }} en maintenant la touche {{ "'u'" | keyword }} enfoncée.

Puis la ligne {{ "LOWER" | red }} en maintenant la touche {{ "'l'" | keyword }} enfoncée.

Comme suit :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/canal-graphique-alertes.png" class="glightbox" data-gallery="galerie" title="Positionnez graphiquement un canal d'alertes">
        <img src="/images/monitor-stock-market/canal-graphique-alertes.png" alt="Positionnez graphiquement un canal d'alertes"/>
    </a>
    <figcaption><em>Positionnez graphiquement un canal d'alertes</em></figcaption>
</figure>

Vous souhaitez supprimer ce Canal cliquez sur la touche {{ "'x'" | keyword }}.

Le {{ "Monitor Stock Market" | keyword }} recalcule à chaque tour les projections des droites du Canal pour alerter si le cours s'approche (Touche) le Canal en Haut ou en Bas ou si le cours le cours Casse le Canal en Haut ou en Bas.

Tout se passe comme si à chaque tour vous réajustiez un seuil limite qui se déplacerait le long de la droite.

## Interface de configuration

Dans le [Monitor Stock Market](./monitor-stock-market.md), le bouton {{ "Alertes Canal" | keywordi }} vous permet d'afficher la fenêtre d'édition de l'Alerte Canal.

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/interface-canal-graphique.png" class="glightbox" data-gallery="galerie" title="Interface de configuration du canal d'alertes">
        <img src="/images/monitor-stock-market/interface-canal-graphique.png" alt="Interface de configuration du canal d'alertes"/>
    </a>
    <figcaption><em>Interface de configuration du canal d'alertes</em></figcaption>
</figure>

Vous avez la possiblité de ne plus utiliser cette alerte en décochant la case {{ "Activer l'alerte" | keywordi }}.

Vous configurer la {{ "Tolérance du Canal" | keywordi }} pour distinguer deux types d'alertes, une alerte {{ "Touche" | keyword }} quand le prix touche le canal ou s'en approche et une alerte lorsque le cours {{ "Casse" | keyword }} le canal.

Vous pouvez ainsi avec le même canal configurer un Retest suivi d'un Pullback du cours de l'action.

Le Temps de rémarment est là pour éviter que ces alarmes ne se déclencent trop souvent.
