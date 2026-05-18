Il existait des scripts d'analyse financière donc d'analyse fondamentale, un accès à l'open data des sociétés côtés en bourse donné par Yahoo Finance mais pas seulement, on trouve le moyen d'obtenir des clefs d'API par exemple du côté de la FRED pour obtenir des données économiques que l'on peut par la suite exploiter dans un script python.

Voici des exemples de scripts python d'analyse financière que vous pouvez exécuter avec la plateforme :

- <a href="https://github.com/SoDevLog/PyTrading/tree/main/TradingInPython/Z-Integration/yfinance" target="_blank">TradingInPython/Z-Integration/yfinance</a>

Les scripts utilisateurs livrés avec l'installation de votre logiciel, sont également ici :

- <a href="https://github.com/SoDevLog/PyTrading/tree/main/TradingInPython/_internal/user_scripts" target="_blank">TradingInPython/_internal/user_scripts</a>

Version > 1.8.2

La plateforme permet maintenant d'exécuter ces scripts. L'utilisateur peut maintenant exécuter ces scripts sans [installation](../index.md#telechargez-le-logiciel-gratuitement) supplémentaire que la plateforme <a href="https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html" target="_blank">TradingInPython</a>.

## Comment utiliser les scripts d'analyse financière

Rendez-vous dans la partie [Comment utiliser l'interpréteur de scripts](interface.md) pour apprendre comment utiliser les scripts utilisateurs.

Vous retrouvez ces scripts [installés](../index.md#telechargez-le-logiciel-gratuitement) sur votre machine à l'endroit suivant sur votre disque dur :

- **C:\Users\\{UserName}\AppData\Local\TradingInPython\user_scripts**

## Résultat de l'exécution du script

Le résultat de l'exécution du script se passe dans la console comme vous pouvez le voir ici avec l'exécution du script {{"greenblatt-000.py"|keyword}} :

<figure style="text-align: center;">
  <a href="/images/script-interpreter/execution-greenblatt.png" class="glightbox" data-gallery="galerie" title="Exécution du script de la formule de Greenblatt">
    <img src="/images/script-interpreter/execution-greenblatt.png" alt="Script runner"/>
  </a>
  <figcaption><em>Exécution du script de la formule de Greenblatt</em></figcaption>
</figure>

Vous pouvez voir dans la console la formule de Greenblatt exécutée pour certaines sociétées des GAFAM et Gartner, Inc. sort avec le meilleur score de 2.0, c'est donc l'action à plus fort potentiel en ce moment selon Greenblatt.

Mais vos scripts peuvent aussi afficher des graphiques. Voici l'analyse de la santé économique de la France par un indice macro-éconmique proche de celui utilisé par l'ISM (Institute for Supply Management) :

<figure style="text-align: center;">
  <a href="/images/script-interpreter/indice-ism-macro-france.png" class="glightbox" data-gallery="galerie" title="Santé économique de la France">
    <img src="/images/script-interpreter/indice-ism-macro-france.png" alt="Santé économique de la France"/>
  </a>
  <figcaption><em>Santé économique de la France</em></figcaption>
</figure>

Vous pouvez afficher ce graph grâce au script Python : [indice-fred-france.py](https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/user_scripts/indice-fred-france.py)

## Votre clef d'API

Pour l'exécution de certains scripts qui vont chercher des données au près des grands sites open data, il faut aller vous enregistrer au près du fournisseur de data afin d'obtenir ce que l'on appel une clef d'API.

Une fois cette clef récupérée vous devez la copier à la place de {{ "YOUR_API_KEY_HERE" | keyword }} dans le script.

## Exemples de scripts à exécuter

Vous trouverez d'autres scripts à exécuter dans le GitHub de la solution à l'endroit suivant :

- [SoDevLog/PyTrading/tree/main/TradingInPython/_internal/user_scripts](https://github.com/SoDevLog/PyTrading/tree/main/TradingInPython/_internal/user_scripts)

Pour télécharger un de ces scripts, vous cliquez dessus puis dans les {{"..."|keywordi}}, cliquez sur Download (télécharger).

_That's All Folks!_

_Have fun!_
