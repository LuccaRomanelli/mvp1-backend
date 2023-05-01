# MVP 1 de Lucca Romanelli

Esse é um projeto com o intuito de ser aprovado na sprint 1 da pos graduação Puc-Rio do curso de desenvolvimento full stack

## Instalação

Use o package manager [pip](https://pip.pypa.io/en/stable/) para instalar.

```bash
pip install -r requirements.txt
```
Ou ative o venv

```bash
.\venv\Scripts\activate 
```

## Iniciar o programa

```python
python app.py

```

## Endpoints
POST /reviews
Create a new review.

Request body
```json
{
  "title": "The Shawshank Redemption",
  "year": 1994,
  "type": "movie",
  "rating": 9,
  "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
}
```
Response
```json
{
  "message": "Review created successfully!"
}
```
GET /reviews
List all reviews.

Response
```json
[
  {
    "id": 1,
    "title": "The Shawshank Redemption",
    "year": 1994,
    "type": "movie",
    "rating": 9,
    "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
  }
]
```

DELETE /reviews/{id}
Delete a review by id.

Response
```json
{
  "message": "Review deleted successfully!"
}
```
## Database
The API uses a SQLite database, which is created and initialized on startup. The database file is named reviews.db.