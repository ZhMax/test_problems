#!/bin/bash

#Директория, где находится файл, содержащий уникальные слова
dir1=`dirname $1`
#Директория, где будут созданы файлы
dir2=$2


cd $dir1

#Имя файла, содержащего уникальные слова
file_name=`basename $1`
file_name_copy=`basename $1 .txt`
file_name_copy=$file_name_copy"_copy.txt"

#Удаление цифр из файла
sed 's/[^a-z]//g' $file_name > $file_name_copy

#Удаление символа переноса строки
sed -i -z 's/\n/ /g' $file_name_copy

#Сохранение файла в переменную
file_str=`cat dracula_unique_words_copy.txt`

#Преобразование строки в массив
read -r -a array_unique_words <<< $file_str
echo "Number of unique words in the text file: ${#array_unique_words[@]}"

#Определение количества слов в массиве
length=${#array_unique_words[@]}
if [[ $length -gt 10 ]]; then
	length=10
fi

#Цикл по элементам массива для создания файлов
for (( i=0; i<$length; i++ ));
do
	touch "$dir2/${array_unique_words[$i]}_$i"
done

rm $file_name_copy