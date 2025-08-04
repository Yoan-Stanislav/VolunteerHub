# VolunteerHub

VolunteerHub е уеб приложение за управление на доброволчески инициативи и събития. Проектът е разработен с Django, Bootstrap и PostgreSQL. Подходящ е за НПО-та, училища и университети, които искат лесно да организират доброволци, събития и кандидатури.

---

## Функционалности

- 🔑 Регистрация и вход за потребители (доброволци и организации)
- 📅 Създаване, редакция и изтриване на събития
- 📝 Кандидатстване за участие в събития
- 🏢 Управление на организации и локации
- 📄 Административен панел с custom функционалности
- 📱 Responsive дизайн (Bootstrap)
- ✅ Валидация на форми и custom error handling
- 🔒 Сигурност: защита на данни, CSRF, rate limiting
- 🧪 Покритие с unit тестове
- 🌐 REST API (базов)
- ⚡ Middleware за логване на грешки и custom 404/500 страници

---


## Визуализации на основните екрани

## Преглед на платформата VolunteerHub

### Регистрация на потребител
![Регистрация](Screenshot3.png)  
*Форма за регистрация на нов доброволец с проверки.*

### Вход в платформата
![Вход](Screenshot4.png)  
*Екран за вход с име и парола.*

### Моят профил
![Моят профил](Screenshot5.png)  
*Детайли за профила и възможност за редакция.*

### Начална страница
![Начална страница](Screenshot6.png)  
*Начален екран със списък на събития.*

### Моите събития
![Моите събития](Screenshot7.png)  
*Таблица с всички събития, в които участваш.*

### Свържи се с нас
![Свържи се с нас](Screenshot8.png)  
*Форма за контакт с екипа.*

### Всички събития
![Всички събития](Screenshot9.png)  
*Преглед на всички събития в платформата.*

### Админ панел (Django admin)
![Админ панел](Screenshot1.png)  
*Достъп до административния панел на Django.*

### REST API (Event List)
![API – Event List](Screenshot2.png)  
*Списък на събитията през Django REST Framework API.*


---

## Инсталация

```bash
git clone https://github.com/Yoan-Stanislav/VolunteerHub.git
cd VolunteerHub
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env       # Попълни променливите!
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
# VolunteerHub

## Какво е това?
Уеб приложение за доброволчески инициативи.

## Как се стартира?
1. Клонирай репото.
2. `pip install -r VolunteerHub/requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`
5. Достъп през [localhost:8000](http://localhost:8000)



