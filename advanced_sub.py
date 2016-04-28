#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указана строка, в которой нужно выполнить замену, а следом
# после стрелки (--->) указан результат замены

# aAc   ---> a!A!c
# aZc   ---> a!Z!c
# aZZc  ---> a!Z!!Z!c
# aBaCa ---> a!B!a!C!a
REGEXP_1 = '(A|Z|B|C)'   # создадим группу №1 - это A или Z или B или C
REGEXP_1_REPL = r'!\1!' # выражение для замены !(группа№1)!  - группа вызывается \№группы

# abc    ---> abc
# abbc   ---> abc
# azzzc  ---> azc
# arrrrc ---> arc
# xxxxxx ---> x
REGEXP_2 = r'(b|z|r|x)\1+'   # любое кол-во повторов одного символа из группы
REGEXP_2_REPL = r'\1'        # заменим на один символ

# this is text         ---> this is text
# this is is text      ---> this *is* text
# this is is is text   ---> this *is* text
# this is text text    ---> this is *text*
# this is is text text ---> this *is* *text*
REGEXP_3 = r'\b(is|text)([\s]\1)([\s]\1)?' # нужно взять с начала слова (\b) два или три 
                                        #повтора слова из группы (is|text)
REGEXP_3_REPL = r'*\1*'  # и заменить на обрамленное *слово*

# one two three ---> two one three
# dog cat wolf  ---> cat dog wolf
# goose car rat ---> goose rat car
REGEXP_4 = '(?P<group1>one|dog|car) (?P<group2>two|cat|rat)' # найти допустимые последовательности из 2-х
REGEXP_4_REPL = '\g<group2> \g<group1>'  # и поменять местами

# cat dog                     ---> cat dog
# cat dog cat                 ---> cat dog cat
# dog cat dog cat cat         ---> dog dog
# dog wolf dog rat rat wolf wolf ---> dog dog rat rat
REGEXP_5 = r'(?P<group1>cat|wolf)[\s](?P<group2>dog([\s]rat[\s]rat)?)[\s]\1[\s]\1' # группу№1 выбросим,
                          # если она встретится 3 раза по схеме (1) (2) (1) (1)
                          # группа 2 хитрая: dog 
                          #            или   dog rat rat
REGEXP_5_REPL = r'\2'
