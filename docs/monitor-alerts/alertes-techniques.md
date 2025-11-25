# Alertes techniques avancées

Il s'agit de placer des alertes sur les cours des actions, en utilisant les {{ "indicateurs techniques" | keyword }}.

Les indicateurs techniques sont calculés à intervalle régulier et les alertes sont vérifiées pour prévenir l'utilisateur.

On sait que quand l'indicateur RSI (Relative Strength Index, Indice de force relative) est inférieur à 30, il indique que la stock est survendue ce qui peut entrainer une baisse du cours et l'action peut devenir une opportunité d'achat.

- Menu {{ "Monitoring" | keywordi }} choisissez {{ "Monitor stock market" | keywordi }}

Dans le Monitor Stock Market Alertes, je vais pouvoir positionner une alerte RSI survendu (30) pour surveiller la stock FORTINET et déclencher une alerte lorsque le calcul de son RSI donne un résultat < 30 :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/alertes-avancees.png" class="glightbox" data-gallery="galerie" title="Stock Monitor Alertes - RSI survendu">
        <img src="/images/monitor-stock-market/alertes-avancees.png" />
    </a>
    <figcaption><em>Stock Monitor Alertes - RSI survendu</em></figcaption>
</figure>

Le bouton "Test" me permet de tester tout de suite mon alerte sans attendre le déclenchement par le Monitor.

Je vais ainsi pouvoir placer plusieurs alertes techniques sur les stocks de mon screener.

- Cassure résistance en volume
- RSI survendu (30)
- RSI suracheté (70)
- Croisement des MA haussier
- Pic de volume x2
- Gap haussier de 3 %
- Bollinger Squeeze

Je vais pouvoir les combiner, sur le modèle de ces alertes génériques, je vais pouvoir ajouter des alertes personnalisées :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/alertes-techniques-personnalisees.png" class="glightbox" data-gallery="galerie" title="Alertes techniques personnalisées">
        <img src="/images/monitor-stock-market/alertes-techniques-personnalisees.png" />
    </a>
    <figcaption><em>Alertes techniques personnalisées</em></figcaption>
</figure>

Par exemple en abaissant le seuil de déclenchement du RSI survendu à 25.

Maintenant ma stock FORTINET ne pleut plus échapper à mes alertes. Ainsi alerté je vais pouvoir prendre les décisions de trading qui s'imposent.

## Vous avez raté quelque chose ?

Voici la une vidéo rapide pour vous présenter les Alertes techniques avancéés de la plateforme :

<figure style="text-align: center;">
    <a href="/images/monitor-stock-market/alertes-techniques-avancees.gif" class="glightbox" data-gallery="galerie" title="Placer une alerte technique RSI oversold">
        <img src="/images/monitor-stock-market/alertes-techniques-avancees.gif"/>
    </a>
    <figcaption><em>Comment placer une alerte technique RSI oversold</em></figcaption>
</figure>

Découvrez rapidement comment vous allez pouvoir placer une alerte technique sur le seuil RSI à 30 afin de détecter si une action est survendue. Comment vous allez pouvoir tester cette alerte afin de la déclencher dans le Monitor Stock Market.
