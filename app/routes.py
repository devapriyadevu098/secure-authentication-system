from flask import (
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    flash,
    session,
)

from app import bcrypt
from app.auth import register_user, login_user
from app.decorators import token_required
from app.models import User
from app.validators import is_valid_email, is_strong_password


def register_routes(app):

    # ==========================
    # HOME PAGE
    # ==========================

    @app.route("/")
    def home():
        return render_template("index.html")

    # ==========================
    # REGISTER PAGE
    # ==========================

    @app.route("/register-page", methods=["GET", "POST"])
    def register_page():

        if request.method == "GET":
            return render_template("register.html")

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not username or not email or not password:
            flash("All fields are required.", "danger")
            return redirect(url_for("register_page"))

        if not is_valid_email(email):
            flash("Invalid email address.", "danger")
            return redirect(url_for("register_page"))

        if not is_strong_password(password):
            flash(
                "Password must contain uppercase, lowercase, number and special character.",
                "danger",
            )
            return redirect(url_for("register_page"))

        response, status = register_user(username, email, password)

        if status == 201:
            flash("Registration successful. Please login.", "success")
            return redirect(url_for("login_page"))

        flash(response["message"], "danger")
        return redirect(url_for("register_page"))

    # ==========================
    # LOGIN PAGE
    # ==========================

    @app.route("/login-page", methods=["GET", "POST"])
    def login_page():

        if request.method == "GET":
            return render_template("login.html")

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user is None:
            flash("Invalid email or password.", "danger")
            return redirect(url_for("login_page"))

        if not bcrypt.check_password_hash(user.password, password):
            flash("Invalid email or password.", "danger")
            return redirect(url_for("login_page"))

        session["user_id"] = user.id

        flash("Welcome back!", "success")

        return redirect(url_for("dashboard"))

    # ==========================
    # DASHBOARD
    # ==========================

    @app.route("/dashboard")
    def dashboard():

        if "user_id" not in session:
            flash("Please login first.", "warning")
            return redirect(url_for("login_page"))

        user = User.query.get(session["user_id"])

        return render_template("profile.html", user=user)

    # ==========================
    # LOGOUT
    # ==========================

    @app.route("/logout")
    def logout():

        session.clear()

        flash("Logged out successfully.", "success")

        return redirect(url_for("home"))

    # ==========================
    # API ROUTES
    # ==========================

    @app.route("/register", methods=["POST"])
    def register():

        data = request.get_json()

        if not data:
            return jsonify({"message": "Invalid JSON"}), 400

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return jsonify({"message": "All fields are required"}), 400

        if not is_valid_email(email):
            return jsonify({"message": "Invalid email address"}), 400

        if not is_strong_password(password):
            return jsonify(
                {
                    "message": "Password must be at least 8 characters and include uppercase, lowercase, digit and special character."
                }
            ), 400

        response, status = register_user(username, email, password)

        return jsonify(response), status

    @app.route("/login", methods=["POST"])
    def login():

        data = request.get_json()

        if not data:
            return jsonify({"message": "Invalid JSON"}), 400

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify(
                {"message": "Email and password are required"}
            ), 400

        response, status = login_user(email, password)

        return jsonify(response), status

    @app.route("/profile", methods=["GET"])
    @token_required
    def profile(current_user):

        return jsonify(
            {
                "id": current_user.id,
                "username": current_user.username,
                "email": current_user.email,
                "created_at": current_user.created_at.isoformat(),
            }
        ), 200