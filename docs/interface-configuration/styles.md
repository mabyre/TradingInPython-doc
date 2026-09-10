# Styles

Les fichiers de styles se trouvent dans le répertoire :

- C:\Users\\**{UserName}**\AppData\Local\TradingInPython\styles

où **{UserName}** est votre nom d'utilisateur sur votre poste.

Les fichiers avec l'extension **.mplstyle** définissent des couleurs et tailles et d'autres caractéristiques pour les graphiques matplot.

Par exemple le mode [DARK](./dark-mode.md) utilise le fichier : **darktradingplot.mplstyle**

## Modifier la taille des fenêtres graphiques

Vous trouvez que les fenêtre sont trop grandes pour votre écran.

Ouvrez le fichier de styles **tradingplot.mplstyle** et le fichier **darktradingplot.mplstyle** si vous utilisez le mode DARK.

Ajoutez la ligne suivante pour rapetisser la taille de la fenêtre graphique :

```
figure.dpi: 65.0
```

par défaut ce paramètre de taille des figures est à **80.0**
