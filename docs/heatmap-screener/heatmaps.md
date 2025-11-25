# Cartes de chaleur & Performances

Vous avez créé vos screeners en utilisant le {{ "Sélecteur de stocks" | keyword }} Menu {{ "Screeners" | keyword }} -> [Gestion des screeners](./screeners.md), vous pouvez afficher des Cartes de chaleur.

Surveillez facilement et rapidement {{ "des dizaines d'actions" | keyword }}, grâce aux indicateurs techniques dans une Carte graphique de couleurs (chaleur).

La Carte de chaleur (heatmap) vous permet de {{ "visualiser les performances d'actions" | keyword }}. Elle est pleine de couleurs vertes claires à vertes foncées pour les cours qui montent et rouges à rouges foncées pour les cours qui baissent, elle permet donc de surveiller la tendance d'un marché sur des dizaines d'actions d'un seul coup d'œil.

La Carte de chaleur calcule des {{ "indicateurs techniques" | keyword }} pour chaque actions afin de délivrer un {{ "Signal d'achat" | keyword }} ou {{ "de vente" | keyword }}.

## Ouvrir une carte de chaleur

Dans le menu {{ "Monitoring" | keyword }} choisissez {{ "Performace Heatmap" | keyword }} (Carte de chaleur et de performances).

<figure style="text-align: center;">
    <a href="/images/heatmap/menu-gestion-screeners.png" class="glightbox" data-gallery="galerie" title="Menu Monitoring">
        <img src="/images/heatmap/menu-gestion-screeners.png" />
    </a>
    <figcaption><em>Menu Monitoring -> Performance heatmap</em></figcaption>
</figure>


Une Heatmap ou carte de chaleur représente les performances des actions sous forme de couleurs avec des couleurs plus ou moins vertes pour les actions à tendance haussière et plus ou moins rouge pour les actions à tendance baissière.

## Choisir un fichier

Créez vos screeners en sélectionnant les actions que vous souhaitez mettre sous surveillance, ouvrez le [Sélecteur de Stocks](screeners.md), choisissez dans la liste des actions de la plateforme celle que vous souhaitez voir dans la Heatmap (Carte de chaleur) :

<figure style="text-align: center;">
    <a href="/images/heatmap/heatmap.png" class="glightbox" data-gallery="galerie" title="Menu screeners">
        <img src="/images/heatmap/heatmap.png" />
    </a>
    <figcaption><em>Carte de chaleur et de performance</em></figcaption>
</figure>

Cliquez sur le bouton {{ "Ouvrir" | keywordi }} pour choisir un fichier screeners (format .json). 

Ici on est avec {{ "info-quantique.json" | keyword }} il y a 5 actoins du marché de l'informatique Quantique :

- Stocks chargées: 5 - QBTS, IONQ, PLTR, QUBT, RGTI

## Exécuter la Carte de chaleur

Lancez l'exécution des calculs pour les actions sélectionnées.

Cliquez sur le bouton {{ "Exécuter" | keywordi }} pour afficher la carte de Performance :

<figure style="text-align: center;">
    <a href="/images/heatmap/heatmap-quantique.png" class="glightbox" data-gallery="galerie" title="Carte de chaleur du marché de l'informatique quantique">
        <img src="/images/heatmap/heatmap-quantique.png"/>
    </a>
    <figcaption><em>Carte de chaleur du marché de l'informatique quantique</em></figcaption>
</figure>

- Intervalle : pour la récupération des données ici `1d` 1 jour
- Sampling : -3 -5 -7 signifie que les calculs vont se faire -3 -5 et -7 jours en arrière

## Interpréter la Carte

Pour comprendre les couleurs de la carte, ouvrez la fiche technique de l'action.

Par exemple pour D-Wave Quantum (QBTS), en maintenant la touche {{ "Ctrl+ Clique" | keyword }} sur la Case de couleur de QBTS :

<figure style="text-align: center;">
    <a href="/images/heatmap/fiche-technique.png" class="glightbox" data-gallery="galerie" title="Fiche technique de l'action">
        <img src="/images/heatmap/fiche-technique.png"/>
    </a>
    <figcaption><em>Fiche technique de l'action</em></figcaption>
</figure>

Vous obtenez la fiche technique de l'action avec ses performances, le Signal est {{ "VENTE" | keyword }}.

Les indicateurs techniques sont mauvais pour QBTS, la couleur de la carte est Rouge.

Dans la fiche technique d'une action, vous retrouvez les indicateurs techniques calculés pour cette action sous surveillance :

{{ "SMA" |  i_tooltip }}, {{ "RSI" | i_tooltip }}, {{ "MACD" | i_tooltip }}, {{ "ADX" | i_tooltip }}, {{ "ATR" | i_tooltip }}, {{ "Bolls" | i_tooltip }}, {{ "OBV" | i_tooltip }} sont calculés et interprétés pour vous dans ce résumé des signaux techniques.

Ces Screeners alertes vous permettent de mettre des dizaines d'actions sous surveillance. La case `AUTO 1m` vous permet de recalculer les indicateurs techniques pour la nouvelle période de temps et de rafraîchir la heatmap.

## Synchronisation avec l'analyse technique

Le côté pratique de la {{ "Carte de Performances" | keyword }}, c'est que vous pouvez, en cliquant sur les carrés d'une stock, synchroniser avec l'action à trader pour afficher le graphe d'une analyse technique.

<figure style="text-align: center;">
    <a href="/images/heatmap/synchro-analyse-technique.gif" class="glightbox" data-gallery="galerie" title="Fiche technique de l'action">
        <img src="/images/heatmap/synchro-analyse-technique.gif"/>
    </a>
    <figcaption><em>Fiche technique de l'action</em></figcaption>
</figure>

Notez deux choses dans cette animation :

1. Passez la souris sur les boutons de cartes, vous avez le nom de l'action qui d'affiche.
2. Sur la partie droite, dans {{ "Stratégie Automation" | keywordi }} l'action est modifiée quand vous cliquez sur le bouton de la carte.

C'est pratique pour lancer une analyse technique de l'action que vous avez dans votre carte.

## Vidéo YouTube

Voici une vidéo : comment surveiller des dizaines d'actions avec les Carte de chaleur et de Performances :

<div align="center" class="md-video">
<iframe width="560" height="315" src="https://www.youtube.com/embed/jTwOgR3HhXE?si=PQ32fBVekfk1MpWM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
