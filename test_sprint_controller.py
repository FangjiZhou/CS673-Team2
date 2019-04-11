import unittest
import json
from app import db, app
import warnings

'''
To run test successfully, plz delete your local app.db first
'''

class SprintTest(unittest.TestCase):
    """
      Sprint Test Case
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

        # Create a company
        json_test_company = {'name': 'company_test_name1', 'comment': 'company_test_comment1'}
        self.client().post('/api/company/', headers={'Content-Type': 'application/json',
                                                     'x-access-token': self.user_admin[
                                                         'token']},
                           data=json.dumps(json_test_company))

        # Create a project
        json_test_project = {
            "name": "project_test_name1",
            "start_date": "2019-04-8 00:00:00",
            "due_date": "2019-5-30 00:00:00",
            "comment": "project_test_comment1",
            "company_id": 1
        }
        self.client().post('/api/project/', headers={'Content-Type': 'application/json',
                                                     'x-access-token': self.user_admin[
                                                         'token']},
                           data=json.dumps(json_test_project))

        # create a sprint
        json_test_sprint1 = {
            "name": "sprint_test_name1",
            "start_date": "2019-04-1 00:00:00",
            "due_date": "2019-04-15 00:00:00",
            "comment": "sprint_test_comment1",
            "project_id": 1
        }
        self.client().post('/api/sprint/', headers={'Content-Type': 'application/json',
                                                    'x-access-token': self.user_admin[
                                                        'token']},
                           data=json.dumps(json_test_sprint1))

    def test_a_create_sprint(self):
        warnings.simplefilter("ignore")
        json_test_sprint2 = {
            "name": "sprint_test_name2",
            "start_date": "2019-04-1 00:00:00",
            "due_date": "2019-04-15 00:00:00",
            "comment": "sprint_test_comment2",
            "project_id": 1
        }
        request_sprint_create = self.client().post('/api/sprint/', headers={'Content-Type': 'application/json',
                                                                              'x-access-token': self.user_admin[
                                                                                  'token']},
                                                       data=json.dumps(json_test_sprint2))
        json_data_test_create_sprint = json.loads(request_sprint_create.data)
        self.assertEqual(json_data_test_create_sprint.get('message'), 'New sprint created!')

    def test_b_update_sprint(self):
        warnings.simplefilter("ignore")
        json_test_update_sprint = {
            "name": "sprint_test_name3",
            "start_date": "2019-05-1 00:00:00",
            "due_date": "2019-05-15 00:00:00"
        }
        request_update_sprint = self.client().put('/api/sprint/1/', headers={'Content-Type': 'application/json',
                                                                            'x-access-token': self.user_admin[
                                                                                'token']},
                                                   data=json.dumps(json_test_update_sprint))
        json_data_test_update_sprint = json.loads(request_update_sprint.data)
        print(json_data_test_update_sprint)
        self.assertEqual(json_data_test_update_sprint.get('message'), 'sprint updated!')

    def test_c_get_all_sprints(self):
        warnings.simplefilter("ignore")
        request_get_all_sprints = self.client().get('/api/sprint/', headers={'Content-Type': 'application/json',
                                                                             'x-access-token': self.user_admin[
                                                                                 'token']}  )
        json_data_test_update_sprint = json.loads(request_get_all_sprints.data)
        res=json_data_test_update_sprint['sprints'][0]['name']
        self.assertEqual(res, 'sprint_test_name1')

    def test_d_get_first_sprint(self):
        warnings.simplefilter("ignore")
        request_get_1st_sprints = self.client().get('/api/sprint/1/', headers={'Content-Type': 'application/json',
                                                                             'x-access-token': self.user_admin[
                                                                                 'token']}  )
        json_data_get_1st_sprint = json.loads(request_get_1st_sprints.data)
        res=json_data_get_1st_sprint['sprint']['name']
        self.assertEqual(res, 'sprint_test_name1')

    def test_e_get_not_exist_sprint(self):
        warnings.simplefilter("ignore")
        request_get_non_exist_sprints = self.client().get('/api/sprint/2/', headers={'Content-Type': 'application/json',
                                                                             'x-access-token': self.user_admin[
                                                                                 'token']}  )
        json_data_get_non_exist_sprint = json.loads(request_get_non_exist_sprints.data)
        res=json_data_get_non_exist_sprint['message']
        self.assertEqual(res, 'No sprint found!')

    def test_f_get_sprint_from_project1(self):
        warnings.simplefilter("ignore")
        request_get_sprint_from_project1 = self.client().get('/api/sprint/project/1/', headers={'Content-Type': 'application/json',
                                                                             'x-access-token': self.user_admin[
                                                                                 'token']}  )
        json_data_sprint_from_project1 = json.loads(request_get_sprint_from_project1.data)
        res=json_data_sprint_from_project1
        self.assertEqual(res, 'sprint_test_name1')



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
