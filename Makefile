run:
	uvicorn src.main:app --reload

a_rev:
	alembic revision --autogenerate -m "Initial tables"

a_up_head:
	alembic upgrade head
