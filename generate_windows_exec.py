import cx_Freeze
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("launchers/gui.py", base=base, icon="gui.ico")]

cx_Freeze.setup(
    name = "PowerSIM-GUI",
    options = {"build_exe":{"packages":["tkinter"], "include_files":["gui.ico","asm-proc/asm_dir.py","asm-proc/assembler.py","pass-handlers/first_pass.py","launchers/gui.py","input.s","launchers/cli.py","simulated-storage/memory_manage.py","asm-proc/processor.py","pass-handlers/second_pass.py","simple.s"]}},
    version = "0.65",
    description = "POWER ISA simulator",
    executables = executables
)
