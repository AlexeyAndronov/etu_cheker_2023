# etu_cheker_2023

 Программа загрузки и обработки данных с сайта "ЛЭТИ" для автоматического формирования списка поступивших, с учетом приоритетов.
 Никаких гарантий, что работает правильно.

Алгоритм:

С сайта подгружаются текущие списки с приоритетами и проверкой, что подан оригинал. 
После этого формируется список абитуриентов и сводная таблица приоритетов по специальностям.
Далее начинается вычеркивание, от большего балла к меньшему.

Как только заканчиваются места на специальности, рассматривается следующий приоритет.
Если приоритеты закончились - выводится соответствующая запись.

Результаты (списки поступивших) формируются в БД в таблице superlist.
