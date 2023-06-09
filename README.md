# Код для решения трех тестовых задач


### Первое задание

Решение первого задания находится в папке: `problem_1_time_series`.
  
Код находится в jupyter notebook: `rocket_classification.ipynb`.  
Папка `datasets` содержит dataset Ham, используемый для решения.  


### Второе задание

Решение второго задания находится в папке: `problem_2_graphs`.

В папке `usermodules` находится модуль, состоящий из файла `usermodule_graph.py`, который содержит    
реализацию класса `GraphClass` для создания графов.

Данный класс включает в себя требуемые методы:

- добавление узла с какой-то информацией;
- добавление ребра между двумя узлами;
- генерация случайного графа;
- отрисовка получившегося графа с matplotlib.

В файле `problem2_1_create_graph.py`
находится код для демонстрации возможностей написанного модуля.

В файле `problem2_2_friends_graph.py`
находится код для решения второй задачи о поиске максимального
количества друзей, которые были бы не в ссоре друг с другом.
Решение задачи выполняется с использование модуля, для построения графов.

Файл `names.txt` содержит мужские и женские имена, чтобы можно было
автоматически генерировать графы, описывающие взаимоотношения между
друзьями.

В папке `results` находятся результаты решения задачи, полученные 
для различных графов.
Текстовые файлы `.txt` хранят информацию о списке смежности графа
и ответ, состоящий из списка друзей, которых можно позвать на пикник.
Графические файлы `.png` хранят изображения графа и раскраску его вершин,
построенную так, что любые две смежные вершины окрашены в разные цвета.


### Третье задание

Решение третьего задания находится в папке: `problem_3_docker_linux`.

Файл `script_for_words_count.sh` содержит скрипт
для подсчета того, сколько раз каждое слово встрачается
в текстовом файле.

Файл `script_for_files_creation.sh` содержит скрипт
для создания файлов с именами, соответсвующими 10
самым встречаемым словам в тексте.

Файл `dracula_unique_words.txt` содержит результат подсчета
того сколько раз каждое слово встречается в тексте 
https://github.com/benbrandt/cs50/blob/master/pset5/texts/dracula.txt

В файле `commands_to_run_scripts.txt` находятся небольшие пояснения к
тому, как были запущены скрипты. 
