#!/bin/bash

if [ -f "$1" ]; then
  echo "Это файл."
elif [ -d "$1" ]; then
  echo "Это директория."
else
  echo "Файл или директория не найдены."
fi