# Indicateur technique boursier filtre de Kalman

En traitement numérique du signal le filtre de Kalman est un **"must have"**, un outil mathématique à essayer.

Rudolf E. Kalman, un ingénieur hongrois-américain, publie en 1960 son article fondateur : "A New Approach to Linear Filtering and Prediction Problems".

L'innovation majeure : Kalman reformule le problème en termes d'espace d'état (**variables d'état** du système) plutôt qu'en termes de **fonctions de transfert**.

Cela permet :

- De traiter des systèmes non-stationnaires (qui évoluent dans le temps)
- Une implémentation récursive très efficace
- Une solution optimale au sens des moindres carrés pour les systèmes linéaires

Le filtre de Kalman résout élégamment ce problème : comment estimer l'état d'un système dynamique à partir de mesures bruitées ?

## Définition générale

Le filtre de Kalman est un algorithme récursif d’estimation qui permet de prédire et de corriger la valeur d’un système dynamique bruité (incertain), à partir de mesures elles-mêmes bruitées.

Autrement dit, il cherche à extraire le "signal réel" d’une série de données bruitées — par exemple, un prix boursier soumis aux fluctuations aléatoires du marché.

C’est une méthode de filtrage optimal au sens de la minimisation de la variance : elle minimise l’erreur quadratique moyenne entre l’état estimé et l’état réel.

Faisons nous grâce des équations, alors pourquoi utiliser le filtrage de Kalman ?

## Une intuition simple

Imaginons de suivre le prix d’une action avec beaucoup de bruit (variations aléatoires).

Le filtre de Kalman agit comme un “observateur intelligent” :

- il prédit la prochaine valeur en supposant une continuité (tendance du marché),
- puis il corrige cette prédiction avec la nouvelle observation réelle,
- en pondérant les deux selon la confiance qu’il accorde à chacun (le bruit).

Résultat : un signal lissé mais réactif, contrairement à une simple moyenne mobile.

## En finance et en trading

Le filtre de Kalman est utilisé pour :

**Filtrage de tendance :**

Lissage intelligent des prix sans le retard typique des moyennes mobiles.

**Prévision à court terme :**

En prolongeant la phase de prédiction, on peut anticiper légèrement les mouvements.

**Arbitrage et pairs trading :**

Utilisé pour estimer le “spread réel” entre deux actifs corrélés.

**Estimation du momentum ou de la volatilité cachée :**

Kalman peut estimer des variables non observables du marché.

## Paramétrage

### Les paramètres les plus importants Variances Q et R

Q : covariance du "process noise" (bruit du système ou processus), contrôle la réactivité du filtre

**Q = diff_var *process_noise_factor* vol_factor**

- augmentation du process_noise_factor => filtre plus réactif
- diminution du process_noise_factor => filtre plus lisse

par défaut process_noise_factor = 0.01 valeurs à tester : 0.005, 0.02, 0.05

R : covariance du bruit de mesure du processus, contrôle de la confiance dans les observations

**R = np.var( prix ) * measurement_noise_factor / vol_factor**

- augmentation de measurement_noise_factor moins de confiance dans les prix plus de lissage
- diminution de measurement_noise_factor plus de confiance filtre plus nerveux

#### Paramètres de bruit du filtre de Kalman :

** process_noise_factor (Q scaling) :**

Contrôle la réactivité du filtre aux changements de tendance

- 0.001 - 0.005 : Très lisse, pour tendances long terme
- 0.01 : Valeur par défaut équilibrée
- 0.02 - 0.05 : Réactif, pour day trading
- 0.1 : Très réactif, risque de sur-ajustement

**measurement_noise_factor (R scaling) :**

Contrôle la confiance accordée aux observations (prix)

- 0.01 - 0.02 : Forte confiance aux prix
- 0.05 : Valeur par défaut équilibrée
- 0.1 - 0.2 : Faible confiance, plus de lissage

#### Recommandations Pratiques

Pour trader **intraday** échelle de temps < 30m

