from downloader import get_files

print(f"Put company's name")
name = input(">")
print(f"You're interested in {name}.")

get_files(name)
