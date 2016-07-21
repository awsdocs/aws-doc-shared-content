# Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

# Although you can include files like this:
#
#  .. include _includes/common_includes.txt
#
# Adding this to the rst_prolog would break includes for topics that exist
# in subdirectories of the 'source' directory.
#
# Instead, we simply gather the information that exists in the default include
# locations and make *that* the rst_prolog.

import os, codecs

rst_prolog = ''

common_includes = [
    '_includes/common_includes.txt',
    '_includes/guide_links.txt',
    '_includes/service_links.txt',
    '_includes/region_includes.txt',
    '_includes.txt'
    ]

for i in common_includes:
    if os.path.exists(i):
        f = codecs.open(i, 'r', 'utf-8')
        rst_prolog += f.read()
        f.close()

print("NOTE: %d lines in rst_prolog." % (rst_prolog.count('\n')+1))
print("      Line numbers will be off by this amount!")

