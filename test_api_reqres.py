import pytest
import requests

class TestReqResAPI:
    """Tests using reqres.in - only free endpoints"""
    
    BASE_URL = "https://reqres.in/api"
    
    def test_get_users_list(self):
        """Test GET users list"""
        response = requests.get(f"{self.BASE_URL}/users?page=2")
        
        assert response.status_code == 200
        
        data = response.json()
        assert "page" in data
        assert "data" in data
        assert len(data["data"]) > 0
        
        # Check user structure
        user = data["data"][0]
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
    
    def test_get_single_user(self):
        """Test GET single user"""
        user_id = 2
        response = requests.get(f"{self.BASE_URL}/users/{user_id}")
        
        assert response.status_code == 200
        
        data = response.json()
        assert data["data"]["id"] == user_id
        assert "@" in data["data"]["email"]


class TestHttpBinAPI:
    """Tests using httpbin.org - no authentication required"""
    
    BASE_URL = "https://httpbin.org"
    
    def test_get_json(self):
        """Test GET JSON response"""
        response = requests.get(f"{self.BASE_URL}/json")
        
        assert response.status_code == 200
        
        data = response.json()
        assert "slideshow" in data
    
    def test_post_data(self):
        """Test POST with JSON data"""
        test_data = {
            "name": "Test User",
            "job": "QA Engineer",
            "age": 30
        }
        
        response = requests.post(f"{self.BASE_URL}/post", json=test_data)
        
        assert response.status_code == 200
        
        result = response.json()
        assert "json" in result
        assert result["json"]["name"] == test_data["name"]
        assert result["json"]["job"] == test_data["job"]
    
    def test_put_data(self):
        """Test PUT request"""
        test_data = {"key": "updated_value"}
        
        response = requests.put(f"{self.BASE_URL}/put", json=test_data)
        
        assert response.status_code == 200
        
        result = response.json()
        assert "json" in result
        assert result["json"]["key"] == "updated_value"
    
    def test_delete_request(self):
        """Test DELETE request"""
        response = requests.delete(f"{self.BASE_URL}/delete")
        
        assert response.status_code == 200
        
        result = response.json()
        assert "url" in result
        assert "/delete" in result["url"]
    
    def test_get_with_params(self):
        """Test GET with query parameters"""
        params = {"name": "John", "age": "25"}
        
        response = requests.get(f"{self.BASE_URL}/get", params=params)
        
        assert response.status_code == 200
        
        result = response.json()
        assert "args" in result
        assert result["args"]["name"] == "John"
        assert result["args"]["age"] == "25"
    
    def test_response_headers(self):
        """Test response headers"""
        response = requests.get(f"{self.BASE_URL}/headers")
        
        assert response.status_code == 200
        assert "application/json" in response.headers["content-type"]
        
        result = response.json()
        assert "headers" in result
    
    def test_status_codes(self):
        """Test different status codes"""
        # Test 200
        response = requests.get(f"{self.BASE_URL}/status/200")
        assert response.status_code == 200
        
        # Test 404
        response = requests.get(f"{self.BASE_URL}/status/404")
        assert response.status_code == 404
        
        # Test 500
        response = requests.get(f"{self.BASE_URL}/status/500")
        assert response.status_code == 500
    
    def test_response_time(self):
        """Test API response time"""
        response = requests.get(f"{self.BASE_URL}/delay/1")  # 1 second delay
        
        assert response.status_code == 200
        # Should take at least 1 second but less than 3
        assert 1.0 <= response.elapsed.total_seconds() < 3.0
    
    def test_basic_auth(self):
        """Test basic authentication"""
        response = requests.get(f"{self.BASE_URL}/basic-auth/user/passwd", 
                              auth=("user", "passwd"))
        
        assert response.status_code == 200
        
        result = response.json()
        assert result["authenticated"] == True
        assert result["user"] == "user"
    
    def test_user_agent(self):
        """Test custom user agent"""
        headers = {"User-Agent": "MyTestApp/1.0"}
        response = requests.get(f"{self.BASE_URL}/user-agent", headers=headers)
        
        assert response.status_code == 200
        
        result = response.json()
        assert "MyTestApp/1.0" in result["user-agent"]