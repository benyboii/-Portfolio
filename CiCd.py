from docx2pdf import convert
from git import Repo
def main():
    doc_convert()
    git_push()

def git_push():
    PATH_OF_GIT_REPO = r'C:\Users\benba\Ben Bar\.git'
    commit = input("Please type the commit: ")
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(commit)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print("Somthing went wrong while pushing the files")

def doc_convert():
    PATH_OF_WORD = r"C:\Users\benba\Ben Bar\CV - Ben Bar.docx"
    print("Converting the word file to pdf..")
    convert(PATH_OF_WORD)


if __name__ == "__main__":
    main()