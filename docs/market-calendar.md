# Calendier des marché financiers

Voici encore une fonctionnalité dont j'ai l'utilité au sein de la palteforme pour ne pas avoir à chercher très loin sur le Web.

## Marché ouvert ou fermé

Si vous êtes pationné de trading, vous avez très certainement vécu cette situtation.

Vous vous levez avec l'espoir de réussir un coup, vous avez repéré une stock que vous aimeriez trader, seulement voilà à **9:01** il ne se passe toujours rien !

Le marché semble figé car il est ... fermé et oui on ne vous avait pas prévenu mais aujourd'hui pas Bourse.

Le Calendrier des marchés est là pour vous donner cette information, le marché va t-il ouvrir ou bien est-ce un jour Off ? Quels sont les prochains jours où le marché est fermé.

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

La liste des Stocks à scanner s'affiche, quand vous cliquez sur le bouton {{"Scanner"|keywordi}} le scan démarre pour aller cherche les data.

## Le fichier de scanning calendar-dividendes.json

Il se trouve dans le répertoire :

- **C:\Users\{Nom d'utilisateur}\AppData\Local\TradingInPython\screeners\calendar-dividendes.json**

C'est lui que vous manipulez avec la fonction [Gestion des liste d'actions](./gestion-liste-actions.md).

Vous ouvrez ce fichier pour ajouter ou supprimer des actions à scanner.

## Tickers

Le champ {{"Tickers"|keywordi}} vous permet de scanner des tickers sans passer par la liste de calendar-dividendes.json pour un scan rapde si vous en avez besoin.

## Fichiers de sauvegarde au format CSV

Deux boutons :

- {{"Export CSV"|keywordi}} : Pour sauver votre scan au format CSV.
- {{"Import CSV"|keywordi}} : Pour importer un scan au paravant effectué et sauvé.

Ansi si vous avez de très grandes listes d'actions à surveiller vous n'êtes pas obligé de réeffectuer le scan.

## Tableau des résultats

Le résultat du scanning affiche les dividendes des actions de la liste.
