---
title: "Découvrez comment backtester vos stratégies de trading technique"
description: "Le backtesting est une fonctionnalité importante pour la validation de vos stratégies de trading technique"
keywords: "backtesting, trading, technique"
---

Le backtesting est une étape essentielle en trading algorithmique. Il permet de tester une stratégie de trading sur des données historiques afin d’en évaluer la performance avant toute mise en production.

Le module de backtesting de TradingInPython propose une approche simple et open source pour simuler des stratégies en Python. Il permet d’analyser les résultats, de visualiser les signaux et d’itérer rapidement sur ses modèles.

Cette documentation présente le fonctionnement du backtesting dans TradingInPython, les options disponibles ainsi que des exemples d’utilisation concrets.

## Fonctionnalités principales

- Simulation de stratégies de trading sur les données historiques
- Visualisation des performances de vos trades
- Analyse des signaux d’achat et de vente en situation réelle
- Intégration avec les indicateurs techniques

## Interface de backtesting

<figure style="text-align: center;">
    <a href="/images/back-testing-interface.png" class="glightbox" data-gallery="galerie" title="Fonctionnalités de Back Testing">
        <img src="/images/back-testing-interface.png" alt="Fonctionnalités de Back Testing"/>
    </a>
    <figcaption><em>Fonctionnalités de Back Testing</em></figcaption>
</figure>

- {{ "(1)" | red }} : Period à none pour utiliser {{ "Date de fin" | keywordi }} et {{ "Date de début" | keywordi }}
- {{ "(2)" | red }} : Les dates seront utilisées
- {{ "(3)" | red }} : Boutons {{ "+ 1" | keywordi }} et {{ "- 1" | keywordi }}

Les boutons {{ "+ 1" | keywordi }} et {{ "- 1" | keywordi }} permettent d'ajouter ou de retirer 1 à la {{ "Date de fin" | keywordi }}, en tenant compte des jours ouvrés, c'est à dire que vous aurez toujours de nouvelles data même si les dates tombent dans les week-end ou les jours non tradés.

Le graphe est affiché et les indicateurs techniques sont recalculés avec les nouvelles valeurs.

Vous aurez ainsi la possibilité de voir dans une situation réelle particulière du passé qu'elle décision de trading vous auriez prise en fonction de votre stratégie de trading et des indicateurs techniques choisis.

## Les datas

Il est donc inutile de générer des données synthétiques de trading, vous pouvez backtester votre stratégie de trading sur tous les cours en choisissant de partir d'une date donnée de prendre vos décisions de trading en effectuant votre analyse technique en temps réel.

Ainsi, vous backtestez sur des données réelles en situation réelle.

## Moteur de backtesting

Vous l'aurez compris, il ne s'agit pas d'un véritable moteur de backtesting mais plutôt d'un mode replay bar-by-bar.

Mais si des besoins de la communauté des utilisateurs se font sentir au delà du mode replay, en langage Python ce sera rapide à développer.

## Pour aller plus loin

Pour aller plus loin, vous pouvez consulter la section sur les [indicateurs techniques](./indicators.md) et la [création de stratégies personnalisées](./open-software.md).
