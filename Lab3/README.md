# Приложение для демонстрации работы базовых растровых алгоритмов
 
**Цель работы:**  
Закрепление теоретического материала и практическое освоение основных возможностей по использованию базовых алгоритмов растеризации отрезков и кривых:  
- Пошаговый алгоритм
- Алгоритм ЦДА (Цифровая Дифракционная Аппаратура)
- Алгоритм Брезенхема
- Алгоритм Брезенхема для окружности
- Алгоритм сглаживания

---

## Использованные средства разработки
- **Python**
- **Pygame**
- **PyQt5**

---

## Задачи работы
1. Создать поле для отображения растеризованного отрезка на экране.
2. Создать удобный и понятный пользовательский интерфейс.
3. Реализовать базовые растровые алгоритмы
   
---

## Сравнительная характеристика растровых алгоритмов рисования

### 1. Алгоритм Брезенхема для рисования линий
**Описание:**  
Алгоритм используется для отрисовки прямой линии между двумя заданными конечными точками.

**Преимущества:**  
- Быстрая и эффективная реализация (использует только целочисленное математическое округление).  
- Создает пиксели, максимально приближенные к идеальной линии.  

**Недостатки:**  
- Не подходит для рисования кривых или сложных фигур.

---

### 2. Алгоритм Брезенхема для рисования окружностей
**Описание:**  
Применяется для рисования окружностей и кругов на растровых экранах.

**Преимущества:**  
- Эффективен, основан на целочисленном округлении.  
- Обеспечивает высокую точность и быстрое выполнение.  

**Недостатки:**  
- Работает только с окружностями неизменной формы.

---

### 3. Алгоритм ЦДА (Цифровая Дифракционная Аппаратура)
**Описание:**  
Используется для рисования линий и кривых на основе градиентов.

**Преимущества:**  
- Может рисовать более сложные кривые (например, сплайны).  
- Использует дифференциацию для вычисления позиций пикселей, что улучшает качество.  

**Недостатки:**  
- Меньшая производительность по сравнению с алгоритмами Брезенхема.  
- Более сложная реализация из-за использования дробных чисел.

---

### 4. Алгоритм сглаживания (Anti-Aliasing)
**Описание:**  
Применяется для уменьшения эффектов ступенчатости (aliasing) и улучшения визуального представления линий и форм.

**Преимущества:**  
- Улучшает визуальное качество отрисовки за счет снижения артефактов.  
- Широко используется в компьютерной графике для реалистичности изображений.  

**Недостатки:**  
- Увеличивает вычислительную сложность.  
- Результаты зависят от настройки параметров.

---

### 5. Пошаговый алгоритм (Step by Step)
**Описание:**  
Пошаговый подход к рисованию линий, где пиксели выбираются шаг за шагом на основе направления и расстояния.

**Преимущества:**  
- Простота реализации, особенно для линий и простых форм.  
- Легко адаптируется для различных форм и размеров.  

**Недостатки:**  
- Неэффективен для сложных форм или линий.  
- Не всегда обеспечивает высокую точность и качество.

---

## Временные характеристики
**\*Диапазон x->[-33,33], y->[-33,33], r->[0,33]**

Параметры входных данных:  
- Для отрезка:  
  - `x0 = -33`, `y0 = -33`  
  - `x1 = 33`, `y1 = 33`  
- Для окружности:  
  - `x0 = 0`, `y0 = 0`, `r = 33`

| Алгоритм                           | Время отрисовки наклонной, мс | Время отрисовки горизонтали, мс | Время отрисовки вертикали, мс | Время отрисовки окружности, мс |
|------------------------------------|-------------------------------|---------------------------------|-------------------------------|----------------|
| Пошаговый алгоритм                 | 0.13                          | 0.12                            | 0.11                          |---             |
| Алгоритм ЦДА                       | 0.16                          | 0.15                            | 0.15                          |---             |
| Алгоритм Брезенхема                | 0.19                          | 0.12                            | 0.18                          |---             |
| Алгоритм Брезенхема для окружности | ---                           | ---                             | ---                           | 0.48           |
| Алгоритм сглаживания               | 0.24                          | 0.13                            | 0.11                          |---             |

---
## Скриншот приложения
![image](https://github.com/user-attachments/assets/7bac2a27-f6e9-4ef0-ace6-871625de0a0b)

## Заключение
1. Алгоритмы Брезенхема идеально подходят для рисования горизонтальных и вертикальных линий и окружностей благодаря высокой производительности.
2. Алгоритм ЦДА более гибкий и подходит для рисования сложных кривых, но требует больше вычислительных ресурсов.
3. Алгоритмы сглаживания значительно улучшают визуальное качество, но увеличивают вычислительную сложность.
4. Пошаговые алгоритмы просты в реализации, но менее точны и производительны.

**Вывод:**  
Выбор алгоритма зависит от конкретной задачи, требований к производительности и качеству графики.
