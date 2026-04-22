---
title: "Comment voyager dans le temps avec les données de bourse"
description: "Configuration de l'interface de récupération des données de bourse"
keywords: "trading, technique, data, yfinance"
---

Le voyage dans le temps est d'une importance cruciale pour le trader. Il lui faut maitriser les différentes échelles de temps qui vont de la milliseconde à la dizaine d'années.

Vous vous rendez bien compte que d'observer le cours d'une action {{ "à la milliseconde dans la journée" | keyword }} ou à l'échelle {{ "1 mois sur dix ans" | keyword }}, vous n'aurez pas le même ressenti du cours de l'action.

Sur la plateforme <a href="https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html" target="_blank">TradingInPython</a>, le voyage dans le temps s'effectue à l'aide de la boite de dialogue {{ "Strategy Automation" | keywordi }}.

Cette boite de dialogue permet de configurer toutes les possibilités de récupération des données de bourse dans le temps par périodes ou nombre de jours ou entre deux dates à toutes les échelles de temps.

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/configuration.png" class="glightbox" data-gallery="galerie" title="Interface de récupération des données de bourse">
        <img src="/images/voyage-dans-le-temps/configuration.png" alt="Configuration" />
    </a>
    <figcaption><em>Interface de récupération des données de bourse</em></figcaption>
</figure>

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/configuration.png" class="glightbox" data-gallery="galerie" title="Interface de récupération des données de bourse">
        <img src="/images/voyage-dans-le-temps/configuration.png" alt="Configuration" />
    </a>
    <figcaption><em>Interface de récupération des données de bourse</em></figcaption>
</figure>

Cette interface se compose trois parties, voici comment voyager dans le temps.

## Période et Intervalle

Le voyage dans le temps s'effectue grâce à la configuration d'un {{ "intervalle" | keyword }} et d'une {{ "période" | keyword }} de temps.

C'est ce que l'on voit {{ "dans la partie (1)" | red }}, vous avez la possibilité de configurer directement l'intervalle et la période :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/interval-period.png" class="glightbox" data-gallery="galerie" title="Période et Intervalle">
        <img src="/images/voyage-dans-le-temps/interval-period.png" alt="Période et Intervalle" />
    </a>
    <figcaption><em>Configuration du voyage dans le temps période et intervalle</em></figcaption>
</figure>

Mais ces valeurs ne conviennent pas à toutes les analyses techniques, loin delà. Il y a donc deux autres parties pour vous permettre de configurer votre voyage dans le temps.

Nous avons une nouvelle interface de configuration de l'Intervalle et de la Période :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/configuration-2.png" class="glightbox" data-gallery="galerie" title="Période et Intervalle">
        <img src="/images/voyage-dans-le-temps/configuration-2.png" alt="Période et Intervalle" />
    </a>
    <figcaption><em>Configuration du voyage dans le temps période et intervalle</em></figcaption>
</figure>

C'est une interface plus UX plus pratique pour les utilisateurs que nous sommes.

## Jours dans le passé et Jours avant la fin

Pour utiliser {{ " la partie (2), choisir 'none' dans 'Period'" | red }}.

Vous avez alors la possibilité de configurer la Period par les deux valeurs {{ "Jours dans le passé" | keywordi }} et {{ "Jours avant la fin" | keywordi }},
elles sont positionnées sur l'axe temporel de la façon suivante :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/jours-avant-la-fin.png" class="glightbox" data-gallery="galerie" title="Partie (2) du voyage dans le temps">
        <img src="/images/voyage-dans-le-temps/jours-avant-la-fin.png" alt="Partie 2" />
    </a>
    <figcaption><em>Partie (2) du voyage dans le temps</em></figcaption>
</figure>

L'axe du temps se déroule de gauche à droite, à droite on est Maintenant.

Ainsi pour regarder le cours de l'action TESLA en arrière de 3 jours sur une période de 10 jours vous avez la configuration suivante :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/trois-jours-dans-le-passé.png" class="glightbox" data-gallery="galerie" title="3 jours dans le passé">
        <img src="/images/voyage-dans-le-temps/trois-jours-dans-le-passé.png" alt="Partie 3" />
    </a>
    <figcaption><em>Voyage dans le temps 3 jours dans le passé</em></figcaption>
</figure>

- {{ "(1)" | red }} Period est à {{ "none" | keywordi }}

- {{ "(2)" | red }} {{ "Jours dans le passé" | keywordi }} = 3 et {{ "Jours avant la fin" | keywordi }} = 10

Nous somme le 27 mars 2025 et l'on regarde le cours de TESLA depuis le 24 mars sur dix jours en arrière.

## Date de début et Date de fin

Dans la {{ "partie (3)" | red }} vous pouvez souhaiter configurer deux dates de cette façon dans le passé :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/date-debut-date-fin.png" class="glightbox" data-gallery="galerie" title="Voyage dans le temps entre deux dates">
        <img src="/images/voyage-dans-le-temps/date-debut-date-fin.png" alt="Partie 3" />
    </a>
    <figcaption><em>Voyage dans le temps entre deux dates</em></figcaption>
