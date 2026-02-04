# Création et gestion des screeners

Les screeners sont des fichiers partagés par les [Cartes de chaleur](./heatmaps.md) et le [Monitor Stock Market](../monitor-alerts/monitor-stock-market.md).

La Gestion des screeners vous permet de créer, de modifier ou de supprimer ces fichiers.

Pour configurer un screener, il faut faire une sélection de stocks et la sauvegarder dans le fichier.

## Ouvrir la gestion des screeners

Menu {{ "Monitoring" | keywordi }} article {{ "Gestion des scrreners" | keywordi }}.

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

Un fois vos fichiers de screeners configurés avec les actions que vous souhaitez surveiller, vous pouvez utiliser ces fichiers dans les [Cartes de Chaleur](./heatmaps.md) et le [Monitor Stock Market](../monitor-alerts/monitor-stock-market.md).
