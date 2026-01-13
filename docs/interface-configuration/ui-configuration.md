# Configuration

Au sein de la plateforme vous allez trouver un certain nombre de facilités, pour [gérer les fenêtres](./windows-management.md) pour configurer les valeurs par défaut de vos indicateurs techniques.

## Paramètrage des indicateurs techniques

Menu {{ "Aide" | keyword }} -> {{ "Paramètres" | keyword }}

<figure style="text-align: center;">
    <a href="/images/interface-configuration/parametres.png" class="glightbox" data-gallery="galerie" title="Paramètres">
        <img src="/images/interface-configuration/parametres.png" title="Mofidier les parmètres"/>
    </a>
    <figcaption><em>Modifier les paramètres</em></figcaption>
</figure>

Tous les indicateurs techniques sont paramètrables ou configurales.

Il vous suffit de modifier la valeurs d'un paramètre de l'indicateur.

Vous avez un bouton {{ "Graphique" | keywordi }} vous voir l'effet immédiat de votre paramètres.

Et {{ "Sauver" | keywordi }} si cela vous convient.

Pour chaque indicateur un bouton {{ "Réinitialiser" | keywordi }} vous permet de remettre la valeur par défaut pour ce paramètre.

{{ "Réinitialiser" | keywordi }} vous permet de remettre toutes les valeurs par défaut.

## Partager la liste des Stocks

Vous avez installé {{ "TradingInPtyhon" | keyword }} sur plusieurs ordinateurs et vous souhaitez partager la liste des stocks entre ces ordinateurs.

Vous allez pouvoir sauver par exemple dans le {{ "Cloud OneDrive" | keyword }} la liste de vos stocks pour la partager entre plusieurs ordinateurs.

Cela se passe dans le fichier :

- **C:\Users\\{UserName}\AppData\Local\TradingInPython\config\fetch_data.json**

à la clef {{ "LIST_STOCKS_FILE_NAME_PATH" | keywordi }} vide pour l'instant :

```json
"LIST_STOCKS_FILE_NAME_PATH": ""
```

Copiez le chemin d'accès vers votre fichier dans le Cloud ou autre et copiez le dans la clef comme ceci :

```json
"LIST_STOCKS_FILE_NAME_PATH": "C:\\Users\\UserName\\OneDrive\\TradingInPython\\stocks\\list_stocks_watching.json"
```

Prenez soin de remplacer {{ "UserName" | keyword }} par votre nom d'utilisateur.

Ainsi les modifications faites à la [liste des stocks](../gestion-liste-actions.md) seront répercutées pour tous vos ordinateurs.
