# Récupération des données du cours de bourse

Il s'agit de récupérer des données au près des plateformes {{ "open data" | keyword }} reliées aux grandes bourses du monde entier. Ces plateformes donne accès aux cours de la bourse par des API que nous utilisons grâce au langage Python.

La plateforme  {{ "TradingInPython" | keyword }} se connecte à n'importe qu'elle source de data, ici nous sommes avec YahooFinance mais vous pouvez tout aussi bien vous connecter à d'autres sources comme IBKR et d'autres.

## Sélection de l'action à trader  

L’application s’ouvre sur la dernière action que vous aviez sélectionnée pour trader.

Exemple : Si vous étiez sur l’action BMW (secteur automobile), vous pouvez passer votre souris sur l’indication "secteur de la stock", l'indication vous demande de choisir le menu "Stocks" pour choisir un autre secteur :

<div style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEg6CQtDn1RWe8qASBzDC9f-8cfbKpNhgIywNwwuN7iNhy_ZXXAO1V5i48f-f80ua_kFjWiShurUUBX5D9V5C5UiGXEET6VWP_BmuYZwqMAjqGoIGE4S1Nb4XMYIZ7XUWFxdYHFqTwb8LxvVDmXUNvSgteK4VGSm1a_2q8R6dLDCwD_e-o5sqx_1Nz_XJmnf"><img alt="Choisir le secteur de la stock à trader" data-original-height="458" data-original-width="272" src="https://blogger.googleusercontent.com/img/a/AVvXsEg6CQtDn1RWe8qASBzDC9f-8cfbKpNhgIywNwwuN7iNhy_ZXXAO1V5i48f-f80ua_kFjWiShurUUBX5D9V5C5UiGXEET6VWP_BmuYZwqMAjqGoIGE4S1Nb4XMYIZ7XUWFxdYHFqTwb8LxvVDmXUNvSgteK4VGSm1a_2q8R6dLDCwD_e-o5sqx_1Nz_XJmnf=s16000" title="Choisir le secteur de la stock à trader" /></a></div>

Cliquez sur le menu "Stocks" pour changer le secteur ou le portefeuille de l'action à trader :

<div style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEiRVq8JuPbCGeJqImrtt0uGAfxMLROV3cKQXEd8xrBE-MEpe31rUGTZcvlcVUDj1GWjWOtZJboLY249XRFG3noWPIm-q8-5CDJcGwuULlx4hXr2QkV4Kq1q-IhemXFl5eSFRymNUIj5hNoR-YfbULoQZUdjx2EVARhD1J4zI6PPsufl715tWEXTTrYLn2be"><img alt="Secteur de la stock à trader" data-original-height="490" data-original-width="322" src="https://blogger.googleusercontent.com/img/a/AVvXsEiRVq8JuPbCGeJqImrtt0uGAfxMLROV3cKQXEd8xrBE-MEpe31rUGTZcvlcVUDj1GWjWOtZJboLY249XRFG3noWPIm-q8-5CDJcGwuULlx4hXr2QkV4Kq1q-IhemXFl5eSFRymNUIj5hNoR-YfbULoQZUdjx2EVARhD1J4zI6PPsufl715tWEXTTrYLn2be=s16000" title="Secteur de la stock à trader" /></a></div>

Vous vous retrouvez avec les actions (stocks) du secteur de l'aérospatial-défense :

<div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEjj668LfHhpnLKH2g6eTHU4waF_RIPZPle6JZEHxH6ildI3gSIvopGutHZQeziIBO-fQ99g8iC-xuIaEVQcQfzGimmRatMkcg2U2rTykcls01W-v1-wq_GCyYkDpk6jwivXFhWCQcrLuxaskYXtQwBYncX5JwzXqzLvaEc3stpyk5RMgqnP7IFdoEIx4s1N" style="margin-left: 1em; margin-right: 1em;"><img alt="" data-original-height="493" data-original-width="424" src="https://blogger.googleusercontent.com/img/a/AVvXsEjj668LfHhpnLKH2g6eTHU4waF_RIPZPle6JZEHxH6ildI3gSIvopGutHZQeziIBO-fQ99g8iC-xuIaEVQcQfzGimmRatMkcg2U2rTykcls01W-v1-wq_GCyYkDpk6jwivXFhWCQcrLuxaskYXtQwBYncX5JwzXqzLvaEc3stpyk5RMgqnP7IFdoEIx4s1N=s16000" /></a></div>

Vous choisissez l'action que vous souhaitez trader parmi ce secteur.

## Choisir l’intervalle et la période  

Vous observez le cours des actions qui vous intéressent en sélectionnant un intervalle de temps et une  période sur laquelle vous souhaitez analyser le cours de ces actions.

Le choix de l'intervalle et de la période se fait parmi les valeurs suivantes :

- L’{{ "intervalle de temps" | keyword }} (Interval) pour l’échantillonnage (1 m, 2 m, 5 m, 15 m, 30 m, 60 m, 1h, 4h, 1d, …)
- La {{ "période d’analyse" | keyword }} (Period) ou bien des dates de début et de fin.

