import os

NAME = 'diary'
# Directory of runtime data, like logs and uploaded files etc
DATA_PATH = "~/Workshop/ArchiveAlpha/EDATRMS/api_data"
# Subdirectory of uploaded files
UPLOAD_DIR = 'uploaded'

# Listen host and port of server
HOST = '0.0.0.0'
PORT = 7000
# Whether in debug mode
DEBUG = True
# Whether to auto load modified code
AUTO_RELOAD = True
# Whether log access record
ACCESS_LOG = True
# Number of working processes
WORKERS = 1
# Valid seconds of session
SESSION_EXPIRY = 30 * 24 * 3600
# Max size of request in bytes
REQUEST_MAX_SIZE = 100 * 1024 * 1024
# Max allowed size of uploaded file in bytes
UPLOAD_FILE_MAX_SIZE = 50 * 1024 * 1024
# Max allowed number of uploaded files
UPLOAD_FILE_MAX_NUMBER = 10
# Endpoint of uploaded files
UPLOAD_FILE_URL_BASE = 'http://localhost:7000/uploaded/'

# MySQL connection parameters
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_DB = 'edatrms'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_TIMEOUT = 1
MYSQL_POOL_MIN_SIZE = 1
MYSQL_POOL_MAX_SIZE = 100

# Redis connection parameters
REDIS_URI = 'redis://@localhost:6379/1'
REDIS_TIMEOUT = 1
REDIS_POOL_MIN_SIZE = 1
REDIS_POOL_MAX_SIZE = 100