# Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

# These are the default extlinks.
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
# For more information about specifying extlinks and how they work, see:
#
# * http://sphinx-doc.org/ext/extlinks.html

aws_docs_url = 'http://docs.aws.amazon.com/'

if 'sphinx.ext.extlinks' not in extensions:
    extensions.append('sphinx.ext.extlinks')

if 'extlinks' not in locals():
    extlinks = {}

extlinks.update({
    'cog-api': (aws_docs_url + 'cognitoidentity/latest/APIReference/API_%s.html', ''),
    'ddb-dg': (aws_docs_url + 'amazondynamodb/latest/developerguide/%s.html', ''),
    'eb-dg': (aws_docs_url + 'elasticbeanstalk/latest/dg/%s.html', ''),
    'ec2-api': (aws_docs_url + 'AWSEC2/latest/APIReference/API_%s.html', ''),
    'ec2-ug': (aws_docs_url + 'AWSEC2/latest/UserGuide/%s.html', ''),
    'emr-api': (aws_docs_url + 'ElasticMapReduce/latest/API/API_%s.html', ''),
    'github': ('https://github.com/aws/%s', ''),
    'gloss': (aws_docs_url + 'general/latest/gr/glos-chap.html#%s', ''),
    'iam-api': (aws_docs_url + 'IAM/latest/APIReference/API_%s.html', ''),
    'iam-ug': (aws_docs_url + 'IAM/latest/UserGuide/%s.html', ''),
    'java-dg': (aws_docs_url + 'AWSSdkDocsJava/latest/DeveloperGuide/%s.html', ''),
    'lam-api': (aws_docs_url + 'lambda/latest/dg/API_%s.html', ''),
    'lam-dg': (aws_docs_url + 'lambda/latest/dg/%s.html', ''),
    's3-bucket-api': (aws_docs_url + 'AmazonS3/latest/API/RESTBucket%s.html', ''),
    's3-object-api': (aws_docs_url + 'AmazonS3/latest/API/RESTObject%s.html', ''),
    's3-service-api': (aws_docs_url + 'AmazonS3/latest/API/RESTService%s.html', ''),
    'sns-api': (aws_docs_url + 'sns/latest/api/API_%s.html', ''),
    'sqs-api': (aws_docs_url + 'AWSSimpleQueueService/latest/APIReference/API_%s.html', ''),
    'sts-api': (aws_docs_url + 'STS/latest/APIReference/API_%s.html', ''),
    'swf-api': (aws_docs_url + 'amazonswf/latest/apireference/API_%s.html', ''),
    'swf-dg' : (aws_docs_url + 'amazonswf/latest/developerguide/%s.html', ''),
    'tke-ug': (aws_docs_url + 'AWSToolkitEclipse/latest/ug/%s.html', ''),
    #
    # Note: to use the 'rande' extlink, specify link text that includes the service's upper-case
    # TLA, and use the lower-case version of the TLA as the link address. For example:
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
    # Same with the console link:
    #
    #    :console`IAM console` <iam>`
    #
    'console': ('https://console.aws.amazon.com/%s/home', ''),
    })

