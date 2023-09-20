# Copyright (c) 2023 구FS, all rights reserved. Subject to the MIT licence in `licence.md`.
x: list[int]=[1]

print("Starting up...")
while True:
    x.append(x[-1]*2)