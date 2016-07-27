# Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

# External link (intersphinx + extlink) definitions

# this is used throughout.
aws_docs_url = 'http://docs.aws.amazon.com/'

# intersphinx locations - with these, you can specify :ref: links directly into
# various guides. For example:
#
#  :ref:`Allow Lambda to assume an IAM role <tke-ug:allow-lam-to-assume-an-iam-role>`
#
# You just specify the guide name as the first parameter in the <link>, and
# then the reference name as the second parameter.
#
# For more information, see: http://www.sphinx-doc.org/en/stable/ext/intersphinx.html

if 'sphinx.ext.intersphinx' not in extensions:
    extensions.append('sphinx.ext.intersphinx')

if 'intersphinx_mapping' not in locals():
    intersphinx_mapping = {}

intersphinx_mapping.update({
    'androiddg': (aws_docs_url + '/mobile/sdkforandroid/developerguide', None),
    'iosdg': (aws_docs_url + '/mobile/sdkforios/developerguide', None),
    'javadg': (aws_docs_url + 'java-sdk/latest/developer-guide', None),
    'tkeug': (aws_docs_url + 'eclipse-toolkit/latest/user-guide', None),
    'unitydg': (aws_docs_url + '/mobile/sdkforunity/developerguide', None),
    'xamarindg': (aws_docs_url + '/mobile/sdkforxamarin/developerguide', None),
    })

# default extlinks.
#
# You can use them in your document source by specifying a link to an API entry like this::
#
#     The :swf-api:`DescribeWorkflowExecution` action returns the taskPriority
#     of the workflow.
#
# A link will be created to the SWF API reference, pointing to the action described in the role's
# text.
#
# You can also specify link text that's different from the link address by enclosing the address in
# angle-brackets, such as:
#
#    :rande:`SWF <swf>`
#
# This is useful when the link address is cased differently than the desired output text, or when
# you want the link to appear differently than the standard presentation.
#
# The links in this file are meant to be available to all guides and shared among them. To add
# non-shared or more specific extlinks of your own, add them to the end of your ``conf.py`` file
# like this::
#
#     extlinks['my-link-role'] = ('link_url', 'link_prefix')
#
# For more information, see: http://sphinx-doc.org/ext/extlinks.html

if 'sphinx.ext.extlinks' not in extensions:
    extensions.append('sphinx.ext.extlinks')

if 'extlinks' not in locals():
    extlinks = {}

# a function to add guide extlinks
def get_guide_extlinks():
    """add extlinks for all of the entries in ../_includes/guide_links.txt"""
    import re
    guide_extlinks = {}
    guide_links_file = open('_includes/guide_links.txt')
    guide_links_contents = guide_links_file.read()
    guide_links_file.close()
    m = '.. _(.*):\s+(.*)/'
    matches = re.findall(m, guide_links_contents)
    for i in matches:
        if 'sdk-net-api' in i[0]:
            guide_extlinks[str.lower(i[0])] = (i[1] + '/items/%s.html', '')
        else:
            guide_extlinks[str.lower(i[0])] = (i[1] + '/%s.html', '')
    return guide_extlinks

extlinks.update(get_guide_extlinks())

# the only things that should be here are extlinks that don't fit the standard
# pattern of 'guide_url/%s.html'
extlinks.update({
    # links to API pages or other non-standard guide links.
    'cog-api': (aws_docs_url + 'cognitoidentity/latest/APIReference/API_%s.html', ''),
    'ec2-api': (aws_docs_url + 'AWSEC2/latest/APIReference/API_%s.html', ''),
    'emr-api': (aws_docs_url + 'ElasticMapReduce/latest/API/API_%s.html', ''),
    'github': ('https://github.com/%s', ''),
    'gloss': (aws_docs_url + 'general/latest/gr/glos-chap.html#%s', ''),
    'iam-api': (aws_docs_url + 'IAM/latest/APIReference/API_%s.html', ''),
    'lam-api': (aws_docs_url + 'lambda/latest/dg/API_%s.html', ''),
    'r53-api': (aws_docs_url + 'Route53/latest/APIReference/API_%s.html', ''),
    's3-bucket-api': (aws_docs_url + 'AmazonS3/latest/API/RESTBucket%s.html', ''),
    's3-object-api': (aws_docs_url + 'AmazonS3/latest/API/RESTObject%s.html', ''),
    's3-service-api': (aws_docs_url + 'AmazonS3/latest/API/RESTService%s.html', ''),
    'sns-api': (aws_docs_url + 'sns/latest/api/API_%s.html', ''),
    'sqs-api': (aws_docs_url + 'AWSSimpleQueueService/latest/APIReference/API_%s.html', ''),
    'sts-api': (aws_docs_url + 'STS/latest/APIReference/API_%s.html', ''),
    'swf-api': (aws_docs_url + 'amazonswf/latest/apireference/API_%s.html', ''),

    #
    # Note: to use the 'rande' or 'console' extlinks, specify link text that
    # includes the service's upper-case TLA, and use the lower-case version of
    # the TLA as the link address. For example:
    #
    #    :rande:`Regions and Endpoints: SWF <swf>`
    #
    # Which will render as:
    #
    #   Regions and Endpoints: SWF
    #
    # and link to:
    #
    #   http://docs.aws.amazon.com/general/latest/gr/rande.html#swf_region
    #
    'rande': (aws_docs_url + 'general/latest/gr/rande.html#%s_region', ''),
    #
    #    :console:`IAM console <iam>`
    #
    'console': ('https://console.aws.amazon.com/%s', ''),
    #
    # For AWS forums. Use like this:
    #
    #    :forum:`Mobile Developer forum <88>`
    #
    'forum': ('http://forums.aws.amazon.com/forum.jspa?forumID=%s', ''),
    })

