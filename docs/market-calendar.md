# Calendier des marché financiers

Voici une fonctionnalité dont nous avons l'utilité au sein de la plateforme pour ne pas avoir à chercher trop loin sur le Web.

## Le Marché est-il ouvert ou fermé ?

Si vous êtes pationné de trading, vous avez très certainement vécu cette situation.

Vous vous levez avec l'espoir de réussir un bon trade, vous avez repéré une stock que vous aimeriez trader, seulement voilà à **9:01** il ne se passe toujours rien !

Le marché semble figé car il est ... fermé et oui, on ne vous avait pas prévenu mais aujourd'hui pas Bourse pas de trade.

Pour éviter des déconvenues, le Calendrier des marchés est là pour vous donner cette information, le marché va t-il ouvrir ou bien est-ce un jour Off ? Quels sont les prochains jours où le marché est fermé.

<figure style="text-align: center;">
    <a href="/images/market-calendar.png" class="glightbox" data-gallery="galerie" title="Calendier des marchés financiers">
        <img src="/images/market-calendar.png" alt="Calendier des marchés financiers"/>
    </a>
    <figcaption><em>Calendier des marchés financiers</em></figcaption>
</figure>

La dernière case de couleur est soit verte, le marché est ouvert soit rouge si le marché est fermé.

Il y a quelques marchés disponibles :

- Paris (CAC40)
- New York (NYSE)
- Nasdaq
- Londres
- Francfort
- Tokyo (Nikkei 225)
- Hong Kong (Hang Seng)
- Shanghai (SSE Composite) **Chine continentale**
- Shenzhen (SZSE Composite) **Chine continentale**
- Seoul (KOSPI) **Corée du Sud**
- Mumbai (SENSEX) **Inde**
- Singapore (STI) **Singapour**
- Sydney (ASX 200) **Australie (Asie-Pacifique)**

## Calendrier des dividendes

Vous constituez des listes d'actions dont vous souhaitez surveiller les dividendes et le Calendrier vous donne les dates d'exclusion, c'est à dire la date avant laquelle vous devez détenir l'action si vous souhaitez toucher un dividende.

La liste des Stocks à scanner s'affiche à l'ouverture du Calendier, quand vous cliquez sur le bouton {{"Scanner"|keywordi}} le scan démarre pour aller cherche les data :

<figure style="text-align: center;">
    <a href="/images/market-calendar-scan.png" class="glightbox" data-gallery="galerie" title="Calendier des marchés financiers - Scan des dividendes">
        <img src="/images/market-calendar-scan.png" alt="Calendier des marchés financiers - Scan des dividendes"/>
    </a>
    <figcaption><em>Calendier des marchés financiers - Scan des dividendes</em></figcaption>
</figure>

## Le fichier de scanning : calendar-dividendes.json

C'est la liste des actions à scanner qui s'affiche dans la partie {{"Stocks :"|keywordi}}.

Ce fichier se trouve dans le répertoire suivant :

- **C:\Users\\{Nom d'utilisateur}\AppData\Local\TradingInPython\screeners\calendar-dividendes.json**

C'est lui que vous manipulez avec la fonction [Gestion des liste d'actions](./gestion-liste-actions.md).

Vous ouvrez ce fichier pour ajouter ou supprimer des actions à scanner pour obtenir les dividendes.

## Tickers

Le champ {{"Tickers"|keywordi}} vous permet de scanner également des tickers sans passer par la liste de 'calendar-dividendes.json' pour un scan rapide si vous en avez besoin.

## Fichiers de sauvegarde au format CSV

Deux boutons :

- {{"Export CSV"|keywordi}} : Pour sauver votre scan au format CSV.
- {{"Import CSV"|keywordi}} : Pour importer un scan au paravant effectué et sauvé.

Ansi si vous avez de très grandes listes d'actions à surveiller vous n'êtes pas obligé de réeffectuer le scan.

## Tableau des résultats

Le résultat du scan affiche les dividendes des actions de la liste dans le tableau.

- {{"Exclu div"|keywordi}} : date d'exclusion des divendes, si vous achetez à cette date c'est trop tard pour toucher un dividende.
- {{"Dans"|keywordi}} : affiche le nombre de jours avant le versement.
- {{"Paiement"|keywordi}} : date à laquelle le divende à été versé.
- {{"Rdt moy 5a"|keywordi}} : en pourcentage sur 5 ans la part du dividende.

En cliquant sur une des lignes du tableau, le calendrier se positionne sur la date.
