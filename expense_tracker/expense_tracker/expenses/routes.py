from flask import Blueprint, render_template, request, redirect, url_for, g, flash
from datetime import datetime
from expense_tracker.db import get_db
from expense_tracker.auth.routes import login_required

bp = Blueprint('expenses', __name__, url_prefix='/expenses')

@bp.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    transactions = db.execute(
        'SELECT t.*, c.name AS category FROM transaction t '
        'JOIN category c ON t.category_id = c.id '
        'WHERE t.user_id = ? ORDER BY t.created_at DESC',
        (g.user['id'],)
    ).fetchall()
    return render_template('expenses/dashboard.html', transactions=transactions)

@bp.route('/add', methods=('GET', 'POST'))
@login_required
def add_transaction():
    db = get_db()
    categories = db.execute('SELECT * FROM category WHERE user_id = ?', (g.user['id'],)).fetchall()

    if request.method == 'POST':
        amount = request.form['amount']
        category_id = request.form['category']
        ttype = request.form['type']
        note = request.form['note']

        if not amount or not category_id:
            flash("Please provide amount and category.")
        else:
            db.execute(
                'INSERT INTO transaction (amount, type, category_id, user_id, created_at, note) '
                'VALUES (?, ?, ?, ?, ?, ?)',
                (amount, ttype, category_id, g.user['id'], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), note)
            )
            db.commit()
            return redirect(url_for('expenses.dashboard'))

    return render_template('expenses/add_transaction.html', categories=categories)
