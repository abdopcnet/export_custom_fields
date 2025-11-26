# Export Custom Fields

<div align="center">
    <h2>Export Custom Fields</h2>
    <p><em>Export Your Frappe Customizations to Version Control</em></p>

![Version](https://img.shields.io/badge/version-26.11.2025-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Frappe](https://img.shields.io/badge/Frappe-v15+-red)

</div>

---

## 🎯 What This App Does

**Export Custom Fields** is a powerful Frappe application that helps developers export all their customizations from the database to JSON files for version control, deployment, and backup purposes.

Instead of manually tracking customizations or losing them during migrations, this app provides a simple, one-click solution to export everything to organized JSON files that can be committed to Git and deployed across environments.

---

## 📺 Video Tutorial

<div align="center">

[![Export Custom Fields Tutorial](https://img.youtube.com/vi/d0xk5-Ye0JM/maxresdefault.jpg)](https://www.youtube.com/watch?v=d0xk5-Ye0JM)

_Click the image above to watch the tutorial video_

</div>

---

## ✨ Key Features

### 📦 **Export Custom Fields & Property Setters**

-   **One-Click Export**: Export all custom fields and property setters for any module with a single button click
-   **Module-Based Organization**: Automatically organizes exports by module, keeping your customizations structured
-   **Sync on Migrate**: Optional automatic synchronization during migrations to ensure customizations are always applied
-   **Grouped by DocType**: Custom fields and property setters are automatically grouped by their target DocType for easy management
-   **Standard Format**: Exports in Frappe's standard JSON format, compatible with built-in import/export tools

<div align="center">
    <img src="./imgs/export_custom_field1.png" alt="Export Custom Field 1" width="600">
    <img src="./imgs/export_custom_field2.png" alt="Export Custom Field 2" width="600">
    <img src="./imgs/export_property_setter.png" alt="Export Property Setter" width="600">
</div>

### 🔧 **Export Server Scripts**

-   **Module-Specific Export**: Export all server scripts belonging to a specific module
-   **Fixtures Integration**: Automatically exports to your app's fixtures folder, ready for deployment
-   **Preserves Order**: Maintains script execution order (idx) and creation timestamps
-   **Developer-Friendly**: Only available in developer mode for security

<div align="center">
    <img src="./imgs/export_server_script1.png" alt="Export Server Script 1" width="600">
    <img src="./imgs/export_server_script2.png" alt="Export Server Script 2" width="600">
</div>

### 🎨 **Export Client Scripts**

-   **Module-Based Filtering**: Export client scripts filtered by module
-   **Fixtures Ready**: Exports directly to fixtures folder for easy deployment
-   **Complete Data**: Includes all script configurations, conditions, and code
-   **Version Control Ready**: JSON format perfect for Git tracking

<div align="center">
    <img src="./imgs/export_client_script1.png" alt="Export Client Script 1" width="600">
    <img src="./imgs/export_client_script2.png" alt="Export Client Script 2" width="600">
</div>

### 🌐 **Export Custom HTML Blocks**

-   **Individual Block Export**: Export specific Custom HTML Blocks to fixtures
-   **Module Selection**: Choose which app's fixtures folder to export to via module selection
-   **Complete Block Data**: Exports HTML, CSS, and JavaScript content
-   **Easy Deployment**: Ready to be synced across environments

<div align="center">
    <img src="./imgs/export_custom_html_block.png" alt="Export Custom HTML Block" width="600">
    <img src="./imgs/export_custom_html_block1.png" alt="Export Custom HTML Block 1" width="600">
    <img src="./imgs/export_custom_html_block2.png" alt="Export Custom HTML Block 2" width="600">
</div>

### 📋 **Export All Fixtures**

-   **Complete App Export**: Export all fixtures for an entire app at once
-   **Comprehensive Coverage**: Includes all fixture types configured in your app
-   **Standard Format**: Uses Frappe's standard fixture export format
-   **Migration Ready**: Perfect for syncing fixtures during migrations

---

## 🚀 How to Use

### **Export Custom Fields & Property Setters**

1. Navigate to any **Custom Field** or **Property Setter** form
2. Ensure the document has a **module** assigned
3. Click the **📦 Export to Module** button (appears in developer mode)
4. All custom fields and property setters for that module will be exported to:
    ```
    {module_name}/custom/{doctype_name}.json
    ```

### **Export Server Scripts**

1. Open any **Server Script** form
2. Ensure the script has a **module** assigned
3. Click the **📦 Export to Module** button
4. All server scripts for that module will be exported to:
    ```
    {app_name}/fixtures/server_script.json
    ```

### **Export Client Scripts**

1. Open any **Client Script** form
2. Ensure the script has a **module** assigned
3. Click the **📦 Export to Module** button
4. All client scripts for that module will be exported to:
    ```
    {app_name}/fixtures/client_script.json
    ```

### **Export Custom HTML Blocks**

1. Open any **Custom HTML Block** form
2. Ensure the block is saved (has a name)
3. Click the **📦 Export to Module** button
4. Select the target module in the prompt dialog
5. The current Custom HTML Block will be exported to:
    ```
    {app_name}/fixtures/custom_html_block.json
    ```

### **Export from Customize Form**

1. Navigate to **Customize Form** for any DocType
2. Click the **📦 Export to Module** button
3. Select the target module and configure options:
    - **Module to Export**: Choose the module containing customizations
    - **Sync on Migrate**: Enable automatic sync during migrations
4. All customizations for that module will be exported

---

## 📁 Export Locations

### **Custom Fields & Property Setters**

```
{app_name}/{module_name}/custom/{doctype_name}.json
```

### **Server Scripts, Client Scripts, Custom HTML Blocks**

```
{app_name}/fixtures/{doctype_name}.json
```

---

## 🎁 What You Get

### **Custom Fields Export Includes:**

-   ✅ All custom fields for the selected module
-   ✅ All property setters for the selected module
-   ✅ Grouped by DocType for easy management
-   ✅ Sync on migrate configuration
-   ✅ Standard Frappe JSON format

### **Scripts Export Includes:**

-   ✅ Complete script code and configurations
-   ✅ Module assignments
-   ✅ Execution order (idx)
-   ✅ All script metadata

### **Custom HTML Block Export Includes:**

-   ✅ HTML content
-   ✅ CSS styles
-   ✅ JavaScript code
-   ✅ Complete block configuration

---

## 🔒 Security & Requirements

-   **Developer Mode Required**: All export functions only work when developer mode is enabled
-   **Module Assignment**: Most exports require documents to have a module assigned
-   **Permissions**: Requires appropriate permissions to access customization forms
-   **Frappe Version**: Compatible with Frappe Framework v15+

---

## 💡 Use Cases

### **Version Control**

Track all your customizations in Git, making it easy to:

-   Review changes over time
-   Roll back to previous versions
-   Collaborate with team members
-   Maintain a history of customizations

### **Deployment**

Deploy customizations across environments:

-   Development → Staging → Production
-   Share customizations between projects
-   Maintain consistency across installations
-   Automated deployment via migrations

### **Backup & Recovery**

-   Backup all customizations before major changes
-   Restore customizations after accidental deletion
-   Maintain multiple backup versions
-   Disaster recovery preparation

### **Development Workflow**

-   Share customizations between developers
-   Document customizations in code
-   Review customization changes in pull requests
-   Maintain clean, organized customization files

---

## 🛠️ Technical Details

### **Export Formats**

-   All exports use Frappe's standard JSON format
-   Compatible with `bench migrate` and fixture syncing
-   Human-readable with proper indentation
-   UTF-8 encoding for international characters

### **File Structure**

-   Custom fields: Organized by module and DocType
-   Scripts: Single file per doctype in fixtures folder
-   Maintains Frappe's standard directory structure

### **Integration**

-   Works seamlessly with Frappe's built-in export/import
-   Compatible with `bench export-fixtures` command
-   Follows Frappe's customization export patterns
-   Respects Frappe's developer mode restrictions

---

## 📝 Notes

-   **Developer Mode**: All export functions require developer mode to be enabled
-   **Module Required**: Most exports require documents to have a module assigned
-   **File Overwriting**: Exports will overwrite existing files in the target locations
-   **Git Integration**: Exported files are ready to be committed to version control
-   **Migration Sync**: Use "Sync on Migrate" option for automatic synchronization

---

## 👨‍💻 Contact

<div align="center">
    <img src="./imgs/ERPNext-support.png" height="200" alt="Future Support" style="border-radius: 20px;">
</div>

-   👨‍💻 Developer: abdopcnet
-   🏢 Company: [Future Support](https://www.future-support.online/)
-   📧 Email: <abdopcnet@gmail.com>
-   🐙 GitHub: [github.com/abdopcnet/export_custom_fields](https://github.com/abdopcnet/export_custom_fields)

**🤝 Need Support or Want to Join? Contact Now:**

### <img src="./imgs/Egypt.svg" width="20" height="20" alt="Egypt Flag"> Egypt Contact

-   📞 **Call:** <img src="./imgs/Egypt.svg" width="16" height="16" alt="Egypt Flag"> [+20 115 648 3669](tel:+201156483669)
-   <img src="./imgs/whatsapp.svg" width="16" height="16" alt="WhatsApp"> **WhatsApp:** <img src="./imgs/Egypt.svg" width="16" height="16" alt="Egypt Flag"> [https://wa.me/201156483669](https://wa.me/201156483669)
-   <img src="./imgs/telegram.svg" width="16" height="16" alt="Telegram"> **Telegram:** [https://t.me/EG_01156483669](https://t.me/EG_01156483669)

### <img src="./imgs/Saudi_Arabia.svg" width="20" height="20" alt="Saudi Arabia Flag"> Saudi Arabia Contact

-   📞 **Call:** <img src="./imgs/Saudi_Arabia.svg" width="16" height="16" alt="Saudi Arabia Flag"> [+966 57 891 9729](tel:+966578919729)
-   <img src="./imgs/whatsapp.svg" width="16" height="16" alt="WhatsApp"> **WhatsApp:** <img src="./imgs/Saudi_Arabia.svg" width="16" height="16" alt="Saudi Arabia Flag"> [https://wa.me/966578919729](https://wa.me/966578919729)
-   <img src="./imgs/telegram.svg" width="16" height="16" alt="Telegram"> **Telegram:** [https://t.me/KSA_0578919729](https://t.me/KSA_0578919729)

### 🌐 Online

-   🌐 **Website:** [future-support.online](https://www.future-support.online/)
-   📧 **Email:** <abdopcnet@gmail.com>
-   🐙 **GitHub:** [github.com/abdopcnet/export_custom_fields](https://github.com/abdopcnet/export_custom_fields)

---

<div align="center">
    <p>Made with ❤️ for Frappe developers</p>
    <p>
        <a href="https://github.com/abdopcnet/export_custom_fields">⭐ Star</a> •
        <a href="https://github.com/abdopcnet/export_custom_fields/issues">🐛 Report Bug</a> •
        <a href="https://github.com/abdopcnet/export_custom_fields/fork">🍴 Fork</a> •
        <a href="https://github.com/abdopcnet/export_custom_fields/stargazers">👀 Watch</a>
    </p>
    <p>
        <img src="https://img.shields.io/github/stars/abdopcnet/export_custom_fields?style=social" alt="GitHub stars">
        <img src="https://img.shields.io/github/forks/abdopcnet/export_custom_fields?style=social" alt="GitHub forks">
        <img src="https://img.shields.io/github/watchers/abdopcnet/export_custom_fields?style=social" alt="GitHub watchers">
    </p>
</div>
