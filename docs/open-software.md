# Open Software - Logiciel Ouvert & Extensions

La plateforme TradingInPyhon est un **système ouvert**, vous avez accès aux codes source des indicateurs utilisés dans la plateforme ainsi vous pouvez vous rendre compte du moteur qui la fait fonctionner.

Et pourquoi pas, vous pouvez coder vos propres indicateurs techniques.

<figure style="text-align: center;">
  <a href="https://github.com/SoDevLog/PyTrading/tree/main/TradingInPython/_internal/digitsignalprocessing" target="_blank" title="GitHub - Digital signal processing">
    <img src="/images/git-hub.png" alt="Capture d'écran" class="noborder" width="450" />
  </a>
  <figcaption><em>Figure 1 – GitHub - Digital signal processing</em></figcaption>
</figure>

## Digital Signal Processing

Plongez directement au cœur de la plateforme, si vous le souhaitez vous pouvez jeter un œil sur les codes sources des indicateurs utilisés dans la plateforme **TradingInPython** :

- [PyTrading - TradingInPython - Digital Signal Processing - indicators.py](https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/digitsignalprocessing/indicators.py)

## Kit de développement TradingInPython

Vous souhaitez acquérir la totalité des codes sources de la plateforme **TradingInPython** :

- [Kit de Trading en Python](https://www.trading-et-data-analyses.com/p/trading-et-data-analyses-en-langage.html)

## Modifier les codes sources de TradingInPython

Le Python est un langage qui permet soit d'exécuter un script soit ce même script compilé.

Vous souhaitez modifier le code de la stratégie automatique des moyennes mobiles c'est très simple :

<figure style="text-align: center;">
  <a href="/images/open-software/sources-python.png" target="_blank" title="Titre de l'image">
    <img src="/images/open-software/sources-python.png" alt="Capture d'écran" class="noborder"/>
  </a>
  <figcaption><em>TradingInPython - Open Software</em></figcaption>
</figure>

- **(1)** Rendez-vous dans le répertoire d'installation de votre logiciel TradingInPython
- **(2)** Vous avez les deux fichiers :

    > - **strategy_sma12e.py** : le script en python
    > - **strategy_sma12e.cp39-win_amd64.pyd** : le même script compilé en Cython

Vous modifiez **strategy_sma12e.py**, vous supprimez **strategy_sma12e.cp39-win_amd64.pyd** et c'est votre script qui sera exécuté à la place.

**WARNING :** Avant de faire cela, il est conseillé de faire une sauvegarde complète de votre installation. Vous pouvez également faire un Clône du GitHub Répertoire : [PyTrading](https://github.com/SoDevLog/PyTrading)
