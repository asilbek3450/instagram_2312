# Django Loyihasi

Bu Django asosidagi INSTAGRAM veb-ilovasi bo'lib, foydalanuvchi hikoyalari, postlari va ularning faoliyatlarini boshqarish uchun mo'ljallangan. Loyihada JWT autentifikatsiyasi, postlar va hikoyalar uchun CRUD amallari va media fayllarni yuklashni qo'llab-quvvatlash mavjud.

## Xususiyatlar

- **JWT Autentifikatsiya**: Ro'yxatdan o'tish, tizimga kirish va foydalanuvchi profilini yangilash.
  - **Postlar Boshqaruvi**: Post yaratish, o'qish, yoqtirish va izohlar qoldirish.
  - **Hikoyalar Boshqaruvi**: Hikoyalar yaratish, ko'rish, yoqtirish va hikoya ko'rishlarining hisobini yuritish.
  - **Media Yuklash**: Postlar va hikoyalar uchun rasmlar yuklash va boshqarish.
  - **Swagger API Hujjatlari**: `drf_yasg` yordamida avtomatik ravishda interaktiv API hujjatlari.

## Talablar

- Python 3.9+
  - Django 5.2+
  - Django REST Framework
  - PostgreSQL (yoki boshqa ma'lumotlar bazasi)
  - `drf_yasg` API hujjatlarini yaratish uchun
  - `Pillow` - rasmni boshqarish uchun

## O'rnatish

### 1-qadam: Repozitoriyani klonlash

```bash
git clone https://github.com/asilbek3450/instagram_2312.git
cd repo-nomi

# 📱 Instagramga o‘xshash Django loyihasi

Ushbu loyiha Django, DRF (Django REST Framework) va JWT (JSON Web Token) asosida yaratilgan bo‘lib, foydalanuvchilar ro‘yxatdan o‘tishi, post va story joylashi, like va comment qilish imkoniyatiga ega.

---

## 🛠 Loyiha uchun kerakli modullar

Quyidagi buyruqlar orqali kerakli kutubxonalarni o‘rnating:

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install drf-yasg
pip install Pillow
```

YOKI 

```
pip install -r requirements.txt
```
