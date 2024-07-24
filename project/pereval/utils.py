def get_media_upload_path(instance, file):
    return f'photos/pereval - {instance.pereval.id}/{file}'