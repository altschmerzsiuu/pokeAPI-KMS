# Simple Pokémon CRUD API

A simple CRUD API built with **FastAPI** using **PokéAPI** as an external Pokémon data source.

This project was made as a simple API exercise using a framework that I am familiar with.

---

## 🚀 Quick Access

If you want to try the API directly without running the project locally, you can open the interactive Swagger documentation below:

**Live Swagger Documentation:**
https://ominous-telegram-wr5755xj4rvq29gvx-8000.app.github.dev/docs

> The live documentation is available only while the development server is running.

For local development, Swagger is available at:

```
http://localhost:8000/docs
```

---

## 🧰 Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Server:** Uvicorn
- **HTTP Client:** Requests
- **Data Validation:** Pydantic
- **External Data Source:** PokéAPI

---

## 📖 What This API Does

This API has two main parts:

### 1. PokéAPI Integration

The API can fetch Pokémon data directly from PokéAPI using a Pokémon name.

Example:

```http
GET /pokemon/pikachu
```

### 2. Local CRUD API

The API also provides simple CRUD operations for Pokémon records stored locally in memory.

The available operations are:

- Create Pokémon
- Read all Pokémon
- Read one Pokémon by ID
- Update Pokémon
- Delete Pokémon

> **Note on Persistence:**
> The local CRUD data is currently stored in memory using a Python list. This means the data will be reset whenever the application restarts.

---

## 🔌 API Endpoints

### 1. Get Pokémon from PokéAPI

```http
GET /pokemon/{name}
```

Fetches Pokémon data directly from PokéAPI.

**Example**

```http
GET /pokemon/pikachu
```

You can also try:

```http
GET /pokemon/ditto
```

**Successful Response**

The response contains the Pokémon data returned by PokéAPI.

**If Pokémon is not found**

The API returns:

```json
{
  "detail": "Data Tidak Ditemukan!"
}
```

with HTTP status `404 Not Found`.

---

### 2. Local CRUD Operations

The following endpoints manage Pokémon records stored in the application's memory.

#### Create Pokémon

```http
POST /pokemon
```

Creates a new Pokémon record. The ID is generated automatically by the application.

**Request Body**

```json
{
  "name": "pikachu",
  "weight": 60,
  "height": 4
}
```

**Example Response**

```json
{
  "id": 1,
  "name": "pikachu",
  "weight": 60,
  "height": 4
}
```

#### Get All Pokémon

```http
GET /pokemon
```

Returns all Pokémon currently stored in memory.

**Example Response**

```json
[
  {
    "id": 1,
    "name": "pikachu",
    "weight": 60,
    "height": 4
  },
  {
    "id": 2,
    "name": "ditto",
    "weight": 40,
    "height": 3
  }
]
```

#### Get Pokémon by ID

```http
GET /pokemon/id/{id}
```

Returns a single Pokémon from the local data by its ID.

**Example**

```http
GET /pokemon/id/1
```

**Example Response**

```json
{
  "id": 1,
  "name": "pikachu",
  "weight": 60,
  "height": 4
}
```

If the ID does not exist, the API returns:

```json
{
  "detail": "Maaf nie, Data tidak ditemukan"
}
```

with HTTP status `404 Not Found`.

#### Update Pokémon

```http
PUT /pokemon/id/{id}
```

Updates an existing Pokémon by ID.

**Example**

```http
PUT /pokemon/id/1
```

**Request Body**

```json
{
  "name": "pikachu-updated",
  "weight": 65,
  "height": 5
}
```

**Example Response**

```json
{
  "id": 1,
  "name": "pikachu-updated",
  "weight": 65,
  "height": 5
}
```

The Pokémon ID remains the same while the other fields are updated.

If the ID does not exist, the API returns `404 Not Found`.

#### Delete Pokémon

```http
DELETE /pokemon/id/{id}
```

Deletes a local Pokémon by ID.

**Example**

```http
DELETE /pokemon/id/1
```

**Example Response**

```json
{
  "id": 1,
  "name": "pikachu",
  "weight": 60,
  "height": 4
}
```

After deletion, the Pokémon will no longer appear in `GET /pokemon` or `GET /pokemon/id/1`.

---

## 🧪 Trying the API with Swagger

The easiest way to test the API is through FastAPI's built-in Swagger UI.

**Local**

After running the server, open:

```
http://localhost:8000/docs
```

**Live**

You can also use the live Swagger documentation:

https://ominous-telegram-wr5755xj4rvq29gvx-8000.app.github.dev/docs

From Swagger, you can:

1. Select an endpoint.
2. Click **Try it out**.
3. Fill in the required parameters or request body.
4. Click **Execute**.
5. Check the response and status code.

---

## 🔄 Simple CRUD Flow

A simple way to test the CRUD flow is:

**1. Create**

```http
POST /pokemon
```

```json
{
  "name": "pikachu",
  "weight": 60,
  "height": 4
}
```

**2. Read**

```http
GET /pokemon
```

**3. Read by ID**

```http
GET /pokemon/id/1
```

**4. Update**

```http
PUT /pokemon/id/1
```

```json
{
  "name": "pikachu-updated",
  "weight": 65,
  "height": 5
}
```

**5. Delete**

```http
DELETE /pokemon/id/1
```

**6. Verify**

```http
GET /pokemon/id/1
```

The last request should return `404 Not Found` because the Pokémon has already been deleted.

---

## 🛠️ How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd pokeAPI-KMS
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

## 📁 Project Structure

```
pokeAPI-KMS/
│
├── app/
│   └── main.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
```

`venv/` is only used for the local Python environment and is excluded from Git through `.gitignore`.

---

## 📝 Notes

- PokéAPI is used as an external data source for Pokémon lookup.
- The local CRUD operations use an in-memory Python list.
- No database is used in this version because the task only requires a simple CRUD API.
- Created, updated, and deleted local records will be reset when the application restarts.
- IDs are generated automatically based on the highest existing ID.

---

## 📌 Error Handling

The API currently handles common cases such as:

| Case | Status |
|------|--------|
| Pokémon not found (PokéAPI) | `404 Not Found` |
| Local Pokémon ID not found | `404 Not Found` |
| Invalid request body | `422 Unprocessable Entity` |

For invalid request bodies, FastAPI/Pydantic automatically validates the input and returns `422 Unprocessable Entity` when the request does not match the expected data structure.

### Example Request Model

The local CRUD endpoints expect:

```json
{
  "name": "pikachu",
  "weight": 60,
  "height": 4
}
```

Where:

- `name` → string
- `weight` → number
- `height` → number

---
