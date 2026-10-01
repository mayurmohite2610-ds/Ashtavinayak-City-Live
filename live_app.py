"""Production entry point for Ashtavinayak City Live."""
from app import app, init_db, start_telegram_thread

init_db()
start_telegram_thread()
