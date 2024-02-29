import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = hash(password)
        # self.password = hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        print(f"Name: {self.name}")
        print(f"Username: {self.username}")
        # print(f"Password: {self.password}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def post(self):
        print(f"Title: {self.title}, Content: {
              self.content}, Author: {self.author}")


def get_user_info():
    name = input("Please enter your name: ")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    return name, username, password


def more_users():
    while True:
        try:
            ans = input("Do you want to add more users (Y/N)? ").upper()
            if ans == "Y":
                print("OK, let's add a new user!")
                return True
            elif ans == "N":
                print("Ok, thank you!")
                return False
            else:
                print("Choose Y or N.")
        except ValueError:
            print("Invalid input.")


def upload():
    title = input("Post title: ")
    content = input("Post content: ")
    author = input("Post author (username): ")
    return title, content, author


def upload_more():
    while True:
        try:
            ans = input("Do you want to upload another post (Y/N)? ").upper()
            if ans == "Y":
                print("OK, initiating a new post...")
                return True
            elif ans == "N":
                print("Ok, thank you!")
                return False
            else:
                print("Choose Y or N.")
        except ValueError:
            print("Invalid input.")


def main():
    members = []
    posts = []
    repost = True
    users = True

    while users:
        print("--- User information ---")
        name, username, password = get_user_info()
        members.append(Member(name, username, password))

        users = more_users()

    print("--- All members ---")
    for member in members:
        member.display()

    while repost:
        print("--- Upload your post ---")
        title, content, author = upload()
        posts.append(Post(title, content, author))

        repost = upload_more()

    author_keyword = None

    print(f"--- All posts by {author_keyword} ---")
    for post in posts:
        if author_keyword == post.author:
            print(post.title)

    search_keyword = None

    print(f"--- Search result for {search_keyword} in content --- ")
    for post in posts:
        if search_keyword in post.content:
            print(post.title)


if __name__ == "__main__":
    main()
