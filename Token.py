import ply.lex as lex
from PyQt5 import uic
from PyQt5 import  Qt
from tkinter import ttk
import tkinter
window = tkinter.Tk()
window.title("Primera parte analixador lexico")
window.geometry("950x550")
window.configure(background='#04D89B')
s = ttk.Style()
s.theme_use('clam')
# Configure the style of Heading in Treeview widget
s.configure('Treeview.Heading', background="#A1AEFD")
table = ttk.Treeview(window, columns=(
"#1", "#2", "#3", "#4"),show='headings') 
table.heading("#1", text="Linea") 
table.heading("#2", text="Token")
table.heading("#3", text="Valor")
table.heading("#4", text="Posicion")
table.column("#1", width=100)  
table.column("#2", width=100)
table.column("#3", width=100)
table.column("#4", width=100)
table.place(x=250, y=40, height=290)
table.tag_configure('odd', background='#A1DCFD')
table.tag_configure('even', background='#A1FDF0')

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'PA',
    'F',
    'CLASS',
    'NO',
    'ME',
    'RE',
    'TT',
    'GS',
    'D'
)
tokens = reservada + (
    #IDENTIFICADORES
    'LETRAS',
    #SIMBOLOS
    'TM',
    'MQ',
    'MAQ',
    'PP',
    'C',
    'PR'

)

# Reglas de Expresiones Regualres para token de Contexto simple

# SIMBOLOS
t_TM = r'(\+ | \-)'
t_MQ = r'<'
t_MAQ = r'>'
t_PP = ':'
t_C = r','
t_PR = r'(\( | \))'



def t_PA(t):
    r'parametro'
    return t

def t_F(t):
    r'Fin'
    return t

def t_CLASS(t):
    r'Clase'
    return t

def t_NO(t):
    r'nombre'
    return t

def t_ME(t):
    r'metodo'
    return t

def t_RE(t):
    r'relacion'
    return t

def t_TT(t):
    r'tipo \s de \s dato'
    return t

def t_GS(t):
    r'(get | set)'
    return t

def t_D(t):
    r'(string|int|float|double)'
    return t

def t_LETRAS(t):
    r'\w+(\s)*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments_ONELine(t):
     r'\/\/(.)*\n\"?\"?'
     t.lexer.lineno += 1
     print("Comentario de una linea")

t_ignore =' \t'

#\"?(\w+ \ *\w*\d* \ *)\"?

def t_error( t):
    global resultado_lexema
    estado = "Novalido {:4} {:16} {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso

def llamarAnalisis():
    data = entry.get()
    print(data)
    print("entro")
    analisis(data)
    for  i in range(len(resultado_lexema)):
            #result = ('\n'.join(map(str, resultado_lexema)))
            table.insert('','end',values=(resultado_lexema[i]),tags=('odd'))
    print('\n'.join(map(str, resultado_lexema)))

def analisis(data):
    table.delete(*table.get_children())
    
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = " {:4}  {:16}  {:16}  {:4}".format(
            str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos)
            )
        resultado_lexema.append(estado)
        print(resultado_lexema)

        # for  i in range(len(resultado_lexema)):
        #     result = ('\n'.join(map(str, resultado_lexema[i])))
        #     table.insert('','end',values=(result),tags=('odd')) 

    return resultado_lexema


if __name__ == '__main__':
    while True:
        style = ttk.Style()
        style.configure(
            "MyEntry.TEntry",
            padding = 60
        )
        entry = ttk.Entry(style="MyEntry.TEntry")
        entry.config(width=75  )
        entry.place(x=230, y=380)
        T = tkinter.Text(window, height = 60, width = 60)
        
        boton = tkinter.Button(text="verificar", command= llamarAnalisis)
        boton.place(x=130, y=420, width=80)
        
        window.mainloop()

