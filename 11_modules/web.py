# Fullstack - API (DS/DA)
import requests # ModuleNotFoundError: No module named 'requests'

response_status = requests.get('https://www.python.org/')
print(response_status)

response_status = requests.get('https://www.python.org/ravi')
print(response_status)
