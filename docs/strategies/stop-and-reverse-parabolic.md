---
description: "Découvrez comment utiliser l'indicateur technique de trading Stop And Reverse Parabolic"
keywords: "indicateur, technique, sar, stop and reverse, parabolic"
---

Le Parabolic Stop And Reverse (Parabolic SAR) est un indicateur technique très populaire, développé par J. Welles Wilder et décrit dans son livre _"New Concepts in Technical Trading Systems"_ publié en 1978.

Cet indiateur de trading technique est conçu pour suivre la tendance et surtout pour déterminer des niveaux dynamiques de {{ "StopLoss" | g_tooltip }}. 

C'est donc un indicateur de tendance contrairement à beaucoup d'autres qui sont des indicateurs de momentum qui mesurent la force du mouvement sans donner la tendance.

L’objectif du Parabolic SAR est d’indiquer à la fois :

- La direction de la tendance en cours,
- Un niveau de stop progressif, qui se rapproche du prix au fur et à mesure que la tendance avance,
- Et un signal potentiel de retournement, lorsque les points “changent de côté” (Stop And Reverse).

## Interface graphique

Cet indicateur technique a été développé dans la plateforme pour être utilisé avec les Fractales de Bill Williams donc, c'est sur le même graphique :

Dans le Menu {{ "Stratégie" | keyword }} choisissez {{ "Fractales de Bill Williams + SAR" | keyword }} :

<figure style="text-align: center;">
  <a href="/images/strategies/stop-and-reverse/interface.png" class="glightbox" data-gallery="galerie" title="Interface graphique de l'indicateur Stop-And-Reverse-Parabolic">
    <img src="/images/strategies/stop-and-reverse/interface.png" alt="Stop-And-Reverse-Parabolic"/>
  </a>
  <figcaption><em>Interface graphique de l'indicateur Stop-And-Reverse-Parabolic</em></figcaption>
</figure>

## Configuration

Cet un indicateur technique qui nécessite des réglages fins en fonction de la volatilité du marché, aussi lorsque vous {{ "passez la souris sur les paramètres" | keyword }} de configuration vous verrez quelques indications concernant le réglage de ces paramètres :

<figure style="text-align: center;">
  <a href="/images/strategies/stop-and-reverse/configuration.png" class="glightbox" data-gallery="galerie" title="Configuration l'indicateur Stop-And-Reverse-Parabolic">
    <img src="/images/strategies/stop-and-reverse/configuration.png" alt="Stop-And-Reverse-Parabolic"/>
  </a>
  <figcaption><em>Configuration - l'indicateur Stop-And-Reverse-Parabolic</em></figcaption>
</figure>

- {{ "BASE STEP" | keyword }} : Détermine la vitesse minimale à laquelle le SAR se rapproche du prix
- {{ "MAX STEP" | keyword }} : Limite la vitesse maximale à laquelle le SAR peut s'accélérer
- {{ "VOLATILITY WINDOW" | keyword }} : Détermine comment la volatilité historique est calculée

## Interprétation

L'indicateur technique Stop And Reverse Parabolic comporte deux signaux formés de petits carrés {{ "rouge" | red }} pour le {{ "SAR bearich" | red }} (tendance baissière) et {{ "vert" | green }} pour le {{ "SAR bullish" | green }} (tendance haussière).

En tendance haussière ou baissière si le signal se rapproche du cours (prix) une inversion (reverse) de tendance peut se produire.

Si le signal du SAR reste éloigné du cours la tendance va se poursuivre.

## Réglage des paramètres du SAR dynamique

Importance des paramètres BASE STEP et MAX STEP :

- {{ "BASE STEP" | keyword }} (valeur de départ par défaut: 0.02)
    - Détermine la vitesse minimale à laquelle le SAR se rapproche du prix
    - Influence la sensibilité initiale de l'indicateur
    - Valeur plus faible = indicateur plus lent et moins de faux signaux
    - Valeur plus élevée = indicateur plus réactif mais risque accru de faux signaux

- {{ "MAX STEP" | keyword }} (valeur maximale par défaut: 0.2)
    - Limite la vitesse maximale à laquelle le SAR peut s'accélérer
    - Contrôle l'agressivité de l'indicateur dans des conditions de forte volatilité
    - Valeur plus faible = moins de réactivité aux mouvements importants
    - Valeur plus élevée = réaction plus rapide mais risque de sortie prématurée de positions

