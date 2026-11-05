---
description: "Découvrez TradingInPython, un logiciel de trading technique Open Software : consultez certains codes sources, intégrez vos scripts Python et développez vos propres stratégies."
keywords: "TradingInPython, open software, logiciel de trading Python, logiciel d'analyse technique, scripts Python, stratégies de trading, indicateurs techniques"
---

# Open Software : une plateforme de trading ouverte et extensible avec Python

{{"TradingInPython"|keyword}} est une plateforme d'analyse technique conçue pour être utilisée immédiatement, mais aussi pour être adaptée par les utilisateurs qui souhaitent aller plus loin dans la programmation. Elle permet d'exploiter les méthodes d'analyse présentées sur ce site dans un environnement graphique, tout en offrant des possibilités d'extension avec le langage {{"Python"|keyword}}.

Vous pouvez commencer par utiliser les indicateurs et les stratégies disponibles, sans programmer. Si vous connaissez le langage de programmation Python, vous pouvez consulter certains codes sources publiés, exécuter vos propres scripts et {{"développer vos propres stratégies de trading"|keyword}}.

## Un logiciel Open Software ce n'est pas un logiciel Open Source

Il est important de distinguer les notions d'{{"Open Source"|keyword}} et d'{{"Open Software"|keyword}}.

La totalité du code source de TradingInPython n'est pas publiée. Le logiciel conserve des composants propriétaires. En revanche, une partie des codes source est accessible et modifiable par l'utilisateur, notamment des algorithmes de traitement du signal, des filtres, des indicateurs techniques et des stratégies de trading.

TradingInPython est donc un {{"logiciel Open Software"|keyword}} : son environnement permet à l'utilisateur d'aller au-delà des fonctionnalités intégrées, en consultant les sources mises à disposition et en ajoutant ses propres scripts et algorithmes Python.

Cette ouverture permet de mettre en pratique les méthodes présentées sur le site dans un logiciel graphique, puis de les adapter progressivement à ses propres besoins.

Pour découvrir comment intégrer et utiliser vos propres stratégies, consultez également la page consacrée à leur utilisation dans la plateforme :

