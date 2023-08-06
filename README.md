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


** Подготовка к запуску **

1. Создание БД.
   Назовите ее etu

2. Создайте в ней все таблицы

CREATE TABLE public.abitur (
	code varchar NOT NULL,
	maxpoint int2 NULL,
	CONSTRAINT abitur_pk PRIMARY KEY (code)
);

CREATE TABLE public.speciality (
	code varchar NOT NULL,
	title varchar NULL,
	url varchar NULL,
	max_abitur int4 NULL,
	CONSTRAINT speciality_pk PRIMARY KEY (code)
);

CREATE TABLE public.superlist (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	spec_id varchar NULL,
	abitur_id varchar NULL,
	"position" int4 NULL,
	points int4 NULL,
	CONSTRAINT superlist_pk PRIMARY KEY (id)
);


CREATE TABLE public.priority (
	id int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	abitur_id varchar NULL,
	speciality_id varchar NULL,
	priority int2 NULL,
	CONSTRAINT newtable_pk PRIMARY KEY (id),
	CONSTRAINT newtable_fk FOREIGN KEY (abitur_id) REFERENCES public.abitur(code),
	CONSTRAINT newtable_fk_1 FOREIGN KEY (speciality_id) REFERENCES public.speciality(code)
);

3. Установите зависимости из req.txt
4. Запустите файл main.py

На экране смотреть не удобно, там только для справки все выводится.
Потом просто смотрите таблицу superlist в БД - там будут все списки с кодами абитуриентов. 

