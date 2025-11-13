# Cartes de chaleur & Performance

Un moyen de surveiller le marché avec des cartes de chaleurs graphiques qui affichent les performances des actions misent sous surveillance.

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/heatmap/menu-gestion-screeners.png" class="glightbox" data-gallery="galerie" title="Menu Monitoring">
        <img src="{{ base_url }}/images/heatmap/menu-gestion-screeners.png" />
    </a>
    <figcaption><em>Menu Monitoring -> Performance heatmap</em></figcaption>
</figure>

Dans le menu **Monitoring** choisissez **Performace Heatmap** (Carte de chaleur et de performances).

Surveillez facilement et rapidement des dizaines d'actions, grâce aux indicateurs techniques dans une Heatmap Performance de la plateforme.

Une Heatmap ou carte de chaleur représente les performances des actions sous forme de couleurs avec des couleurs plus ou moins vertes pour les actions à tendance haussière et plus ou moins rouge pour les actions à tendance baissière.

Créez vos screeners en sélectionnant les actions que vous souhaitez mettre sous surveillance, ouvrez le [Sélecteur de Stocks](screeners.md), choisissez dans la liste des actions de la plateforme celle que vous souhaitez voir dans la Heatmap (Carte de chaleur) :

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/heatmap/heatmap.png" class="glightbox" data-gallery="galerie" title="Menu screeners">
        <img src="{{ base_url }}/images/heatmap/heatmap.png" />
    </a>
    <figcaption><em>Carte de chaleur et de performance</em></figcaption>
</figure>

Cliquez sur le bouton **Ouvrir** pour choisir un fichier screeners .json. Ici on est avec **info-quantique.json** il y a 5 actoins du marché de l'informatique Quantique :

- Stocks chargées: 5 - QBTS, IONQ, PLTR, QUBT, RGTI

Cliquez sur le bouton **Exécuter** pour afficher la carte de Performance :

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/heatmap/heatmap-quantique.png" class="glightbox" data-gallery="galerie" title="Carte de chaleur du marché de l'informatique quantique">
        <img src="{{ base_url }}/images/heatmap/heatmap-quantique.png"/>
    </a>
    <figcaption><em>Carte de chaleur du marché de l'informatique quantique</em></figcaption>
</figure>

- Intervalle : pour la récupération des données ici '1d' 1 jour
- Sampling : -3 -5 -7 signifie que les calculs vont se faire -3 -5 et -7 jours en arrière

Pour comprendre les couleurs de la carte vous ouvrez la fiche technique de l'action par exemple 

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/heatmap/fiche-technique.png" class="glightbox" data-gallery="galerie" title="Fiche technique de l'action">
        <img src="{{ base_url }}/images/heatmap/fiche-technique.png"/>
    </a>
    <figcaption><em>Fiche technique de l'action</em></figcaption>
</figure>
