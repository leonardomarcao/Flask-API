from flask_script import Manager
from app import app

manager = Manager(app)

# Database migrations commandW

if __name__ == '__main__':
    manager.run()
