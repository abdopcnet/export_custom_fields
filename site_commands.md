# Frappe Bench Site Commands Reference

Complete guide to all available site management commands in Frappe/ERPNext.

## Table of Contents
- [Variables Setup](#variables-setup)
- [Site Creation & Setup](#site-creation--setup)
- [Backup & Restore](#backup--restore)
- [Site Destruction & Reinstall](#site-destruction--reinstall)
- [App Management](#app-management)
- [User Management](#user-management)
- [Database & Migration](#database--migration)
- [Database Cleanup](#database-cleanup)
- [Development & Testing](#development--testing)

---

## Variables Setup

```bash
# Common variables for your site
site_name=erp.khubara-almal.com
database_sql=/home/frappe/20251117_000340-erp_khubara-almal_com-database.sql.gz
public_files=/home/frappe/20251117_000340-erp_khubara-almal_com-files.tar
private_files=/home/frappe/20251117_000340-erp_khubara-almal_com-private-files.tar.zip
encryption_key="ZtjABV-XLk1tEaANGi2zBhfVF1DXUl13msMsV1so9HE="
admin_password="123123@"
db_root_password="your_mariadb_root_password"
```

---

## Site Creation & Setup

### Create a New Site

```bash
# Basic site creation
bench new-site $site_name

# With custom options
bench new-site $site_name \
  --db-name custom_db_name \
  --db-password "db_password" \
  --admin-password $admin_password \
  --db-root-password $db_root_password \
  --install-app erpnext \
  --install-app hrms \
  --set-default

# With MariaDB/PostgreSQL options
bench new-site $site_name \
  --db-type mariadb \
  --db-host localhost \
  --db-port 3306 \
  --admin-password $admin_password
```

**Available Options:**
- `--db-name` - Database name
- `--db-password` - Database password
- `--db-type` - Database type (mariadb/postgres)
- `--db-host` - Database host
- `--db-port` - Database port
- `--db-root-username` - Root username (default: "root")
- `--db-root-password` - Root password
- `--admin-password` - Administrator password
- `--install-app` - Install apps (can use multiple times)
- `--set-default` - Set as default site
- `--force` - Force creation if site exists

### Set Default Site

```bash
# Set a site as default
bench use $site_name
```

### Add Site to Hosts File

```bash
# Add site to /etc/hosts (requires sudo)
bench --site $site_name add-to-hosts
```

---

## Backup & Restore

### Create Backup

```bash
# Database only
bench --site $site_name backup

# With files (public and private)
bench --site $site_name backup --with-files

# With custom backup path
bench --site $site_name backup \
  --with-files \
  --backup-path /home/frappe/backups \
  --compress

# Backup specific DocTypes only
bench --site $site_name backup \
  --include "Sales Invoice,Purchase Invoice,Stock Entry"

# Exclude specific DocTypes
bench --site $site_name backup \
  --with-files \
  --exclude "Communication,Version,Activity Log"

# Custom paths for each component
bench --site $site_name backup \
  --with-files \
  --backup-path-db /path/to/db \
  --backup-path-files /path/to/public \
  --backup-path-private-files /path/to/private \
  --backup-path-conf /path/to/config
```

**Available Options:**
- `--with-files` - Include public and private files
- `--compress` - Compress files
- `--backup-path` - Path for all backup files
- `--backup-path-db` - Database backup path
- `--backup-path-files` - Public files backup path
- `--backup-path-private-files` - Private files backup path
- `--backup-path-conf` - Config backup path
- `--include` / `--only` / `-i` - Include specific DocTypes (comma-separated)
- `--exclude` / `-e` - Exclude specific DocTypes (comma-separated)
- `--ignore-backup-conf` - Ignore backup config settings
- `--verbose` - Verbose output
- `--old-backup-metadata` - Use older backup metadata format

### Restore from Backup

```bash
# Full restore with encryption and files
bench --verbose --site $site_name restore $database_sql \
  --encryption-key "$encryption_key" \
  --with-public-files $public_files \
  --with-private-files $private_files \
  --admin-password $admin_password \
  --force

# Database only
bench --site $site_name restore $database_sql

# With database root password
bench --site $site_name restore $database_sql \
  --db-root-password $db_root_password \
  --force

# With custom database name
bench --site $site_name restore $database_sql \
  --db-name custom_database_name \
  --admin-password $admin_password

# Install specific apps after restore
bench --site $site_name restore $database_sql \
  --install-app erpnext \
  --install-app hrms \
  --force
```

**Available Options:**
- `--encryption-key` - Backup encryption key
- `--with-public-files` - Path to public files tar
- `--with-private-files` - Path to private files tar
- `--db-root-username` - MariaDB root username
- `--db-root-password` - MariaDB root password
- `--db-name` - Custom database name
- `--admin-password` - Administrator password
- `--install-app` - Install apps after restore (multiple)
- `--force` - Ignore validations and warnings

### Partial Restore

```bash
# Restore specific DocTypes to existing site
bench --site $site_name partial-restore $database_sql \
  --verbose

# With encryption
bench --site $site_name partial-restore $database_sql \
  --encryption-key "$encryption_key" \
  --verbose
```

**Available Options:**
- `--encryption-key` - Backup encryption key
- `--verbose` / `-v` - Verbose output

---

## Site Destruction & Reinstall

### Drop Site

```bash
# Delete site (with backup)
bench drop-site $site_name

# With database root password
bench drop-site $site_name \
  --db-root-password $db_root_password

# Without backup (dangerous!)
bench drop-site $site_name \
  --no-backup \
  --force

# Custom archive path
bench drop-site $site_name \
  --archived-sites-path /home/frappe/archived_sites
```

**Available Options:**
- `--db-root-username` - MariaDB root username
- `--db-root-password` - MariaDB root password
- `--archived-sites-path` - Custom archive location
- `--no-backup` - Skip backup before deletion
- `--force` - Force deletion even on errors

### Reinstall Site

```bash
# Reinstall site (wipe and start fresh)
bench --site $site_name reinstall

# With confirmation skip
bench --site $site_name reinstall \
  --yes \
  --admin-password $admin_password

# With database credentials
bench --site $site_name reinstall \
  --admin-password $admin_password \
  --db-root-password $db_root_password \
  --yes
```

**Available Options:**
- `--admin-password` - New administrator password
- `--db-root-username` - MariaDB root username
- `--db-root-password` - MariaDB root password
- `--yes` - Skip confirmation prompt

---

## App Management

### Install App

```bash
# Install single app
bench --site $site_name install-app erpnext

# Install multiple apps
bench --site $site_name install-app erpnext hrms insights

# Force install
bench --site $site_name install-app erpnext --force
```

**Available Options:**
- `--force` - Force installation

### List Installed Apps

```bash
# Text format
bench --site $site_name list-apps

# JSON format
bench --site $site_name list-apps --format json
```

**Available Options:**
- `--format` / `-f` - Output format (text/json)

### Uninstall App

```bash
# Uninstall app (with prompts)
bench --site $site_name uninstall-app custom_app

# Skip confirmation
bench --site $site_name uninstall-app custom_app --yes

# Dry run (see what will be deleted)
bench --site $site_name uninstall-app custom_app --dry-run

# Without backup
bench --site $site_name uninstall-app custom_app \
  --yes \
  --no-backup

# Force uninstall
bench --site $site_name uninstall-app custom_app \
  --yes \
  --force
```

**Available Options:**
- `--yes` / `-y` - Skip confirmation
- `--dry-run` - Preview deletions
- `--no-backup` - Skip backup
- `--force` - Force removal

### Remove from Installed Apps List

```bash
# Remove app from list without uninstalling
bench --site $site_name remove-from-installed-apps custom_app
```

---

## User Management

### Add System Manager

```bash
# Basic
bench --site $site_name add-system-manager admin@example.com

# With details
bench --site $site_name add-system-manager admin@example.com \
  --first-name "System" \
  --last-name "Administrator" \
  --password "secure_password" \
  --send-welcome-email
```

**Available Options:**
- `--first-name` - First name
- `--last-name` - Last name
- `--password` - User password
- `--send-welcome-email` - Send welcome email

### Add User

```bash
# Add regular user
bench --site $site_name add-user user@example.com \
  --first-name "John" \
  --last-name "Doe" \
  --password "password123" \
  --user-type "System User" \
  --add-role "Sales User" \
  --add-role "Purchase User" \
  --send-welcome-email
```

**Available Options:**
- `--first-name` - First name
- `--last-name` - Last name
- `--password` - User password
- `--user-type` - User type (System User/Website User)
- `--add-role` - Roles to assign (multiple)
- `--send-welcome-email` - Send welcome email

### Disable User

```bash
# Disable a user account
bench --site $site_name disable-user user@example.com
```

### Set Password

```bash
# Set user password (interactive)
bench --site $site_name set-password user@example.com

# Set password directly
bench --site $site_name set-password user@example.com "new_password"

# Logout from all sessions
bench --site $site_name set-password user@example.com "new_password" \
  --logout-all-sessions
```

**Available Options:**
- `--logout-all-sessions` - Logout user from all sessions

### Set Admin Password

```bash
# Set administrator password (interactive)
bench --site $site_name set-admin-password

# Set directly
bench --site $site_name set-admin-password $admin_password

# With logout
bench --site $site_name set-admin-password $admin_password \
  --logout-all-sessions
```

**Available Options:**
- `--logout-all-sessions` - Logout from all sessions

### Set Last Active for User

```bash
# Update user's last active timestamp
bench --site $site_name set-last-active-for-user --user user@example.com
```

---

## Database & Migration

### Run Migrations

```bash
# Run all migrations
bench --site $site_name migrate

# Skip failing patches
bench --site $site_name migrate --skip-failing

# Skip search index rebuilding
bench --site $site_name migrate --skip-search-index

# Both options
bench --site $site_name migrate \
  --skip-failing \
  --skip-search-index
```

**Available Options:**
- `--skip-failing` - Skip patches that fail
- `--skip-search-index` - Skip search indexing

### Run Specific Patch

```bash
# Run a single patch
bench --site $site_name run-patch erpnext.patches.v14_0.update_integration_request

# Force run even if already executed
bench --site $site_name run-patch erpnext.patches.v14_0.update_integration_request \
  --force
```

**Available Options:**
- `--force` - Force execution

### Reload DocType

```bash
# Reload DocType schema
bench --site $site_name reload-doctype "Sales Invoice"
```

### Reload Doc

```bash
# Reload specific document
bench --site $site_name reload-doc accounts doctype "Sales Invoice"
```

### Add Database Index

```bash
# Add single column index
bench --site $site_name add-database-index \
  --doctype "Sales Invoice" \
  --column posting_date

# Multi-column index
bench --site $site_name add-database-index \
  --doctype "Sales Invoice" \
  --column posting_date \
  --column customer
```

**Available Options:**
- `--doctype` - DocType name
- `--column` - Column name (multiple for compound index)

### Describe Database Table

```bash
# Get table statistics
bench --site $site_name describe-database-table \
  --doctype "Sales Invoice"

# With column cardinality
bench --site $site_name describe-database-table \
  --doctype "Sales Invoice" \
  --column customer \
  --column posting_date
```

**Available Options:**
- `--doctype` - DocType name (required)
- `--column` - Columns for detailed stats (multiple)

---

## Database Cleanup

### Clear Log Table

```bash
# Clear old log entries
bench --site $site_name clear-log-table \
  --doctype "Error Log" \
  --days 30

# Without backup
bench --site $site_name clear-log-table \
  --doctype "Activity Log" \
  --days 90 \
  --no-backup
```

**Available Options:**
- `--doctype` - Log DocType (required)
- `--days` - Keep records for N days
- `--no-backup` - Skip backup

**Supported Log DocTypes:**
- Error Log
- Activity Log
- Email Queue
- Communication
- Version
- Access Log
- View Log

### Trim Database

```bash
# Remove ghost tables (deleted DocTypes)
bench --site $site_name trim-database

# Dry run
bench --site $site_name trim-database --dry-run

# JSON output
bench --site $site_name trim-database \
  --format json \
  --dry-run

# Without backup (not recommended)
bench --site $site_name trim-database \
  --yes \
  --no-backup
```

**Available Options:**
- `--dry-run` - Preview only
- `--format` / `-f` - Output format (text/json)
- `--no-backup` - Skip backup
- `--yes` / `-y` - Skip confirmation

### Trim Tables

```bash
# Remove unused columns from tables
bench --site $site_name trim-tables

# Dry run
bench --site $site_name trim-tables --dry-run

# JSON format
bench --site $site_name trim-tables \
  --format json

# Without backup
bench --site $site_name trim-tables --no-backup
```

**Available Options:**
- `--dry-run` - Preview only
- `--format` / `-f` - Output format (json/table)
- `--no-backup` - Skip backup

---

## Development & Testing

### Browse Site

```bash
# Open site in browser
bench --site $site_name browse

# Login as specific user (requires developer_mode)
bench --site $site_name browse \
  --user Administrator

# With session end time
bench --site $site_name browse \
  --user user@example.com \
  --session-end "2025-12-31T23:59:59.000000+00:00"

# With audit trail user
bench --site $site_name browse \
  --user user@example.com \
  --user-for-audit admin@example.com
```

**Available Options:**
- `--user` - Login as user (developer_mode or Administrator only)
- `--session-end` - Session expiry (ISO8601 format)
- `--user-for-audit` - User for audit trail

### Start Ngrok Tunnel

```bash
# Start ngrok (requires authtoken in site_config.json)
bench --site $site_name ngrok

# HTTPS only
bench --site $site_name ngrok --bind-tls

# Use default authtoken from ngrok config
bench --site $site_name ngrok --use-default-authtoken
```

**Available Options:**
- `--bind-tls` - HTTPS tunnel only
- `--use-default-authtoken` - Use ngrok's default config

### Frappe Recorder

```bash
# Start recording
bench --site $site_name start-recording

# Stop recording
bench --site $site_name stop-recording
```

### Build Search Index

```bash
# Rebuild website search index
bench --site $site_name build-search-index
```

### Publish Realtime Event

```bash
# Publish event
bench --site $site_name publish-realtime "custom_event" \
  --message "Event message" \
  --room "room_name" \
  --user user@example.com \
  --doctype "Sales Invoice" \
  --docname "SI-0001"
```

**Available Options:**
- `--message` - Event message
- `--room` - Room name
- `--user` - Target user
- `--doctype` - DocType
- `--docname` - Document name
- `--after-commit` - Publish after commit

---

## Common Workflows

### Complete Site Restore

```bash
# 1. Set variables
site_name=erp.khubara-almal.com
database_sql=/home/frappe/20251117_000340-erp_khubara-almal_com-database.sql.gz
public_files=/home/frappe/20251117_000340-erp_khubara-almal_com-files.tar
private_files=/home/frappe/20251117_000340-erp_khubara-almal_com-private-files.tar.zip
encryption_key="ZtjABV-XLk1tEaANGi2zBhfVF1DXUl13msMsV1so9HE="
admin_password="123123@"

# 2. Restore site with files
bench --verbose --site $site_name restore $database_sql \
  --encryption-key "$encryption_key" \
  --with-public-files $public_files \
  --with-private-files $private_files \
  --admin-password $admin_password \
  --force

# 3. Run migrations
bench --site $site_name migrate

# 4. Build search index
bench --site $site_name build-search-index

# 5. Set as default
bench use $site_name

# 6. Open in browser
bench --site $site_name browse --user Administrator
```

### Fresh Site Setup

```bash
# 1. Create new site
bench new-site $site_name \
  --admin-password $admin_password \
  --install-app erpnext \
  --install-app hrms \
  --set-default

# 2. Add system manager
bench --site $site_name add-system-manager admin@company.com \
  --first-name "System" \
  --last-name "Admin" \
  --password "password123"

# 3. Run migrations
bench --site $site_name migrate

# 4. Create backup
bench --site $site_name backup --with-files
```

### Site Cleanup

```bash
# 1. Clear old logs
bench --site $site_name clear-log-table --doctype "Error Log" --days 30
bench --site $site_name clear-log-table --doctype "Activity Log" --days 90

# 2. Trim database
bench --site $site_name trim-database --yes

# 3. Trim tables
bench --site $site_name trim-tables

# 4. Create backup after cleanup
bench --site $site_name backup --with-files --compress
```

---

## Tips & Best Practices

### Always Backup Before Major Operations
```bash
# Before restore, reinstall, or uninstall
bench --site $site_name backup --with-files
```

### Use Verbose Mode for Troubleshooting
```bash
bench --verbose --site $site_name <command>
```

### Check Site Status
```bash
# List all apps
bench --site $site_name list-apps

# Check if site exists
bench --site $site_name migrate --help
```

### Multiple Sites
```bash
# Run command on multiple sites
bench --site site1.local --site site2.local migrate
```

### Database Credentials
Store in environment variables for security:
```bash
export DB_ROOT_PASSWORD="your_secure_password"
bench --site $site_name restore $database_sql \
  --db-root-password "$DB_ROOT_PASSWORD"
```

---

## Troubleshooting

### Restore Fails
```bash
# Check file exists
ls -lh $database_sql

# Check encryption
file $database_sql

# Try without encryption key if not encrypted
bench --site $site_name restore $database_sql --force
```

### Migration Errors
```bash
# Skip failing patches
bench --site $site_name migrate --skip-failing

# Run specific patch
bench --site $site_name run-patch module.patch_name --force
```

### Permission Issues
```bash
# Fix permissions
sudo chown -R frappe:frappe /home/frappe/frappe-bench/sites/$site_name
```

### Site Not Found
```bash
# List all sites
bench --site all list-apps

# Check current directory
cd /home/frappe/frappe-bench
```

---

## Quick Reference

| Command | Purpose |
|---------|---------|
| `bench new-site` | Create new site |
| `bench restore` | Restore from backup |
| `bench backup` | Create backup |
| `bench migrate` | Run migrations |
| `bench drop-site` | Delete site |
| `bench reinstall` | Wipe and reinstall site |
| `bench install-app` | Install app on site |
| `bench uninstall-app` | Remove app from site |
| `bench list-apps` | List installed apps |
| `bench set-admin-password` | Change admin password |
| `bench use` | Set default site |
| `bench browse` | Open site in browser |

---

**Last Updated:** November 17, 2025  
**Frappe Version:** 15  
**Site:** erp.khubara-almal.com
