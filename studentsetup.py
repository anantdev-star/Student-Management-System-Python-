from cx_Freeze import*
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table ={
    ("Desktopshortcut", 
    "DesktopFolder",
    "StudentManagementSysytemComplete",
    "TARGETDIR",
    "[TARGETDIR]\StudentManagementSysytemComplete.exe",
    None,
    None,
    None,
    None,
    None,
    None,
    "TARGETDIR"
    )
}
msi_data = {"Shortcut":shortcut_table}

bdist_msi_options = {'data':msi_data}
setup(
    version="0.1",
    description="Student Management Sysytem Developed By Anant Dubey",
    author="Anant Dubey",
    name = "Student Management Sysytem",
    executables=[
        Executable(
            script="StudentManagementSysytemComplete.py",
            base = base,

        )
    ]
)