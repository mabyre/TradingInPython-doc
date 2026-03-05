# Configuration & Settings

Au sein de la plateforme vous allez trouver un certain nombre de facilités, pour [gérer les fenêtres](./windows-management.md), pour configurer les valeurs par défaut de vos indicateurs techniques et pour configurer d'autres paramètres.

Menu {{ "Aide" | keyword }} -> {{ "Paramètres" | keyword }}

## Paramètres généraux

### MODE

Dark Mode ou mode sombre :

[Comment passer en mode sombre ?](./dark-mode.md)

- **dark** : cocher la case pour passer en mode sombre.

### MONITOR

- **run_at_start** : cocher la casse pour exécuter le monitor à l'ouverture de la fenêtre.

Lorsque vous souhaitez Monitorer le marché, vous pouvez choisir d'axécuter le [Monitoring des alertes](../monitor-alerts/monitor-stock-market.md) quand vous ouvrez la fenêtre.

Ce qui permet tout de suite d'aller consulter les alertes qui se sont déclenchées.

Mais par exemple si vous avez énormément de Stocks à monitorer cela peut être pénalisant d'exécuter le monitoring vous positionnez alors ce paramètre à faux en décochant la case.

## Réglez les paramètrage des indicateurs techniques

Tous les paramètres des indicateurs ne sont pas référencés ici, vous trouverez dans la documentation, dans les formations à quoi correspondent ces paramètres et comment ajuster leurs valeurs à votre trading.

Cette fenêtre n'est peut-être pas à jour des derniers paramètres de la dernière version de la plateforme mais voici à quoi elle ressemble :

<figure style="text-align: center;">
    <a href="/images/interface-configuration/parametres.png" class="glightbox" data-gallery="galerie" title="Paramètres">
        <img src="/images/interface-configuration/parametres.png" title="Mofidier les parmètres"/>
    </a>
    <figcaption><em>Modifier les paramètres</em></figcaption>
</figure>

Tous les indicateurs techniques sont paramètrables ou configurales avec des valeurs par défaut que vous pouvez modifier. Il vous suffit de modifier les valeurs d'un paramètre de l'indicateur que vous souhaitez dans la fenêtre {{ "Paramètres" | keywordi }}.

Vous avez le bouton {{ "Graphique" | keywordi }} pour voir immédiatement l'effet de votre paramètres sur le graphe.

Et le bouton {{ "Sauver" | keywordi }} pour seuvegrader cette valeur si elle vous convient.

Pour chaque indicateur un bouton {{ "Réinitialiser" | keywordi }} vous permet de remettre la valeur par défaut pour ce paramètre.

{{ "Réinitialiser" | keywordi }} vous permet de remettre toutes les valeurs par défaut.

### RSI

L'indicateur technique {{ "RSI" | i_link }} - Relative Strength Index son paramètre :

- **window** : largeur de la moyenne mobile

### MACD

L'indicateur technique {{ "MACD" | i_link }} - Moving Average Convergence Divergence

- **histo** : afficher ou non son histogramme

Cet indicateur est calculé grâce à trois moyennes mobiles :

- **short_window** : moyenne mobile courte
- **long_window** : moyenne mobile longue
- **signal_window** : moyenne mobile du signal

## Partagez la liste des Stocks entre plusieurs ordinateurs

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

!!! warning

    Il s'agit d'une opération délicate, le moindre caractère de travers et la plateforme risque de ne plus fonctionner.

    Si vous avez un soucis vous pouvez toujours reprendre le fichier original qui se trouve dans le {{ "GitHub" | g_tooltip }} :

    - [original fetch_data.json](https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/config/fetch_data.json)

