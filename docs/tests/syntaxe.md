# Syntaxe Markdown


## Décalage des listes à puces 

Par défaut VSCode sauve les fichiers Markdown avec 2 espaces au lieu de 4 pour la syntaxe stricte **MarkDown**

Paramètres utilisateur **Ctrl+Shift+P** → Preferences: Open Settings (JSON)

```
"[markdown]": {
    "editor.insertSpaces": true,
    "editor.tabSize": 4,
    "editor.formatOnSave": false
}
```

- text1
    - text2
        - text3

## Link target="_blank"

Il n'y a pas de moyen de faire des liens qui ouvrent de nouvelles fenêtre donc HTML :

<a href="https://github.com/SoDevLog/PyTrading/wiki/Installation" target="_blank">Installation</a>

```html
<a href="https://github.com/SoDevLog/PyTrading/wiki/Installation" target="_blank">Installation</a>
```
