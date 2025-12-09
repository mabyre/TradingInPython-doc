# Analyse de la Pression Volumique

Considèrons que les volumes d'achats exercent une pression {{ "à la hausse" | keyword }} alors que les volumes de ventes exercent une pression {{ "à la baisse" | keyword }}.

Au sein de la plateforme, l'analyse de la pression volumique des flux vous permet de savoir si {{ "les acheteurs sont à la manoeuvre" | keyword }} ou si ce sont {{ "les vendeurs" | keyword }}.

Nous avons poussé cette analyse technique à son niveau le plus haut ...

## Interface

C'est un outil {{ "exclusif" | keyword }} de notre plateforme, le résultat d'analyses mathématiques et algorithmiques des indicateurs sur les volumes, pour arriver à un outil pratique qui vous permette à coup sûr de savoir si ce sont les acheteurs ou bien si ce sont les vendeurs qui sont à la manœuvre.

Voici l'outil d'analyse de la pression volumique des flux d'achats et de ventes :

<figure style="text-align: center;">
    <a href="/images/strategies/volume-pression/interface.png" class="glightbox" data-gallery="galerie" title="Analyse de la pression du flux volumique">
        <img src="/images/strategies/volume-pression/interface.png" alt="alt" />
    </a>
    <figcaption><em>Analyse de la pression du flux volumique</em></figcaption>
</figure>

Au centre le graphe, le cours et un indicateurs technique du flux volumique qui est l'intégrale des volumes de vente et des volumes d'achats.

A droite, toutes les statistiques sur les volumes d'{{ "achat" | green }} et de {{ "vente" | red }}.

- Un volume d'achat est {{ "vert" | green }} si à la fin de la séance, ce volume d'échange de titres, fait monter le prix.
- Un volume d'achat est {{ "rouge" | red }} si à la fin de la séance, il fait baisser le prix.

Vous pouvez voir ici que sur le cours de l'action TESLA, ces deux derniers jours la pression de vente de {{ "17,54 %" | red }} c'est à dire que les vendeurs vendent plus que les acheteurs de 17,54 %.

Vous savez qu'une séance d'achat et de vente dans la chambre de compensation se termine par un achat (une barre verte) si le pris de clôture est supérieur au prix d'ouverture et une vente (barre rouge) si le pris de clôture est inférieur au pris d'ouverture.

## Volume incertain

Mais que se passe t-il lorsque le prix d'ouverture est égale au prix de clôture ? Et bien c'est là que la colonne {{ "Uncertain" | keywordi }} intervient, on a ainsi une vision précise des séances et celles qui sont incertaines ne sont comptabilisées ni comme achat ni comme vente.

C'est l'objet de la case à cocher {{ "Algo 1/2" | keywordi }} vous permettre de visualiser l'incertitude des acheteurs et des vendeurs.

## Zoomez pour recalculer la pression volumique

La fonction de {{ "ZOOM" | keyword }}, la loupe dans la tool barre [MatPlotLib](../draw-on-charts/navigate-on-charts.md#toolbar-matplotlib]) vous permet de refaire les calculs pour la zone que vous choisissez avec ce zoom :

Avec la fonction {{ "ZOOM" | keyword }}, je focalise sur la partie droite du graphe :

<figure style="text-align: center;">
    <a href="/images/strategies/volume-pression/tesla.png" class="glightbox" data-gallery="galerie" title="TESLA - Zoom sur la partie droite du graphe">
        <img src="/images/strategies/volume-pression/tesla.png" alt="alt" />
    </a>
    <figcaption><em>TESLA - Zoom sur la partie droite du graphe</em></figcaption>
</figure>

Pour cette partie du graphe, la pression de vente est de {{ "23,11 %" | red }} recalculée à chaque zoom.

Vous pouvez donc voir instantanément que la pression de vente sur le cours de l'action TESLA augmente c'est derniers temps.

La {{ "courbe bleue" | blue }}, c'est l'intégrale des achats et des ventes, elle semble suivre le cours de l'action mais les moments intéressants c'est quand cette courbe indique que l'action est à la vente et que le prix ne baisse plus. Il se créé alors une tension ou pression du flux volumique. C'est un renversement de {{ "tendance haussier" | keyword }}.

## Renversement de tendance

A l'inverse, un autre moment intéressant, quand la pression d'achat est importante et que le prix ne monte pas, c'est en général le prélude à un reversement de {{ "tendance baissier" | keyword }}.

Vous savez que le cours des actions est comme un élastique qui créé des tensions, il y a des tensions qui s'exercent qui s'emmagasinent et se libèrent parfois d'un seul coup.

Par exemple pour {{ "DASSAULT AVIATION" | keyword }} nous avons en ce moment :

<figure style="text-align: center;">
    <a href="/images/strategies/volume-pression/dassault-aviation.png" class="glightbox" data-gallery="galerie" title="DASSAULT AVIATION - Analyse de la pression volumique">
        <img src="/images/strategies/volume-pression/dassault-aviation.png" alt="alt" />
    </a>
    <figcaption><em>DASSAULT AVIATION - Analyse de la pression volumique</em></figcaption>
</figure>

Vous pouvez voir que le cours en rouge est très différent de l'intégrale des flux. Pour {{ "DASSAULT AVIATION" | keyword }} le prix monte alors que la pression de vente est de 27,53 %.

Notre outil est un l'{{ "analyseur de cette pressions volumique" | keyword }}.

Vous verrez qu'à l'usage cet outil vient confirmer vos autres analyses technique et qu'il vous permet d'assurer son trading de façon assez sereine.

## Analyse dynamique de la pression volumique

Grâce à la {{ "roulette de la souris" | keyword }}, les calculs de la pression volumique sont effectués en temps réel pendant le déplacement du graphe, ce qui permet d'analyser les changements de tendance :

<figure style="text-align: center;">
    <a href="/images/strategies/volume-pression/animation.gif" class="glightbox" data-gallery="galerie" title="Analyse Dynamique de la pression volumique des flux">
        <img src="/images/strategies/volume-pression/animation.gif" alt="alt" />
    </a>
    <figcaption><em>Analyse Dynamique de la pression volumique des flux</em></figcaption>
</figure>

Dans cette courte vidéo du graphe d'EXAIL TECHNO à l'échelle de temps `1 jour` sur la période de six derniers mois, la pression volumique est à l'achat de {{ "8,43%" | green }}. Avec la roulette de fais défiler le graphe vers la droite et la pression volumique est recalculée en temps réel pour déminuer et passer à une pression de vente qui augmente.

A la fin, la pression volumique de vente grimpe jusqu'à près de 50%. Il y a donc 50 % de plus de ventes que d'achats.

Inutile de vous dire que dans ce cas, le cours de l'action va chuter.

## Vidéo YouTube

Vous avez raté quelque chose, regardez l'outil en action dans la plateforme de Trading, une vidéo qui vous montre le calcul de la pression volumique au fur et à mesure du déplacement d'un graphe à l'aide de [MatplotLib](../draw-on-charts/navigate-on-charts.md) :

<div align="center" class="md-video">
<iframe width="560" height="315" src="https://www.youtube.com/embed/NQvGApxtcA0?si=sUbcdshdYvx5KPTG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## Support

Vous avez des questions n'hésitez pas à contacter le [Support](../support-faq.md)

- <a href="https://www.trading-et-data-analyses.com/p/abonnement.html" target="_blank">Abonnement à la plateforme TradingInPython</a>
