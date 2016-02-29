My personal site and portfolio
==============================

Static, pelican_ generated, site.

.. code-block:: bash

    # virtualenv is highly recommended
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

.. _pelican: http://docs.getpelican.com/

Download required pelican plugins, regenerate, serve, and sync the site to my server with:

.. code-block:: bash

    make get_plugins  # a must!
    make regenerate
    make serve
    make rsync_upload

Moreover, autoenv_ is really fun. Use it!

.. _autoenv: https://github.com/horosgrisa/autoenv
