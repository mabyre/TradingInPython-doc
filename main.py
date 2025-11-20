""" 
    Define the function to add glossary terms as link & tooltips
    - Filters_for_glossary_tooltips_and_links
    
    Define the function to add indicators terms as link & tooltips
    - Filters_for_indicators
    
    - Text_color_filters
"""
from email.mime import text
import yaml
from markupsafe import Markup, escape

def define_env( env ):
    
    #
    # Text_color_filters
    #
    
    @env.filter
    def keyword( text ):
        return f'<span class="text-keyword">{text}</span>'

    # keywordi : keyword dans les interfaces
    @env.filter
    # Des citations entre guillemets
    def keywordi( text ):
        return f'<span class="text-keyword">"{text}"</span>'    

    @env.filter
    def green( text ):
        return f'<span class="text-green">{text}</span>'
    
    @env.filter
    def red( text ):
        return f'<span class="text-red">{text}</span>'
        
    #
    # Filters_for_glossary_tooltips_and_links
    #
    
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
        definition = None
        
        for key in glossary:
            # Compare in lowercase
            if key.lower() == term.lower():
                definition = glossary[ key ]
                break
            
            # Compare with 's' at the end
            if key.lower() + 's' == term.lower():
                definition = glossary[ key ]
                break
    
        if not definition:
            return f'{term} not in glossary!'
        
        term_escaped = escape( term )
        first_line = definition.strip().split("\n", 1)[0]
        html = f'<span title="{first_line}" style="border-bottom:1px dotted;cursor:help"><b>{term_escaped}</b></span>'
        
        return Markup( html )  # Markup = ne pas échapper à l'affichage
    
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
        _key = None
        
        for key in glossary:
            # Compare in lowercase
            if key.lower() == term.lower():
                _key = key
                break
                        
            # Compare with 's' at the end
            if key.lower() + 's' == term.lower():
                _key = key
                break
    
        if not _key:
            return f'{term} not in glossary!'
        
        #base_url = env.conf['site_url'] if env.conf.get('site_url') else env.variables.get('base_url', '')
        base_url = env.variables.get('base_url', '')
        anchor = _key.lower().replace( " ", "-" )  # pour les ancres typiques Markdown
        href = f'{base_url}/glossaire/#{anchor}'
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

    #
    # Filters_for_indicators
    #
    
    with open("docs/indicators.yml", "r", encoding="utf-8") as f:
        indicators = yaml.safe_load(f)
    
    @env.filter
    def i_tooltip( term ):
        """
        Crée un span HTML avec tooltip.
        
        Exemple d'utilisation dans un fichier Markdown :
            {{ "RSI" | g_tooltip }}
        Le tooltip n'affiche que la première ligne de la définition du glossaire.
        """
        definition = None
        
        for key in indicators:
            # Compare in lowercase
            if key.lower() == term.lower():
                definition = indicators[ key ]
                break
            
            # Compare with 's' at the end
            if key.lower() + 's' == term.lower():
                definition = indicators[ key ]
                break
    
        if not definition:
            return f'{term} not in indicators!'
        
        term_escaped = escape( term )
        first_line = definition.strip().split("\n", 1)[0]
        html = f'<span title="{first_line}" style="border-bottom:1px dotted;cursor:help"><b>{term_escaped}</b></span>'
        
        return Markup( html )  # Markup = ne pas échapper à l'affichage

    @env.filter
    def i_link( term ):
        """
        Génère un lien Markdown/HTML vers le glossaire.
        
        Exemple :
            {{ gl("RSI") }}
        Résultat :
            <a href="{{ base_url }}/glossaire/#rsi">RSI</a>
        """
        _key = None
        
        for key in indicators:
            # Compare in lowercase
            if key.lower() == term.lower():
                _key = key
                break
                        
            # Compare with 's' at the end
            if key.lower() + 's' == term.lower():
                _key = key
                break
    
        if not _key:
            return f'{term} not in indicators!'
        
        #base_url = env.conf['site_url'] if env.conf.get('site_url') else env.variables.get('base_url', '')
        base_url = env.variables.get('base_url', '')
        anchor = _key.lower().replace( " ", "-" )  # pour les ancres typiques Markdown
        href = f'{base_url}/indicators/#{anchor}'
        html = f'<a href="{href}">{term}</a>'
        return Markup( html )

    # --- Macro : génère la section Markdown complète ---
    @env.macro
    def generate_indicators():
        """
        Genère le Glossaire dans une page Markdown.
        
        Exemple d'utilisation dans glossaire.md :
            {{ generate_glossary() }}
        """
        if not indicators:
            return Markup("_Aucune entrée dans le glossaire._")

        lines = []
        for term, definition in indicators.items():
            lines.append( f"## {escape(term)}\n" )
            lines.append( f"{definition}\n" )

        return Markup("\n".join(lines))    