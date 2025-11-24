# TradingInPtyhon Plateforme de Trading Technique

## Documentation

- [TradingInPtyhon Documentation (Publication url)](https://mabyre.github.io/TradingInPython-doc/)
- [TradingInPython Software (Plateforme)](https://www.trading-et-data-analyses.com/p/plateforme-de-trading-technique.html)

## Site MkDocs

- [Tester sur serveur local](#tester-sur-le-serveur-local)
- [Déployer sur le GitHub](#déployer-sur-le-github)

## Install

Création du répertoire avec ce qu'il faut dedans :

```text
> pip install mkdocs
> pip install mkdocs-material
> mkdocs new TradingInPython-doc 
```

## Numéroter les headers automatiquement

```text
> pip install mkdocs-enumerate-headings-plugin
> pip uninstall mkdocs-enumerate-headings-plugin
> pip install mkdocs-macros-plugin
```

## Servir le site MkDocs en local

```text
Set-Location -LiteralPath "c:\Users\Bruno\Documents\GitHub\TradingInPython-doc\TradingInPython-doc"; python -m mkdocs serve --dev-addr=127.0.0.1:8000
```

Exécution

>PS C:\Users\Bruno\Documents\GitHub\trading-in-python> Set-Location -LiteralPath "c:\Users\Bruno\Documents\GitHub\trading-in-python\trading-in-python-doc"; python -m mkdocs serve --dev-addr=127.0.0.1:8000
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 1.00 seconds
INFO    -  [16:24:32] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [16:24:32] Serving on <http://127.0.0.1:8000/>
INFO    -  [16:25:49] Browser connected: <http://127.0.0.1:8000/>
INFO    -  [16:30:08] Browser connected: <http://127.0.0.1:8000/>
INFO    -  [16:31:24] Browser connected: <http://127.0.0.1:8000/>

Création de tout un tas de JS

```text
> mkdocs gh-deploy
```

Publier le tout avec Fork

```text
> git remote add origin <https://github.com/mabyre/TradingInPython-doc.git>
> git branch -M main
> git push -u origin main
```

Site accessible à l'adresse :

<https://mabyre.github.io/TradingInPython-doc/>

## Tester sur le serveur Local

```text
> cd .\TradingInPython-doc\
> mkdocs serve
```

Lorsque je modifie le fichier :

\GitHub\TradingInPython-doc\TradingInPython-doc\docs\index.md

Et que je fais Save :

>INFO    -  Documentation built in 0.20 seconds
INFO    -  [18:01:30] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO    -  [18:01:30] Serving on <http://127.0.0.1:8000/>
INFO    -  [18:01:34] Browser connected: <http://127.0.0.1:8000/>
INFO    -  [18:02:25] Detected file changes
INFO    -  Building documentation...
INFO    -  [18:02:25] Reloading browsers
INFO    -  [18:02:33] Browser connected: <http://127.0.0.1:8000/>
INFO    -  [18:02:52] Detected file changes

## Déployer sur le GitHub

```text
> mkdocs gh-deploy --remote-branch=gh-pages --remote-name=origine
```

Avec Fork pousser sur le GitHub ce qui a changé de la branch "gh-pages"
