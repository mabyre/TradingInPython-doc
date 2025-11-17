import yaml
from markupsafe import Markup, escape

# Define the function to add glossary terms as tooltips
#
def define_env( env ):
    with open("docs/glossaire.yml", "r", encoding="utf-8") as f:
        glossary = yaml.safe_load(f)

    @env.filter
    def g_tooltip( term ):
        """
        Crée un span HTML avec tooltip.
        
        Exemple d'utilisation dans un fichier Markdown :
            {{ "RSI" | g_tooltip }}
        Le tooltip n'affiche que la première ligne de la définition du glossaire.
        """
        definition = glossary.get( term )
        if definition:
            term_escaped = escape( term )
            first_line = definition.strip().split("\n", 1)[0]
            html = f'<span title="{first_line}" style="border-bottom:1px dotted;cursor:help"><b>{term_escaped}</b></span>'
            return Markup( html )  # Markup = ne pas échapper à l'affichage

        return f'{term} not in glossary'
    
    @env.macro
    def gtooltip( term ):
        """       
        Utilise g_tooltip pour en faire une macro.
        
        Exemple :
            {{ gtooltip("RSI") }}
        """       
        return g_tooltip( term ) 

    @env.filter
    def g_link( term ):
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
        return Markup( html )

    # --- Macro : génère la section Markdown complète ---
    @env.macro
    def generate_glossary():
        """
        Genère le Glossaire dans une page Markdown.
        
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
    