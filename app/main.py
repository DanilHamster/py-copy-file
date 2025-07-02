def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    firs_file = parts[1]
    second_file = parts[2]

    if firs_file == second_file:
        return

    try:
        with (open(firs_file, "r") as file_in,
              open(second_file, "w") as file_out):
            file_out.write(file_in.read()
                           )

    except FileNotFoundError:
        pass
