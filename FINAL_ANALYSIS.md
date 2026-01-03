# التحليل النهائي - DocTypes التي تحتاج أزرار Export/Set Module

## المعيار الأساسي

**نضيف الأزرار فقط للـ DocTypes التي:**

-   ✅ **ليس لديها تصدير تلقائي** في `on_update()` أو `before_save()` للموديول المحدد
-   ❌ **لديها تصدير تلقائي** → لا تحتاج أزرار

---

## التحليل التفصيلي

### ✅ DocTypes التي تحتاج أزرار (لا يوجد تصدير تلقائي)

| DocType      | التحليل                                                                   | الكود                    | النتيجة            |
| ------------ | ------------------------------------------------------------------------- | ------------------------ | ------------------ |
| **Web Page** | ❌ لا يوجد `on_update()` مع `export_module_json()` أو `export_to_files()` | لا يوجد في `web_page.py` | ✅ **تحتاج أزرار** |

---

### ❌ DocTypes التي لا تحتاج أزرار (لديها تصدير تلقائي)

| DocType             | طريقة التصدير          | الموقع          | شروط التصدير                          |
| ------------------- | ---------------------- | --------------- | ------------------------------------- |
| **Page**            | `export_module_json()` | `on_update()`   | `standard="Yes"` + `developer_mode`   |
| **Report**          | `export_doc()`         | `on_update()`   | دائماً في `developer_mode`            |
| **Dashboard**       | `export_to_files()`    | `on_update()`   | `is_standard=True` + `developer_mode` |
| **Dashboard Chart** | `export_to_files()`    | `on_update()`   | `is_standard=True` + `developer_mode` |
| **Form Tour**       | `export_to_files()`    | `on_update()`   | `is_standard=True` + `developer_mode` |
| **Number Card**     | `export_to_files()`    | `on_update()`   | `is_standard=True` + `developer_mode` |
| **Workspace**       | `export_to_files()`    | `on_update()`   | `public=True` + `developer_mode`      |
| **Notification**    | `export_module_json()` | `on_update()`   | `is_standard=True` + `developer_mode` |
| **Print Format**    | `export_module_json()` | `on_update()`   | `standard="Yes"` + `developer_mode`   |
| **Web Form**        | `export_module_json()` | `on_update()`   | `is_standard=True` + `developer_mode` |
| **Website Theme**   | `export_doc()`         | `on_update()`   | `custom=False` + `developer_mode`     |
| **Web Template**    | `export_to_files()`    | `before_save()` | `standard=True` + `developer_mode`    |

---

## الخلاصة النهائية

### ✅ DocTypes التي يجب الاحتفاظ بها (تحتاج أزرار)

1. **Web Page** - ✅ الوحيد الذي يحتاج أزرار

### ❌ DocTypes التي يجب إزالتها (لديها تصدير تلقائي)

يجب إزالة الأزرار والملفات الخاصة بـ:

1. **Page** ❌
2. **Report** ❌
3. **Dashboard** ❌
4. **Dashboard Chart** ❌
5. **Form Tour** ❌
6. **Number Card** ❌
7. **Workspace** ❌
8. **Notification** ❌
9. **Print Format** ❌
10. **Web Form** ❌
11. **Web Template** ❌
12. **Website Theme** ❌

---

## ملاحظات مهمة

### Web Template

```python
def before_save(self):
    if frappe.conf.developer_mode:
        if self.standard:
            self.export_to_files()  # ← تصدير تلقائي
```

-   **لديها تصدير تلقائي** في `before_save()` عندما `standard=True`
-   لا تحتاج أزرار

### الفرق بين التصدير التلقائي واليدوي

-   **التصدير التلقائي**: يحدث تلقائياً عند الحفظ (في `on_update()` أو `before_save()`)
-   **التصدير اليدوي**: يحتاج ضغط زر (في تطبيقنا يصدر إلى `fixtures/`)

حتى لو كان التصدير التلقائي يصدر إلى `{module}/{doctype}/` واليدوي يصدر إلى `fixtures/`، المستخدم قال بوضوح: **"الملفات التي ترحل تلقائياً للموديول المحدد عند الحفظ تلقائياً لا داعي لعمل أزرار لها"**

---

## الإجراء المطلوب

1. ✅ **الاحتفاظ بـ**: Web Page فقط
2. ❌ **إزالة**: جميع DocTypes الأخرى (12 DocType)
