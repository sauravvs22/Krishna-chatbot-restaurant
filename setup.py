import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

_version_ = "0.0.0"
REPO_NAME = "Text-Summarization-Project"
AUTHOR_USER_NAME = "sauravvs22"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "sauravsonawane31@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package of NLP Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sauravvs22/Text-Summarization-Project",
    project_urls={
        "Bug Tracker": "https://github.com/sauravvs22/Text-Summarization-Project/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    

)
