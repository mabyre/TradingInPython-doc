# Syntaxe Markdown

## Colors

Du texte en <span class="text-red">rouge et en bold</span>

```html
<span class="text-red">rouge et en bold</span>
```

Du texte en <span class="text-green">vert et en bold</span>

Du texte en <span class="text-keyword">couleur keyword bold</span>

```html
<span class="text-keyword">vert et en keyword bold</span>
```

Grâce au @env.filter dans main.py :

{{ "Ce texte est en couleur 'keyword'" | keyword }}

```markdown
{% raw %}
{{ "Ce texte est en couleur 'keyword'" | keyword }}
{% endraw %}
```


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

