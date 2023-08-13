def extensions(filename):
    ext = filename.split('.')[-1].lower()

    images_mime_type = ["gif", "jpg", "jpeg", "png"]
    text_mime_type = ["txt"]
    application_mime_type = ["zip", "pdf"]

    if ext in images_mime_type:
        return f"image/{ext}"
    elif ext in text_mime_type:
        return f"text/plain"
    elif ext in application_mime_type:
        return f"application/{ext}"
    else:
        return "application/octet-stream"


if __name__ == '__main__':
    # testing
    all_types = ["gif", "jpg", "jpeg", "png", "txt", "zip", "pdf", ""]
    all_files = [".".join(("bla", ext)) for ext in all_types]

    for file in all_files:
        print(f"{file:10} {extensions(file)}")
