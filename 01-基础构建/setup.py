from cx_Freeze import setup, Executable



# TARGET
target = Executable(
    script="use_calculator.py",
    base="Win32GUI",
)

# SETUP CX FREEZE
setup(
    executables = [target]
    
)
