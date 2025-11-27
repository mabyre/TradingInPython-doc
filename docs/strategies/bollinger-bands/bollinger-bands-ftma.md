# Bandes de Bollinger FTMA

Ce sont les {{ "Bandes de Bollinger" | keyword }} Four Times frame Mobile Average {{ "FTMA" | keyword }} sur quatre horizons de temps différents.

L'intérêt des Bandes de Bollinger sur des horizons de temps différents, 
c'est que cet outil mathématique peut être considérer comme une décomposition temporelle (ou fréquentielle : {{ "f = 1/T" | keyword }}).

Cet outil de trading technique va donc nous donner énormément d'informations sur le signal (cours de l'action à trader).

## Interface

Voici l'interface qui permet de piloter cette stratégie :

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/interface.png" class="glightbox" data-gallery="galerie"  title="Bandes de Bollinger">
        <img src="/images/strategies/bollinger-bands/interface.png"/>
    </a>
    <figcaption><em>Bandes de Bollinger</em></figcaption>
</figure>

Quand les Bandes de Bollinger s'alignent, cela indique généralement une tendance claire. Quand elles se contractent c'est souvent avant un mouvement fort.

## Configuration

L'interface de Configuration vous permet de modifier les horizons des Four Times Mobile Average (FTMA), les moyennes mobiles des Bandes de Bollinger.

Le Slider vous permet de les déplacer toutes les quatre ensemble.

<figure style="text-align: center;">
    <a href="/images/strategies/bollinger-bands/config.png" class="glightbox" data-gallery="galerie"  title="Bandes de Bollinger - Configuration">
        <img src="/images/strategies/bollinger-bands/config.png"/>
    </a>
    <figcaption><em>Bandes de Bollinger - Configuration</em></figcaption>
</figure>

Les boutons vous permettent de choisir parmi trois choix différents :

- {{ "Default Short" | keywordi }} pour mettre les valeurs courtes pour les 4 FTMA Bolls.
- {{ "Default" | keywordi }} pour remettre les valeurs par défaut.
- {{ "Default Long" | keywordi }} pour mettre les valeurs longues pour les 4 FTMA Bolls.

Vous pouvez choisir des valeurs pour chacune des FTA 1, 2, 3, 4 et le bouton {{ "Save" | keywordi }} vous permet de sauver ces valeurs pour l'action en cours.

- {{ "Read" | keywordi }} pour relire les valeurs sauvegardées.

## Comment trader

Voici une page dédiée à un trade en tendance haussière avec les Bandes de Bollinger FTMA :

- [Trader avec les Bandes de Bollinger FTMA](./bollinger-bands-ftma-trading.md)

## Vidéo sur YouTube

Vous avez raté quelque chose :

<div align="center" class="md-video">
<iframe width="560" height="315" src="https://www.youtube.com/embed/vyCHZOKIokg?si=73ddSsx-bJKCydbc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

Voilà vous savez tout sur les stratégies à base de Bandes de Bollinger.
