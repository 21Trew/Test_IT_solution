import cv2
import numpy as np

# Функция для создания видео с бегущей строкой
def create_hire_video_opencv():
    # Текст поздравления
    hire_message = "Thank you for hiring me! :)"

    # Размеры видео (ширина x высота)
    width, height = 1920, 1080

    # Задаём параметры - видеопоток с частотой 24 кадра в секунду
    out = cv2.VideoWriter("C:/Python/projects/hire_video_opencv.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 60, (width, height))

    # Создаем кадр с черным фоном
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Начальные координаты для бегущей строки
    x, y = width, height // 2

    # Установим параметры шрифта
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2.5
    font_thickness = 4
    font_color = (255, 255, 255)  # Белый цвет текста

    # Пройдемся по каждому кадру
    for t in range(180):  # 3 секунды с частотой 60 кадра/сек
        # Очистка кадра
        frame.fill(0)

        # Новые координаты для бегущей строки
        x -= 15  # Скорость бегущей строки

        # Вот тут добавим текст
        cv2.putText(frame, hire_message, (x, y), font, font_scale, font_color, font_thickness)

        # Тут запишем кадр
        out.write(frame)

    # Закроем тут видеопоток
    out.release()

# Создаём видео 
create_hire_video_opencv()