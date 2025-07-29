import os
import uuid
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()


#  Supabase credentials

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY") 
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY) 

def upload_image_to_supabase(file):
    file_ext = os.path.splitext(file.name)[1]
    unique_filename = f"{uuid.uuid4()}{file_ext}"
    path_in_bucket = f"product/{unique_filename}"

    # Read file content from InMemoryUploadedFile
    file_content = file.read()

    # Upload file content as bytes
    response = supabase.storage.from_(SUPABASE_BUCKET).upload(
        path_in_bucket,
        file_content,
        {"content-type": file.content_type}
    )

    if hasattr(response, "error") and response.error:
        raise Exception(f"Supabase upload failed: {response.error.message}")

    public_url = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(path_in_bucket)
    return public_url





