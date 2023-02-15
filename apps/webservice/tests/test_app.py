from tests.conf_test import client


# perform basic tests to check the API
# impossible to test all the endpoints because they are calling the database

def test_status_code_ok(client):
	# existing endpoint
	response = client.get('/api/v1')
	assert response.status_code == 200

def test_status_code_not_ok(client):
	# incorrect endpoint
	response = client.get('/api')
	assert response.status_code == 404

def test_return_welcome(client):
	# test response
	response = client.get('/api/v1')
	data = response.data.decode()
	assert data == 'Welcome to Movie API!'
