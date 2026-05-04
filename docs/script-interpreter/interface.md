Grâce au langage de programmation {{"Python"|g_tooltip}} la plateforme permet d'exécuter vos scripts (les scripts que vous écrivez ou que vous prenez comme exemple) sans [installation](../index.md#telechargez-le-logiciel-gratuitement) supplémentaire que la plateforme <a href="https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html" target="_blank">TradingInPython</a>.

## Interface d'exécution des scripts utilisateurs

L'interpréteur de script python est accessible dans le Menu {{"Monitoring"|keyword}} -> {{"Scripts"|keyword}}

Deux parties :

- {{"Stocks"|keywordi}} pour les paramètres la listes des actions
- {{"Script Python"|keywordi}} pour votre script en python

<figure style="text-align: center;">
  <a href="/images/script-interpreter/interface.png" class="glightbox" data-gallery="galerie" title="Interface d'exécution des scripts Python">
    <img src="/images/script-interpreter/interface.png" alt="Script runner"/>
  </a>
  <figcaption><em>Interface d'exécution des scripts Python</em></figcaption>
</figure>

- Le bouton {{"Ouvrir"|keywordi}} de la partie {{"Stocks"|keywordi}} vous permet d'aller chercher une liste d'actions.
- Le bouton {{"Ouvrir"|keywordi}} de la partie {{"Script Python"|keywordi}} vous permet d'aller chercher un script à exécuter.

Vous retrouvez ces scripts [installés](../index.md#telechargez-le-logiciel-gratuitement) sur votre machine à l'endroit suivant sur votre disque dur :

- **C:\Users\{UserName}\AppData\Local\TradingInPython\user_scripts**

Pour exécuter le script :

- Le bouton {{"Exécuter"|keywordi}} lance l'exécution du script.

## Résultat de l'exécution du script

Le résultat de l'exécution du script se passe dans la console comme vous pouvez le voir ici avec l'exécution du script {{"greenblatt-000.py"|keyword}} :

<figure style="text-align: center;">
  <a href="/images/script-interpreter/execution-greenblatt.png" class="glightbox" data-gallery="galerie" title="Exécution du script de la formule de Greenblatt">
    <img src="/images/script-interpreter/execution-greenblatt.png" alt="Script runner"/>
  </a>
  <figcaption><em>Exécution du script de la formule de Greenblatt</em></figcaption>
</figure>

Vous pouvez voir dans la console la formule de Greenblatt exécutée pour certaines sociétées des GAFAM et Gartner, Inc. sort avec le meilleur score de 2.0, c'est donc l'action à plus fort potentiel en ce moment selon Greenblatt.

## API scripts

Une api est fournie pour permettre à vos scripts d'utiliser les données de la plateforme, ainsi lorsque vous créez un screener (une liste d'actions que vous sélectionnez) cette liste peut être utilisée par votre script.

Voici un script qui vous montre comment utiliser l'API :

- <a href="https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/user_scripts/use_api.py" target="_blank">user_scripts/use_api.py</a>

Si j'exécute ce script comme montré si dessous :

<figure style="text-align: center;">
  <a href="/images/script-interpreter/api-user-scripts.png" class="glightbox" data-gallery="galerie" title="Exécution du script de la formule de Greenblatt">
    <img src="/images/script-interpreter/api-user-scripts.png" alt="Script runner"/>
  </a>
  <figcaption><em>Exécution du script de la formule de Greenblatt</em></figcaption>
</figure>

J'ai cliqué sur {{"Ouvrir"|keywordi}} de la partie {{"Script Python"|keywordi}} pour aller cherche le script {{"use_api.py"|keyword}}. Puis j'ai cliqué sur le bouton {{"Exécuter"|keywordi}} pour exécuter ce script.

Vous voyez dans la Console s'afficher les paramètres transmis au script {{"use_api.py"|keyword}}, il ne vous suffit plus que de copier/coller ce script pour écrire le votre.

## Règles d'écriture des scripts

Et le plus important sans doute, vous pouvez écrire vos propres scripts en python.

Il faut que les librairies standards qu'utilise votre script soient les même que celles qu'utilise la plateforme.

Si vous écrivez des scripts un peu complexes avec des fonctions, vous devez simplement avoir une fonction {{"main"|keyword}} de la façon suivante :

```python

def main():
    print('Hello world!')

if __name__ == "__main__":
    main()
```

## Exemples de scripts à exécuter

Vous trouverez d'autres scripts à exécuter dans le GitHub de la solution à l'endroit suivant :

- [SoDevLog/PyTrading/tree/main/TradingInPython/_internal/user_scripts](https://github.com/SoDevLog/PyTrading/tree/main/TradingInPython/_internal/user_scripts)

Pour télécharger un de ces scripts, vous cliquez dessus puis dans les {{"..."|keywordi}}, cliquez sur Download (télécharger).

## Conclusion

Si vous l'utilisez de façon intensive, vous pourrez voir que vous avez accès au code de TradingInPython, certains script font appel à des modules interne de la plateforme. C'est donc une porte ouverte au code déjà écris pour la plateforme et que vous pouvez utiliser.

Dans un futur proche nous allons utiliser les indicateurs de la plateforme pour créer des filtres screener puissants afin de trouver des actions à trader.
