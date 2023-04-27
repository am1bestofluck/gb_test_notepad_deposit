from pathlib import Path

BASEPATH = Path("./notepad/db/db_taxi.sql") if\
    Path("./notepad/db/db_taxi.sql").exists() else\
    Path("./db/db_taxi.sql")

DRIVERNOTES="notes_drv"
CARNOTES="notes_car"

def main():
    print(BASEPATH)
    print(BASEPATH.exists())

if __name__ == "__main__":
    main()