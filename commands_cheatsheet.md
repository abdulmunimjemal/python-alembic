# Alembic Commands Cheat Sheet

## Basic Commands

- **Init a New Migration Environment:**

```bash
alembic init alembic
```

Initializes a new Alembic environment in the "alembic" directory.

- **Create a New Migration Script:**

```bash
alembic revision -m "description"
```

Creates a new migration script with a descriptive message.

- **Create a New Auto-Generated Migration Script:**

```bash
alembic revision --autogenerate -m "description"
```

Generates a new migration script based on the detected changes in the models.

- **Upgrade the Database:**

```bash
alembic upgrade head
```

Upgrades the database to the latest version.

- **Downgrade the Database:**

```bash
alembic downgrade -1
```

Downgrades the database by one version.

- **Show Current Revision:**

```bash
alembic current
```

Displays the current version of the database.

- **Show Migration History:**

```bash
alembic history
```

Shows a list of all migrations, ordered by date.

- **Show Detailed Information of a Specific Revision:**

```bash
alembic show <revision>
```

Shows the details of a specific migration revision.

## Advanced Commands

- **Stamp the Database with a Specific Revision:**

```bash
alembic stamp <revision>
```

Sets the revision in the database without performing any migrations.

- **Merge Two Revisions:**

```bash
alembic merge -m "merge message" <revision1> <revision2>
```

Creates a new migration that merges two branches.

- **Run a Custom Script:**

```bash
alembic run <script>
```

Executes a custom script in the Alembic environment.

## Configuration and Customization

- **Specify Configuration File:**

```bash
alembic -c /path/to/alembic.ini <command>
```

Specifies a different Alembic configuration file.

- **Generate SQL for a Migration:**

```bash
alembic upgrade head --sql
```

- **Generate SQL for a Specific Revision:**

```bash
alembic upgrade head --sql
```

Generates SQL statements for the migration instead of applying them.

- **Environment Configuration:**

```python
# in alembic/env.py
from myapp import mymodel
target_metadata = mymodel.Base.metadata
```

## Useful Tips

- More Commands: https://alembic.sqlalchemy.org/en/latest/api/commands.html
- Display the current revision for a database: `alembic current`.
- View migrations history: `alembic history --verbose`.
- Revert all migrations: `alembic downgrade base`.
- Revert migrations one by one: `alembic downgrade -1`.
- Apply all migrations: `alembic upgrade head`.
- Apply migrations one by one: `alembic upgrade +1`.
- Display all raw SQL: `alembic upgrade head --sql`.
- Reset the database: `alembic downgrade base && alembic upgrade head.`
