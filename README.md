# Repo demonstrating failure of operator import precedence

Running this, the PY2 version of the test passes while the PY3 version fails with

```
...

line 414
    raise exception_type, self._exception, self._traceback
                        ^
SyntaxError: invalid syntax
================================================================================
INFO: Elapsed time: 0.814s, Critical Path: 0.63s
INFO: 2 processes: 2 darwin-sandbox.
INFO: Build completed, 1 test FAILED, 2 total actions
//boto_stuff:helloworld_test                                    (cached) PASSED in 0.5s
//boto_stuff:helloworld_test2                                            FAILED in 0.5s
  /private/var/tmp/<...>/helloworld_test2/test.log

Executed 1 out of 2 tests: 1 test passes and 1 fails locally.
INFO: Build completed, 1 test FAILED, 2 total actions
```

This error is correct for trying to run the backport of futures under python3

(Bazel version 0.27.2) 
