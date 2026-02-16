---
description: "Grâce au langage python la plateforme est un logiciel ouvert, vous pouvez y intégrer vos propres scripts"
keywords: "open software, python, trading, technique"
---

# Open Software - Logiciel Ouvert & Extensions

La plateforme de Trading Technique {{ "TradingInPyhon" | keyword }} est un {{ "système ouvert" | keyword }}, vous avez accès aux codes source des indicateurs utilisés dans la plateforme ainsi vous pouvez vous rendre compte du moteur qui la fait fonctionner et y faire éventuellement des modifications.

Et pourquoi pas, ne pas coder vous même, vos propres indicateurs techniques.

<figure style="text-align: center;">
  <a href="https://github.com/SoDevLog/PyTrading/tree/main/TradingInPython/_internal/digitsignalprocessing" target="_blank" title="GitHub - Digital signal processing">
    <img src="/images/git-hub.png" alt="Capture d'écran" class="noborder" width="450" />
  </a>
  <figcaption><em>GitHub - Digital signal processing</em></figcaption>
</figure>

## Digital Signal Processing

Ouvrez le capot et découvrez les algorithmes de traitement du signal en {{ "Python" | g_tooltip }} utilisés par la plateforme :

- <a href="https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/digitsignalprocessing/" target="_blank">TradingInPython/DigitSignalProcessing/</a>

Plongez directement au cœur de la plateforme, si vous le souhaitez vous pouvez jeter un œil sur les codes sources des indicateurs utilisés dans la plateforme {{ "TradingInPython" | keyword }} :

- <a href="https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/digitsignalprocessing/indicators.py" target="_blank">TradingInPython/DigitSignalProcessing/indicators.py</a>

## Kit de développement TradingInPython

Vous souhaitez acquérir la totalité des codes sources de la plateforme {{ "TradingInPython" | keyword }}, c'est possible :

- [Kit de Trading en Python](https://www.trading-et-data-analyses.com/p/trading-et-data-analyses-en-langage.html)

## Modifier les codes sources de TradingInPython

Le Python est un langage qui permet soit d'exécuter un script soit ce même script compilé.

Vous souhaitez modifier le code de la stratégie automatique des Moyennes Mobiles, c'est très simple :

<figure style="text-align: center;">
  <a href="/images/open-software/sources-python.png" target="_blank" title="Titre de l'image">
    <img src="/images/open-software/sources-python.png" alt="Capture d'écran" class="noborder"/>
  </a>
  <figcaption><em>TradingInPython - Open Software</em></figcaption>
</figure>

- {{ "(1)" | red }} : Rendez-vous dans le répertoire d'installation de votre logiciel TradingInPython
- {{ "(2)" | red }} : Vous avez les deux fichiers :

    > - {{ "strategy_sma12e.py" | keyword }} : le script en python
    > - {{ "strategy_sma12e.cp39-win_amd64.pyd" | keyword }} : le même script compilé en Cython

Vous modifiez {{ "strategy_sma12e.py" | keyword }}, vous supprimez {{ "strategy_sma12e.cp39-win_amd64.pyd" | keyword }} et c'est votre script qui sera exécuté à la place.

!!! danger "DANGER"

    Avant de faire cela, il est conseillé de faire une sauvegarde complète de votre installation.

    Vous pouvez également faire un **Clône du GitHub** du répertoire : [PyTrading](https://github.com/SoDevLog/PyTrading)

## Développez votre stratégie de trading technique

Vous souhaitez profiter de l'éco-système {{ "TradingInPython" | keyword }} pour développer votre propre stratégie de trading technique, n'hésitez pas contactez nous :

- <a href="https://www.trading-et-data-analyses.com/p/formulaire-de-contact.html" target="_blank">Contactez le support de la plateforme</a>
