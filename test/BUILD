load("@rules_python//python:defs.bzl", "py_test")
load("@my_deps//:requirements.bzl", "requirement")

py_test(
    name = "test_larry",
    srcs = ["test_larry.py"],
    imports = ["../larry/"],
    deps = [
        "//larry:larry",
        requirement("pytest"),
    ],
)
