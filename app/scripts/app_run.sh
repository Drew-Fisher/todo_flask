echo running ${FLASK_ENVIORMENT}
if [[ ${FLASK_ENVIORMENT} == "local" ]]
then
    flask --app app.py --debug run --host=0.0.0.0 --port=5000
else
    gunicorn -w 4 -b
fi
