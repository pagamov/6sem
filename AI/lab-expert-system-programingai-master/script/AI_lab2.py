from pyknow import *

class PL(KnowledgeEngine):
    @Rule(OR(Fact('опыт программирования'), Fact('последовательность'), Fact('ручная работа с памятью')))
    def imperative(self):
        self.declare(Fact('императивный'))
        
    @Rule(OR(Fact('часто запускет программу'), Fact('быстрый код'), Fact('опыт работы с памятью и архитектурой'), 
           Fact('ручная работа с памятью'), Fact('опыт программирования')))
    def compilation(self):
        self.declare(Fact('компилируемый'))

    @Rule(OR(Fact('опыт работы с памятью и архитектурой'), Fact('ручная работа с памятью'), Fact('быстрый код')))
    def low_level(self):
        self.declare(Fact('низкий уровень'))
        
    @Rule(OR(Fact('нравится ставить условия'), Fact('первый язык программирования')))
    def logical(self):
        self.declare(Fact('логический'))
        
    @Rule(OR(Fact('первый язык программирования'), Fact('автоматическое очищение памяти'), Fact('не знает что такое терминал'),
          Fact('скорость разработки'), Fact('часто изменяет код')))
    def interpretable(self):
        self.declare(Fact('интерпретируемый'))

    @Rule(OR(Fact('автоматическое очищение памяти'),Fact('не знает что такое терминал'),
          Fact('скорость разработки'), Fact('прототипирование')))
    def high_level(self):
        self.declare(Fact('высокий уровень'))
    @Rule(OR(Fact('высокий уровень'), Fact('низкий уровень')))
    def high_or_low_level(self):
        self.declare(Fact('н/в уровень'))

    @Rule(Fact('низкий уровень'),
          Fact('компилируемый'),
          Fact('императивный'),
          Fact('многопоточность'), NOT(OR(
                Fact('высокий уровень'),
                Fact('интерпретируемый'),
                Fact('скрипты'),
                Fact('ООП'),
                Fact('кроссплатформенность'),
                Fact('сборщик мусора'),
                Fact('функциональный'),
                Fact('JIT'),
                Fact('логический'))))
    def C(self):
        self.declare(Fact(pl = 'C'))

    @Rule(Fact('низкий уровень'),
          Fact('компилируемый'),
          Fact('императивный'),
          Fact('многопоточность'),
          Fact('ООП'), NOT(OR(
                Fact('высокий уровень'),
                Fact('интерпретируемый'),
                Fact('скрипты'),
                Fact('кроссплатформенность'),
                Fact('сборщик мусора'),
                Fact('функциональный'),
                Fact('JIT'),
                Fact('логический'))))
    def Cpp(self):
        self.declare(Fact(pl = 'C++'))

    @Rule(Fact('н/в уровень'),
          Fact('компилируемый'),
          Fact('императивный'),
          Fact('многопоточность'),
          Fact('ООП'),
          Fact('кроссплатформенность'),
          Fact('сборщик мусора'), NOT(OR(
                Fact('интерпретируемый'),
                Fact('скрипты'),
                Fact('функциональный'),
                Fact('JIT'),
                Fact('логический'))))
    def CSharp(self):
        self.declare(Fact(pl = 'C#'))

    @Rule(Fact('н/в уровень'),
          Fact('компилируемый'),
          Fact('императивный'),
          Fact('многопоточность'),
          Fact('ООП'),
          Fact('кроссплатформенность'),
          Fact('сборщик мусора'),
          Fact('JIT'), NOT(OR(
                Fact('интерпретируемый'),
                Fact('скрипты'),
                Fact('функциональный'),
                Fact('логический'))))
    def Java(self):
        self.declare(Fact(pl = 'Java'))

    @Rule(Fact('высокий уровень'),
          Fact('интерпретируемый'),
          Fact('императивный'),
          Fact('скрипты'),
          Fact('ООП'),
          Fact('кроссплатформенность'),
          Fact('сборщик мусора'),
          Fact('функциональный'),
          Fact('JIT'), NOT(OR(
                Fact('интерпретируемый'),
                Fact('скрипты'),
                Fact('функциональный'),
                Fact('логический'))))
    def JS(self):
        self.declare(Fact(pl = 'JavaScript'))

    @Rule(Fact('н/в уровень'),
          Fact('компилируемый'),
          Fact('интерпретируемый'),
          Fact('скрипты'),
          Fact('ООП'),
          Fact('многопоточность'),
          Fact('сборщик мусора'), NOT(OR(
                Fact('кроссплатформенность'),
                Fact('функциональный'),
                Fact('императивный'),
                Fact('JIT'),
                Fact('логический'))))
    def Lisp(self):
        self.declare(Fact(pl = 'Lisp'))

    @Rule(Fact('высокий уровень'),
          Fact('интерпретируемый'),
          Fact('императивный'),
          Fact('скрипты'),
          Fact('ООП'),
          Fact('кроссплатформенность'),
          Fact('сборщик мусора'),
          Fact('многопоточность'),
          Fact('JIT'), NOT(OR(
                Fact('функциональный'),
                Fact('компилируемый'),
                Fact('низкий уровень'),
                Fact('логический'))))
    def Python(self):
        self.declare(Fact(pl = 'Python'))

    @Rule(Fact('низкий уровень'),
          Fact('компилируемый'),
          Fact('императивный'),
          Fact('многопоточность'),
          Fact('ООП'),
          Fact('функциональный'), NOT(OR(
                Fact('высокий уровень'),
                Fact('интерпретируемый'),
                Fact('скрипты'),
                Fact('кроссплатформенность'),
                Fact('сборщик мусора'),
                Fact('JIT'),
                Fact('логический'))))
    def FSharp(self):
        self.declare(Fact(pl = 'F#'))

    @Rule(Fact('высокий уровень'),
          Fact('логический'),
          Fact('сборщик мусора'),
          Fact('скрипты'),
          Fact('интерпретируемый'), NOT(OR(
                Fact('многопоточность'),
                Fact('компилируемый'),
                Fact('императивный'),
                Fact('низкий уровень'),
                Fact('ООП'),
                Fact('кроссплатформенность'),
                Fact('функциональный'),
                Fact('JIT'))))
    def Prolog(self):
        self.declare(Fact(pl = 'Prolog'))

    @Rule(Fact('н/в уровень'),
          Fact('компилируемый'),
          Fact('императивный'),
          Fact('многопоточность'),
          Fact('ООП'),
          Fact('скрипты'),
          Fact('функциональный'), NOT(OR(
                Fact('интерпретируемый'),
                Fact('кроссплатформенность'),
                Fact('сборщик мусора'),
                Fact('JIT'),
                Fact('логический'))))
    def Swift(self):
        self.declare(Fact(pl = 'Swift'))

    @Rule(Fact('низкий уровень'),
          Fact('компилируемый'),
          Fact('императивный'), NOT(OR(
                Fact('высокий уровень'),
                Fact('интерпретируемый'),
                Fact('скрипты'),
                Fact('ООП'),
                Fact('кроссплатформенность'),
                Fact('многопоточность'),
                Fact('сборщик мусора'),
                Fact('функциональный'),
                Fact('JIT'),
                Fact('логический'))))
    def asm(self):
        self.declare(Fact(pl = 'Assembler'))

    @Rule(Fact('низкий уровень'),
          Fact('интепретируемый'),
          Fact('скрипты'), NOT(OR(
                Fact('высокий уровень'),
                Fact('ООП'),
                Fact('императивный'),
                Fact('кроссплатформенность'),
                Fact('многопоточность'),
                Fact('сборщик мусора'),
                Fact('функциональный'),
                Fact('JIT'),
                Fact('логический'),
                Fact('компилируемый'))))
    def bash(self):
        self.declare(Fact(pl = 'Bash'))

    @Rule(Fact(pl = MATCH.a))
    def print_result(self,a):
          print('Язык программирования - {}'.format(a))
                    
    def factz(self,l):
        for x in l:
            self.declare(x)

ex1 = PL()
ex1.reset()
ex1.factz([
    Fact('опыт работы с памятью и архитектурой'), #input facts
          Fact('опыт программирования'),
          Fact('быстрый код')])
ex1.run()
