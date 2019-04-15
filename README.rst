My personal site and portfolio
==============================

Static, pelican_ generated, site.

.. code-block:: bash

    make get_plugins       # only once
    pip install pip-tools  # only once (preferabely in a virtualenv)
    pip-sync               # only once
    make regenerate
    make serve