### Recommandations de réglage

- Pour les marchés peu volatils:
    - {{ "BASE STEP" | keyword }}: 0.01 - 0.02
    - {{ "MAX STEP" | keyword }}: 0.1 - 0.15
    - Effet: indicateur plus lent, filtrant mieux les bruits du marché

- Pour les marchés de volatilité moyenne:
    - {{ "BASE STEP" | keyword }}: 0.02 - 0.03
    - {{ "MAX STEP" | keyword }}: 0.15 - 0.2
    - Effet: équilibre entre réactivité et stabilité

- Pour les marchés très volatils:
    - {{ "BASE STEP" | keyword }}: 0.03 - 0.05
    - {{ "MAX STEP" | keyword }}: 0.2 - 0.25
    - Effet: indicateur plus réactif aux mouvements rapides du marché

- Pour le day trading/scalping:
    - {{ "BASE STEP" | keyword }}: 0.03 - 0.05
    - {{ "MAX STEP" | keyword }}: 0.25 - 0.3
    - Effet: signaux plus fréquents mais potentiellement moins fiables

Le paramètre {{ "VOLATILITY WINDOW" | keyword }} (par défaut: 20) est également important car il détermine comment la volatilité historique est calculée.

Valeurs à considérer :

- {{ "Court terme (5-10)" | keyword }} : plus réactif aux changements récents de volatilité
- {{ "Moyen terme (15-30)" | keyword }} : équilibre entre réactivité et stabilité
- {{ "Long terme (40+)" | keyword }} : plus stable, moins sensible aux changements temporaires

## Pourquoi ajuster ces paramètres

Adaptation aux différents instruments financiers :

- Chaque actif a sa propre signature de volatilité.

Adaptation aux timeframes :

- Timeframes courts (minutes, heures): paramètres plus réactifs
- Timeframes longs (jours, semaines): paramètres plus conservateurs

Personnalisation selon votre style de trading :

- Trading de tendance: paramètres plus conservateurs pour rester dans la tendance
- Trading de contre-tendance: paramètres plus réactifs pour capturer les inversions

Adaptation aux conditions de marché changeantes :

- La volatilité des marchés évolue avec le temps, rendant nécessaire l'ajustement périodique des paramètres.

Pour optimiser ces paramètres, vous pouvez :

- Faire des tests de backtesting sur différentes périodes historiques
- Observer comment l'indicateur se comporte dans différentes conditions de marché
- Ajuster progressivement les paramètres plutôt que de faire des changements radicaux
- Comparer les résultats avec d'autres indicateurs de tendance pour validation

L'avantage majeur du {{ "SAR avec facteur d'accélération dynamique" | keyword }} est justement qu'il s'adapte à la volatilité, réduisant ainsi le besoin d'ajustements manuels fréquents des paramètres.

## Importance du paramètre VOLATILITY WINDOW

Ce paramètre définit la période sur laquelle la volatilité est calculée (nombre de bougies/périodes utilisées). Il influence directement:

La sensibilité au changement de volatilité: Plus la fenêtre est courte, plus l'indicateur réagit rapidement aux changements de volatilité.

La stabilité des signaux: Plus la fenêtre est longue, plus la mesure de volatilité est stable (mais potentiellement moins réactive).

La qualité des signaux: Un réglage optimal filtre les faux signaux tout en captant les mouvements significatifs.

### Recommandations de réglage selon le contexte

#### Par timeframe

Timeframes courts (1min - 15min):

- {{ "VOLATILITY WINDOW" | keyword }}: 10-15
- Raison: Environnement plus bruyant nécessitant une réponse rapide aux changements

Timeframes intermédiaires (30min - 4h):

- {{ "VOLATILITY WINDOW" | keyword }}: 15-25
- Raison: Équilibre entre réactivité et stabilité

Timeframes longs (journalier et plus):

- {{ "VOLATILITY WINDOW" | keyword }}: 20-40
- Raison: Privilégie la stabilité et la capture des tendances de fond

#### Par type d'actif

Actions individuelles:

- {{ "VOLATILITY WINDOW" | keyword }}: 15-25
- Raison: Volatilité généralement plus élevée et spécifique à l'entreprise