- [Stratégies de trading technique dans TradingInPython](https://www.trading-et-data-analyses.com/p/strategies-dans-tradinginpython.html)

## Les algorithmes de traitement du signal publiés sur GitHub

Les algorithmes de traitement du signal utilisés par la plateforme sont accessibles publiquement. Vous pouvez consulter leur code, comprendre leur fonctionnement et vous en inspirer pour vos propres développements.

<figure style="text-align: center;">
  <a href="https://github.com/SoDevLog/PyTrading/tree/main/TradingInPython/_internal/digitsignalprocessing" target="_blank" title="GitHub - Digital Signal Processing">
    <img src="/images/git-hub.png" alt="Répertoire GitHub des algorithmes Digital Signal Processing de TradingInPython" class="noborder" width="450" />
  </a>
  <figcaption><em>Les sources Digital Signal Processing publiées sur GitHub</em></figcaption>
</figure>

Le répertoire {{"Digital Signal Processing"|keyword}} rassemble des algorithmes écrits en {{ "Python" | g_tooltip }} utilisés dans les traitements et les indicateurs de la plateforme :

- [Consulter le répertoire Digital Signal Processing sur GitHub](https://github.com/SoDevLog/PyTrading/tree/main/TradingInPython/_internal/digitsignalprocessing)
- [Consulter le fichier `indicators.py`](https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/digitsignalprocessing/indicators.py), qui regroupe les implémentations des indicateurs techniques.

Vous pouvez ainsi examiner le code plutôt que de considérer les indicateurs comme des outils opaques. Ces sources constituent également des exemples pour apprendre à construire vos propres traitements de données financières.

## Exécuter vos propres scripts Python dans TradingInPython

{{"TradingInPython"|keyword}} utilise les possibilités du langage Python pour permettre l'exécution de scripts personnalisés. Les scripts peuvent être exécutés directement par l'environnement Python de la plateforme. Certains composants ou stratégies peuvent également être distribués sous forme de modules compilés avec {{"Cython"|keyword}}.

Il n'est donc pas nécessaire de modifier les fichiers internes du logiciel pour commencer à développer vos outils. La plateforme intègre un {{"interpréteur de scripts Python"|keyword}} qui permet de lancer des scripts utilisateurs depuis son interface.

Cette solution permet de :

- exécuter les scripts Python fournis avec la plateforme,
- analyser une valeur ou une liste d'actions sélectionnée,
- exploiter les informations transmises par la plateforme à travers son API de scripts,
- afficher les résultats dans la console et produire vos propres analyses.

Les listes d'actions constituées avec les screeners servent de données d'entrée à vos scripts. Vous pouvez donc associer sélection de valeurs, analyse financière et programmation Python dans un même environnement.

Pour découvrir le fonctionnement de cette interface, les scripts fournis et l'API disponible, consultez la documentation :

- [Comment utiliser l'interpréteur de scripts Python](https://trading-in-python.sodevlog.com/script-interpreter/interface/)
- [Scripts d'analyse financière](https://trading-in-python.sodevlog.com/script-interpreter/financial-analysis-scripts/)
- [Exemples de scripts utilisateurs sur GitHub](https://github.com/SoDevLog/PyTrading/tree/main/TradingInPython/_internal/user_scripts)

Sur une installation Windows, les scripts utilisateurs sont regroupés dans le répertoire `user_scripts` du dossier de données de TradingInPython, sous le profil de l'utilisateur :

```text
C:\Users\{UserName}\AppData\Local\TradingInPython\user_scripts
```

## Pour modifier une stratégie Python existante

Pour les utilisateurs qui souhaitent intervenir plus directement sur une stratégie livrée avec le logiciel, certains fichiers Python peuvent être étudiés et adaptés pour vos besoins.

Prenons l'exemple de la stratégie des moyennes mobiles :

<figure style="text-align: center;">
  <a href="/images/open-software/sources-python.png" target="_blank" title="Fichiers Python de la stratégie des moyennes mobiles">
    <img src="/images/open-software/sources-python.png" alt="Exemple de fichiers source Python et de module compilé pour une stratégie TradingInPython" class="noborder" />
  </a>
  <figcaption><em>Exemple de fichiers associés à une stratégie Python</em></figcaption>
</figure>

Le dépôt GitHub contient le fichier source de cette stratégie :

- [`strategy_sma12e.py`](https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/strategy_sma12e.py)

Lorsque votre installation contient à la fois le fichier Python et le module compilé correspondant, le fonctionnement dépend de la version distribuée :

- le fichier `.py` contient le script Python lisible et modifiable ;
- le fichier `.pyd` est un module d'extension compilé à l'aide de Cython.

Dans le mécanisme utilisé pour cette stratégie, si vous souhaitez tester votre version du script, vous pouvez modifier le fichier `.py` et mettre temporairement de côté le module `.pyd` correspondant afin que Python charge le script source à la place.

!!! danger "Précautions avant toute modification"

    - Faites une sauvegarde de votre installation avant de modifier un fichier interne.
    - Ne déplacez que le module compilé correspondant exactement au script que vous souhaitez remplacer.
    - Conservez une copie du fichier d'origine afin de pouvoir revenir en arrière.
    - Une mise à jour ou une réinstallation de la plateforme peut remplacer vos modifications.

Vous pouvez également cloner le dépôt du projet pour travailler sur les fichiers sources dans un environnement de développement séparé :

- [Dépôt GitHub SoDevLog/PyTrading](https://github.com/SoDevLog/PyTrading)

## L'environnement de développement de TradingInPython

{{"TradingInPython"|keyword}} s'appuie sur une stack de développement, sur plusieurs outils utilisés pour développer, maintenir et distribuer la plateforme. Ils constituent l'environnement de travail du projet, ils ne sont pas nécessaires pour utiliser l'application.

Voici la stack de développement :

- [Python](https://www.python.org/) : langage de programmation utilisé pour les scripts, les traitements de données et les stratégies.
- [Visual Studio Code](https://code.visualstudio.com/) : environnement de développement (IDE) utilisé pour écrire et déboguer les scripts Python ainsi que pour travailler sur les procédures de construction et d'installation.
- [Fork](https://fork.dev/) : outil de gestion des versions Git et d'interfaçage avec GitHub.
- [Cython](https://cython.readthedocs.io/) : outil permettant de compiler les modules Python en extensions natives.
- [PyInstaller](https://pyinstaller.org/) : outil utilisé pour préparer la distribution de l'application Python en regroupant le programme et ses dépendances.
- [Inno Setup](https://jrsoftware.org/isinfo.php) : outil de création de l'installateur Windows.

Ces outils illustrent la chaîne de développement utilisée autour de TradingInPython, depuis l'écriture du code jusqu'à la préparation de sa distribution sur Windows.

## Kit de développement TradingInPython

Vous souhaitez accéder aux codes sources des outils et des scripts Python du Kit de Trading pour aller plus loin dans leur personnalisation et leur développement ? C’est l’objet du Kit de Trading en Python. Consultez sa présentation :

- [Kit de Trading en Python et Data Analyses](https://www.trading-et-data-analyses.com/p/trading-en-python.html)

Le Kit est une offre distincte de l'application TradingInPython prête à l'emploi. Sa présentation détaille son contenu et ses modalités.

## Développer vos propres stratégies de trading

L'interpréteur de scripts est un premier moyen de personnaliser vos analyses. Pour aller plus loin, TradingInPython met à disposition une API permettant de développer des stratégies et d'exploiter les données fournies par la plateforme.

Vous pouvez découvrir les principes de création des stratégies, consulter les exemples disponibles et adapter votre approche à vos propres règles d'analyse :

- [Vue d'ensemble des stratégies de trading](https://trading-in-python.sodevlog.com/strategies/)
- [Documentation de l'interpréteur et de l'API des scripts](https://trading-in-python.sodevlog.com/script-interpreter/interface/)
- [Exemple de stratégie des moyennes mobiles](https://github.com/SoDevLog/PyTrading/blob/main/TradingInPython/_internal/strategy_sma12e.py)

## À propos du développement de la plateforme

TradingInPython est développé par [Bruno](https://www.linkedin.com/in/bruno-raby/), CTO de SoDevLog, à partir du Kit de Trading. Le projet s'appuie également sur les logiciels libres, les bibliothèques open source et le travail des développeurs qui contribuent à ces écosystèmes.

## Besoin d'informations ou d'accompagnement ?

Vous souhaitez développer une stratégie de trading technique, comprendre les possibilités d'extension ou obtenir des précisions sur le Kit de développement ?

- [Contacter le support de TradingInPython](https://www.trading-et-data-analyses.com/p/formulaire-de-contact.html)
