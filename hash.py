import os

try:
    import pyperclip
    import hashlib
    import argparse
except:
    os.system("pip  install argparse")
    os.system("pip  install hashlib")
    os.system("pip  install pyperclip")
    os.system("clear")

parser = argparse.ArgumentParser(description="Hashing Text")
parser.add_argument(
    "-t", "--text", type=str, help="Text that will be hashed", required=True
)
parser.add_argument(
    "-c",
    "--copy",
    help="copy hashed to clipboard",
    action="store_true",
    default=False,
    required=False,
)

parser.add_argument(
    "-m",
    "--Method",
    type=str,
    help="defult: Md5",
    choices=[
        "sha1",
        "md5",
        "sha224",
        "sha256",
        "sha384",
        "sha512",
        "sha3_224",
        "sha3_256",
        "sha3_384",
        "sha3_512",
        "snake_128",
        "snake_256",
    ],
    default="md5",
    required=False,
)
args = parser.parse_args()
hash_function = getattr(hashlib, args.Method)
hashed = hash_function(str(args.text).encode()).hexdigest()
if args.copy == True:
    pyperclip.copy(hashed)
else:
    pass
print(f"{args.Method} Hash is :", hashed)
