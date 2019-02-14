# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db
from datetime import datetime


# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


# Define a User model
class User(Base):
    __tablename__ = 'user'

    # User Name
    name = db.Column(db.String(128),  nullable=False)
    # Identification Data: email & password
    email = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(255),  nullable=False)
    # Authorisation Data: role & status
    profile = db.Column(db.String(128), nullable=False)
    skills = db.Column(db.String(128), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password, profile, skills, admin):
        self.name = name
        self.email = email
        self.password = password
        self.profile = profile
        self.skills = skills
        self.admin = admin

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    badge = db.Column(db.String(150), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    is_full_time = db.Column(db.Boolean, nullable=False)

    # 1 to 1 relationship with user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('employee', lazy=True))

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(192), nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(192), nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(192), nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(192), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment = db.Column(db.Text, nullable=True)

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Sprint(db.Model):
    __tablename__ = 'sprint'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(192), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    comment = db.Column(db.Text, nullable=True)


    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Issue(db.Model):
    __tablename__ = 'issue'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(192), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(192), nullable=False)

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class IssueTracking(db.Model):
    __tablename__ = 'issue_tracking'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    comment = db.Column(db.Text, nullable=True)

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(192), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(192), nullable=False)

    # 1 to 1 relationship with Sprint
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprint.id'), nullable=False)
    sprint = db.relationship('Sprint', backref=db.backref('task', lazy=True))

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class TaskTracking(db.Model):
    __tablename__ = 'task_tracking'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    comment = db.Column(db.Text, nullable=True)

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class ChatRoom(db.Model):
    __tablename__ = 'chat_room'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(192), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.Text, nullable=True)
    sending_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self):
        return True

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

