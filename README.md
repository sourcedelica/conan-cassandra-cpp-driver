# [Conan](http://conan.io) recipe for Cassandra C/C++ driver

## Setup

### Conan
```
pip install conan
```

## Building a new version of the package

1. Edit `conanfile.py` and `test_package/conanfile.py` and change the
   `version` attribute to the new version number.
2. Run `conan test_package`  
 
The syntax for `conan test_package` is  
```
conan test_package [-o cassandra-cpp-driver:option=value]...
```

`conan test_package` will build the driver and install the package in your local 
Conan repository under `~/.conan/data`.  It will also run a smoke test 
against the package (TODO).

### Build Options

Supported options are:
 
|Option     |Values                             |Default  |Description             | 
|:----------|:----------------------------------|:--------|:-----------------------|
|`shared`   |`True`, `False`                    | `False` | Build shared libraries (static always built) |

For example, to build with shared libraries use:
```
conan test_package -o cassandra-cpp-driver:shared=True 
```

Conan keeps track of the option values used and each built combination of
options is a different package.

## Uploading built packages to `conan.io`
```
conan upload --all cassandra-cpp-driver/version@user/channel
```
where _version_, _user_, and _channel_ are the same values from 
[Building a new version](#building-a-new-version-of-the-package) above.

This command will upload all of the packages built with that _version_ 
to the `conan.io` repository.

After the package is uploaded successfully you should commit and push 
the updated `conanfile.py` files to Github.
