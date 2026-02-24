---
description: "Tracez un canal sur le graphique pour être alerté quand le cours sort de ce canal"
keywords: "stock, alertes, trading, technique, monitor, market, canal"
---

Sur la stratégie de trading technique {{ "Bollinger Bands FTMA" | keywordi }} vous allez tracer un canal d'alertes.

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

## Interface de configuration

Dans le [Monitor Stock Market](./monitor-stock-market.md), le bouton {{ "Alertes Canal" | keywordi }} vous permet d'afficher la fenêtre d'édition de l'Alerte Canal.

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/interface-canal-graphique.png" class="glightbox" data-gallery="galerie" title="Interface de configuration du canal d'alertes">
        <img src="/images/monitor-stock-market/interface-canal-graphique.png" alt="Interface de configuration du canal d'alertes"/>
    </a>
    <figcaption><em>Interface de configuration du canal d'alertes</em></figcaption>
</figure>

Vous avez la possiblité de ne plus utiliser cette alerte en décochant la case {{ "Activer l'alerte" | keywordi }}.

Vous configurer la {{ "Tolérance du Canal" | keywordi }}. Vous aurez deux types d'alertes, une alerte {{ "Touche" | keyword }} quand le prix touche le canal ou s'en approche avec cette valeur de la Tolérance canal vous configurez ce type d'alerte, et une alerte {{ "Casse" | keyword }} lorsque le canal est cassé.

Vous pouvez ainsi avec le même canal configurer un Retest suivi d'un Pullback du cours de l'action.

Le Temps de rémarment est là pour éviter que ces alarmes ne se déclencent trop souvent.
