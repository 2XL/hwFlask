from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from config import config_by_name
from project.main import app, db

app.config.from_object(config_by_name['dev'])
migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
