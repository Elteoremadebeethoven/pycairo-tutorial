def get_full_path_to_export(os,file):
    # Get file full path
    path = os.path.dirname(os.path.realpath(file))
    # Get folder name
    folder_name = os.path.basename(os.path.normpath(path))
    # Get file name
    file_name = os.path.basename(file)
    # Get root folder
    current_file = os.getcwd()
    # Get exports folder path
    main_exports_folder = os.path.join(current_file, "exports")
    # Get exports + folder_name
    export_folder = os.path.join(main_exports_folder, folder_name)
    if not os.path.isdir(export_folder):
        os.makedirs(export_folder)
    full_path = os.path.join(export_folder, file_name)
    return full_path
