## Optumall App Django-Rest-Framework

**Yuklab Olish**
```
git clone https://github.com/dilmurod1701/Optumall.git

```
**Foydalanish**
```
 pip install -r requirements.txt
```
**Dasturni Ishlatish**
  * Dasturni pasdagi komandani terminal bilan ishga tushuring: 
```
python manage.py runserver
```


**Dasturni Boshqarish**

- `GET/` :  http://127.0.0.1:8000/api/products - Barcha mahsulotlarni ko'rish uchun
- `Get / Post` :   http://127.0.0.1:8000/api/new - Yangi mahsulot qo'shish
- `Put / Patch` :  http://127.0.0.1:8000/api/<int:pk>/update - Mahsulotlarni id bo'yicha yangilash
- `Get/` :   http://127.0.0.1:8000/api/category/<str:name> - Mahsulotlarni Category bo'yicha qidirish
- `Get/` : http://127.0.0.1:8000/api/search/<str:title> - Mahsulotlarni Title bo'yicha qidirish
- `Delete/` :  http://127.0.0.1:8000/api//api/product/<id>/delete - Mahsulotlarni ochirish 
- `GET/` :  http://127.0.0.1:8000/api/user/<username>  - Foydalanuvchi ma'lumotlari
- `Put / Patch` :  http://127.0.0.1:8000/api/user/<username>/update  -  Foydalanuvchi ma'lumotlarini yangilash
  
