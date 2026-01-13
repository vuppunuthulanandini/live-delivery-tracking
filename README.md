# live-delivery-tracking
Developed a real-time delivery tracking system with Flask, SQLite, and Leaflet.js, featuring live driver location streaming and LLM-based human-readable ETA messages, demonstrating skills in AI integration, full-stack development, and real-time data pipelines.
The Live Delivery Tracking System is a full-stack project that simulates a real-time delivery tracking platform similar to Uber or Swiggy. It demonstrates the integration of live data streaming, backend APIs, and LLM-based intelligent features, showcasing my capabilities in building AI-powered applications and handling dynamic real-world data.

In this project, simulated drivers send their live location updates every few seconds to a Flask-based backend API. The backend stores this data in an SQLite database and calculates the Estimated Time of Arrival (ETA) to the destination. To enhance user experience, I integrated a small LLM-based function that converts the raw ETA into human-readable messages, such as “Driver 101 is on the way. Estimated arrival: 7 minutes,” demonstrating practical usage of language models for intelligent notifications. This highlights my ability to combine AI/LLM technologies with real-time data processing.

The frontend is built using HTML, CSS, and JavaScript, leveraging Leaflet.js for interactive map visualization. The map fetches the latest driver location from the backend API every 2 seconds, creating a smooth live tracking experience for users. This implementation emphasizes my knowledge of real-time data streaming, API integration, and frontend-backend communication.

Key technical skills demonstrated include:

Python Flask for backend API development

SQLite for efficient data storage

REST API design for real-time communication

Live data streaming handling from multiple simulated drivers

LLM-based message generation for user-friendly ETA notifications

Frontend visualization using Leaflet.js

This project showcases my ability to build end-to-end AI-powered systems, integrating real-time data pipelines, full-stack development, and LLM capabilities. It is a scalable foundation that can be extended with features like multiple drivers, traffic prediction, dynamic routing, or enhanced LLM-powered notifications, making it a strong demonstration of both technical skill and creativity.

Overall, this project highlights my expertise in AI integration, live streaming, and full-stack engineering, making it a valuable addition to my portfolio and a strong talking point for recruiters or internships in AI, data engineering, or software development.
this is the project structure:
live_delivery_project/
│
├── backend/
│   ├── app.py                 # Main Flask/FastAPI app (API routes)
│   ├── db.py                  # Database connection & queries
│   ├── eta.py                 # ETA calculation logic
│   ├── llm.py                 # AI / LLM based response or prediction logic
│   ├── config.py              # App configuration (DB path, secrets)
│   ├── requirements.txt       # Backend dependencies
│   ├── .env                   # Environment variables (DO NOT PUSH)
│   │
│   ├── templates/
│   │   └── map.html            # Live map UI (delivery tracking)
│   │
│   └── __pycache__/            # Auto-generated (DO NOT PUSH)
│
├── driver_simulator/
│   └── driver.py               # Simulates delivery agent GPS updates
│
├── database/
│   ├── delivery.db             # SQLite database (optional to push)
│   └── schema.sql              # DB schema (tables)
│
├── docs/
│   ├── api_flow.md             # API flow explanation
│   ├── architecture.md         # System design
│
├── tests/
│   ├── test_eta.py
│   └── test_api.py
│
├── .gitignore                  # Ignore env, pycache, db
├── README.md                   # Project overview (VERY IMPORTANT)
└── run.sh / run.bat             # Start script