- Q plus élevé : process_noise_factor = 0.05
- R plus faible : measurement_noise_factor = 0.02
- Lookback court : 20-30

Pour **swing trading** (daily)

- Q modéré : process_noise_factor = 0.01
- R modéré : measurement_noise_factor  = 0.05
- Lookback moyen : 40-60

Pour **investissement** (weekly+)

- Q faible : process_noise_factor = 0.005
- R élevé : measurement_noise_factor = 0.1
- Lookback long : 80-100

### Paramétrage de la volatilité

La fenêtre de volatilité est un paramètre de régularisation temporelle, ce paramètre est crucial et souvent sous-estimé :

Calcule de l'écart-type glissant des rendements logarithmiques sur N périodes.

```Python
# Calcul volatilité

log_returns = np.diff( np.log( np.maximum( prix, 1e-10 ) ) )
returns_series = pd.Series( log_returns )
volatility_series = returns_series.rolling(
    window=self.volatility_window,
    min_periods=1
).std()

volatility = volatility_series.bfill().values
volatility = np.concatenate([[volatility[0]], volatility])
```

Paramétrage de **volatility_window**

- Court = Réactif mais bruyant
- Long = Stable mais lent

Dans le cas d'un interval_dates = '30m'

- Une journée de trading = ~13 périodes de 30min (9h30-17h)
- Une semaine = ~65 périodes

**volatility_window** recommandé:

- Scalping (1-5min) : 10-20 périodes (10-100 min)
- Intraday (30min) : 15-25 périodes (7h-12h)
- Swing (1h-4h) : 30-50 périodes (1-2 jours)
- Position (daily) : 20-30 jours

Relation entre les paramètres volatility_window et look_back et l'interval de temps :

**volatility_window** à peu près égal à  **look_back** / 2

