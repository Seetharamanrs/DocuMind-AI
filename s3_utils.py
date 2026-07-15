# This code snippet for the AWS deployment
import boto3

import boto3

BUCKET_NAME = "documind-ai-storage-668855907104-ap-south-1-an"

s3 = boto3.client(
    "s3",
    region_name="ap-south-1"
)
BUCKET_NAME = "documind-ai-storage"

PDF_KEY = "documents/policy_document.pdf"

FAISS_KEY = "vector_store/faiss_index.bin"

CHUNKS_KEY = "vector_store/chunks.pkl"


def upload_file(local_path, s3_key):
    """
    Upload any file from EC2 to S3.
    """

    s3.upload_file(
        local_path,
        BUCKET_NAME,
        s3_key
    )


def download_file(s3_key, local_path):
    """
    Download any file from S3 to EC2.
    """

    s3.download_file(
        BUCKET_NAME,
        s3_key,
        local_path
    )
def upload_vector_store():

    upload_file(
        "vector_store/faiss_index.bin",
        "vector_store/faiss_index.bin"
    )

    upload_file(
        "vector_store/chunks.pkl",
        "vector_store/chunks.pkl"
    )


def download_vector_store():

    download_file(
        "vector_store/faiss_index.bin",
        "vector_store/faiss_index.bin"
    )

    download_file(
        "vector_store/chunks.pkl",
        "vector_store/chunks.pkl"
    )