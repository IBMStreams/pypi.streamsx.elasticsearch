# coding=utf-8
# Licensed Materials - Property of IBM
# Copyright IBM Corp. 2018

"""
Overview
++++++++

Provides classes and functions to store tuple data as JSON documents in Elasticsearch indices for use with Streaming Analytics service on
IBM Cloud and IBM Streams including IBM Cloud Pak for Data.

Credentials
+++++++++++

Elasticsearch credentials are defined using a Streams **application configuration** or the `Compose for Elasticsearch` **connection string**.

Setup connection string
=======================

You can connect to your *Elasticsearch cloud service* with the connection strings that is provided in the Overview tab of your service dashboard.

The connection string for the *Elasticsearch cloud service* can be applied with the ``credentials`` parameter::

    connection = 'https://<USER>:<PASSWORD>@<HOST>:<PORT>/'
    s.for_each(es.Insert(credentials=connection, index_name='test-index-cloud'))


Setup application configuration
===============================

By default an application configuration named `es` is used for the ``credentials`` parameter.
A different configuration name can be specified using the ``credentials``
parameter.

The default configuration is "es", this can be set:

* Using the "Application Configuration" tab of the "Streams Console"
* Using page selected by the sub tab "Application Configuration"
* Create a "New application configuration..." using the "Name" "es", no description is necessary
* Set the following properties for your Elasticsearch database connection: "nodeList" (value <HOST>:<PORT>), "userName", "password", "sslEnabled" (value true|false), "sslTrustAllCertificates" (value true|false)


"""

__version__='1.3.2'

__all__ = ['Insert', 'download_toolkit', 'bulk_insert', 'bulk_insert_dynamic']
from streamsx.elasticsearch._elasticsearch import Insert, download_toolkit, bulk_insert, bulk_insert_dynamic
