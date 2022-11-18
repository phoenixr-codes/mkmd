****
mkmd
****

============
Installation
============

.. code-block:: bash
    
    pip install mkmd


==========
Quickstart
==========

.. code-block::
    
    import mkmd
    
    with mkmd.Markdown("document.md") as md:
         md.add_heading("Welcome")
         md.add_paragraph("Thank you for using mkmd!")


===
API
===

----
mkmd
----

.. automodule:: mkmd


----------
mkmd.utils
----------

.. automodule:: mkmd.utils
