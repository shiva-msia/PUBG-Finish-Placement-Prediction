create_db: config/config.yml
	python run.py create_db --user root --password <password>
generate_features: config/config.yml
	python run.py generate_features --config=config/config.yml --user root --password <password>
train_model: config.yml
	python run.py train_model --config=config/config.yml
score_model: config/config.yml
	python run.py score_model --config=config/config.yml
evaluate_model: config/config.yml
	python run.py evaluate_model --config=config/config.yml

# Run the Flask application
app: app/app.py
	python run.py app