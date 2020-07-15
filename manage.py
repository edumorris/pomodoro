from app import create_app, db
from flask_script import Manager, Server
from app.models import Comment, User, Pitch
from flask_migrate import Migrate, MigrateCommand

# App instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)
@manager.command
def test():
       '''
       Run the unit test
       '''
       import unittest
       tests = unittest.TestLoader().discover('tests')
       unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
       return dict(app = app, db = db, Comment = Comment, User = User, Pitch = Pitch)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()