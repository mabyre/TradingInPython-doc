Lorsque vous venez d'installer la plateforme <a href="https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html" target="_blank">TradingInPython</a>, elle est livrée avec une liste d'actions à trader mais vous aurez envie de modifier cette liste.

Si vous avez déjà le {{"Nom"|keywordi}} et le {{"Symbole"|keywordi}} de l'action que vous souhaitez analyser techniquement vous pouvez l'[ajouter](#ajouter).

## Importer des actions

L'import d'actions (de titres, ETF, etc) peut se faire à l'unité ou en masse par l'{{"Importateur de stocks"|keyword}} (ations) depuis des sources multiples comme : YahooFinance, le NASDAQ, le marché EURONEXT.

- Menu {{ "Stocks" | keywordi }} -> {{ "Impoter des stocks" | keywordi }}

<figure style="text-align: center;">
    <a href="/images/gestion-stocks/menu-stocks-importer.png" class="glightbox" data-gallery="galerie" title="Menu Stocks -> Importer des stocks">
        <img src="/images/gestion-stocks/menu-stocks-importer.png" alt="" />
    </a>
    <figcaption><em>Menu Stocks -> Importer des Stocks</em></figcaption>
</figure>

Vous ouvrez l'{{"Importateur de stocks"|keyword}} multi-sources :

<figure style="text-align: center;">
    <a href="/images/gestion-stocks/import-stocks.png" class="glightbox" data-gallery="galerie" title="Menu Stocks -> Importer des stocks">
        <img src="/images/gestion-stocks/import-stocks.png" alt="" />
    </a>
    <figcaption><em>Menu Stocks -> Importer des Stocks</em></figcaption>
</figure>

Et vous recherchez parmi des sources à importer une action à trader. Une action à trader, c'est un {{"nom"|keywordi}} et un {{"ticker"|keywordi}} d'identification du titre sur les marchés boursier.

## Importer plus simplement

Si vous avez déjà le {{"nom de l'action"|keyword}} et son {{"ticker"|keyword}}, vous pouvez importer plus simplement, directement dans la [gestion de la liste des actions](#gerer-la-liste-des-actions).

### Trouver une action à trader

L'importateur de stocks est ouvert sur tous les marchés, trouver une action peut-être fastidieu.

Commençons par la source {{ "Yahoo Finance" | keywordi }} le marché français. Il ne vous reste qu'à cliquer sur le bouton {{ "Charger" | keywordi }} pour charger la liste des permières actions du marché français.

<figure style="text-align: center;">
    <a href="/images/gestion-stocks/yahoo-france.png" class="glightbox" data-gallery="galerie" title="Importer des stocks de la source Yahoo">
        <img src="/images/gestion-stocks/yahoo-france.png" alt="" />
    </a>
    <figcaption><em>Importer des stocks de la source Yahoo</em></figcaption>
</figure>

En grisé vous avez des actions qui sont déjà importés dans {{"TradingInPtyhon"|keyword}}, vous allez pouvoir en importer beaucoup d'autres.

La recherche de tires à trader n'est pas aussi simple qu'il y parait. Au début de votre trading vous allez chercher des actions chez votre brooker pour trouver le {{"nom"|keywordi}} et le {{"ticker"|keywordi}} que vous pourrez importer on va dire "à l'unité" et puis viendra la temps ou vous aurez envie d'analyser techniquement des listes de plus en plus importantes de titres.

Mais il existe des centaines de milliers de produits financiers à trader et même si on arrivait à en faire la liste à un instant donné, il faudrait la mettre à jour en permance, cela est bien sûr impossible, nous devons trouver des sources qui se chargent de la mise à jour pour nous.

{{"YahooFinance"|keyword}} est une source qui vous limite au chargement de 250 titres par page et ceci pour limiter la bande passante.

Donc l'importateur de titre de {{"TradingInPython"|keyword}} s'adapte a cette source mais aussi à d'autres sources plus souple comme le NASDAQ avec plus de 10 000 titres à importer.

Et donc, on y va petit à petit.

Vous pouvez demandez à YahooFinance un premier classement :

- Capitalisation : pour trouver les actions de cac40 par exemple
- Volume moyen : trouver les actions à plus forte volatilité
- Symbole de A à Z : c'est le classement par ticker

### Afficher le secteur et l'industrie

Les champs 'Secteur' et 'Industrie' sont important pour le trader qui cherche des informations sur un marché par exemple celui des semi-conducteurs ou du health-care.

L'importateur de stocks vous donne cette information sur une seconde requête grâce au bouton : {{"Charger secteur/industrie"|keywordi}}

Ce bouton n'est actif que si vous avez déjà effectué un premier chargement de page.

Soit vous cliquez directement de dessus vous allez chercher les champs 'Secteur' et 'Industrie' de tous les stocks chargés.

!!! danger "Attention ça peut être long !"

    Et vous risquez de recevoir le message suivant :

    **ERROR: YFinance.Ticker: Too Many Requests. Rate limited. Try after a while.**

Mais si vous sélectionnez dans la liste un ensemble d'actions vous obtiendrez les deux champs qui nous manquent.

### Importer avec une Catégorie

Au moment de cliquer sur le bouton : {{"Importer la sélection"|keywordi}}

Vous pouvez importer avec une Catégorie d'action existant déjà dans TradingInPython.

### Conclusion sur l'importation de stocks

C'est une fonctionnalité qu'il faut manier avec précaution, il faut avoir déjà un peu l'habitude mais vous apprendrez vite à vous en servir.

!!! danger "Faites attention !"

    On a vite fait de faire des listes trop grandes.

C'est tout pour le moment, c'est une nouvelle fonctionnalité des versions > v1.9.2 qui sera très certainement améliorée et mieux décrite.

## Gérer la liste des actions

Maintenant vous pouvez ajouter des actions à trader sans utiliser l'Importateur de stocks.

Pour gérer la liste des {{ "actions" | g_tooltip }}, en ajouter, en modifier ou en supprimer, vous trouverez le Menu :

- Menu {{ "Stocks" | keywordi }} -> {{ "Gestion des stocks" | keywordi }}

<figure style="text-align: center;">
    <a href="/images/gestion-stocks/menu-stocks.png" class="glightbox" data-gallery="galerie" title="Menu Stocks -> Gestion des Stocks">
        <img src="/images/gestion-stocks/menu-stocks.png" alt="" />
    </a>
    <figcaption><em>Menu Stocks -> Gestion des Stocks</em></figcaption>
</figure>

Avec la Liste des Actions à trader :

<figure style="text-align: center;">
    <a href="/images/gestion-stocks/gestion-stocks.png" class="glightbox" data-gallery="galerie" title="Gestion des Stocks">
        <img src="/images/gestion-stocks/gestion-stocks.png" alt="" width="550"/>
    </a>
    <figcaption><em>Gestion des Stocks - Listes des Actions à analyser</em></figcaption>
</figure>

Sélectionnez une Action, choisissez une Stratégie, cliquez sur {{ "Graphique" | keywordi }} le graphique de l'action s'affiche.

Notez les trois boutons en bas de la fenêtre : {{ "Ajouter" | keywordi }}, {{ "Modifier" | keywordi }}, {{ "Supprimer" | keywordi }}.

### Ajouter

Il y a déjà des centaines d'actions référencées dans la plateforme mais peut être pas celle que vous souhaitez analyser.

Pour ajouter une action, vous devez vous enquérir du {{ "Nom" | keywordi }} et du {{ "Symbole" | keywordi }} de l'action que vous souhaitez analyser.

- Menu {{"Stocks"|keywordi}} -> {{ "Impoter des stocks"|keywordi}} -> Cliquez sur {{"Ajouter"|keywordi}} :

<figure style="text-align: center;">
    <a href="/images/gestion-stocks/gestion-stocks-add.png" class="glightbox" data-gallery="galerie" title="Gestion des Stocks - Ajouter">
        <img src="/images/gestion-stocks/gestion-stocks-add.png" alt="" />
    </a>
    <figcaption><em>Gestion des Stocks - Ajouter une Stock</em></figcaption>
</figure>

Le champ {{"Menu:"|keywordi}} c'est une catégorie que vous allez choisir pour l'action sur vous importez. Exemple vous écrivez dans ce champ {{"Action à surveiller"|keywordi}} vous allez retouver dans la liste toutes les actions qui vous avez catégorisé {{"Action à surveiller"|keywordi}}. C'est très souple, c'est vous qui choisissez.

Notez que le champ {{ "Menu:" | keywordi }} est avec {{ "autocomplétion" | keyword }}, cela veut dire que si vous tapez un <kbd>a</kbd>, vous avez la liste de tous les menu commençants par un <kbd>a</kbd> qui va apparaître.

Vous sélectionnez un Menu préexisant par les touches {{ "flêche haut" | keyword }}, {{ "flêche bas" | keyword }} puis {{ "entrer" | keyword }}.

???+ warning "Pour sélectionner un menu à l'autocomplétion"

    Les composants graphiques de Tkinter ne vous permettent pas de sélectionner le menu proposé par l'autocomplétion avec la souris, vous devez impérativement utiliser les flêches pour choisir un menu préselectionné.

### Modifier

Vous souhaitez par exemple modifier l'action AIR LIQUIDE, sélectionnez la dans la liste et cliquez sur {{"Modifier"|keywordi}} (ou double cliquez sur la ligne) pour ouvrir le formulaire :

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNDkHCmRqigm00DPprmdwrlGfb-cbAcxJcPont8GanbxBH8XpCSE-kqcylQzwtWGQ8VTRZB1h7Ab1C-TaBDF2wDfrH7fBFM3K3T36hb4zoeRr813YofFrjg3AX_1nGjgqSnqQ9xKBgJb195c_XLUzLle4RBqvIVO_dLqHNKxG1N0VhhKejrh_sXQBVmqKA/s259/2025-01-24_12h26_52.png" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="201" data-original-width="259" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNDkHCmRqigm00DPprmdwrlGfb-cbAcxJcPont8GanbxBH8XpCSE-kqcylQzwtWGQ8VTRZB1h7Ab1C-TaBDF2wDfrH7fBFM3K3T36hb4zoeRr813YofFrjg3AX_1nGjgqSnqQ9xKBgJb195c_XLUzLle4RBqvIVO_dLqHNKxG1N0VhhKejrh_sXQBVmqKA/s16000/2025-01-24_12h26_52.png" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Modification de AIR LIQUIDE</td></tr></tbody></table>

Si vous laissez {{ "Menu:" | keywordi }} vide, l'action AIR LIQUIDE se retrouvera dans la liste des actions {{ "Non classées" | keywordi }}, sinon remplissez ce champ avec {{ "A" | keyword }} pour retrouver l'action dans la liste des {{ "A" | keyword }}.

Vous pouvez également mettre par exemple : {{ "Mes nouvelles actions à analyser" | keyword }}, AIR LIQUIDE se retrouvera dans une nouvelle liste nommée : {{ "Mes nouvelles actions à analyser" | keyword }}.

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPfjeP-vAFsi2rp-YDnzEfc0AGSDqiB-rucOMJbQhrYZNm_A5ciT3l8edXR3ZKOl-98Miz0VmLW-osAHGQy_eS-OfMwAGeQ9lDTglfoTrVBLCP-kuIvyE57YRAXKmz2cWx0PVIiINqbZcbqFwUjFfb9J8Iymc1Ugq_ZSRFv6JkI4r4lD0qnISkYELLoUea/s466/2025-01-24_12h34_38.png" style="margin-left: auto; margin-right: auto;"><img alt="Liste crée &quot;Mes nouvelles actions à analyser&quot;" border="0" data-original-height="466" data-original-width="356" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPfjeP-vAFsi2rp-YDnzEfc0AGSDqiB-rucOMJbQhrYZNm_A5ciT3l8edXR3ZKOl-98Miz0VmLW-osAHGQy_eS-OfMwAGeQ9lDTglfoTrVBLCP-kuIvyE57YRAXKmz2cWx0PVIiINqbZcbqFwUjFfb9J8Iymc1Ugq_ZSRFv6JkI4r4lD0qnISkYELLoUea/s16000/2025-01-24_12h34_38.png" title="Liste crée &quot;Mes nouvelles actions à analyser&quot;" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Liste crée "Mes nouvelles actions à analyser"</td></tr></tbody></table>

Vous pouvez ainsi créer autant de listes dans le Menu en choisissant le libellé que vous souhaitez.

### Supprimer

Vous supprimer une action en la sélectionnant dans la liste et en cliquant sur le bouton {{"Supprimer"|keywordi}}.

Vous pouvez également supprimer une liste d'actions par {{"sélection multiple"|keyword}}, soit en maintenant la touche Maj. ou la touche Ctrl.

???+ warning "Sélection multiple dans une liste"

    Les composants graphiques Tkinter sont au départ livrés avec un minimum d'intéraction utilisateur. La sélection multiple se fait uniquement avec la touche Maj. ou la touche Ctrl.

### Filtrer

Vous ne savez plus où vous avez rangé l'action, il vous suffit de cliquer sur le menu :

- {{ "Stocks" | keywordi }} -> {{ "Gestion des stocks" | keywordi }}

et de vous servir de la partie {{ "Filter:" | keywordi }} qui filtre aussi bien par {{ "Nom" | keyword }} par {{ "Symbol" | keyword }} ou par {{ "Menu" | keyword }}.

<figure style="text-align: center;">
    <a href="/images/gestion-stocks/gestion-stocks-filter.png" class="glightbox" data-gallery="galerie" title="Gestion des Stocks - Filtrer">
        <img src="/images/gestion-stocks/gestion-stocks-filter.png" alt="" />
    </a>
    <figcaption><em>Gestion des Stocks - Filtrer</em></figcaption>
</figure>

Avec {{ "Aero" | keywordi }} je filtre tous les Stocks du domaine de Aerospace-defense.

## Tradez

Vous avez déjà sans doute remarqué qu'en sélectionnant une actions dans la liste, la fenêtre principale {{"Strategy Automation"|keywordi}} vous indique un message : {{"Choisissez une stratégie..."|keywordi}}.

Il vous suffit dans le menu {{"Stratégies"|keyword}} de choisir par exemple {{"Ichimoku Kynko Hyo"|keyword}} pour découvrir l'analyse technique de l'action que vous avez sélectionnée dans la liste.

<figure style="text-align: center;">
    <a href="/images/gestion-stocks/ichimoku.png" class="glightbox" data-gallery="galerie" title="Gestion des Stocks - Filtrer">
        <img src="/images/gestion-stocks/ichimoku.png" alt="" />
    </a>
    <figcaption><em>Gestion des Stocks - Filtrer</em></figcaption>
</figure>
