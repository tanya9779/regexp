#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указана строка, в которой нужно выполнить замену, а следом
# после стрелки (--->) указан результат замены

# bab ---> bzb
# bcb ---> bzb
# bxb ---> bzb
REGEXP_1 = '[acx]'    # один из символов a c x меняем
REGEXP_1_REPL = 'z'   # на z

# abcXYZabc   ---> abcabc
# XaYbZcWaM   ---> abca
# abc XYZabc  ---> abc abc
REGEXP_2 = '[A-Z]'   # если встретим Большие буквы A - Z
REGEXP_2_REPL = ''   # удалим их

# abcABCabc  ---> abcABCabc
# DaEbFcAaB  ---> abcAaB
# abcXYZabc  ---> abcXYZabc
# XaYbZcZaY  ---> XaYbZcZaY
# DXEYFZabc  ---> XYZabc
# ADBECFXYZ  ---> ABCXYZ
REGEXP_3 = '[D-F]'   # если встретим Большие буквы D - Z
REGEXP_3_REPL = ''   # удалим их

# abc0abc   ---> abcabc
# 1a2b3c4   ---> abc
# a123!@#bc ---> abc
REGEXP_4 = '[^a-z]' # если встретим все кроме маленьких букв
REGEXP_4_REPL = ''  # удалим их

# a,b,c d,e,f      ---> a_b_c_d_e_f
# abc!@#a          ---> abc___a
# abc!@#,./abc abc ---> abc______abc_abc
REGEXP_5 = '[^a-z]'  # если встретим все кроме маленьких букв
REGEXP_5_REPL = '_'  # заменим на _

# a abc aa bb  ---> a aa bb
# a def dd fd  ---> a dd fd
# x xy xyz yz  ---> x xy yz
# x xyz xyz yz ---> x yz
REGEXP_6 = '[a-z]{3}[\s]'      # если встретим тройки из букв
REGEXP_6_REPL = ''             # удалим их

# AabcdZ ---> abcd
# BabcdC ---> BabcdC
# aAbZcd ---> aAbZcd
# AabcdY ---> abcdY
# BabcdZ ---> Babcd
REGEXP_7 = '(^A)|(Z$)'   # если встретим A в начале строки или Z в конце строки
REGEXP_7_REPL = ''       # удалим их

# a b c  ---> a b c
# a  b c ---> a b c
# d    f ---> d f
REGEXP_8 = '[\s]{2,}'    # если встетим более 1 пробела подряд
REGEXP_8_REPL = ' '      # заменим на один пробел

# a ab abc abcd ab ---> a ab ab
# a xyz xyz a      ---> a a
# d xy xyza a      ---> d xy a
# a xyzzy b        ---> a xyzzy b
REGEXP_9 = '[\s]([a-z]{3,4}[\s])+'    # слова из трёх или четырех букв
REGEXP_9_REPL = ' '                   # удалим
