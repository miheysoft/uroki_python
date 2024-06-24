#!/bin/bash 

operation="$1"

case "$operation" in
    "-i")
        rclone sync --delete-after yandex:/python ~/Документы/python
        ;;

    "-o")
        rclone sync --delete-after ~/Документы/python yandex:/python
        ;;
    *)
        echo "Указана недопустимая опция"
        exit 1
        ;;
    esac

#rclone sync --delete-after yandex:/ci /media/usb/mega/ci
#rclone sync --delete-after yandex:/работа/works /media/usb/mega/работа/works
#rclone sync --delete-after ~/Документы/обмен/михеев yandex:/работа/works/михеев
