Intro
=====
This wrapper has both asynchronous & synchronous support, this intro will cover the basic of both.
Lucily for you the API for asynchronous (awaiting) & synchronous (blocking) is identical.


Getting started
---------------

**Awaiting**

.. code-block:: python

    import proxycheck

    client = proxycheck.Awaiting(
        key="..."
    )

    ip = client.ip("98.75.2.4")

    if await ip.proxy():
        print("Is proxy")
    
    risk_score = await ip.risk()
    latitude, longitude = await ip.geological()

    data = await ip.get()

    # A client should always be closed after being used!
    await client.close()


**Blocking**

.. code-block:: python

    import proxycheck

    client = proxycheck.Blocking(
        key="..."
    )

    ip = client.ip("98.75.2.4")

    if ip.proxy():
        print("Is proxy")
    
    risk_score = ip.risk()
    latitude, longitude = ip.geological()

    data = ip.get()

    # Python's garbage collector should
    # close connections correctly for Blocking.
    client.close()