Indices boursiers:

- {{ "VOLATILITY WINDOW" | keyword }}: 20-30
- Raison: Volatilité plus modérée, mouvements plus graduels

Forex (paires majeures):

- {{ "VOLATILITY WINDOW" | keyword }}: 20-30
- Raison: Volatilité généralement plus prévisible

Crypto-monnaies:

- {{ "VOLATILITY WINDOW" | keyword }}: 10-20
- Raison: Très haute volatilité nécessitant une adaptation plus rapide

#### Par style de trading

Scalping/Day Trading :

- {{ "VOLATILITY WINDOW" | keyword }}: 10-15
- Raison: Nécessite une réactivité maximale aux changements de volatilité

Swing Trading :

- {{ "VOLATILITY WINDOW" | keyword }}: 15-25
- Raison: Équilibre entre réactivité et stabilité

Position Trading :

- {{ "VOLATILITY WINDOW" | keyword }}: 25-40
- Raison: Filtrage optimal du bruit de marché pour les positions longue durée

### Méthodes d'optimisation du VOLATILITY WINDOW

Optimisation par backtesting :

- Testez différentes valeurs (par exemple, 10, 15, 20, 25, 30, 40)
- Analysez les métriques de performance (rendement, ratio de Sharpe, drawdown)
- Choisissez la valeur offrant le meilleur compromis performance/stabilité

Optimisation par corrélation à la volatilité réalisée :

- Comparez les résultats avec des mesures de volatilité comme l'ATR (Average True Range)
- Sélectionnez la valeur produisant une corrélation optimale avec la volatilité réalisée

Optimisation visuelle :

- Tracez le SAR avec différentes valeurs de {{ "VOLATILITY WINDOW" | keyword }}
- Observez visuellement quand l'indicateur génère trop de faux signaux (fenêtre trop courte) ou manque des inversions importantes (fenêtre trop longue)

Optimisation adaptative :

- Considérez une approche où le {{ "VOLATILITY WINDOW" | keyword }} lui-même s'adapte aux conditions du marché
- Par exemple, réduire la fenêtre lorsque la volatilité est élevée et l'augmenter lorsqu'elle est faible

### Conseils pratiques

Évitez le sur-ajustement (overfitting) :

- Testez sur différentes périodes de temps
- Vérifiez que la performance est robuste dans différentes conditions de marché

Considérez l'interaction avec les autres paramètres :

- Un {{ "VOLATILITY WINDOW" | keyword }} plus court peut nécessiter un base_step plus conservateur
- Un {{ "VOLATILITY WINDOW" | keyword }} plus long peut fonctionner avec un max_step plus élevé

Surveillance continue :

- Réévaluez périodiquement le réglage optimal, surtout après des changements significatifs de régime de marché

L'optimisation du {{ "VOLATILITY WINDOW" | keyword }} est souvent un compromis entre réactivité et stabilité. 

La valeur idéale dépend fortement du contexte spécifique de trading et peut nécessiter des ajustements selon l'évolution des conditions de marché.

## Algorithme en Python

Open Software, d'écouvrez les codes source de l'indicateur technique Stop and Reverse Parabolic :

- <a href="https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/digitsignalprocessing/indicators.py" target="_blank">Indicateur technique Stop And Reverse Parabolic</a>

Sous la dénomination : {{ "calculate_sar_with_dynamic_af" | keyword }}

## En définitive

Dans la pratique avec la plateforme logicielle TradingInPython, vous aurez des indications contextuelles qui vous donneront des valeurs pour ces trois paramètres.

Regardez l'interface de [Configuration](#configuration) vous avez un bouton {{ "Save" | keyword }} pour sauvegarder vos réglages pour l'action en cours.

## Vidéo YouTube

Vous avez raté quelque chose, vous pouvez retrouver le paramétrage de l'indicateur technique SAR parabolic et dynamique dans la vidéo :

<div align="center" class="md-video">
<iframe width="560" height="315" src="https://www.youtube.com/embed/rCy6f5hxRj4?si=cLvnvuIzeQpRAWeX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## Plateforme de trading technique

Abonnez-vous :

- <a href="https://www.trading-et-data-analyses.com/p/abonnement.html" target="_blank">Abonnez-vous à la pplateforme de trading TradingInPython</a>

