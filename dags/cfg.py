# from decouple import Config, RepositoryIni


# config = Config(RepositoryIni("secrets/settings.ini"))
# API_KEYS = config("API_KEY", default=[], cast=lambda v: [s.strip() for s in v.split(',')])

API_KEYS=["7dcda545-b2a4-4ec5-8f75-f1a4b40d47db"]

# if __name__ == "__main__":
#   print(API_KEYS)