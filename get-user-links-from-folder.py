import sys, os

def get_folders(directory):
    return [name for name in os.scandir(directory) if os.path.isdir(os.path.join(directory, name))]

def get_subfolders(directory):
    site = directory.split('\\')[2]
    url_prefix = "https://kemono.party/" + site + "/user/"
    folders = get_folders(directory)
    
    subfolders = []
    for folder in folders:
        user = folder.name.split('[')[1][:-1]
        subfolders.append(url_prefix + user)
    
    return subfolders
    
    
def add_prefix(root, site):
    return os.path.join(root, site)

if __name__ == "__main__":
    if (len(sys.argv)) != 2:
        print("Usage: get-user-links-from-folder <root KemonoDL folder>")
        sys.exit()

    root = sys.argv[1]
    folders = get_folders(root)
    
    sites = list(map(lambda x: os.path.join(root, x), folders))
    
    links = []
    for site in sites:
        subfolders = get_subfolders(site)
        links = [*links, *subfolders]
    
    for link in links:
        print(link)
        