</figure>

Pour spécifier deux dates, vous devez mettre zéro dans les deux cases :

- "{{ "Jours dans le passé" | red }}" = 0
- "{{ "Jours avant la fin" | red }}" = 0

Sur le boite de dialogue {{ "Strategy Automotion" | keywordi }} {{ "(1)" | red }} :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/entre-deux-dates.png" class="glightbox" data-gallery="galerie" title="Voyage dans le temps entre deux dates">
        <img src="/images/voyage-dans-le-temps/entre-deux-dates.png" alt="Partie 3" />
    </a>
    <figcaption><em>Voyage dans le temps entre deux dates</em></figcaption>
</figure>

Attention au format des dates c'est : {{ "année-mois-jour" | red }}.

C'est un  peu fastidieux alors ces dates peuvent être choisies graphiquement.

## Aide graphique à la sélection des dates

### Sélectionnez une date dans le passé

Marquez une annotation date en maintenant la touche {{ "d" | keywordi }} et en cliquant sur le graphe. Une barre verticale se déssine avec la date en bas du graphe sur l'axe des abscisses :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/selecte-une-date.png" class="glightbox" data-gallery="galerie" title="Sélectionnez une date">
        <img src="/images/voyage-dans-le-temps/selecte-une-date.png" alt="Partie 3" />
    </a>
    <figcaption><em>Sélectionnez une date</em></figcaption>
</figure>

- {{ "(1)" | red }} Sélectionnez une date avec la touche {{ "d" | keywordi }}

- {{ "(2)" | red }} Cliquez sur {{ "Set" | keywordi }} pour "setter" la date

Le message en vert vous indique qu'une date a été sélectionnée.

Cliquez sur le bouton {{ "Graphique" | keywordi }}  :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/une-date-selected.png" class="glightbox" data-gallery="galerie" title="Sélectionnez une date">
        <img src="/images/voyage-dans-le-temps/une-date-selected.png" alt="Partie 3" />
    </a>
    <figcaption><em>Sélectionnez une date cliquez sur Graphique</em></figcaption>
</figure>

Le graphique s'affiche alors depuis la date sélectionnée.

### Sélectionnez deux dates

Pour seletionner une plage de temps, vous pouvez "setter" les deux dates de votre voyage dans le temps par l'interface graphique, de la façon suivante :

Vous positionnez deux annotations et vous cliquez sur le bouton {{ "Set" | keywordi }} :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/selecte-deux-dates.png" class="glightbox" data-gallery="galerie" title="Sélectionnez deux dates">
        <img src="/images/voyage-dans-le-temps/selecte-deux-dates.png" alt="Partie 3" />
    </a>
    <figcaption><em>Sélectionnez deux dates</em></figcaption>
</figure>

- {{ "(1)" | red }} Maintenez la touche {{ "d" | keywordi }} pendant que vous cliquez sur le graphe une première fois.

- {{ "(2)" | red }} Maintenez la touche {{ "d" | keywordi }} pendant que vous cliquez sur le graphe une deuxième fois

- {{ "(3)" | red }} Cliquez sur le bouton {{ "Set" | keywordi }} :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/interface-deux-date-selected.png" class="glightbox" data-gallery="galerie" title="Voyage entre deux dates">
        <img src="/images/voyage-dans-le-temps/interface-deux-date-selected.png" alt="Image" />
    </a>
    <figcaption><em>Voyage dans le temps entre deux dates</em></figcaption>
</figure>

L'interface de récupération des données a été "settée" (configurée) avec vos deux dates.

La touche {{ "Now" | keywordi }} vous permet de remettre la date du jour dans le champs {{ "Date de fin" | keywordi }}.

Pour terminer, cliquez sur le bouton {{ "Graphique" | keywordi }} et vous obtenez le graphique d'action TESLA pour les deux dates que vous avez choisies :

<figure style="text-align: center;">
    <a href="/images/voyage-dans-le-temps/entre-deux-dates-2.png" class="glightbox" data-gallery="galerie" title="Voyage entre deux dates">
        <img src="/images/voyage-dans-le-temps/entre-deux-dates-2.png" alt="Image" />
    </a>
    <figcaption><em>Voyage dans le temps entre deux dates positionnées graphiquement</em></figcaption>
</figure>

## Supprimer les annotations

Vous avez placé trop d'annotations pour pouvoir les {{ "Setter" | keyword }} comme dates afni de tracer un graphique. Le message de la fenêtre {{ "Strategy Automation" | keywordi }} vous l'indique.

Placez votre souris sur le graphe concerné et tapez {{ "Ctrl+D" | keywordi }} pour effacer les annotations.

## Plateforme de trading technique

Voilà, vous savez tout sur le voyage dans le temps grâce à la plateforme d'analyse technique :

- <a href="https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html">TradingInPython</a>
