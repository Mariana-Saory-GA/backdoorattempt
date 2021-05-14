# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

setup(
    name = "cliente",
    version = "0.1",
    description = "",
    executables = [Executable("cliente.py")]
)