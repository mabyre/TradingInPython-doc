# Monitor Stock Market

Monitorer le marché grâce aux alertes techniques.

Vous avez créé vos screeners en utilisant le {{ "Sélecteur de stocks" | keywordi }} :

- Menu {{ "Monitoring" | keywordi }} -> ["Gestion des screeners"](../heatmap-screener/screeners.md)

Vous pouvez maintenant configurer des Alertes sur les cours de bourse.

C'est l'{{ "aboutissement de votre analyse technique" | keyword }}, vous avez déterminé que l'objectif de cours à atteindre est de tant, vous allez pouvoir positionner une alerte pour être prévenu lorsque le cours atteindra cette valeur.

Vous souhaitez être prévenu sur les volumes d'échanges, et sur tout autre événement qui peut se produire sur la stock c'est l'objet du Monitor Stock Market : mettre le marché sous surveillance.

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/interface.png" class="glightbox" data-gallery="galerie" title="Monitor Stock Market Alertes">
        <img src="/images/monitor-stock-market/interface.png" />
    </a>
    <figcaption><em>Monitor Stock Market Alertes</em></figcaption>
</figure>

L'onglet {{ "Monitoring" | keywordi }} vous permet de visualiser les alertes qui ont été déclenchées.

Vous allez pouvoir recevoir un email avec l'ensemble des alertes que vous avez positionné et qui se sont déclenchées.

## Alertes simples en prix et en volume

Positionnez des alertes sur les prix et les volumes.

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/edition-alerte.png" class="glightbox" data-gallery="galerie" title="Positionnez une alerte simple">
        <img src="/images/monitor-stock-market/edition-alerte.png" />
    </a>
    <figcaption><em>Monitor Stock Market - Positionnez une alerte simple</em></figcaption>
</figure>

- **(1)** Double cliquez sur l'une de ligne représentant une action que vous souhaitez monitorer
- **(2)** Fenêtre pour éditer les alertes de l'action

Temps de réarmement (minutes) : pour ne pas avoir cette chaque minute dans le compte rendu des alertes déclenchée vous spécifiez un temps au bout duquel l'alerte sera réarmée.

## Tableau de bord du Monitor Stocks Market Alertes

Les colonnes du Monitor Stocks Market :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/tableau-de-bord.png" class="glightbox" data-gallery="galerie" title="Tableau de bord du Monitor Stock Market">
        <img src="/images/monitor-stock-market/tableau-de-bord.png" />
    </a>
    <figcaption><em>Tableau de bord du Monitor Stock Market</em></figcaption>
</figure>

- **(1)** L'indication du **Prix Achat** ou PRU (prix de revient unitaire) vous permet de savoir où vous en êtes à la hausse ou à la baisse.
- **(2)** **Prix courant** récupéré en temps réel.
- **(3) Prix %** : l'écart calculé avec la dernière valeur du cours et la première valeur de la séquence de données ici : période 5d donc le Prix % est l'écart entre la dernière valeur du cours et le cours il y a 5 jours.

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/valeur-prix.png" class="glightbox" data-gallery="galerie" title="Valeur du Prix % sur les cinq derniers jours">
        <img src="/images/monitor-stock-market/valeur-prix.png" />
    </a>
    <figcaption><em>Valeur du Prix % sur les cinq derniers jours</em></figcaption>
</figure>

- **Tr** : Temps de réarmement

La période est calculé en fonction de l'Intervalle choisi pour avoir assez de données. Le choix de l'intervalle est important pour les alertes en volume.

Pour positionner une alerte en volume les colonnes Vol, Vol Tot, et Vol Max sont calculées en utilisant cet intervalle.

## Vous avez raté quelque chose ?

Voici la une vidéo rapide pour vous présenter les Alertes de la plateforme :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/alertes-techniques.gif" class="glightbox" data-gallery="galerie" title="Placer une alerte">
        <img src="/images/monitor-stock-market/alertes-techniques.gif"/>
    </a>
    <figcaption><em>Comment placer une alerte</em></figcaption>
</figure>

Découvrez rapidement comment vous allez pouvoir placer une alerte afin de la déclencher dans le Monitor Stock Market.