Grâce à l'interface :

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhD_7q2X-Ee4TwywyhcC0AFeh90036CqVw6KCfA-h0UXc7DnIMwr8TV3okxiyRhNSYclOd82vUXRs1FWtAHKnzJ_OalUXr3oqOmWsl58eShURV7kuRfFY8M0xjbqMlh_79q-zAvMh8XBKAYzn6BZNdzt9uzWX9sjPIRgg5ct4UXFczMcOzeRsSogsX_XgiS/s458/2025-01-27_15h08_47.png" style="margin-left: auto; margin-right: auto;"><img alt="TradingInPython" border="0" data-original-height="458" data-original-width="272" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhD_7q2X-Ee4TwywyhcC0AFeh90036CqVw6KCfA-h0UXc7DnIMwr8TV3okxiyRhNSYclOd82vUXRs1FWtAHKnzJ_OalUXr3oqOmWsl58eShURV7kuRfFY8M0xjbqMlh_79q-zAvMh8XBKAYzn6BZNdzt9uzWX9sjPIRgg5ct4UXFczMcOzeRsSogsX_XgiS/s16000/2025-01-27_15h08_47.png" title="TradingInPython" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Sélection de l'action et de la période d'analyse</td></tr></tbody></table>

### Paramètres supportés  

- `period : 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max`.
- `interval : 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 4h, 1d, 5d, 1wk, 1mo, 3mo`.

> Note : Les données intraday (ex : 1 m, 2 m) ne peuvent pas s’étendre sur une période trop ancienne.
> Vous risquez alors de voir un message {{ "NO DATA" | keyword }} afficher sur l'interface.

Vous choisissez ensuite parmi les stratégies d'analyses proposées par la plateforme de trading.

## Récupération des datas sur une période de temps donnée

Vous avez {{ "trois façons" | keyword }} de récupérer des données :

- La première c'est avec {{ "Interval" | keywordi }} et {{ "Period" | keywordi }} mais cette méthode est limitée et vous ne pouvez pas retourner dans le passé.

De toutes les façons, sélectionnez un "Interval" d'échantillonnage et en suite,

- Pour utiliser {{ "Jours dans le passé" | keywordi }} et {{ "Jours avant la fin" | keywordi }} sélectionnez "none" (tout en bas de la liste) dans "Period".

Vous pouvez alors remonter dans le passé sur une période de temps égale à "Jours avant la fin" moins "Jours dans le passé".

- Pour utiliser les deux dates {{ "Date de début" | keywordi }} et {{ "Date de fin" | keywordi }}, il vous faut mettre :

  - {{ "Period" | keywordi }} à "none"
  - {{ "Jours dans le passé" | keywordi }} à 0
  - {{ "Jours avant la fin" | keywordi }} à 0

Dans ce cas, les données sont récupérées entre {{ "Date de début" | keywordi }} et {{ "Date de fin" | keywordi }}.

Le bouton {{ "Now" | keywordi }} vous permet de remplir automatiquement {{ "Date de fin" | keywordi }} avec la date d'aujourd'hui.

Voici une page pour vous expliquer en détails comment faire :

- [Voyagez dans le temps](./voyage-dans-le-temps.md)

## Récupération des données en temps réel

Pour chacune des stratégies, vous avez la case {{ "AUTO" | keywordi }} dans la fenêtre {{ "Indicateurs secondaires" | keywordi }}
pour récupérer les données en {{ "temps réel" | keyword }}, à intervalle de temps régulier,
ainsi vous pouvez voir les graphiques du cours de l'action se dessiner au fil du temps.

<figure style="text-align: center;" title="Récupération des datas en temps réel">
  <img src="{{ base_url }}/images/recuperation-des-data/mode-auto.png" class="noborder"/>
  <figcaption><em>Récupération des data en temps réel</em></figcaption>
</figure>

Vous avez la possibilité de suivre le cours de l’action minute par minute :  

- Cochez la case {{ "AUTO" | keywordi }} (ou mode automatique) pour que les données soient récupérées en continu.
- Une thread dédiée démarre pour récupérer les données en temps réel, et les graphiques se mettent à jour dynamiquement.

La console vous prévient que le mode Automatique a démarré :

<figure style="text-align: center;" title="Console indication mode AUTO">
  <img src="{{ base_url }}/images/recuperation-des-data/console-mode-auto.png" class="noborder"/>
  <figcaption><em>Console indication mode AUTO</em></figcaption>
</figure>

La console affiche le message "Auto started ...".

## Remarques pratiques  

- Veillez à choisir l’{{ "intervalle" | keyword }} en fonction de votre horizon de trading : `intraday, swing, ou long terme`.  
- Prenez garde à la {{ "granularité" | keyword }} : par exemple, un intervalle de 1 m sur une période de plusieurs mois peut être lourd en données.  
- Si vous utilisez les dates de début/fin plutôt que {{ "period" | keyword }}, vous avez plus de flexibilité pour remonter dans les archives.  
- Pour un suivi réel (minute par minute), vous avez l’option [AUTO](#recuperation-des-donnees-en-temps-reel).

## Exemple de code avec la librairie yfinance

Si vous souhaitez, voici un le code Python illustrant la récupération des données :

```python
import yfinance as yf

ticker = yf.Ticker("BMW.DE")  # Symbole de l’action

data = ticker.history(
    interval="1h",
    period="6mo",            # exemple pour les 6 derniers mois
    prepost=True             # si disponible, inclure pré- et post-marché
)

# Différentes façons d'appeler la fonction de récupération des donnée
data = ticker.history( 
    period=period_select, 
    interval=interval_fecth, 
    prepost=prepost, 
    auto_adjust=auto_adjust
)

data = ticker.history( 
    start=_date_start, 
    end=_date_end, 
    interval=interval_fecth, 
    prepost=prepost, 
    auto_adjust=auto_adjust
)

```
