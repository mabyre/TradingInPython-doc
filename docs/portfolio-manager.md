# Gestionnaire de Portefeuilles

Le gestionnaire de portefeuilles est l'outil indispensable du trader afin de centraliser les achats les ventes les gains les pertes, les coûts dans un tableau de bord de calcul du rendement réel de votre trading.

## Ouvrir le Gestionnaire de Portefeuilles

Ouvrir le gestionnaire de portefeuilles dans le **Menu Monitoring** -> **Portefeuilles**

<figure style="text-align: center;" title="Portfolio - Gestionnaire de Portefeuilles">
  <img src="{{ base_url }}/images/portfolio/menu.png" class="noborder"/>
  <figcaption><em>Portfolio - Gestionnaire de Portefeuilles</em></figcaption>
</figure>

Créer votre premier portefeuille :

<figure style="text-align: center;" title="Portfolio - Gestionnaire de Portefeuilles">
  <img src="{{ base_url }}/images/portfolio/creer.png" class="noborder"/>
  <figcaption><em>Créer votre premier portefeuille</em></figcaption>
</figure>

Si vous êtes positionné dans les Screeners remontez vers le répertoire **"_internal"** pour choisir le répertoire "portfolios" :

<figure style="text-align: center;" title="Portfolio - Gestionnaire de Portefeuilles">
  <img src="{{ base_url }}/images/portfolio/trouver.png" class="noborder"/>
  <figcaption><em>Trouvez le répertoire **portfolios**</em></figcaption>
</figure>

Sélectionnez ce répertoire, cliquez sur le bouton **"Enregistrer"** :

<figure style="text-align: center;" title="Portfolio - Gestionnaire de Portefeuilles">
  <img src="{{ base_url }}/images/portfolio/enregistrer.png" class="noborder"/>
  <figcaption><em>Enregistrez votre premier portefeuille</em></figcaption>
</figure>

La création de votre portefeuille est un succès :

<figure style="text-align: center;" title="Portfolio - Gestionnaire de Portefeuilles">
  <img src="{{ base_url }}/images/portfolio/creation-succes.png" class="noborder"/>
  <figcaption><em>Enregistrez votre premier portefeuille</em></figcaption>
</figure>

## Enregistrer une transaction

Remplissez une Nouvelle transaction

<figure style="text-align: center;" title="Portfolio - Gestionnaire de Portefeuilles">
  <img src="{{ base_url }}/images/portfolio/transaction.png" class="noborder"/>
  <figcaption><em>Enregistrez une transaction</em></figcaption>
</figure>

- (1) Type : cliquez Achat en vert et Vente en rouge selon que vous enregistrez un achat ou une vente
- (2) Ticker : exemple Air Liquide le ticker est AI.PA vous le trouvez à de nombreux endroit dans la plateforme
- (3) Quantité, Prix, Frais, ...

Cliquez sur Ajouter la transaction elle apparait dans **"Historique des transaction"**

N'oubliez pas les frais c'est très important pour connaitre la performance réelle de votre Portefeuille.

## Le tableau de bord

Le Gestionnaire de Portefeuilles, vous permet de consolider votre trading par la gestion rigoureuse de tous vos actes d'achats/ventes dans un Portefeuille qui centralise tous vos achats, vos ventes et calcule l'efficacité de vos trades.

Le Gestionnaire de Portefeuilles vous permet de gérer l'état exacte de vos trades :

Il consolide l'ensemble de vos achats et de vos ventes d'Actions, d'**ETF, Forex, Crytos, Futures, etc**. Il comptabilise tout ça dans un tableau de bord qui vous permet de savoir exactement où vous en êtes.

Sans lui vous êtes perdu.

Je consolide tous mes achats/ventes dans le Volet Transactions :

<figure style="text-align: center;" title="Portfolio - Gestionnaire de Portefeuilles">
  <img src="{{ base_url }}/images/portfolio/tableau-de-bord.png" class="noborder"/>
  <figcaption><em>Le tableau de bord</em></figcaption>
</figure>

Avec de grandes indications :

- Le Solde Net Investi : Total de vos achats - Total de vos ventes
- La Valeur actuelle : La quantité de vos positions en cours x pris courant
- P&L Réalisé : Profit et Pertes (Profit and Loss) réalisé sur les positions clôturées
- P&L Non Réaslié : Profit et Pertes non réalisé sur les positions en cours
- P&L Total : Profit et Pertes totales
- Rendement : Le rendement total de votre portefeuille en temps réel

Le Bouton **"Actualiser les prix"** va chercher les prix courants pour actualiser toutes les données de votre portefeuille TradingInPython.

Le Volet Positions calcule sur les transactions les potions en cours et les positions clôturées ainsi vous avez un bilan comptable réel de tous vos trades.

Le Volet Rapport reprends tous c'est éléments dans un rapports que vous pouvez enregistrer au format texte.

## Open Software

Vous avez besoin d'ouvrir le capot de la machine pas de problème retrouver le code Python du Gestionnaire de Portefeuille dans le GitHub de la solution TradingInPython :

[SoDevLog PyTrading/TradingInPython/portfolios/portfolio.py](https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/portfolios/portfolio.py)

[Ancienne documentation - Gestionnnaire de portefeuilles - Généralités](https://www.trading-et-data-analyses.com/p/gestionnaire-de-portefeuilles.html)

[Ancienne documentation - Gestionnnaire de portefeuilles - En action](https://www.trading-et-data-analyses.com/2025/10/portfolio-portefeuille-actions.html)

_Contenu à compléter._
