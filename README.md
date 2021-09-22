# bazel_python_demo
使用bazel构建python项目

## 1.简单的构建
构建规则参见根目录下的BUILD文件。
```bash
$ bazel build main
INFO: Analyzed target //:main (18 packages loaded, 94 targets configured).
INFO: Found 1 target...
Target //:main up-to-date:
  bazel-bin/main
INFO: Elapsed time: 15.128s, Critical Path: 0.04s
INFO: 5 processes: 5 internal.
INFO: Build completed successfully, 5 total actions
```
构建完成后，
```bash
$ ./bazel-bin/main
hello world
```

## 2.对第三方包的依赖管理
构建规则参见根目录下的BUILD和WORKSPACE文件。
```bash
$ bazel build main2
INFO: Analyzed target //:main2 (19 packages loaded, 579 targets configured).
INFO: Found 1 target...
Target //:main2 up-to-date:
  bazel-bin/main2
INFO: Elapsed time: 6.173s, Critical Path: 0.10s
INFO: 5 processes: 5 internal.
INFO: Build completed successfully, 5 total actions
```
构建完成后，
```bash
$ ./bazel-bin/main2
[0.14104721 0.78952585 0.44296877 0.80411774 0.49069414 0.15124714
 0.70101288 0.25044066 0.10049017 0.40712893]
```

## 3.bazel test
我们构建了一个larry的python库，构建规则见larry/BUILD。  
同时我们撰写了测试用例。构建规则见test/BUILD
```bash
bazel test test:test_larry
INFO: Analyzed target //test:test_larry (17 packages loaded, 753 targets configured).
INFO: Found 1 test target...
Target //test:test_larry up-to-date:
  bazel-bin/test/test_larry
INFO: Elapsed time: 16.101s, Critical Path: 10.45s
INFO: 5 processes: 3 internal, 2 darwin-sandbox.
INFO: Build completed successfully, 5 total actions
//test:test_larry                                                        PASSED in 10.0s

Executed 1 out of 1 test: 1 test passes.
INFO: Build completed successfully, 5 total actions
```