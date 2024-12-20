# Приложение для обработки и сжатия изображений

## Введение

В данном проекте разработано приложение для обработки изображений с использованием языка программирования Python и библиотек OpenCV и Tkinter. Приложение реализует различные методы обработки изображений и алгоритмы сжатия графической информации. Основные функции включают линейное контрастирование, пороговую обработку и сжатие изображений в формате JPEG.

## Цели и задачи проекта

Целями проекта являются:
- Реализация алгоритмов обработки изображений.
- Реализация методов сжатия графической информации.
- Создание удобного графического интерфейса для пользователя.

Задачи, поставленные в рамках проекта:
1. Разработка интерфейса для загрузки и отображения изображений.
2. Реализация методов обработки изображений, таких как:
   - Линейное контрастирование.
   - Простая и адаптивная пороговая обработка.
   - Поэлементные операции (сложение, вычитание, умножение, деление).
3. Реализация функции сжатия изображений с возможностью выбора качества.
4. Подбор базы изображений для тестирования с различными характеристиками.

## Графический интерфейс

Интерфейс приложения выполнен с использованием библиотеки Tkinter. Он включает следующие элементы:
- Кнопка для загрузки изображения.
- Кнопки для применения различных методов обработки.
- Поля для ввода значений, необходимых для поэлементных операций и настройки качества JPEG.
- Поля для отображения загруженного и обработанного изображений.

### Скриншот интерфейса

![image](https://github.com/user-attachments/assets/4ff0ce65-4fd8-43f5-ab5b-6a47a787b1e5)



## Методы обработки изображений

### 1. Линейное контрастирование
Метод увеличивает контраст изображения, что позволяет улучшить его визуальное восприятие.

### 2. Пороговая обработка
- **Простая пороговая обработка**: Применяется фиксированный порог для преобразования изображения в черно-белое.
- **Адаптивная пороговая обработка**: Использует методы адаптивной обработки, которые учитывают локальные характеристики изображения.

### 3. Поэлементные операции
Позволяют производить математические операции над изображениями, такие как:
- Сложение
- Вычитание
- Умножение
- Деление

## Алгоритмы сжатия изображений

Приложение реализует метод сжатия изображений в формате JPEG. Пользователь может задать коэффициент качества сжатия в диапазоне от 0 до 200, что позволяет управлять компромиссом между качеством изображения и размером файла.

## База изображений для тестирования

Для тестирования были подобраны изображения с различными характеристиками:
- **Зашумленные изображения**: Используются для проверки устойчивости методов к шуму.
- **Размытие**: Проверяет, как методы обрабатывают размытые изображения.
- **Малоконтрастные изображения**: Проверяет эффективность контрастирования.

## Результаты и выводы

Приложение успешно реализует заданные методы обработки и сжатия изображений. Оно позволяет пользователю легко загружать, обрабатывать и сохранять изображения. База тестовых изображений подтверждает эффективность примененных методов.

## Заключение

Разработка приложения для обработки и сжатия изображений является важной задачей, которая находит применение в различных областях, включая фотографию, веб-дизайн и графику. В рамках данного проекта были достигнуты поставленные цели и реализованы основные функции, что позволяет с уверенностью утверждать о его успешности.


