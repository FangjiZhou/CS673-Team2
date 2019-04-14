import unittest
import json
from app import db, app
import warnings


class RoleTest(unittest.TestCase):
    """
      team Test Case
      by Duo chen
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
        json_admin_user = {"name": "chenduo", "email": "chenduo@gmail.com",
                           "password": "chenduo", "admin": True,
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

        # Create test company
        json_test_company = {'name': 'companyA', 'comment': 'companyA'}
        self.client().post('/api/company/', headers={'Content-Type': 'application/json',
                                                     'x-access-token': self.user_admin[
                                                         'token']},
                           data=json.dumps(json_test_company))
        json_test_team1 = {'name': 'team 1', 'comment': 'team 1 comment', 'company_id': 1}
        self.client().post('/api/team/', headers={'Content-Type': 'application/json',
                                                  'x-access-token': self.user_admin[
                                                      'token']},
                           data=json.dumps(json_test_team1))

    def test_create_team(self):
        """ test team creation with admin account """
        warnings.simplefilter("ignore")
        json_test_team2 = {'name': 'team 2', 'comment': 'team 2 comment', 'company_id': 1}
        request_team_admin_create_1 = self.client().post('/api/team/', headers={'Content-Type': 'application/json',
                                                                              'x-access-token': self.user_admin[
                                                                                  'token']},
                                                       data=json.dumps(json_test_team2))

        json_data_test_admin_create_team = json.loads(request_team_admin_create_1.data)
        self.assertTrue(json_data_test_admin_create_team.get('message'))
        self.assertEqual(json_data_test_admin_create_team.get('message'), 'New Team created!')
        self.assertEqual(request_team_admin_create_1.status_code, 200)

        json_test_team3 = {'name': 'team 3', 'comment': 'team 3 comment', 'company_id': 2}
        request_team_admin_create_2 = self.client().post('/api/team/', headers={'Content-Type': 'application/json',
                                                                                'x-access-token': self.user_admin[
                                                                                    'token']},
                                                         data=json.dumps(json_test_team3))
        json_data_test_admin_create_team_with_wrong_company = json.loads(request_team_admin_create_2.data)
        self.assertTrue(json_data_test_admin_create_team_with_wrong_company.get('message'))
        self.assertEqual(json_data_test_admin_create_team_with_wrong_company.get('message'), 'No Company found with '
                                                                                             'id 2')

    def test_get_first_team(self):
        warnings.simplefilter("ignore")
        request_first_team = self.client().get('/api/team/1/', headers={'Content-Type': 'application/json',
                                                                        'x-access-token': self.user_admin['token']})
        json_data_first_team = json.loads(request_first_team.data)

        self.assertTrue(json_data_first_team.get('team'))
        json_team1_name = json_data_first_team.get('team')['name']
        self.assertEqual(json_team1_name, 'team 1')

    def test_get_all_team(self):
        warnings.simplefilter("ignore")
        request_get_all_team = self.client().get('/api/team/', headers={'Content-Type': 'application/json',
                                                                        'x-access-token': self.user_admin['token']})
        json_data_get_all_team = json.loads(request_get_all_team.data)
        json_team_name = json_data_get_all_team.get('teams')[0]['name']
        self.assertEqual(json_team_name, 'team 1')

    def test_e_update_role(self):
        warnings.simplefilter("ignore")
        json_test_update_team = {'name': 'team 4', 'comment': 'team comment5'}
        request_update_team = self.client().put('/api/team/1/', headers={'Content-Type': 'application/json',
                                                                         'x-access-token': self.user_admin[
                                                                             'token']},
                                                data=json.dumps(json_test_update_team))
        json_data_update_team = json.loads(request_update_team.data)
        self.assertEqual(json_data_update_team.get('message'), 'team updated!')

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
