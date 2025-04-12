# Django Loyiha O'rnatish Qo'llanma (README.md)

```markdown
# Django Web Loyihasi - O'rnatish Qo'llanma

## Dastlabki talablar
- Python 3.8+ o'rnatilgan bo'lishi kerak
- Pip paket menejeri yangilangan bo'lishi kerak

## 1. Loyihani klonlash
```bash
git clone <loyiha-manzili>
cd <loyiha-nomi>
```

## 2. Virtual muhit yaratish va faollashtirish
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

## 3. Kerakli kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

## 4. Ma'lumotlar bazasi sozlamalari
```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Superuser yaratish (admin panel uchun)
```bash
python manage.py createsuperuser
```

## 6. Statik fayllarni yig'ish
```bash
python manage.py collectstatic
```

## 7. Loyihani ishga tushirish
```bash
python manage.py runserver
```

## 8. Test ishlatish
```bash
python manage.py test
```

## Muhim fayllar va kataloglar
- `/venv` - Virtual muhit
- `/static` - Statik fayllar
- `/templates` - HTML shablonlar
- `requirements.txt` - Kerakli kutubxonalar ro'yxati

## Yordam
Agar muammo yuzaga kelsa, quyidagilarni tekshiring:
1. Virtual muhit faolligiga ishonch hosil qiling
2. `pip freeze` va `requirements.txt` faylidagi kutubxonalar mosligini tekshiring
3. Ma'lumotlar bazasi migratsiyalarini qayta ishga tushiring

Loyiha muvaffaqiyatli ishga tushdi! Endi brauzeringizda http://localhost:8000 manzilini oching.
```

Bu README.md fayliga loyihani ishga tushirish uchun zarur bo'lgan barcha komandalar kiritilgan. Uni loyiha ildiz katalogiga joylashtiring.