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

## Скриншот

![Скриншот](Screenshot.png)

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


![screenshot](./Screenshot.png)

