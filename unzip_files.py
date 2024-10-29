import zipfile


def unzip_data_files(input_folder):
    for filename in os.listdir(input_folder):

        if filename.endswith(".zip"):
            zip_path = os.path.join(input_folder, filename)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(input_folder)

            print(f"Extracted {filename} to {input_folder}")