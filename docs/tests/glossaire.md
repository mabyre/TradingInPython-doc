# Utilisation du Glosssaire et de Indicators

- **glossaire.md** : markdown page générée automatiquement avec le contenu du fichier glossaire

- **glossaire.yml** : le glossaire proprement dit

- main.py script python, fonctions de génération des link et tooltip et du glossaire.md

## Fonction du script main.py

### Glossaire

#### g_tooltip

Utilisation du filter **g_tooltip** {{ "Action" | g_tooltip }}

Utilisation du filter **g_tooltip** {{ "action" | g_tooltip }}

Utilisation du filter **g_tooltip** {{ "actions" | g_tooltip }}

Utilisation du filter **g_tooltip** {{ "Actions" | g_tooltip }}

Utilisation du filter **g_tooltip** {{ "Pas_Dans_Glossaire" | g_tooltip }}

```
{% raw %}
{{ "Action" | g_tooltip }}
{% endraw %}
```

#### g_link

Utilisation du filter **g_link** {{ "MatPlotLib" | g_link }}

Utilisation du filter **g_link** {{ "matplotlib" | g_link }}

Utilisation du filter **g_link** {{ "matplotlibs" | g_link }}

Utilisation du filter **g_link** {{ "sactions" | g_link }}

Utilisation du filter **g_link** {{ "Pas_Dans_Glossaire" | g_link }}

```
{% raw %}
{{ gtooltip("MatPlotLib") }}
{% endraw %}
```

### Indicators

Utilisation du filter **i_tooltip** {{ "RSI" | i_tooltip }}

Utilisation du filter **i_tooltip** {{ "rsi" | i_tooltip }}

Utilisation du filter **i_tooltip** {{ "rsis" | i_tooltip }}

Utilisation du filter **g_link** {{ "Pas_Dans_Indicators" | g_link }}

```
{% raw %}
{{ "RSI" | i_tooltip }}
{% endraw %}
```

Utilisation du filter **i_link** {{ "RSI" | i_link }}

Utilisation du filter **i_link** {{ "rsi" | i_link }}

Utilisation du filter **i_link** {{ "rsis" | i_link }}

Utilisation du filter **i_link** {{ "Pas_Dans_Indicators" | i_link }}

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

### Macro gtooltip

Utilisation de la macro **gtooltip** {{ gtooltip("MatPlotLib") }}

Utilisation de la macro **gtooltip** {{ gtooltip("matplotlibs") }}

Utilisation de la macro **gtooltip** {{ gtooltip("Pas_Dans_Glossaire") }}

```
{% raw %}
{{ "MatPlotLib" | g_link }}
{% endraw %}
```
