#!/bin/sh
# Install project dependencies and patch django-messages for Django 5 compatibility

set -e

pip install -r requirements.txt

# Locate installed package
PKG_PATH=$(python - <<'PY'
import django_messages, os
print(os.path.dirname(django_messages.__file__))
PY
)

# Replace deprecated translation functions
sed -i \
    -e 's/ugettext_lazy/gettext_lazy/g' \
    -e 's/ugettext_noop/gettext_noop/g' \
    -e 's/ugettext/gettext/g' \
    "$PKG_PATH"/*.py

# Remove python_2_unicode_compatible decorator
sed -i '/python_2_unicode_compatible/d' "$PKG_PATH/models.py"

# Replace deprecated models.permalink
sed -i "s/from django.core.urlresolvers import reverse/from django.urls import reverse/" "$PKG_PATH"/views.py "$PKG_PATH"/tests.py

# Patch get_absolute_url implementation
sed -i "/get_absolute_url = models.permalink/d" "$PKG_PATH/models.py"

