# Ichimoku & Deeplearning

La graphe Ichimoku et sa prédiction.

## 1. Interface

Dans le Menu **Stratégie** choisissez **Ichimoku-Kinko-Hyo** :

<figure style="text-align: center;">
  <a href="/images/strategies/ichimoku/ichimoku-kinko-hyo.png" title="Stratégie Ichimoku-Kinko-Hyo" target="_blank">
    <img src="/images/strategies/ichimoku/ichimoku-kinko-hyo.png" class="glightbox" data-gallery="galerie" width="6500"/>
  </a>
  <figcaption><em>Interface - Stratégie Ichimoku-Kinko-Hyo</em></figcaption>
</figure>

## 3. Configuration

Remarquez l'interface de configuration avec trois parties :

<figure style="text-align: center;">
  <a href="/images/strategies/ichimoku/config-ichimoku-kinko-hyo.png" title="Configuration de l'Ichimoku-Kinko-Hyo" target="_blank">
    <img src="/images/strategies/ichimoku/config-ichimoku-kinko-hyo.png" class="glightbox" data-gallery="galerie"/>
  </a>
  <figcaption><em>Configuration - Stratégie Ichimoku-Kinko-Hyo</em></figcaption>
</figure>

- (1) Longueur des moyennes mobiles de la Tenken, Kijun et Senkou
- (2) Configuration du nombre de jours prédiction
- (3) Choix prédéfinis des longueurs pour les signaux Tenken, Kijun et Senkou

## 3. Prédiction keras et tensorflow

### 3.1. Calculer la Prédiction

<figure style="text-align: center;">
  <a href="/images/strategies/ichimoku/ichimoky-prediction.png" title="Ichimoku-Kinko-Hyo signal prédiction" target="_blank">
    <img src="/images/strategies/ichimoku/ichimoky-prediction.png" class="glightbox" data-gallery="galerie"/>
  </a>
  <figcaption><em>Ichimoku-Kinko-Hyo Calculer la prédiction</em></figcaption>
</figure>

- (1) Cochez la case **Forcasting** pour afficher le signal de prédiction
- (2) Le signal de prédiction calculer par l'entrainement du réseau de neurones

### 3.2. Lire le signal de prédiction

<figure style="text-align: center;">
  <a href="/images/strategies/ichimoku/ichimoky-prediction-signal.png" title="Ichimoku-Kinko-Hyo prédiction" target="_blank">
    <img src="/images/strategies/ichimoku/ichimoky-prediction-signal.png" class="glightbox" data-gallery="galerie"/>
  </a>
  <figcaption><em>Ichimoku-Kinko-Hyo Lire le signal de prédiction</em></figcaption>
</figure>

- (1) - L'outil Zoom de Matplotlib
- (2) - Le signal de prédiction

Avec l'outil zoom je fais un zoom sur la fin du graphe, je peux lire le signal de prédiction qui possède trois états.

### 3.3. Trois états du signal

<figure style="text-align: center;">
  <a href="/images/strategies/ichimoku/ichimoku-signal-zoom.png" title="Ichimoku-Kinko-Hyo lecture du signal" target="_blank">
    <img src="/images/strategies/ichimoku/ichimoku-signal-zoom.png" class="glightbox" data-gallery="galerie"/>
  </a>
  <figcaption><em>Ichimoku-Kinko-Hyo Lire le signal de prédiction</em></figcaption>
</figure>

- (1) Vente
- (2) Neutre
- (3) Achat

Bien sûr avec Safran en ce moment ce signal est à l'achat.
