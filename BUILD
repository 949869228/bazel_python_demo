load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
  name = "main",
  srcs = ["main.py"],
)

load("@my_deps//:requirements.bzl", "requirement")
py_binary(
  name = "main2",
  srcs = ["main2.py"],
  deps = [requirement("numpy")]
)
