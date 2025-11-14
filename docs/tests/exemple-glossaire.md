# Utilisation du Glosssaire

- **glossaire.md** : markdown page générée automatiquement avec le contenu du fichier glossaire

- **glossaire.yml** : le glossaire proprement dit

- main.py script python, fonctions de génération des link et tooltip et du glossaire.md

## Fonction du script main.py

Utilisation du filter **g_tooltip** {{ "MACD" | g_tooltip }}

```
{% raw %}
{{ "MACD" | g_tooltip }}
{% endraw %}
```

Utilisation du filter **g_link** {{ "MACD" | g_link }}

```
{% raw %}
{{ "MACD" | g_link }}
{% endraw %}
```

Utilisation du filter **g_tooltip** {{ "RSI" | g_tooltip }}

Utilisation du filter **g_link** {{ "RSI" | g_link }}

```
{% raw %}
{{ "RSI" | g_link }}
{% endraw %}
```

Utilisation de la macro **gtooltip** {{ gtooltip("RSI") }}

```
{% raw %}
{{ gtooltip("RSI") }}
{% endraw %}
```

## A la main

Création de Tooltip "à la main" [RSI]({{ base_url }}/glossaire/#rsi).

Voir la définition de [ICI]({{ base_url }}/glossaire/#ici).

Voir la définition de [ICI]({{ base_url }}/glossaire/#ICI).

Voir la définition de [Ici c'est là]({{ base_url }}/glossaire/#ici-cest-la).
