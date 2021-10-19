load("//src/pytest:defs.bzl", "pytest_test")

pytest_test(
    name = "test_larry",
    srcs = ["test_larry.py"],
    imports = ["../larry/"],
    deps = [
        "//larry:larry",
    ],
)
