load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "9d68f24659e8ce8b736590ba1e4418af06ec2552",
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

load("@rules_python//python:pip.bzl", "pip_repositories")
pip_repositories()

load("@rules_python//python:pip.bzl", "pip_import")
pip_import(
    name="bototest",
    requirements = "//boto_stuff:requirements.txt",
)

load("@bototest//:requirements.bzl", "pip_install")
pip_install()
