# Intraday VWAP + STOCH

Maintenant, passons à l'{{ "Intraday" | keyword }}, c'est à dire le trading au sein de la journée, le suivi minutes par minute du cours des actions.

## Interface

Vous souhaitez suivre le cours de votre action durant la journée pour savoir quels sont les meilleurs moments d'entrée et de sortie, la stratégie {{ "VWAP" | i_link }} + {{ "STOCH" | i_link }} Intraday, est adaptée à cette analyse du cours dans la journée :

<figure style="text-align: center;">
    <a href="/images/strategies/intraday-vwap-stoch/interface.png" class="glightbox" data-gallery="galerie" title="Intraday VWAP + STOCH">
        <img src="/images/strategies/intraday-vwap-stoch/interface.png"/>
    </a>
    <figcaption><em>Intraday VWAP + STOCH</em></figcaption>
</figure>

## Configuration

Configuration de l'indicateur {{ "STOCH" | i_tooltip }} pour le suivi intraday du cours de l'action.

<figure style="text-align: center;">
    <a href="/images/strategies/intraday-vwap-stoch/configuration.png" class="glightbox" data-gallery="galerie" title="Configuration - Intraday VWAP + STOCH">
        <img src="/images/strategies/intraday-vwap-stoch/configuration.png"/>
    </a>
    <figcaption><em>Configuration - Intraday VWAP + STOCH</em></figcaption>
</figure>

Les boutons de l'interface de Configuration, vous permettent de choisir les valeurs aux moyennes mobiles de l'indicateur STOCH adaptées aux échelles de temps :

- Default Long : valeurs adaptées à un trading long sur 1 heure
- Default short : pour un trading plus court
- Default : pour un trading au plus court

Vous avez également le choix des valeurs K% D% et Smooth que vous pouvez sauvegarder pour l'action en cours.

Si le prix est au dessus du {{ "VWAP" | i_tooltip }} alors il est surestimé et une correction vers le bas pourrait se produire, si au contraire le prix est en dessous, une correction à la hausse pourrait se produire.

Dans cette stratégie vous avez également deux autres indicateurs l'{{ "ATR" | i_link }} et le {{ "OBV" | i_link }}.

## Suivi en temps réel

Dans la fenêtre indicateurs secondaires la case à cocher {{ "AUTO" | keywordi }} (fetch data en mode automatique) vous permet de relancer l'acquisition des données toutes les minutes en foonction de l'échelle de temps choisie.

Pour suivre le cours des actions en temps réel :

<figure style="text-align: center;">
    <a href="/images/strategies/intraday-vwap-stoch/indicateurs-secondaires.png" class="glightbox" data-gallery="galerie" title="Suivi du cours en temps réel">
        <img src="/images/strategies/intraday-vwap-stoch/indicateurs-secondaires.png"/>
    </a>
    <figcaption><em>Mode AUTO - Suivi du cours en temps réel</em></figcaption>
</figure>
