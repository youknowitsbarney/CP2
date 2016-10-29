from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from database.models import User

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


def make_shell_context():
	return dict(app=app, db=db, User=User)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()