My personal site and portfolio
==============================

Static, pelican_ generated, site. I tend to use conda_ recently. Create and activate your environment with:

.. code-block:: bash

    conda env create -f environment.yml
    conda activate tomgurion.me

.. _pelican: http://docs.getpelican.com/
.. _conda: http://conda.pydata.org/

Download required pelican plugins, regenerate, serve, and sync the site to my server with:

.. code-block:: bash

    make get_plugins  # a must!
    make regenerate
    make serve
    make rsync_upload

Feeling extra fency? use the git hook to sync the site automatically on every push to github:

.. code-block:: bash

    cp git_hooks/pre-push .git/hooks
    chmod +x .git/hooks/pre-push

Moreover, autoenv_ is really fun. Use it!

.. _autoenv: https://github.com/horosgrisa/autoenv
