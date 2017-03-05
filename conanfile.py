import os
from conans import ConanFile
from conans import CMake


class CassandraCppDriverConan(ConanFile):
    version = '2.5.0'

    name = "cassandra-cpp-driver"
    url = "https://github.com/sourcedelica/conan-cassandra-cpp-driver"
    license = "Apache-2.0"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    requires = "LibUV/1.9.1@cloudwall/stable", "OpenSSL/1.0.2i@lasote/stable"
    description = "Cassandra C/C++ driver"
    source_dir = "cpp-driver"
    build_dir = "cpp-driver/build"

    def source(self):
        self.run_command("git clone https://github.com/datastax/cpp-driver.git")
        self.run_command("git checkout -b %s.x %s" % (self.version, self.version), self.source_dir)

    def build(self):
        defs = {
            "CASS_BUILD_STATIC": "ON",
            "CASS_BUILD_SHARED": "ON" if self.options.shared else "OFF",
               "LIBUV_ROOT_DIR": self.deps_cpp_info["LibUV"].rootpath,
             "OPENSSL_ROOT_DIR": self.deps_cpp_info["OpenSSL"].rootpath
        }
        if not os.path.isdir(self.build_dir):
            os.makedirs(self.build_dir)
        cmake = CMake(self.settings)
        cmake.configure(self, vars=defs, source_dir="..", build_dir=self.build_dir)
        cmake.build(self)

    def run_command(self, cmd, cwd=None):
        self.output.info(cmd)
        self.run(cmd, True, cwd)

    def package(self):
        self.copy("*.h",           dst="include", src="%s/include" % self.source_dir)
        self.copy("libcassandra*", dst="lib",     src=self.build_dir)

    def package_info(self):
        self.cpp_info.libs = ["cassandra_static"]
