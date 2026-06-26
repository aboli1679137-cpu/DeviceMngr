from app import app, init_db
init_db()
print("Database initialized and ready.")

# Quick API test
app.testing = True
client = app.test_client()

# Test dashboard
r = client.get('/api/dashboard')
assert r.status_code == 200
d = r.get_json()
print(f"Dashboard: OK ({d['total']} systems)")

# Test page renders
pages = ['/', '/add-system', '/systems', '/systems/customer', '/systems/for-sale', '/systems/internal', '/repair', '/settings']
for p in pages:
    r = client.get(p)
    assert r.status_code == 200, f"Failed: {p}"
print(f"All {len(pages)} pages render correctly")

import os
os.remove(app.config['DATABASE'])
print("Cleanup done. ALL CHECKS PASSED")
