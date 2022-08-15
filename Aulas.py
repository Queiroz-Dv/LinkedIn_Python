from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar

def Aula1():
    f = 0
    print(f)

    f = "abc"

    def Funcao():
        f = "def"
        print(f)

    Funcao()
    print(f)

def Aula2():
    def FuncaoSemArgumentos():
        print("Eu sou uma função")

    def FuncaoComArgumentos(arg1, arg2):
        print(arg1 + " " + arg2)

    def FuncaoQueRetornaValor(x):
        return x * x * x

def Aula3():
    def Condicionais():
        x, y = 1000, 100
        if (x < y):
            print("x é menor do que y")
        else:
            print("x é maior do que y")

def Aula4():
    def LoopWhile():
        x = 0
        while (x < 5):
            print(x)
            x = x + 1

def Aula5():
    def LoopFor():
        for x in range(5, 10):
            print(x)

    def LoopArray():
        dias = ["segunda", "terça", "quarta",
                "quinta", "sexta", "sabado", "domingo"]
        for dia in dias:
            print(dia)

    def LoopEnum():
        dias = ["segunda", "terça", "quarta",
                "quinta", "sexta", "sabado", "domingo"]
        for index, dia in enumerate(dias):
            print(index, dia)

def Aula6():
    def LoopBreak():
        for x in range(5, 10):
            if x == 7:
                break
            print("O valor de x é: ", x)

    def LoopContinue():
        for x in range(5, 10):
            if x == 7:
                continue
            print("O valor de x é: ", x)

def Aula7():
    class minhaClasse():
        def __init__(self):
            self.meuAtributo = "Passando pelo construtor!"

        def meuMetodo(self):
            print("Passando pelo método")

        def meuSegundoMetodo(self, valor):
            self.outroAtributo = valor
            print(self.outroAtributo)

    def CriaObjeto():
        meuObj = minhaClasse()
        var1 = meuObj.meuAtributo
        print(var1)

        meuObj.meuMetodo()

        meuObj.meuSegundoMetodo("Executando outro método")

def Aula8():
    def ManipulaDataHora():
        hoje = date.today()
        print("Hoje é: ", hoje)
        print("Partes da data: ", hoje.day, hoje.month, hoje.year)
        print("Número do dia da semana: ", hoje.weekday())
        dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]
        print("Nome abreviado do dia da semana: ", dias[hoje.weekday()])

        data = datetime.now()
        print("Data e hora: ", data)

        tempo = datetime.time(data)
        print("Hora atual: ", tempo)

def Aula9():
    def FormataDataHora():
        hoje = datetime.now()
        print(hoje.strftime("O ano é: %y"))
        print(hoje.strftime("Data e hora local: %c"))
        print(hoje.strftime("A hora atual é: %I:%M:%S %p"))

def Aula10():
    def deltaTempo():
        delta = timedelta(days=86, hours=8532, minutes= 7645)
        print(delta)

        hoje = datetime.now()
        print("Data no futuro: ", hoje + delta)
        print("Data no passado: ", hoje - delta)

def Aula11():
    def QuantosDiasFaltam(ano, mes, dia):
        hoje = date.today()
        dataProcurada = date(ano, mes, dia)

        qtoDias = dataProcurada - hoje

        mensagemRetorno = "Faltam " + str(qtoDias).replace("days, 0:00:00", "") + " dias para a data " + dataProcurada.strftime("%d/%m/%y")
        print(mensagemRetorno)

def Calendario():
    calendariotexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario = calendariotexto.formatmonth(2022,6)
    print(txtCalendario)