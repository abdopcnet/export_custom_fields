# استراتيجية التصدير - استخدام الدوال الأصلية

## المبدأ

جميع دوال التصدير يجب أن تستخدم نفس الدوال الأصلية التي يستخدمها `on_update()` أو `before_save()` في Frappe.

---

## أنواع التصدير

### 1. `export_module_json()` - للـ DocTypes التالية:

-   **Page**: `export_module_json(doc, doc.standard == "Yes", doc.module)`
-   **Web Form**: `export_module_json(doc, doc.is_standard, doc.module)`
-   **Notification**: `export_module_json(doc, doc.is_standard, doc.module)`
-   **Print Format**: `export_module_json(doc, doc.standard == "Yes", doc.module)`

**شروط**: فقط الـ documents التي `standard="Yes"` أو `is_standard=True`

### 2. `export_to_files()` - للـ DocTypes التالية:

-   **Dashboard**: `export_to_files([["Dashboard", name, f"{module} Dashboard"]], module)`
-   **Dashboard Chart**: `export_to_files([["Dashboard Chart", name]], module)`
-   **Form Tour**: `export_to_files([["Form Tour", name]], module)`
-   **Number Card**: `export_to_files([["Number Card", name]], module)`
-   **Workspace**: `export_to_files([["Workspace", name]], module)` - فقط `public=True`
-   **Web Template**: `doc.export_to_files()` - فقط `standard=True`

**شروط**:

-   Dashboard, Dashboard Chart, Form Tour, Number Card → فقط `is_standard=True`
-   Workspace → فقط `public=True`
-   Web Template → فقط `standard=True`

### 3. `export_doc()` - للـ DocTypes التالية:

-   **Report**: `doc.export_doc()` - جميع الـ documents
-   **Website Theme**: `doc.export_doc()` - فقط `custom=False`

**شروط**:

-   Report → جميع الـ documents
-   Website Theme → فقط `custom=False`

### 4. `export_json()` إلى fixtures - للـ DocTypes التالية:

-   **Web Page**: `export_json("Web Page", path, filters={"module": module})` - جميع الـ documents

**شروط**: جميع الـ documents (لا يوجد تصدير تلقائي)

---

## التطبيق

لكل DocType:

1. نحصل على جميع الـ documents في module (مع الفلاتر المناسبة)
2. لكل document، نستدعي نفس الدالة الأصلية
3. نستخدم نفس الشروط (`is_standard`, `standard`, `public`, `custom`)
