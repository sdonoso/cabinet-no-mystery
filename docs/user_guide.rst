Guia de Usuario (Desarrollo)
============================

Guía Básica para Montar el Proyecto
-----------------------------------

En este documentos encontraras una descripcion de la estructura del repo e instrucciones
de instalacion y como obtener los datos.

Instalacion de librerias
^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   Estamos usando Python 3.10, nada asegura que el proyecto corra con otras versiones de
   python

.. code-block:: console

   $ pip install -r requirements/base.txt
   $ pip install -r requirements/dev.txt

Setear chequeos estaticos
^^^^^^^^^^^^^^^^^^^^^^^^^

Para que los hooks de pre-commit se corran automaticamente (y que tu codigo no se caiga
inesperadamente en CI) corre

.. code-block:: console

   $ pre-commit install

Listo! Con esto, cada vez que comitees se van a correr los checks estaticos, para este
repo puedes revisar ``.pre-commit-config.yaml`` si quieres revisar cuales son.

Si quieres commitear sin que se ejecuten los hooks puedes usar la opcion
``--no-verify``, pero ahi el CI se va a caer y ojala el mergeo este bloqueado si no
funciona el CI.


Obtener los datos: DVC
^^^^^^^^^^^^^^^^^^^^^^



Testear el Proyecto
^^^^^^^^^^^^^^^^^^^


Compilación de la documentación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Para compilar la documentación:

.. code-block:: console

   $ cd docs
   $ cd make clean
   $ cd make html


Descripción de los datos raw
----------------------------

Items ``***_items.json``
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
    