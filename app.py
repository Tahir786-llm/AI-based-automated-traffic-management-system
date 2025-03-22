from flask import Flask, jsonify, render_template
from flask_graphql import GraphQLView
from flask_cors import CORS
from backend.graphql_schema import schema

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# GraphQL API Endpoint
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"}), 200

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