look_back à peu près égal à 2 * (durée moyenne d'un trade / intervalle)

Exemple pour un interval de 30min et un trade de 2-3 jours :

**lookback** = 2.5 jours * 13 périodes/jour = 32-40 périodes

**volatility_window** = 40 / 2 = 20 périodes

## Interface du filtre de Kalman

Stratégie automatique de trading grâce au filtre de Kalman, implémenté dans la plateforme.

En implémentant cette stratégie dans la plateforme, j'obtiens les graphes suivants :

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/kalman-filter/interface.png" class="glightbox" data-gallery="galerie" title="Calcul de la tendance par le filtre de Kalman">
        <img src="{{ base_url }}/images/strategies/kalman-filter/interface.png"/>
    </a>
    <figcaption><em>Calcul de la tendance par le filtre de Kalman</em></figcaption>
</figure>

Notez l'interface de Configuration qui vous permet de configurer les paramètres évoqués plus haut.

Avec les calculs complémentaires affichés dans la console :

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/kalman-filter/console.png" class="glightbox" data-gallery="galerie" title="Statistiques calculées par le filtre de Kalman">
        <img src="{{ base_url }}/images/strategies/kalman-filter/console.png"/>
    </a>
    <figcaption><em>Statistiques calculées par le filtre de Kalman</em></figcaption>
</figure>

## Interprétation des graphes

### Signaux d'achat et de vente

Ils ont calculés à l'aide de :

- la velocity et la tendance calculée par le Filtre de Kalman,
- de l'accélération filtrée acceleration_smooth,
- la position relative : composante cyclique
- et l'incertitude normalisée

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/kalman-filter/signaux-achat-vente.png" class="glightbox" data-gallery="galerie" title="Statistiques calculées par le filtre de Kalman">
        <img src="{{ base_url }}/images/strategies/kalman-filter/signaux-achat-vente.png"/>
    </a>
    <figcaption><em>Filtre de Kalman - signaux d'achat et de vente</em></figcaption>
</figure>

La vélocité calculée par le Filtre de Kalman varie beaucoup en fonction du signal (du cours) aussi on affiche dans la console des statistiques sur cette vélocité pour permettre le réglage du seuil de détection des signaux d'achat/vente.

On implémentera deux façons de régler le seuil de vélocité qui indique un signal d'achat/vente soit manuel 0.03 soit adaptatif.

### Composante Cyclique et RSI

L'incertitude de Kalman converge très vite vers une valeur et faire graphe avec, ce n'est pas très utile. Vous retrouverez, dans l'implémentation au sein de la plateforme sans doute le RSI (momentum) du Cycle.

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/kalman-filter/incertitude-kalman.png" class="glightbox" data-gallery="galerie" title="Statistiques calculées par le filtre de Kalman">
        <img src="{{ base_url }}/images/strategies/kalman-filter/incertitude-kalman.png"/>
    </a>
    <figcaption><em>Filtre de Kalman - signaux d'achat et de vente</em></figcaption>
</figure>

#### Composante cyclique

Elle représente les fluctuations à court-moyen terme de la série temporelle, une fois la tendance retirée.

Elle capture :

- Les cycles économiques ou saisonniers
- Les variations autour de la tendance de long terme
- Les écarts temporaires par rapport à la trajectoire principale

Des valeurs positives du signal indiquent que la série est au-dessus de sa tendance, des valeurs négatives qu'elle est en-dessous.

**L'incertitude de Kalman (bandes de confiance)**

Les bandes autour de la composante cyclique représentent l'incertitude de l'estimation. Elles sont généralement tracées à ±2 écarts-types et indiquent :

Largeur des bandes :

- Des bandes étroites = estimation précise, le filtre est confiant
- Des bandes larges = estimation incertaine, plus de volatilité dans les données

Évolution temporelle :

Les bandes se resserrent généralement au fil du temps à mesure que le filtre accumule des observations et "apprend".

Un élargissement soudain peut signaler un changement de régime ou un choc structurel.

#### Interprétation pratique

Identification des cycles : Repérez les oscillations régulières pour détecter des patterns récurrents

Détection d'anomalies : Si la composante cyclique sort des bandes d'incertitude, cela suggère un événement inhabituel

Qualité du modèle : Des bandes très larges peuvent indiquer que le modèle a du mal à capturer la dynamique des données

Prévision : L'incertitude croissante dans le futur reflète la dégradation naturelle de la précision des prévisions

Cette analyse est particulièrement utile pour décomposer une série en ses éléments structurels (tendance + cycle) tout en quantifiant l'incertitude associée.

### Vélocité et Accélération de la Tendance

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/kalman-filter/velocite-acceleration-tendance.png" class="glightbox" data-gallery="galerie" title="Statistiques calculées par le filtre de Kalman">
        <img src="{{ base_url }}/images/strategies/kalman-filter/velocite-acceleration-tendance.png"/>
    </a>
    <figcaption><em>Vélocité et Accélération de la Tendance</em></figcaption>
</figure>

Informations cruciales sur la dynamique de la tendance d'une série temporelle. Voici comment l'interpréter :

#### Vélocité (Vitesse) de la Tendance

La vélocité représente le taux de changement de la tendance, c'est-à-dire sa pente ou sa dérivée première :

- Vélocité positive : la tendance est croissante (hausse)
- Vélocité négative : la tendance est décroissante (baisse)
- Magnitude de la vélocité : indique l'intensité du mouvement (rapide vs lent)
- Vélocité proche de zéro : la tendance est stable, en plateau

#### Accélération de la Tendance

L'accélération mesure le changement de la vélocité, donc la dérivée seconde :

Accélération positive : la tendance s'accélère (momentum croissant)

- Si vélocité > 0 : la hausse s'intensifie
- Si vélocité < 0 : la baisse ralentit (possibilité de retournement)

Accélération négative : la tendance décélère (momentum décroissant)

- Si vélocité > 0 : la hausse ralentit
- Si vélocité < 0 : la baisse s'intensifie

Accélération nulle : la vélocité est constante (mouvement uniforme)

#### Interprétations Pratiques

Points de retournement :

- Quand la vélocité traverse zéro : changement de direction de la tendance
- Quand l'accélération traverse zéro : point d'inflexion, changement de momentum

Signaux combinés :

- Vélocité et accélération positives : tendance haussière forte et croissante
- Vélocité positive, accélération négative : tendance haussière mais qui s'essouffle
- Vélocité et accélération négatives : tendance baissière forte et croissante
- Vélocité négative, accélération positive : tendance baissière qui s'affaiblit (potentiel rebond)

Applications :

- Trading : anticiper les retournements de tendance
- Prévision : évaluer la dynamique future
- Détection d'anomalies : identifier les changements brusques de comportement

Ce type d'analyse permet d'aller au-delà de la simple observation de la tendance en capturant sa dynamique interne, offrant ainsi des signaux plus précoces sur les évolutions futures.

### Volatilité du marché et Confiance des Signaux

<figure style="text-align: center;">
    <a href="{{ base_url }}/images/strategies/kalman-filter/velocite-confiance.png" class="glightbox" data-gallery="galerie" title="Statistiques calculées par le filtre de Kalman">
        <img src="{{ base_url }}/images/strategies/kalman-filter/velocite-confiance.png"/>
    </a>
    <figcaption><em>Vélocité et Accélération de la Tendance</em></figcaption>
</figure>

#### Volatilité du marché

Représente l'incertitude ou la variance des observations du prix

Calculée souvent via l'écart-type mobile ou la variance des innovations du filtre :

- Pics de volatilité = périodes turbulentes, changements brusques, incertitude élevée
- Faible volatilité = marché calme, tendance stable

#### Confiance des signaux

Dérivée de la variance de l'estimation (P dans l'équation du filtre de Kalman), représente la fiabilité de l'estimation de la tendance.

