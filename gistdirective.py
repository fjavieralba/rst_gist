from docutils.parsers.rst import directives, Directive
from docutils import nodes

class Gist(Directive):
    """ Embed Github Gist Snippets in rst text

        GIST_ID and FILENAME are required.

        Usage:
          .. gist:: GIST_ID FILENAME
    
    """

    required_arguments = 2
    optional_arguments = 0
    option_spec = {
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):
        gist_id = self.arguments[0].strip()
        filename = self.arguments[1].strip()

        embed_html_code = """
        <script src="https://gist.github.com/%s.js?file=%s">
        </script>
        """ % (gist_id, filename)

        return [ nodes.raw('', embed_html_code, format='html') ]

directives.register_directive('gist', Gist)