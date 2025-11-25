# Essai avec le thème Material

[MkDocs - Material - Tooltips](https://squidfunk.github.io/mkdocs-material/reference/tooltips/)

[Hover me](https://example.com "I'm a tooltip!")

```
{% raw %}
[Hover me](https://example.com "I'm a tooltip!")
{% endraw %}
```

[Tooltip en html](#html "I'm a tooltip to go to html!")

```
{% raw %}
[Tooltip en html](#html "I'm a tooltip to go to html!")
{% endraw %}
```

## Html

Voici un texte avec un <span title="Ceci est un tooltip en langage naturel.">tooltip</span>.

```html
Voici un texte avec un <span title="Ceci est un tooltip en langage naturel.">tooltip</span>.
```

**Ne fonctionne pas :**

:material-information-outline:{ title="Important information" }

The HTML specification is maintained by the W3C.

*[HTML]: Hyper Text Markup Language

*[W3C]: World Wide Web Consortium

[Subscribe to our newsletter](#){ .md-button .md-button--primary }

## Tooltip & Glossaire

[Glossaire](glossaire.md)
