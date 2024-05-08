# VendorManagement

Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics

## Prerequisites

- Python (version 3.10.8)
- Django (version 4.2.7)

## Installation

# 1. Clone the repository:
   bash:  
   git clone https://github.com/Anshikk/Vendor_M.git 


# 2.Install dependencies:
pip install -r requirements.txt  

# 3.Database setup:
python manage.py makemigrations  
python manage.py migrate  

# Start the server:
python manage.py runserver  

# Access API endpoints:

## Vendor API: /vendor/
Purchase Order API: /purchase-order/  
Historical Performance API: /vendor/historical_performance  

# Access token  
'/gettoken/' #provide username and password in json eg. { "username":"anshika","password":"kushwaha" }    
 
## Running Tests  
Run the test suite:  
  python manage.py test  
