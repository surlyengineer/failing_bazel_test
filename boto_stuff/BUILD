package(default_visibility = ["//visibility:public"])
load("@bototest//:requirements.bzl", "requirement")

py_test(
    name = "boto_test",
    srcs = ["boto_test.py"],
    deps = [
        requirement("boto3"),
        requirement("six"),
    ],
)

py_library(
    name = "helloworld",
    srcs = ["helloworld.py"],
    deps = [
        requirement("boto3"),
    ]
)

#py_test(
#    name = "helloworld_test",
#    srcs = ["helloworld_test.py"],
#    imports = ["."],
#    deps = [":helloworld"],
#    python_version = "PY2",
#)

py_test(
    name = "helloworld_test_py3",
    srcs = ["helloworld_test_py3.py"],
    imports = ["."],
    deps = [":helloworld"],
    python_version = "PY3",
)
