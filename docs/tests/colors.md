Du texte en <span class="text-red">rouge et en bold</span>

```html
<span class="text-red">rouge et en bold</span>
```

Du texte en <span class="text-green">vert et en bold</span>

```html
<span class="text-red">rouge et en bold</span>
```

Du texte en <span class="text-keyword">couleur keyword bold</span>

```html
<span class="text-keyword">vert et en keyword bold</span>
```

## Filtres de Couleur

Grâce au @env.filter dans main.py :

{{ "Ce texte est en couleur 'keyword'" | keyword }}

```markdown
{% raw %}
{{ "Ce texte est en couleur 'keyword'" | keyword }}
{% endraw %}
```

{{ "Ce texte est en couleur 'red'" | red }}

```markdown
{% raw %}
{{ "Ce texte est en couleur 'red'" | red }}
{% endraw %}
```
