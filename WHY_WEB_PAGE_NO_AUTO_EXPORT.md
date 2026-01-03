# لماذا Web Page لا تصدر تلقائياً؟

## السبب الرئيسي

**Web Page لا تصدر تلقائياً لأنها لا تحتوي على حقل `standard` أو `is_standard`**

---

## المقارنة مع DocTypes الأخرى

### ✅ DocTypes التي لديها تصدير تلقائي

جميع DocTypes التي لديها تصدير تلقائي تحتوي على حقل `standard` أو `is_standard`:

| DocType             | الحقل                 | القيمة  | الكود                                                           |
| ------------------- | --------------------- | ------- | --------------------------------------------------------------- |
| **Page**            | `standard` (Select)   | `"Yes"` | `export_module_json(self, self.standard == "Yes", self.module)` |
| **Web Form**        | `is_standard` (Check) | `True`  | `export_module_json(self, self.is_standard, self.module)`       |
| **Web Template**    | `standard` (Check)    | `True`  | `if self.standard: self.export_to_files()`                      |
| **Print Format**    | `standard` (Select)   | `"Yes"` | `export_module_json(self, self.standard == "Yes", self.module)` |
| **Website Theme**   | `custom` (Check)      | `False` | `if not self.custom: self.export_doc()`                         |
| **Dashboard**       | `is_standard` (Check) | `True`  | `if self.is_standard: export_to_files(...)`                     |
| **Dashboard Chart** | `is_standard` (Check) | `True`  | `if self.is_standard: export_to_files(...)`                     |
| **Form Tour**       | `is_standard` (Check) | `True`  | `if self.is_standard: export_to_files(...)`                     |
| **Number Card**     | `is_standard` (Check) | `True`  | `if self.is_standard: export_to_files(...)`                     |
| **Notification**    | `is_standard` (Check) | `True`  | `export_module_json(self, self.is_standard, self.module)`       |
| **Workspace**       | `public` (Check)      | `True`  | `if self.public: export_to_files(...)`                          |

### ❌ Web Page

**Web Page لا تحتوي على حقل `standard` أو `is_standard` في JSON schema**

```json
// web_page.json - لا يوجد حقل standard أو is_standard
{
  "fields": [
    {"fieldname": "title", ...},
    {"fieldname": "route", ...},
    {"fieldname": "published", ...},  // ✅ هذا الحقل موجود
    {"fieldname": "module", ...},     // ✅ هذا الحقل موجود
    // ❌ لا يوجد "standard" أو "is_standard"
  ]
}
```

---

## كيف يعمل التصدير التلقائي؟

### 1. `export_module_json()` Function

```python
def export_module_json(doc: "Document", is_standard: bool, module: str) -> str | None:
    """Make a folder for the given doc and add its json file"""
    if not frappe.flags.in_import and is_standard and frappe.conf.developer_mode:
        # ← يتطلب is_standard=True
        from frappe.modules.export_file import export_to_files
        export_to_files(record_list=[[doc.doctype, doc.name]], record_module=module, create_init=is_standard)
        return os.path.join(...)
```

**يتطلب `is_standard=True` للتصدير!**

### 2. مثال: Page (لديها تصدير تلقائي)

```python
# page.py
def on_update(self):
    path = export_module_json(self, self.standard == "Yes", self.module)
    #                                        ↑
    #                                  يستخدم حقل standard
```

### 3. مثال: Web Form (لديها تصدير تلقائي)

```python
# web_form.py
def on_update(self):
    path = export_module_json(self, self.is_standard, self.module)
    #                                        ↑
    #                                  يستخدم حقل is_standard
```

### 4. Web Page (لا يوجد تصدير تلقائي)

```python
# web_page.py
class WebPage(WebsiteGenerator):
    # ❌ لا يوجد on_update() override
    # ❌ لا يوجد حقل standard أو is_standard
    # ❌ WebsiteGenerator.on_update() لا يقوم بالتصدير
```

---

## WebsiteGenerator.on_update()

```python
# website_generator.py
class WebsiteGenerator(Document):
    def on_update(self):
        self.send_indexing_request()  # ← فقط indexing
        self.remove_old_route_from_index()  # ← فقط route management
        # ❌ لا يوجد export_module_json() أو export_to_files()
```

**WebsiteGenerator لا يقوم بالتصدير!**

---

## الخلاصة

### لماذا Web Page لا تصدر تلقائياً؟

1. ✅ **Web Page لا تحتوي على حقل `standard` أو `is_standard`**
2. ✅ **Web Page لا تحتوي على `on_update()` override مع التصدير**
3. ✅ **WebsiteGenerator (الكلاس الأب) لا يقوم بالتصدير في `on_update()`**
4. ✅ **`export_module_json()` يتطلب `is_standard=True` للعمل**

### النتيجة

**Web Page لا يمكن أن تكون "standard" لأنها لا تحتوي على الحقل المطلوب، وبالتالي لا يتم تصديرها تلقائياً.**

---

## الحل: استخدام التصدير اليدوي

لذلك، **Web Page تحتاج إلى أزرار تصدير يدوية** (Export to Module / Set Module) لأنها:

-   ❌ لا لديها تصدير تلقائي
-   ✅ تحتوي على حقل `module`
-   ✅ يمكن تصديرها يدوياً إلى `fixtures/Web Page.json`
