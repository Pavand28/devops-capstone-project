```python
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    # Enable CORS for API requests
    CORS(app)

    # Add security headers using Talisman
    Talisman(
        app,
        force_https=False,
        content_security_policy={
            "default-src": "'self'",
            "style-src": ["'self'", "'unsafe-inline'"],
            "script-src": ["'self'"],
        },
    )

    return app
```
