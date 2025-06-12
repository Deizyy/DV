from flask import Blueprint, render_template, request, redirect, url_for
from models import accounts, get_account_by_number

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def home():
    return render_template('home.html', accounts=accounts)

@home_bp.route('/balance', methods=['GET'])
def balance():
    account_number = request.args.get('account_number')
    account = get_account_by_number(account_number)
    if account:
        return f"יתרת חשבון {account.account_number}: {account.balance} ש\"ח"
    return "חשבון לא נמצא"

@home_bp.route('/deposit', methods=['POST'])
def deposit():
    account_number = request.form.get('account_number')
    amount = float(request.form.get('amount', 0))
    account = get_account_by_number(account_number)
    if account:
        account.balance += amount
        return f"הופקדו {amount} ש\"ח לחשבון {account.account_number}. יתרה חדשה: {account.balance}"
    return "חשבון לא נמצא"

@home_bp.route('/withdraw', methods=['POST'])
def withdraw():
    account_number = request.form.get('account_number')
    amount = float(request.form.get('amount', 0))
    account = get_account_by_number(account_number)
    if account:
        if account.balance >= amount:
            account.balance -= amount
            return f"נמשכו {amount} ש\"ח מהחשבון {account.account_number}. יתרה חדשה: {account.balance}"
        else:
            return "יתרה לא מספיקה"
    return "חשבון לא נמצא"
