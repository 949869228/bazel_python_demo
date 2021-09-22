load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.4.0/rules_python-0.4.0.tar.gz",
    sha256 = "954aa89b491be4a083304a2cb838019c8b8c3720a7abb9c4cb81ac7a24230cea",
)


load("@rules_python//python:pip.bzl", "pip_install")

# Create a central external repo, @deps, that contains Bazel targets for all the
# third-party packages specified in the requirements.txt file.
pip_install(
    name="my_deps",
    requirements="//:requirements.txt",
)