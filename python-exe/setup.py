from cx_Freeze import setup, Executable

setup(
    name="MA_SUPER_APPLICATION",
    version="1.0",
    description="Description de votre application",
    executables=[Executable("main.py", base="Console")],
)