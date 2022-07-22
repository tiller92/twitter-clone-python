"""Message model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


from email.mime import message
import os
from unittest import TestCase

from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class MessageModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_message_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )
      

        db.session.add(u)
        db.session.commit()

        m = Message(text='test message', user_id=u.id)
        db.session.add(m)
        db.session.commit()
        # User should have 1 messages & no followers
        self.assertEqual(len(u.messages), 1)
        self.assertEqual(len(u.followers), 0)
  
  

class MessageModelTestCaseTwo(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_message_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )
      

        db.session.add(u)
        db.session.commit()

        m = Message(text='test message', user_id=u.id)
        db.session.add(m)
        db.session.commit()
        # User should have 1 messages & no followers
        self.assertEqual(len(u.messages), 1)
        self.assertEqual(u.messages[0].text, 'test message')