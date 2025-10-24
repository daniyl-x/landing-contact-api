## Configuration
Deafult config file is located at the `app/default_config.py`. \
Custom configuration should be done in the `instance/config.py`. \
`instance/` directory is created on the start of the app if not exists.

### Output data
The recieved data will be written to the `instance/OUTPUT_FILENAME`, where
OUTPUT_FILENAME is set in the config.


## Running the app
To run the app, you can use the next basic uWSGI command:
```sh
uwsgi --http 0.0.0.0:80 --master -p 4 -w app:app
```
