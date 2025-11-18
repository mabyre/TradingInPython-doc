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

## YouTube intégration

<div align="center" class="md-video">
<iframe width="560" height="315" src="https://www.youtube.com/embed/z4gIwwcPSW4?si=X_mP1gMcAAO3n87s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

```html
<div align="center" class="md-video">
<iframe width="560" height="315" src="https://www.youtube.com/embed/z4gIwwcPSW4?si=X_mP1gMcAAO3n87s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
```

