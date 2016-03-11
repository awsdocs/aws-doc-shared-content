# Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

# _default-includes.txt contains common includes for every AWS Sphinx project.
rst_prolog = """
.. include:: _default-includes.txt
"""
# if there's a _includes.txt file in the project, automatically include it.
if os.path.exists('_includes.txt'):
    rst_prolog = rst_prolog + ('.. include:: _includes.txt\n')

