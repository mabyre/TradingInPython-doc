# Bandes de Bollinger

Vous trouverez facilement sur le Net de la documentation sur les {{ "Bandes de Bollinger" | keyword }}, elle est plétorique, voici la mise en oeuvre des indicateurs techniques {{ "Bolls" | i_link }} dans la plateforme {{ "TradingInPython" | keyword }}.

{{ "John Bollinger" | keyword }}, un analyste technique américain, a créé les Bandes de Bollinger au début des années 1980. Il cherchait un moyen de mesurer si les prix étaient relativement hauts ou bas par rapport à leurs niveaux récents en utilisant la volatilité comme référence plutôt que des pourcentages fixes.

Il a l'idée d'encadrer une moyenne mobile avec deux bandes calculées à partir de l'écart-type. Quand les marchés deviennent volatils, les bandes s'élargissent quand ils se calment, elles se resserrent.

Bollinger a officiellement publié sa méthode en 1983, et elle est rapidement devenue l'un des indicateurs techniques les plus populaires au monde. Il a même déposé le nom "Bollinger Bands®" comme marque en 2011.

L'ironie ? Bollinger lui-même insiste toujours sur le fait que ses bandes ne doivent jamais être utilisées seules comme système de trading, mais plutôt combinées avec d'autres indicateurs - exactement comme dans la stratégie FTMA que tu nous allons explorer !

Cette technique est utilisée pour trader sur tous les marchés : forex, crypto, matières premières, indices...

Sur la plateforme nous avons implémenté les stratégies de trading suivantes :

- Les [Bandes Bollinger FTMA](bollinger-bands-ftma.md) : les bandes de Bollinger sur 4 horizons de temps différents (Four Timesframe Mobile Average)
- Les [Doubles de Bandes de Bollinger](bollinger-bands-double.md) : cette fois avec deux bandes de même horizon mais des écarts types différentes (standard déviation)
- Les [FTMA Bolls + histogramme](bollinger-bands-ftma-histogramme.md) : cette fois on s'intéresse de plus prês à l'histogrammes créé par les Bandes de Bollinger
