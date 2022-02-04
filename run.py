import os


def main():
    print(os.environ['GITHUB_ACTIONS_CONTEXT'])


if __name__ == '__main__':
    main()


