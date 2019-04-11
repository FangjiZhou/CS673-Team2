import unittest
import json
from app import db, app
import warnings


class RoleTest(unittest.TestCase):
    """
      Roles Test Case
      by Zicheng Wang
    """

    def setUp(self):
        """
        Test Setup
        """
        self.app = app
        self.client = self.app.test_client
        with self.app.app_context():
            # create all tables
            db.create_all()

        # Create tests users
        json_admin_user = {"name": "wzc_admin", "email": "wzc_admin@email.com",
                           "password": "wzc", "admin": True,
                           "profile": "Software Engineer",
                           "skills": ["java", "C#", "Python"]}

        self.client().post('/api/user/',
                           headers={'Content-Type': 'application/json',
                                    'x-access-token': ''},
                           data=json.dumps(json_admin_user))

        self.user_admin = {
            'username': json_admin_user['email'],
            'password': json_admin_user['password'],
            'token': ''
        }

        # Get tokens
        json_login_admin = {
            "username": self.user_admin['username'],
            "password": self.user_admin['password']
        }
        res_login_admin = self.client().post('/api/login',
                                             headers={'Content-Type': 'application/json',
                                                      'Authorization': 'Basic'},
                                             data=json.dumps(json_login_admin))
        json_data_login_admin = json.loads(res_login_admin.data)
        self.user_admin['token'] = json_data_login_admin.get('token')

        # Create test roles
        json_test_role1 = {'name': 'role_test_name1', 'comment': 'role_test_comment1'}
        self.client().post('/api/role/', headers={'Content-Type': 'application/json',
                                                  'x-access-token': self.user_admin[
                                                      'token']},
                           data=json.dumps(json_test_role1))

    def test_a_create_role(self):
        """ test role creation with admin account """
        warnings.simplefilter("ignore")
        json_test_role2 = {'name': 'role_test_name2', 'comment': 'role_test_comment2'}
        request_role_admin_create = self.client().post('/api/role/', headers={'Content-Type': 'application/json',
                                                                              'x-access-token': self.user_admin[
                                                                                  'token']},
                                                       data=json.dumps(json_test_role2))
        json_data_test_admin_create_role = json.loads(request_role_admin_create.data)
        self.assertTrue(json_data_test_admin_create_role.get('message'))
        self.assertEqual(json_data_test_admin_create_role.get('message'), 'New Role created!')
        self.assertEqual(request_role_admin_create.status_code, 200)

    def test_b_get_first_role(self):
        warnings.simplefilter("ignore")
        request_first_role = self.client().get('/api/role/1/', headers={'Content-Type': 'application/json',
                                                                        'x-access-token': self.user_admin['token']})
        json_data_first_role = json.loads(request_first_role.data)
        self.assertTrue(json_data_first_role.get('role'))
        json_role1_name = json_data_first_role.get('role')['name']
        self.assertEqual(json_role1_name, 'role_test_name1')

    def test_c_get_all_roles(self):
        warnings.simplefilter("ignore")
        request_get_all_roles = self.client().get('/api/role/', headers={'Content-Type': 'application/json',
                                                                         'x-access-token': self.user_admin['token']})
        json_data_get_all_roles = json.loads(request_get_all_roles.data)
        json_role1_name = json_data_get_all_roles.get('roles')[0]['name']
        self.assertEqual(json_role1_name, 'role_test_name1')

    def test_d_not_exist_role(self):
        warnings.simplefilter("ignore")
        request_2_role = self.client().get('/api/role/2/', headers={'Content-Type': 'application/json',
                                                                    'x-access-token': self.user_admin['token']})
        json_data_2nd_role = json.loads(request_2_role.data)
        self.assertEqual(json_data_2nd_role.get('message'), 'No role found!')

    def test_e_update_role(self):
        warnings.simplefilter("ignore")
        json_test_update_role = {'name': 'role_test_name3', 'comment': 'role_test_comment3'}
        request_update_role = self.client().put('/api/role/1/', headers={'Content-Type': 'application/json',
                                                                         'x-access-token': self.user_admin[
                                                                             'token']},
                                                data=json.dumps(json_test_update_role))
        json_data_update_role = json.loads(request_update_role.data)
        self.assertEqual(json_data_update_role.get('message'), 'role updated!')

    def tearDown(self):
        """
        Tear Down
        """
        with self.app.app_context():
            # Drop all tables
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    unittest.main()
