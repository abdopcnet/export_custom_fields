# تحليل DocTypes مع حقل Module

## ملخص DocTypes

من فحص كود Frappe، هذه هي النتائج:

### 1. DocTypes مع تصدير تلقائي (Auto-export في on_update)

هذه DocTypes **لديها تصدير تلقائي** ولا تحتاج إلى تصدير يدوي:

| DocType                    | طريقة التصدير          | شروط التصدير                          | ملفات إضافية                             |
| -------------------------- | ---------------------- | ------------------------------------- | ---------------------------------------- |
| **DocType**                | `export_doc()`         | `custom=False` + `developer_mode`     | Python controller files                  |
| **Module Onboarding**      | `export_to_files()`    | دائماً                                | JSON فقط                                 |
| **Dashboard**              | `export_to_files()`    | `is_standard=True` + `developer_mode` | JSON فقط                                 |
| **Dashboard Chart Source** | `export_to_files()`    | دائماً                                | **`.js` file**                           |
| **Dashboard Chart**        | `export_to_files()`    | `is_standard=True` + `developer_mode` | JSON فقط                                 |
| **Number Card**            | `export_to_files()`    | `is_standard=True` + `developer_mode` | JSON فقط                                 |
| **Form Tour**              | `export_to_files()`    | `is_standard=True` + `developer_mode` | JSON فقط                                 |
| **Workspace**              | `export_to_files()`    | `public=True` + `developer_mode`      | JSON فقط                                 |
| **Print Format**           | `export_module_json()` | `standard="Yes"`                      | JSON فقط                                 |
| **Report**                 | `export_doc()`         | دائماً                                | JSON فقط                                 |
| **Page**                   | `export_module_json()` | `standard="Yes"`                      | **`.js` file**                           |
| **Web Form**               | `export_module_json()` | `is_standard=True`                    | **`.js` + `.py` files**                  |
| **Website Theme**          | `export_doc()`         | `custom=False` + `developer_mode`     | JSON فقط                                 |
| **Notification**           | `export_module_json()` | `is_standard=True`                    | **`.html/.md/.txt` files**               |
| **Server Script**          | `export_doc()`         | دائماً                                | **`.py` file** (via `get_code_fields()`) |

### 2. DocTypes التي تم إضافتها في التطبيق (تحتاج تصدير يدوي)

هذه DocTypes **تم إضافتها** في تطبيق `export_custom_fields`:

| DocType             | حالة التصدير التلقائي                               | ملاحظات                  |
| ------------------- | --------------------------------------------------- | ------------------------ |
| **Web Page**        | ❌ لا يوجد                                          | ✅ تمت إضافتها بشكل صحيح |
| **Page**            | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |
| **Report**          | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |
| **Dashboard**       | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |
| **Dashboard Chart** | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |
| **Form Tour**       | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |
| **Number Card**     | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |
| **Workspace**       | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |
| **Notification**    | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |
| **Print Format**    | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |
| **Web Form**        | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |
| **Web Template**    | ❓ `export_to_files()` موجود لكن ليس في `on_update` | ✅ يمكن الاحتفاظ بها     |
| **Website Theme**   | ⚠️ لديه تصدير تلقائي                                | ⚠️ مكرر - يمكن إزالته    |

### 3. DocTypes Child Tables (لا يجب إضافتها)

| DocType                         | نوع           | ملاحظات                               |
| ------------------------------- | ------------- | ------------------------------------- |
| **User Type Module**            | Child Table   | لا يمكن تصديرها مباشرة                |
| **Print Format Field Template** | DocType منفصل | لديه حقل `module` لكن ليس child table |

### 4. DocTypes التي تصدر بملفات مختلفة عن JSON فقط

| DocType                    | ملفات إضافية     | طريقة التصدير                                         |
| -------------------------- | ---------------- | ----------------------------------------------------- |
| **Server Script**          | `.py`            | `get_code_fields() -> {"script": "py"}`               |
| **Page**                   | `.js`            | `export_module_json()` + إنشاء `.js` file             |
| **Web Form**               | `.js` + `.py`    | `export_module_json()` + إنشاء `.js` + `.py` files    |
| **Notification**           | `.html/.md/.txt` | `export_module_json()` + إنشاء ملف حسب `message_type` |
| **Dashboard Chart Source** | `.js`            | `export_to_files()` إلى ملف `.js`                     |

## التوصيات

### 1. DocTypes التي يجب إزالتها (لديها تصدير تلقائي)

يمكن إزالة الأزرار والملفات الخاصة بالـ DocTypes التالية لأنها **لديها تصدير تلقائي**:

-   ✅ **Page** - لديه تصدير تلقائي
-   ✅ **Report** - لديه تصدير تلقائي
-   ✅ **Dashboard** - لديه تصدير تلقائي
-   ✅ **Dashboard Chart** - لديه تصدير تلقائي
-   ✅ **Form Tour** - لديه تصدير تلقائي
-   ✅ **Number Card** - لديه تصدير تلقائي
-   ✅ **Workspace** - لديه تصدير تلقائي
-   ✅ **Notification** - لديه تصدير تلقائي
-   ✅ **Print Format** - لديه تصدير تلقائي
-   ✅ **Web Form** - لديه تصدير تلقائي
-   ✅ **Website Theme** - لديه تصدير تلقائي

### 2. DocTypes التي يجب الاحتفاظ بها

-   ✅ **Web Page** - لا يوجد تصدير تلقائي
-   ❓ **Web Template** - `export_to_files()` موجود لكن ليس في `on_update` (يمكن التحقق أكثر)

### 3. ملاحظة مهمة

الـ DocTypes التي لديها تصدير تلقائي **تتصدر تلقائياً عند الحفظ** في developer mode. إضافة أزرار تصدير يدوية لها قد يكون **مكرراً وغير ضرورياً**.

## المراجع

-   `/home/erp/erp15/apps/frappe/frappe/modules/export_file.py` - `write_document_file()` و `write_code_files()`
-   `/home/erp/erp15/apps/frappe/frappe/modules/utils.py` - `export_module_json()`
-   `/home/erp/erp15/apps/frappe/frappe/core/doctype/doctype/doctype.py` - DocType `on_update()`
-   `/home/erp/erp15/apps/frappe/frappe/printing/doctype/print_format/print_format.py` - Print Format `on_update()`
-   `/home/erp/erp15/apps/frappe/frappe/core/doctype/server_script/server_script.py` - Server Script `get_code_fields()`
