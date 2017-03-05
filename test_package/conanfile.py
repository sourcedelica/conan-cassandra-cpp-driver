from conans import ConanFile, CMake
import os


class CassReuseConan(ConanFile):
    version = '2.5.0'
    username = 'sourcedelica'
    channel = 'testing'
    requires = "cassandra-cpp-driver/%s@%s/%s" % (version, username, channel)
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        binary = os.sep.join([".", "bin", "test_compile"])
        self.output.info("Running %s" % binary)
        self.run(binary)
