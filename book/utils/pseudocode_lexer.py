from pygments.lexer import RegexLexer, bygroups
from pygments.token import Keyword, Name, String, Number, Operator, Text, Comment, Name

class PseudocodeLexer(RegexLexer):
    name = 'Pseudocode'
    aliases = ['pseudocode']
    filenames = ['*.pse']

    tokens = {
        'root': [
            (r'\b(Funcion|FinFuncion|Algoritmo|FinAlgoritmo|Inicio|Fin|Si|SiNo|Sino|FinSi|Mientras|FinMientras|Para|FinPara|Escribir|Leer|Con Paso|Hacer|Repetir|Hasta Que|Segun|De Otro Modo|:|,|Entonces|Desde|Hasta|Dimension|Mostrar)\b', Keyword),  # Keywords
            (r'".*?"', String),         # Strings
            (r'//.*', Comment),         # Comments
            (r'\b[0-9]+\b', Number),    # Numbers
            (r'[+\-*/=<>MOD^]', Operator),  # Operators
            (r'\b[a-z_][a-z0-9_]*\b', Name),  # Variables
            (r'\s+', Text),             # Whitespace
            (r'\b(sen|cos|tan|asen|acos|atan|raiz|ln|exp|redon|trunc|abs|Longitud|SubCadena|Concatenar|ConvertirANumero|ConvertirATexto|Mayusculas|Minusculas|Azar|HoraActual|FechaActual|PI|Euler)\b', Name),               # Functions
        ],
    }
