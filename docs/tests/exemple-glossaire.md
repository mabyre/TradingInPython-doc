# Utilisation du Glosssaire

- **glossaire.md** : markdown page générée automatiquement avec le contenu du fichier glossaire

- **glossaire.yml** : le glossaire proprement dit

- main.py script python de génération des link et tooltip et du glossaire.md

## Fonction du script main.py


Utilisation de **glink** {{ glink("RSI") }}

```
{% raw %}
{{ glink("RSI") }}
{% endraw %}
```


Utilisation de **glink** {{ glink("Action") }}

Utilisation de **gtooltip** {{ gtooltip("Action") }} c'est caca

```
{% raw %}
{{ gtooltip("Action") }}
{% endraw %}
```

Utilisation de **gtooltip** {{ gtooltip("RSI") }} c'est caca


## A la main

Création de Tooltip "à la main" [RSI]({{ base_url }}/glossaire/#rsi).

Voir la définition de [ICI]({{ base_url }}/glossaire/#ici).

Voir la définition de [ICI]({{ base_url }}/glossaire/#ICI).

Voir la définition de [Ici c'est là]({{ base_url }}/glossaire/#ici-cest-la).
