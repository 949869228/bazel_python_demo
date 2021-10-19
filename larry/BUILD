load("@rules_python//python:defs.bzl", "py_library")
load("@deps//:requirements.bzl", "requirement")


py_library(
    name = "larry",
    srcs = ["larry.py", "__init__.py"],
    deps = [requirement("numpy")],
    visibility = ["//visibility:public"],
)