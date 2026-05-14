# Création et gestion des screeners

Les screeners sont des fichiers au format JSon partagés par les [Cartes de chaleur](./heatmap-screener/heatmaps.md), le [Monitor Stock Market](./monitor-alerts/monitor-stock-market.md) et le Calendrier des dividendes.

La Gestion des screeners vous permet de créer, de modifier ou de supprimer ces fichiers.

Pour configurer un screener, il faut faire une sélection de stocks et la sauvegarder dans le fichier.

## Ouvrir la gestion des screeners

Menu {{ "Monitoring" | keywordi }} article {{ "Gestion des screeners" | keywordi }}.

<figure style="text-align: center;" title="Création des screeners">
  <img src="/images/heatmap-screener/menu-gestion-screeners.png" alt="" class="noborder"/>
  <figcaption><em>Menu Monitoring -> Gestion des screeners</em></figcaption>
</figure>

En cliquant sur le Menu {{ "Monitoring" | keywordi }} -> {{ "Gestion des scrreners" | keywordi }} vous ouvrez la fenêtre suivante :

<figure style="text-align: center;" title="Création des screeners">
  <img src="/images/heatmap-screener/selecteur-de-stocks.png" class="noborder" alt=""/>
  <figcaption><em>Création des screeners</em></figcaption>
</figure>

- {{ "(1)" | red }} : Le fichier de screener sélectionné ici aero-space-defense.json
- {{ "(2)" | red }} : Il y a 13 stocks sélectionnés dans ce screener sur les 234 en tout
- {{ "(3)" | red }} : Indique que les actions BAE SYSTEMS et BWXT sont dans le screener {{ "aero-space-defense.json" | keyword }}

## Modifier un screener

Vous pouvez cocher ou décocher des stocks pour les ajouter ou les retirer du screener :

<figure style="text-align: center;" title="Afficher la sélection">
  <img src="/images/heatmap-screener/screeners-selection.png" class="noborder" alt=""/>
  <figcaption><em>Création des screeners</em></figcaption>
</figure>

- {{ "(1)" | red }} : Effacer le filtre de sélection pour retrouver la liste complète des stocks.
- {{ "(2)" | red }} : Cliquer sur {{ "Sélection" | keywordi }} pour afficher la liste des stocks déjà dans le screener.

Le {{ "Filtre" | keywordi }} vous permet de trouver d'autres sotcks à ajouter dans votre screener. Vous pouvez rechercher une stock par son {{ "Nom" | keywordi }} son {{ "Symbole" | keywordi }} ou son {{ "Menu" | keywordi }}.

## Créer ou modifier un screener

Un fois la selection effectuée, vous sauver votre screener en venant écraser l'ancienne version du fichier.

- {{ "Ouvrir" | keywordi }} vous permet de changer de screener.
- {{ "Sauver" | keywordi }} vous permet de sauver les modifications que vous avez faites en écrasant le fichier existant.
- {{ "Supprimer" | keywordi }} vous supprimer un fichier de screener.

Vous créez un nouveau screener simplement en changeant le nom du fichier au moment de le sauvegarder.

## Utilisez vos screener

Un fois vos fichiers de screeners configurés avec les actions que vous souhaitez surveiller, vous pouvez utiliser ces fichiers dans les [Cartes de Chaleur](./heatmap-screener/heatmaps.md) et le [Monitor Stock Market](./monitor-alerts/monitor-stock-market.md).

## Erreur screener trop grand

Vous avez créé un screener en cochant toutes les {{"stocks"|g_tooltip}}, comme par exemple le screener {{"surveillance_totale.json"|keyword}} qui doit comporter aujourd'hui plus d'une centaine d'actions.

Vous ouvrez le {{"Monitoring"|keyword}} -> {{"Monitorez le marché"|keyword}}. De façon automatique l'application va se lancer dans des tas de calculs sur toutes les stocks du fichier et cela prend trop de temps.

Seulement voilà, le dernier screener ouvert est enregistré dans les settings (paramètres) donc, même si vous fermez l'application, la fenêtre {{"Monitorez le marché"|keyword}} recommence à s'ouvrir sur le même screener et redémarre ses calculs interminables.

Pour vous en sortir :

- Fermez l'application en fermant la Console (fenêtre noire) toutes les fenêtres se ferment.
- Ouvrez, non plus {{"Monitoring"|keyword}} -> {{"Monitorez le marché"|keyword}} mais {{"Monitoring"|keyword}} -> {{"Cartes de chaleur"|keyword}}.

Cette fois les calculs de la fenêtre ne sont pas lancés automtiquement, vous avez la possiblité de modifier le screener en cliquant sur {{"Ouvrir"|keywordi}} et en choisissant un fichier de screener que vous savez être "calculable" (comportant moins de stocks).

- Fermez la fenêtre {{"Cartes de chaleur"|keyword}}
- Ouvrez la fenêtre {{"Monitorez le marché"|keyword}}, elle s'ouvre maintenant avec le nouveau screener "calculable".
