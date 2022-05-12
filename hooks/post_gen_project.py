import os
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.example != "y" %} tests/testthat/test_testthat.r {% endif %}',
    '{% if cookiecutter.tests != "y" %} tests/ {% endif %}',
    '{% if cookiecutter.doc != "y" %} man/ {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        else:
            os.unlink(path)
