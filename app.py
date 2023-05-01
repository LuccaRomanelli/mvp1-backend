from flask import Flask, request, jsonify, make_response
from models import Review
from database import get_db,init_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/reviews', methods=['POST'])
def create_review():
    db = get_db()
    data = request.get_json()
    review = Review(title=data['title'], year=data['year'], type=data['type'], rating=data['rating'], description=data['description'])
    db.add(review)
    db.commit()
    return jsonify({'message': 'Review created successfully!'})

@app.route('/reviews', methods=['GET'])
def get_reviews():
    db = get_db()
    reviews = db.query(Review).all()
    return jsonify([review.to_dict() for review in reviews])

@app.route('/reviews/<int:id>', methods=['DELETE'])
def delete_review(id):
    db = get_db()
    review = db.query(Review).get(id)
    if review:
        db.delete(review)
        db.commit()
        return jsonify({'message': 'Review deleted successfully!'})
    else:
        return jsonify({'error': 'Review not found.'}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
