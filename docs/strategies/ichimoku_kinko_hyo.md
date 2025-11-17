# Ichimoku Kinko Hyo & Deeplearning

L'indicateur technique Ichimoku Kinko Hyo est une stratégie à lui tout seul. C'est une analyse technique extrêment graphique qui permet en un coup d'oeil de détecter les grandes tendances du cours de l'action.

Voici le graphe de l'indicateur technique **Ichimoku-Kinko-Hyo** et sa prédiction **Keras**.

## Interface

Dans le Menu **Stratégie** choisissez **Ichimoku-Kinko-Hyo** :

<figure style="text-align: center;" title="Interface de l'Ichimoku-Kinko-Hyo">
  <a href="{{ base_url }}/images/strategies/ichimoku/ichimoku-kinko-hyo.png" class="glightbox" data-gallery="galerie">
    <img src="{{ base_url }}/images/strategies/ichimoku/ichimoku-kinko-hyo.png" width="6500"/>
  </a>
  <figcaption><em>Interface - Stratégie Ichimoku-Kinko-Hyo</em></figcaption>
</figure>

## Configuration

Remarquez l'interface de configuration avec trois parties :

<figure style="text-align: center;" title="Configuration de l'Ichimoku-Kinko-Hyo">
  <a href="{{ base_url }}/images/strategies/ichimoku/config-ichimoku-kinko-hyo.png" class="glightbox" data-gallery="galerie">
    <img src="{{ base_url }}/images/strategies/ichimoku/config-ichimoku-kinko-hyo.png"/>
  </a>
  <figcaption><em>Configuration - Stratégie Ichimoku-Kinko-Hyo</em></figcaption>
</figure>

- **(1)** Longueur des moyennes mobiles de la Tenken, Kijun et Senkou
- **(2)** Configuration du nombre de jours prédiction
- **(3)** Choix prédéfinis des longueurs pour les signaux Tenken, Kijun et Senkou

## Prédiction keras et tensorflow

### Calculer la Prédiction

<figure style="text-align: center;"  title="Ichimoku-Kinko-Hyo signal prédiction">
  <a href="{{ base_url }}/images/strategies/ichimoku/ichimoky-prediction.png" class="glightbox" data-gallery="galerie">
    <img src="{{ base_url }}/images/strategies/ichimoku/ichimoky-prediction.png"/>
  </a>
  <figcaption><em>Ichimoku-Kinko-Hyo Calculer la prédiction</em></figcaption>
</figure>

- **(1)** Cochez la case **Forcasting** pour afficher le signal de prédiction
- **(2)** Le signal de prédiction calculer par l'entrainement du réseau de neurones

### Lire le signal de prédiction

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/ichimoku/ichimoky-prediction-signal.png" title="Ichimoku-Kinko-Hyo prédiction" target="_blank">
    <img src="{{ base_url }}/images/strategies/ichimoku/ichimoky-prediction-signal.png" class="glightbox" data-gallery="galerie"/>
  </a>
  <figcaption><em>Ichimoku-Kinko-Hyo Lire le signal de prédiction</em></figcaption>
</figure>

- **(1)** - L'outil Zoom de Matplotlib
- **(2)** - Le signal de prédiction

Avec l'outil zoom je fais un zoom sur la fin du graphe, je peux lire le signal de prédiction qui possède trois états.

### Les trois états du signal

<figure style="text-align: center;">
  <a href="{{ base_url }}/images/strategies/ichimoku/ichimoku-signal-zoom.png" title="Ichimoku-Kinko-Hyo lecture du signal" target="_blank">
    <img src="{{ base_url }}/images/strategies/ichimoku/ichimoku-signal-zoom.png" class="glightbox" data-gallery="galerie"/>
  </a>
  <figcaption><em>Ichimoku-Kinko-Hyo Lire le signal de prédiction</em></figcaption>
</figure>

- **(1)** Vente
- **(2)** Neutre
- **(3)** Achat

Bien sûr avec Safran en ce moment ce signal est à l'achat.

## Formation

- <a href="https://www.trading-et-data-analyses.com/2024/10/formation-ichimoku-kinko-hyo.html" target="_blank">Formation à l'Ichimoky Kinko Hyo</a>


## Algorithme

Découvrez l'implémentation {{ "Python" | g_tooltip }} de cet indicateur technique au sein de la plateforme :

- <a href="https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/digitsignalprocessing/ichimoku_kinko_hyo.py" target="_blank">GitHub - Digital Signal Processing - Ichimoku Kinko Hyo</a>
