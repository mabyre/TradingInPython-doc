# Intraday VWAP + STOCH

Maintenant, passons à l'Intraday, le trading au sein de la journée.

Vous souhaitez suivre le cours de votre action durant la journée pour savoir quels sont les meilleurs moments d'entrée et de sortie, la stratégie {{ "VWAP" | i_link }} + {{ "STOCH" | i_link }} Intraday, est adaptée à cette analyse du cours dans la journée :

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/intraday-vwap-stoch/interface.png" class="glightbox" data-gallery="galerie" title="Intraday VWAP + STOCH">
        <img src="{{ base_url }}/images/strategies/intraday-vwap-stoch/interface.png"/>
    </a>
    <figcaption><em>Intraday VWAP + STOCH</em></figcaption>
</figure>

Les boutons de la Configuration :

- Default Long
- Default short
- Default 

sont là pour donner des valeurs aux moyennes mobiles de l'indicateur STOCH.

Dans cette stratégie vous avez également deux autres indicateurs l'{{ "ATR" | i_tooltip }} et le {{ "OBV" | i_tooltip }}.

Si le prix est au dessus du {{ "VWAP" | i_tooltip }} alors il est surestimé et une correction vers le bas pourrait se produire, si au contraire le prix est en dessous, une correction à la hausse pourrait se produire.
