#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указаны строки, соответствующие этому выражению (они отмечены знаком +),
# а также строки, не соответствующие этому выражению (отмечены знаком -)

# + a
# + ab
# - b
# - ba
REGEXP_1 = '^[a]{1}[b]?'  # в начале строки д.б. a обязательно потом b необязательно

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = '^[a][abc][b]$' # в начале строки a потом a или b или c потом b

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = '^sofia\.mp[34]$'  # точка экранирована конструкцией \. для цифр варианты 3 или 4

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = '^(taverna)|(versus)|(vera)|(zveri)$' # простое ИЛИ

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = '^[a|b]{3}$' # три повтора одной из букв a b

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = '^(Ok|ab){3}$' # три повтора одной из фраз Ok или ab

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = '(aaa\sAaa\saaa)|(aaa\saaa\sAaa)|(Aaa\saaa\saaa)'  # пробел записывается \s

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = '^a(bc|bc03|-b-c-3|\.b\.c\.0)$' # точка записана \.