- Confiance élevée = le filtre est sûr de son estimation, signaux fiables
- Confiance faible = incertitude sur la tendance réelle, prudence nécessaire

Relations clés à observer, relation inverse typique :

- Volatilité augmente implique que la Confiance diminue
- Volatilité diminue implique que la Confiance augmente

Parce que quand le marché est volatil, le filtre devient moins certain de ce qu'est la vraie tendance sous-jacente.

#### Utilisation pratique

Filtrage des signaux : N'agir que lorsque la confiance dépasse un seuil (ex: >70%)

Ajustement du risque : Réduire la taille de position quand volatilité ↑ et confiance ↓

Détection de régimes : Les changements de volatilité peuvent signaler des transitions de marché

Validation croisée : Combiner avec d'autres indicateurs lors de périodes de faible confiance

Ce graphe est essentiellement un indicateur de qualité qui vous aide à distinguer les signaux fiables des signaux bruités dans votre stratégie de trading basée sur le filtre de Kalman.

## Code Source

Retrouvez les codes source de ces travaux sur le Filtre de Kalman comme indicateur technique boursier pour la stratégie automatique trading Kalman sur le GitHub de la plateforme TradingInPython :

- [SoDevLog PyTrading TradingInPython - kalman_filter_forcast.py](https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/strategies/kalman_filter_forcast.py)

Retrouvez les algorithmes en python de la plateforme téléchargez et installez le logiciel.

## Conclusion

Nous avons là, un véritable système de trading complet avec des notions que nous connaissons déjà bien comme la tendance, le momentum et les retournements.

Cette stratégie automatique affiche ses performances pour vous permettre d'ajuster les paramètres du Filtre de Kalman pour une plus grande efficacité.

Ce système de traing peut être utiliser quelque soit le style de trading intraday, swing ou investissements long terme.

Il doit bien sûr être utilisé avec des indicateurs techniques complémentaires pour venir corroborer les informations données par le filtre de Kalman.

A l'utilisation nous verrons par exemple que les signaux d'achats et de vente sont plutôt fantaisistes et à ne pas prendre au pied de la lettre. Le filtre de Kalman est surtout un détecteur de tendance.

Venez faire vos analyses techniques avec la plateforme de trading technique TradingInPython :

- [Plateforme de Trading Technique - Téléchargez](https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html)

Cet article vous a plu n'hésitez pas à commenter à partager ...
