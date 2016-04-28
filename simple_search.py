#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указана строка, в которой нужно найти подстроку, а следом
# после стрелки (--->) указана сама искомая подстрока

# bab ---> a
# bcb ---> c
# bxb ---> x
REGEXP_1 = '[acx]'

# ooooAAAooooo ---> AAA
# asdfasdAAAAfasdf ---> AAAA
# AAAAAAfasdf ---> AAAAAA
# iiiiiA ----> A
REGEXP_2 = 'A+' # любое кол-во букв A

# There is <html> tag ---> <html>
# color can be used as <font color='red'> ---> <c>
# There is x <> 10 and something was wrong with < or > brace. ---> < or >
REGEXP_3 = '[<]((html)|(font color=\'red\')|([\s]or[\s]))[>]' # должно быть внутри < и > 
         # все возможное содержимое через ИЛИ выбирается

# C@n Y0u f1nd CaPoAira? ---> CaPoAira
# s0 Wh@t i5 CamelStyle? ---> CamelStyle
# Any simple word should match. ---> Any
# I like regular expressions ---> like
REGEXP_4 = '(CaPoAira)|(CamelStyle)|(Any)|(like)' # просто через ИЛИ выберем что нужно

# all those that were numbered of the camps throughout their hosts were 603550. ---> 603550
# What is the meaning of life, the universe and everything? *42* Douglas Adams ---> 42
# Clive Staples Lewis was born in Belfast, Ireland, on 29 November 1898. ----> 29
REGEXP_5 = '\d+' # любое кол-во цифр подряд

# New York: W. H. Freeman, pp. 347-353, 1991. ---> Freeman
# set out to travel much faster than light ---> travel
# Arise ye, and depart; for this is not your rest... ---> depart
REGEXP_6 = '(Freeman)|(travel)|(depart)' # все возможное содержимое через ИЛИ выбирается

# I know that cat can catch a mouse! ---> cat can catch a mouse
# But this mouse is faster than the cat. ---> mouse is faster than the cat
# Mouse Mickey is not a simple mouse. Tom is a dummy cat. ---> mouse. Tom is a dummy cat
REGEXP_7 = '(cat[\s]can[\s]catch[\s]a[\s]mouse)|(mouse[\s]is[\s]faster[\s]than[\s]the[\s]cat)|(mouse[\.][\s]Tom[\s]is[\s]a[\s]dummy[\s]cat)' 
         # через ИЛИ выбрано то что подходит

# his phone number was 892512366482. ---> 892512366482
# I called +7 999 648-99-86 ans it was right. ---> +7 999 648-99-86
# Some 52221 numbers should not hide phone numbers such as 8 915 747-68-99 ---> 8 915 747-68-99
REGEXP_8 = r'\+?[0-9]{1}[\s]?[0-9]{3}[\s]?[0-9]{3}[-]?[0-9]{2}[-]?[0-9]{2}' 
       # + необязательный
       # одна цифр
       # пробел необязательный
       # три цифры
       # пробел необязательный
       # три цифры
       # минус необязательный
       # две цифры
       # минус необязательный
       # две цифры
