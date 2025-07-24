# CourseRec

A chatbot for TrentU students that will assist in choosing courses  

This is a full-stack web application with a **Django backend** and a **React frontend**. The backend provides a RESTful API using Django REST Framework, and the frontend is built with React and communicates with the backend via API calls.

---

## 📁 Project Structure

```
root/
├── backend/       # Django project
|   ├── conversations/
|   |   └── ...
|   ├── recommendation/
|   |   └── ...
|   ├── users/
|   |   └── ...
│   ├── courserec/
│   |   └── ...
|   ├── manage.py
|   └── .env
├── data/
|   └── ...
├── docker/
|   └── docker-compose.yml
├── frontend/      # React app (Create React App)
|   ├── courserec
|   │   ├── package.json
|   |   ├── public/
|   │   └── src/
|   │       └── ...
├── fine-tuning
|   ├── fine-tuning-gpt04mini.py
|   ├── testing-fine-tuned-model.py
├── pre-processing
|   ├── chattypeconversion.py
|   ├── question.py
|   ├── train_val_spilt.py
|   └──validate.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* Node.js 14+
* npm or yarn
* pip
* docker

### `.env` file
Create a `.env` file in the `backend` directory as show in the [Project Structure](https://github.com/HamzaGiTX786/Course-Rec/tree/master?tab=readme-ov-file#-project-structure). Inside the `.env` file store your OPENAI API key as such
```
OPENAI_API_KEY = ....
```

---

1. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## 📊  MySQL Database Setup (via Docker)

1. Navigate to the docker directory:

```bash
cd docker
```
2. Start the container
   
```bash
docker-compose -f docker-compose.yml up
```

## 🔧 Backend Setup (Django)

1. Navigate to the backend directory:

```bash
cd backend
```

2. Apply migrations and run the server:

```bash
python manage.py migrate
python manage.py runserver
```

The backend server will run at: `http://127.0.0.1:8000/`

---

## 💻 Frontend Setup (React)

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm run dev
```

The frontend will run at: `http://localhost:5173/`

---

## 🔗 Connecting Frontend and Backend

Ensure that API calls from React are directed to the correct backend URL. You can use environment variables (`.env`) or proxy settings in `package.json`:

```json
"proxy": "http://127.0.0.1:8000"
```

---

## 🛠️ Build for Production

### Backend

* Collect static files:

```bash
python manage.py collectstatic
```

### Frontend

* Build React app:

```bash
npm run build 
```

* Copy the contents of `frontend/build/` into Django's static directory or configure Django to serve it.

---
### TODO
---
## 🔪 Testing

### Backend

```bash
python manage.py test
```

### Frontend

```bash
npm test  # or yarn test
```

---

## 📄 License

This project is licensed under the MIT License

---

## 🤛️ Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## ✨ Acknowledgments

* [Django](https://www.djangoproject.com/)
* [React](https://reactjs.org/)
* [Django REST Framework](https://www.django-rest-framework.org/)
