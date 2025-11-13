import yaml
from markupsafe import Markup, escape

# Define the function to add glossary terms as tooltips
#
def define_env( env ):
    with open("docs/glossaire.yml", "r", encoding="utf-8") as f:
        glossary = yaml.safe_load(f)

    @env.macro
    def gtooltip( term ):
        definition = glossary.get( term )
        if definition:
            return tooltip( term, definition ) 
        return f'{term} (not in glossary)'

    @env.filter
    def tooltip( term, definition ):
        """
        Crée un span HTML avec un tooltip.
        """
        term_escaped = escape(term)
        def_escaped = escape(definition.replace("\n", " ").strip())
        html = f'<span title="{def_escaped}" style="border-bottom:1px dotted;cursor:help">{term_escaped}</span>'
        return Markup(html)  # Markup = ne pas échapper à l'affichage

    @env.macro
    def glink( term ):
        """
        Génère un lien Markdown/HTML vers le glossaire.
        Exemple :
            {{ gl("RSI") }}
        Résultat :
            <a href="{{ base_url }}/glossaire/#rsi">RSI</a>
        """
        base_url = env.conf['site_url'] if env.conf.get('site_url') else env.variables.get('base_url', '')
        anchor = term.lower().replace(" ", "-")  # pour les ancres typiques Markdown
        href = f"{base_url}/glossaire/#{anchor}"
        html = f'<a href="{href}">{term}</a>'
        return Markup(html)

    # --- Macro : génère la section Markdown complète ---
    @env.macro
    def generate_glossary():
        """
        Retourne un texte Markdown contenant toutes les définitions du glossaire.
        Exemple d'utilisation dans glossaire.md :
            {{ generate_glossary() }}
        """
        if not glossary:
            return Markup("_Aucune entrée dans le glossaire._")

        lines = []
        for term, definition in glossary.items():
            lines.append( f"## {escape(term)}\n" )
            lines.append( f"{definition}\n" )

        return Markup("\n".join(lines))
    