---
description: "Mettez les marchés financiers sous surveillance, voici le monitor stock market"
keywords: "stock, alertes, trading, technique, monitor, market"
---

# Monitor Stock Market

Monitorez le marché grâce aux alertes techniques et mettez le marché sous surveillance.

Vous avez créé vos screeners (liste des actions à mettre sous surveillance) en utilisant le {{ "Sélecteur de stocks" | keywordi }} :

- Menu {{ "Monitoring" | keywordi }} -> ["Gestion des screeners"](../heatmap-screener/screeners.md)

Vous pouvez maintenant configurer des Alertes sur les cours de bourse.

C'est l'{{ "aboutissement de votre analyse technique" | keyword }}, vous avez déterminé que l'objectif de cours à atteindre pour entrer ou sortir de position est de tant, vous allez pouvoir positionner une alerte pour être prévenu lorsque le cours atteindra cette valeur.

Votre analyse technique montre qu'il faut que la stock sorte de la zone de surachat pour entrer en position, vous mettez une [alerte technique](./alertes-techniques.md) sur le niveau du {{ "RSI" | i_link }}.

Vous souhaitez être prévenu sur les volumes d'échanges, et sur tout autre événement qui peut se produire sur la stock c'est l'objet du Monitor Stock Market : {{ "mettre le marché sous surveillance" | keyword }}.

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/interface.png" class="glightbox" data-gallery="galerie" title="Monitor Stock Market Alertes">
        <img src="/images/monitor-stock-market/interface.png" />
    </a>
    <figcaption><em>Monitor Stock Market Alertes</em></figcaption>
</figure>

L'onglet {{ "Monitoring" | keywordi }} vous permet de visualiser les alertes qui ont été déclenchées.

## Alertes simples en prix et en volume

Positionnez des alertes sur les prix et les volumes :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/edition-alerte.png" class="glightbox" data-gallery="galerie" title="Positionnez une alerte simple">
        <img src="/images/monitor-stock-market/edition-alerte.png" />
    </a>
    <figcaption><em>Monitor Stock Market - Positionnez une alerte simple</em></figcaption>
</figure>

- {{ "(1)" | red }} : Double cliquez sur l'une de ligne représentant une action que vous souhaitez monitorer
- {{ "(2)" | red }} : Fenêtre pour éditer les alertes de l'action

- {{ "Temps de réarmement (minutes)" | blue }} : Spécifiez un temps au bout duquel l'alarme sera réarmée (retestée) pour ne pas avoir cette alerte toutes les minutes dans le compte rendu des alertes déclenchées.

## Alertes à date

Vous pouvez déclencher un message dans le volet monitoring à une date que vous spécifiez comme par exemple : effectuer une nouvelle analyse technique ou bien que les dividendes sur ce cours arrivent.

## Tableau de bord du Monitor Stocks Market Alertes

Les colonnes du Monitor Stocks Market :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/tableau-de-bord.png" class="glightbox" data-gallery="galerie" title="Tableau de bord du Monitor Stock Market">
        <img src="/images/monitor-stock-market/tableau-de-bord.png" />
    </a>
    <figcaption><em>Tableau de bord du Monitor Stock Market</em></figcaption>
</figure>

- {{ "(1)" | red }} : L'indication du {{ "Prix Achat" | keywordi }} ou PRU (prix de revient unitaire) vous permet de savoir où vous en êtes à la hausse ou à la baisse.
- {{ "(2)" | red }} : {{ "Prix courant" | keywordi }} récupéré en temps réel.
- {{ "(3)" | red }} : {{ "Prix %" | keywordi }} l'écart calculé avec la dernière valeur du cours et la première valeur de la séquence de données ici : période 5d donc le Prix % est l'écart entre la dernière valeur du cours et le cours il y a 5 jours.

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/valeur-prix.png" class="glightbox" data-gallery="galerie" title="Valeur du Prix % sur les cinq derniers jours">
        <img src="/images/monitor-stock-market/valeur-prix.png" />
    </a>
    <figcaption><em>Valeur du Prix % sur les cinq derniers jours</em></figcaption>
</figure>

- {{ "Tr" | keywordi }} : Temps de réarmement

La période est calculé en fonction de l'Intervalle choisi pour avoir assez de données. Le choix de l'intervalle est important pour les alertes en volume.

Pour positionner une alerte en volume les colonnes Vol, Vol Tot, et Vol Max sont calculées en utilisant cet intervalle.

- {{ "Monitor" | keywordi }} : Décochez cette case pour ne plus recevoir les alertes concernant ce titre, remarquez que le {{ "Prix Courant" | keywordi }} est à zéro pour les titres qui ne sont pas monitorés.

## Couleurs des lignes d'alertes

Pour voir graphiquement si vous avez positionné une alerte sur un titre, la ligne correspondante est colorée :

- <span style="color: #f1f1f1; font-weight: bold;">en blanc</span> : pas d'alerte positionné sur la valeur
- <span style="color: #dfdfdf; font-weight: bold;">en gris</span> : seule une alerte de date est posiionnée
- <span style="color: #bcdfc4; font-weight: bold;">en vert clair</span> : une alerte simple en prix ou en volume est positionnée
- <span style="color: #b4d7dd; font-weight: bold;">en bleu clair</span> : une alerte technique avec indicateur positionnée
- <span style="color: #83b39c; font-weight: bold;">en vert foncé clair</span> : à la fois une alerte simple et une alarte technique

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/couleurs-lignes.png" class="glightbox" data-gallery="galerie" title="Indication de couleur des alertes">
        <img src="/images/monitor-stock-market/couleurs-lignes.png"/>
    </a>
    <figcaption><em>Indication de couleur des alertes</em></figcaption>
</figure>

Pour éditer une alerte avancée, vous avez le bouton {{ "Alertes Avancées" | keywordi }} mais vous pouvez également maintenir la touche {{ "Ctrl" | keyword }} en cliquant sur la ligne du titre concerné.

## Recevoir les alertes par email

Afin de recevoir les alertes du Monitor Stock Market vous devez au préalable avoir renseigné votre email dans le Menu {{ "Aide -> Smtp" | keyword }}

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/smtp.png" class="glightbox" data-gallery="galerie" title="Renseignez votre email pour recevoir les alertes">
        <img src="/images/monitor-stock-market/smtp.png" />
    </a>
    <figcaption><em>Renseignez votre email pour recevoir les alertes</em></figcaption>
</figure>

En suite, cochez la case {{ "Envoyer emails" | keywordi }}

Vous allez pouvoir recevoir un email avec l'ensemble des alertes que vous avez positionné et qui se sont déclenchées.

## Vous avez raté quelque chose ?

Voici la une vidéo rapide pour vous présenter les Alertes de la plateforme :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/alertes-techniques.gif" class="glightbox" data-gallery="galerie" title="Placer une alerte">
        <img src="/images/monitor-stock-market/alertes-techniques.gif"/>
    </a>
    <figcaption><em>Comment placer une alerte</em></figcaption>
</figure>

Découvrez rapidement comment vous allez pouvoir placer une alerte afin de la déclencher dans le Monitor Stock Market.
