#!/bin/bash
#Скрипт для подсчета уникальных слов в файле, путь к которому задается $1
#Результат сохраняется в директорию $2

dir1=`dirname $1`
dir2=$2
cd $dir1

file_name=`basename $1`
file_name_copy=`basename $1 .txt`
file_name_copy=$file_name_copy"_copy.txt"
cp -f $file_name $file_name_copy

#Удаление пустых строк
sed -i -r '/^\s*$/d' $file_name_copy

#Привидение символов к нижнему регистру
sed -i 's/[A-Z]/\L&/g' $file_name_copy

#Удаление лишних символов
sed -i "s/'s//g" $file_name_copy
sed -i 's/[^a-z ]//g' $file_name_copy

#Удаление символа новой строки
sed -i -z 's/\n/ /g' $file_name_copy
#Запись файла в переменную
file_str=`cat $file_name_copy`

#Преобразование строки в массив
read -r -a array <<< $file_str
echo "Number of words in the text file: ${#array[@]}"

#Массив уникальных слов
IFS=' ' read -r -a array_unique_words <<< "$(echo "${array[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' ')"
echo "Number of unique words in the text file: ${#array_unique_words[@]}"

#Создание файла для хранения уникальных слов
file_name_unique_words=`basename $1 .txt`
file_name_unique_words=$file_name_unique_words"_unique_words.txt"
echo '' > "$file_name_unique_words"

#Цикл по уникальным словам, который подсчитывает повторение каждого слова
#в файле $file_name_copy, содержащий весь текст в виде строки
length=${#array_unique_words[@]}
#$length
for (( i=0; i<$length; i++ ));
do	
	#определяем длину каждого слова, чтобы исключить короткие слова
	word_length=`echo "${array_unique_words[$i]}" | wc -c`
	if [[ $word_length -gt 2 ]]; then
		#подсчет повторений слова ${array_unique_words[$i]} в $file_name_copy
		word_count=`grep -o -w "${array_unique_words[$i]}" $file_name_copy | wc -w`
		#запись слова и полученного числа в файл
		echo "${array_unique_words[$i]} $word_count" >> "$file_name_unique_words"
	fi
done

#сортировка уникальных слов по количеству повторений
sort -nr -k 2 $file_name_unique_words -o $file_name_unique_words
#вывод на экран топ 20 слов
sed -n '1,20p' $file_name_unique_words

#Перемещение файла в нужную директорию
mv $file_name_unique_words "$dir2/$file_name_unique_words"

rm $file_name_copy
