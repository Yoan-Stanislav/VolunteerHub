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


## 📸 Демонстрация на VolunteerHub

### 1. Регистрация на нов потребител
![Регистрация](Screenshot1.png)
> Потребителят въвежда своите данни, за да си направи нов профил.

---

### 2. Вход в профила
![Вход](Screenshot2.png)
> Влизане с потребителско име и парола.

---

### 3. Начална страница след вход
![Начало](Screenshot3.png)
> Посреща те "Добре дошли във VolunteerHub!" и може да разгледаш всички събития.

---

### 4. Моят профил
![Моят профил](Screenshot4.png)
> Виждаш имейл, телефон, дата на раждане и умения.

---

### 5. Моите събития
![Моите събития](Screenshot5.png)
> Таблица с всички събития, които си създал – можеш да ги редактираш, триеш или разглеждаш детайли.

---

### 6. Всички събития
![Всички събития](Screenshot6.png)
> Пълен списък на всички доброволчески събития във платформата.

---

### 7. Свържи се с нас
![Свържи се с нас](Screenshot7.png)
> Форма за контакт с екипа на сайта.

---

### 8. Django Admin панел
![Django Admin](Screenshot8.png)
> Пълен административен контрол върху всички модели и данни.

---

### 9. REST API събития
![REST API](Screenshot9.png)
> Преглед и работа с API-то за събития през Django REST Framework.

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



