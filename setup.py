from sys import executable

from cx_Freeze import setup, Executable

setup(
    name="TicTacToe",
    version="1.0",
    description="TicTacToe Game by Orixos",
    executables=[Executable("play.py")]
)
