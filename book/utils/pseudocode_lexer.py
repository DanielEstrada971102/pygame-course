from pygments.lexer import RegexLexer, bygroups
from pygments.token import Keyword, Name, String, Number, Operator, Text, Comment, Name

class PseudocodeLexer(RegexLexer):
    name = 'Pseudocode'
    aliases = ['pseudocode']
    filenames = ['*.pse']

    tokens = {
        'root': [
            (r'\b(Funcion|Algoritmo|FinAlgoritmo|Inicio|Fin|Si|SiNo|Mientras|Para|Escribir|Leer|Con Paso|Hacer|Repetir|Hasta Que|Segun|De Otro Modo|:|Entonces)\b', Keyword),  # Keywords
            (r'".*?"', String),         # Strings
            (r'\b[0-9]+\b', Number),    # Numbers
            (r'[+\-*/=<>MOD^]', Operator),  # Operators
            (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', Name),  # Variables
            (r'#.*$', Comment),         # Comments
            (r'\s+', Text),             # Whitespace
            (r'\b(sen|cos|tan|asen|acos|atan|raiz|ln|exp|redon|trunc|abs|Longitud|SubCadena|Concatenar|ConvertirANumero|ConvertirATexto|Mayusculas|Minusculas|Azar|HoraActual|FechaActual|PI|Euler)\b', Name),               # Functions
        ],
    }
