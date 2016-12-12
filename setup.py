import cx_Freeze

executables = [cx_Freeze.Executable("server.py")]

cx_Freeze.setup(
    name="2D Game",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":[]}},
    executables = executables

    )