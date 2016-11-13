import unittest

from project.main.app import app


class FlaskTestCase(unittest.TestCase):
    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure view contains following string
    def test_view_contain_string(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'login' in response.data)

    # Ensure login successfull with valid credentials
    def test_success_login(self):
        tester = app.test_client(self)
        response = tester.post('/login',
                               data=dict(username='user',
                                         password='pass'),
                               follow_redirects=True)
        self.assertIn(b'you just log in', response.data)

    # Ensure require login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/',follow_redirects=True)
        self.assertTrue(b'you need to login first' in response.data)

    # Ensure
    def test_post_show_up(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="user", password="pass"),
            follow_redirects=True
        )
        self.assertIn(b'Good person', response.data)
        pass


if __name__ == '__main__':
    unittest.main()

"""
never want to mix test data with real data
"""
