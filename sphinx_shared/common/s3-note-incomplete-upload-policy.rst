.. admonition:: Best Practice

    As a **best practice**, we recommend that you enable the :s3-api:`AbortIncompleteMultipartUpload
    <RESTBucketPUTlifecycle>` lifecycle on your buckets.

    |S3| supports a bucket lifecycle rule that you can use to direct |S3| to abort multipart uploads
    that don't complete within a specified number of days after being initiated. When a multipart
    upload is not completed within the time frame, Amazon S3 aborts the upload and deletes the
    incomplete upload data.

    For more information, see :s3-ug:`Lifecycle Configuration for a Bucket with Versioning
    <lifecycle-configuration-bucket-with-versioning>` in the |s3-ug|.
