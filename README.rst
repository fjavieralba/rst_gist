rst_gist
########

This small piece of code is an rst directive that allows you to embed Github Gist snippets in your rst_ docs. This can be used in Pelican_ blog generator since it uses rst as it source for generating pages.

Usage
-----

::

    .. gist:: <GIST_ID> <FILENAME>


To know your ``GIST_ID`` and ``FILENAME`` simply go to your gist in githube and click on *"embed"* option. The HTML you see contains your ``GIST_ID`` and ``FILENAME``: ``<script src="https://gist.github.com/<GIST_ID>.js?file=<FILENAME>"></script>``

Install on Pelican
------------------

If you want to easily embed gists snippets in your pelican blog, all you have to do is:

 - Download the gistdirective.py file
 - Download the pelican code
 - Add gistdirective.py to the ``pelican/pelican`` folder
 - Modify the file ``pelican/pelican/readers.py`` and add the following import:

    ::

       from pelican import gistdirective

 - Install pelican from source:

    ::

       $ cd <pelican_home>
       $ python setup.py install

And voilà, you can use gist directive to embed your snippets.

.. _rst: http://docutils.sourceforge.net/rst.html
.. _Pelican: http://blog.notmyidea.org/pelican-a-simple-static-blog-generator-in-python.html

