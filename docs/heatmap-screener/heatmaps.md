# Cartes de chaleur & Performance

Vous avez créé vos screeners en utilisant le **Sélecteur de stocks** Menu **Screeners** -> [Gestion des screeners]({{ base_url }}/heatmap-screener/screeners/), vous pouvez afficher des Cartes de chaleur.

Surveillez facilement et rapidement **des dizaines d'actions**, grâce aux indicateurs techniques dans une Carte graphique de couleurs (chaleur).

La Carte de chaleur (heatmap) vous permet de **visualiser les performances d'actions**. Elle est pleine de couleurs vertes claires à vertes foncées pour les cours qui montent et rouges à rouges foncées pour les cours qui baissent, elle permet donc de surveiller la tendance d'un marché sur des dizaines d'actions d'un seul coup d'œil.

La Carte de chaleur calcule des **indicateurs techniques** pour chaque actions afin de délivrer un **Signal d'achat** ou **de vente**.

## Ouvrir une carte de chaleur

Dans le menu **Monitoring** choisissez **Performace Heatmap** (Carte de chaleur et de performances).

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/heatmap/menu-gestion-screeners.png" class="glightbox" data-gallery="galerie" title="Menu Monitoring">
        <img src="{{ base_url }}/images/heatmap/menu-gestion-screeners.png" />
    </a>
    <figcaption><em>Menu Monitoring -> Performance heatmap</em></figcaption>
</figure>


Une Heatmap ou carte de chaleur représente les performances des actions sous forme de couleurs avec des couleurs plus ou moins vertes pour les actions à tendance haussière et plus ou moins rouge pour les actions à tendance baissière.

## Choisir un fichier

Créez vos screeners en sélectionnant les actions que vous souhaitez mettre sous surveillance, ouvrez le [Sélecteur de Stocks](screeners.md), choisissez dans la liste des actions de la plateforme celle que vous souhaitez voir dans la Heatmap (Carte de chaleur) :

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/heatmap/heatmap.png" class="glightbox" data-gallery="galerie" title="Menu screeners">
        <img src="{{ base_url }}/images/heatmap/heatmap.png" />
    </a>
    <figcaption><em>Carte de chaleur et de performance</em></figcaption>
</figure>

Cliquez sur le bouton **Ouvrir** pour choisir un fichier screeners .json. Ici on est avec **info-quantique.json** il y a 5 actoins du marché de l'informatique Quantique :

- Stocks chargées: 5 - QBTS, IONQ, PLTR, QUBT, RGTI

## Exécuter la Carte de chaleur

Lancez l'exécution des calculs pour les actions sélectionnées.

Cliquez sur le bouton **Exécuter** pour afficher la carte de Performance :

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/heatmap/heatmap-quantique.png" class="glightbox" data-gallery="galerie" title="Carte de chaleur du marché de l'informatique quantique">
        <img src="{{ base_url }}/images/heatmap/heatmap-quantique.png"/>
    </a>
    <figcaption><em>Carte de chaleur du marché de l'informatique quantique</em></figcaption>
</figure>

- Intervalle : pour la récupération des données ici `1d` 1 jour
- Sampling : -3 -5 -7 signifie que les calculs vont se faire -3 -5 et -7 jours en arrière

## Interpréter la Carte

Pour comprendre les couleurs de la carte, ouvrez la fiche technique de l'action.

Par exemple pour D-Wave Quantum (QBTS), en maintenant la touche **Ctrl+ Clique** sur la Case de couleur de QBTS :

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/heatmap/fiche-technique.png" class="glightbox" data-gallery="galerie" title="Fiche technique de l'action">
        <img src="{{ base_url }}/images/heatmap/fiche-technique.png"/>
    </a>
    <figcaption><em>Fiche technique de l'action</em></figcaption>
</figure>

Vous obtenez la fiche technique de l'action avec ses performances, le Signal est **VENTE**. 

Les indicateurs techniques sont mauvais pour QBTS, la couleur de la carte est Rouge.

Dans la fiche technique d'une action, vous retrouvez les indicateurs techniques calculés pour cette action sous surveillance :

{{ "SMA" |  g_tooltip }}, {{ "RSI" | g_tooltip }}, {{ "MACD" | g_tooltip }}, {{ "ADX" | g_tooltip }}, {{ "ATR" | g_tooltip }}, {{ "Bolls" | g_tooltip }}, {{ "OBV" | g_tooltip }} sont calculés et interprétés pour vous dans ce résumé des signaux techniques.

Ces Screeners alertes vous permettent de mettre des dizaines d'actions sous surveillance. La case `AUTO 1m` vous permet de recalculer les indicateurs techniques pour la nouvelle période de temps et de rafraîchir la heatmap.

## Synchronisation avec l'analyse technique

Le côté pratique de la Carte de Performance, notez deux choses dans l'animation suivante :

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/heatmap/synchro-analyse-technique.gif" class="glightbox" data-gallery="galerie" title="Fiche technique de l'action">
        <img src="{{ base_url }}/images/heatmap/synchro-analyse-technique.gif"/>
    </a>
    <figcaption><em>Fiche technique de l'action</em></figcaption>
</figure>

1. Passez la souris sur les boutons de cartes, vous avez le nom de l'action qui d'affiche
2. Sur la partie droite l'action est modifiée quand vous cliquez sur le bouton de la carte

C'est pratique pour lancer une analyse technique de l'action que vous avez dans votre carte.

## Vidéo YouTube

Voici une vidéo : comment surveiller des dizaines d'actions avec les Carte de chaleur et de Performances :

<div align="center" class="md-video">
<iframe width="560" height="315" src="https://www.youtube.com/embed/jTwOgR3HhXE?si=PQ32fBVekfk1MpWM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
