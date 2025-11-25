# Notes

## CNAME

A propos du CNAME écrasé à chaque publication :

- avec fork postionnement dans gh-pages
- copie du fichier CNAME à la racine du Site
- publication du CNAME dans la branche gh-pages

<figure style="text-align: center;">
    <a href="/images/notes/cname.png" class="glightbox" data-gallery="galerie" title="Titre de l'image">
        <img src="/images/notes/cname.png" alt="Image 2" />
    </a>
    <figcaption><em>Figure 1 – Cliquez pour agrandir</em></figcaption>
</figure>

Le CNAME de Site est écrasé car il n'y a pas de CNAME dans /docks

Ce que publie la commande mkdocs gh-deploy --remote-branch=gh-pages --remote-name=origine c'est de /docs dans /site

Donc si le CNAME est mal placé et ne se trouve pas dans /docs alors il est effacé de /site avant la plublication

Si 

## Localize MkDocs

Localize :

- [https://www.mkdocs.org/user-guide/localizing-your-theme/](https://www.mkdocs.org/user-guide/localizing-your-theme/)

## Glossaire plugin

Obsolète !!!

> pip install mkdocs-glossary-plugin
>
> pip uninstall mkdocs-glossary-plugin

## Macro



```
{% raw %}

{% endraw %}
```

