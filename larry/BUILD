load("@rules_python//python:defs.bzl", "py_library")
load("@my_deps//:requirements.bzl", "requirement")


py_library(
    name = "larry",
    srcs = ["larry.py"],
    deps = [requirement("numpy")],
    visibility = ["//visibility:public"],
)