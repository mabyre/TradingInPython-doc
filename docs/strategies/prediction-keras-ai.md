# Prédiction de trading avec Keras (LSTM & Deep Learning en Python)

Cette stratégie permet d’utiliser le deep learning (réseaux LSTM avec Keras et TensorFlow) pour prédire l’évolution des prix et générer des signaux de trading automatisés dans TradingInPython.

## Architecture de la stratégie IA

La stratégie repose sur un pipeline classique de machine learning appliqué aux séries temporelles :

Données de marché > Séquences temporelles > Modèle LSTM > Prédiction > Signal trading

## Exemple de programmation du modèle LSTM

```python
model = Sequential()
model.add(LSTM(50, return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
```

## Interface graphique

Cette stratégie est accéssible {{ "Menu" | keyword }} {{ "Stratégie" | keywordi }} -> {{ "Prédiction Keras" | keywordi }}

<figure style="text-align: center;">
    <a href="/images/strategies/prediction-keras/keras-tensorflow.png" class="glightbox" data-gallery="galerie" title="Prédiction avec Keras et TensorFlow">
        <img src="/images/strategies/prediction-keras/keras-tensorflow.png"/>
    </a>
    <figcaption><em>Prédiction avec Keras et TensorFlow</em></figcaption>
</figure>

- {{ "Days in past" | keyword }} : Entrainement du modèle x_train contient des séquences de DAYS_IN_PAST jours.
- {{ "Days in futur" | keyword }}  : Nombre de jours de prédiction
- {{ "EPOCHS" | keyword }}  : Un epoch signifie une itération complète à travers le jeu de données d'entraînement.
- {{ "LSMT UNITS" | keyword }}  : Types de couches dans le réseau de neurones.
- {{ "Drop Out" | keyword }}  : Empêche le surapprentissage en désactivant aléatoirement une fraction des unités.

## Résultat de la prédiction

Le modèle produit une estimation de la tendance future des prix.

Exemple de prédiction réalisée avec un modèle LSTM dans TradingInPython.

- La courbe de prix (candlesticks) représente le marché réel  
- La courbe bleue correspond à la prédiction du modèle  
- Les zones vertes et rouges illustrent les signaux exploités  

Dans cet exemple :

- {{ "Données passées" | keyword }} : 80 périodes  
- {{ "Horizon de prédiction" | keyword }} : 12 périodes  
- {{ "LSTM units" | keyword }} : 50  
- {{ "Dropout" | keyword }} : 0.2  

Le modèle suit la tendance globale du marché tout en filtrant une partie du bruit, ce qui permet de générer des signaux exploitables.

## Performance du modèle

Le modèle est évalué avec une fonction de perte de type {{ "Mean Squared Error (MSE)" | keyword }}.

Dans cet exemple :

- Score : 0.025  
- Bonne capacité à suivre la tendance  
- Sensibilité aux retournements rapides  

Ces résultats montrent que le modèle est pertinent pour une utilisation en complément d'autres indicateurs.

## Limites de l’intelligence artificielle en trading

- Overfitting sur les données historiques
- Marchés non stationnaires
- Bruit important dans les séries financières
- Difficulté à généraliser

Ces éléments doivent être pris en compte dans toute stratégie de trading basée sur le machine learning.

## Formation

Retrouvez les articles du blog sur la formation à Tensorflow :

- <a href="https://www.trading-et-data-analyses.com/search/label/TensorFlow" target="_blank">Trading et Data Analyses - Tensorflow</a>

## Vidéo YouTube

<div align="center" class="md-video">
<iframe width="560" height="315" src="https://www.youtube.com/embed/vyCHZOKIokg?si=xK4dVqW1k6323_Xv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## Abonnement

Pour utiliser pleinement cette stratégie au sein de la plateforme, il vous faut vous abonner :

- <a href="https://www.trading-et-data-analyses.com/p/abonnement.html" target="_blank">TradingInPython - Abonnement</a>

## Questions

Vous avez des questions n'hésitez pas, nous sommes là pour tout vous expliquer.

- [Support & FAQ](../support-faq.md)
