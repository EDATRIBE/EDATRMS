import os

# Directory of runtime data, like logs and uploaded files etc
DATA_PATH = os.path.expanduser("~/Workshop/ArchiveAlpha/EDATRMS/api/api_data")


# Subdirectory of logs
# (Must be created manually before the first boot)
LOGS_DIR = "logs"

# Subdirectory of semi-static files like .md etc
# (Must be created manually before the first boot)
ANNOUNCEMENTS_DIR = "announcements"
ANNOUNCEMENTS_ORDER_PREFIX = "@"


# Max allowed size of uploaded file in bytes
UPLOAD_FILE_MAX_SIZE = 50 * 1024 * 1024
# Max allowed number of uploaded files
UPLOAD_FILE_MAX_NUMBER = 10
# Subdirectory of files uploaded to 'local' region
LOCAL_FILES_DIR = "local"
# LOCAL_FILES_URL_BASE = 'http://localhost:7000/local/'
LOCAL_FILES_URL_BASE = "api/local/"
