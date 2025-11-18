# Utilisation du Glosssaire et de Indicators

- **glossaire.md** : markdown page générée automatiquement avec le contenu du fichier glossaire

- **glossaire.yml** : le glossaire proprement dit

- main.py script python, fonctions de génération des link et tooltip et du glossaire.md

## Fonction du script main.py

### Glossaire

Utilisation du filter **g_tooltip** {{ "Action" | g_tooltip }}

```
{% raw %}
{{ "Action" | g_tooltip }}
{% endraw %}
```

Utilisation de la macro **gtooltip** {{ gtooltip("MatPlotLib") }}

```
{% raw %}
{{ gtooltip("MatPlotLib") }}
{% endraw %}
```


Utilisation du filter **g_link** {{ "MatPlotLib" | g_link }}

```
{% raw %}
{{ "MatPlotLib" | g_link }}
{% endraw %}
```

### Indicators

Utilisation du filter **i_tooltip** {{ "RSI" | i_tooltip }}

```
{% raw %}
{{ "RSI" | i_link }}
{% endraw %}
```

Utilisation du filter **i_link** {{ "RSI" | i_link }}

```
{% raw %}
{{ "RSI" | i_link }}
{% endraw %}
```


## A la main

Création de Tooltip "à la main" [RSI]({{ base_url }}/glossaire/#rsi).

Voir la définition de [ICI]({{ base_url }}/glossaire/#ici).

Voir la définition de [ICI]({{ base_url }}/glossaire/#ICI).

Voir la définition de [Ici c'est là]({{ base_url }}/glossaire/#ici-cest-la).

## Indicators
