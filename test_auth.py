"""
Test script to verify registration and login flow
Run this after starting Django dev server: python test_auth.py
"""
import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000/api/v1"

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def test_registration(username, email, password):
    """Test user registration"""
    print_section("TESTING REGISTRATION")
    
    data = {
        "username": username,
        "email": email,
        "password": password
    }
    
    print(f"📤 Sending registration request...")
    print(f"   Username: {username}")
    print(f"   Email: {email}")
    print(f"   Password: {'*' * len(password)}")
    
    try:
        response = requests.post(
            f"{BASE_URL}/register/",
            json=data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"\n✓ Response Status: {response.status_code}")
        print(f"✓ Response Body: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 201:
            print(f"\n✅ Registration Successful!")
            return True
        else:
            print(f"\n❌ Registration Failed: {response.json()}")
            return False
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

def test_login(username, password):
    """Test user login"""
    print_section("TESTING LOGIN")
    
    data = {
        "username": username,
        "password": password
    }
    
    print(f"📤 Sending login request...")
    print(f"   Username: {username}")
    print(f"   Password: {'*' * len(password)}")
    
    try:
        response = requests.post(
            f"{BASE_URL}/login/",
            json=data,
            headers={"Content-Type": "application/json"},
            cookies={}
        )
        
        print(f"\n✓ Response Status: {response.status_code}")
        print(f"✓ Response Body: {json.dumps(response.json(), indent=2)}")
        print(f"✓ Cookies Set: {response.cookies}")
        
        if response.status_code == 200:
            print(f"\n✅ Login Successful!")
            return response.cookies
        else:
            print(f"\n❌ Login Failed: {response.json()}")
            return None
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return None

def test_protected_endpoint(cookies):
    """Test accessing protected dashboard endpoint"""
    print_section("TESTING PROTECTED ENDPOINT")
    
    print(f"📤 Sending request to protected endpoint...")
    print(f"   Using cookies: {cookies}")
    
    try:
        response = requests.get(
            f"{BASE_URL}/dashboard-protected/",
            cookies=cookies,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"\n✓ Response Status: {response.status_code}")
        print(f"✓ Response Body: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print(f"\n✅ Protected Endpoint Access Successful!")
            return True
        else:
            print(f"\n❌ Access Denied: {response.json()}")
            return False
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

def main():
    print("\n" + "🔐 " * 20)
    print("  AUTHENTICATION FLOW TEST")
    print("🔐 " * 20)
    print(f"\nStarted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Base URL: {BASE_URL}")
    
    # Test values
    username = f"testuser_{int(datetime.now().timestamp())}"
    email = f"{username}@test.com"
    password = "TestPass123"
    
    # Step 1: Register
    if test_registration(username, email, password):
        # Step 2: Login
        cookies = test_login(username, password)
        
        if cookies:
            # Step 3: Access protected endpoint
            test_protected_endpoint(cookies)
    
    print("\n" + "=" * 60)
    print("✓ Test completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
